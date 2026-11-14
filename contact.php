<?php
// Formulaire de devis arboritaille.ch — envoi e-mail depuis le serveur, sauvegarde CSV hors docroot, envoi au CRM (Make).
// Aucun secret dans ce fichier : la configuration Make est lue dans le dossier privé (voir $PRIVE).
date_default_timezone_set('Europe/Zurich');
mb_internal_encoding('UTF-8');

$DEST  = 'contact@arboritaille.ch';                 // destinataire visible : le client
$BCC   = 'aymeric@cleanibat.fr';                    // copie cachée (et destinataire unique en mode ?test=1)
$FROM  = 'Arboritaille <no-reply@arboritaille.ch>'; // expéditeur du domaine (SPF)
$PRIVE = dirname($_SERVER['DOCUMENT_ROOT']) . '/prive_arboritaille'; // hors docroot : config Make + CSV
if (!is_dir($PRIVE)) { $PRIVE = __DIR__ . '/../prive_arboritaille'; }
$CSV   = $PRIVE . '/leads_site.csv';
$TEST  = isset($_GET['test']) && $_GET['test'] === '1';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); header('Content-Type: text/plain; charset=UTF-8'); echo 'Methode non autorisee.'; exit; }
if (!empty($_POST['_honey'])) { header('Location: /merci', true, 303); exit; }

function v($k){ return isset($_POST[$k]) ? trim(strip_tags((string)$_POST[$k])) : ''; }
$nom=v('Nom'); $tel=v('Téléphone'); $email=v('Email'); $ville=v('Localité'); $besoin=v('Besoin'); $msg=v('Message');
$src=v('Source'); $sujet=v('Sujet'); $lp=preg_replace('/[^a-z0-9_-]/i','',v('lp'));
$origine=v('Origine'); if(!in_array($origine,['Site','SEO','Google Ads','Meta Ads','Autre'],true)) $origine='Site';

if ($nom==='' || $tel==='' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  http_response_code(400); header('Content-Type: text/plain; charset=UTF-8');
  echo 'Merci de vérifier le nom, le téléphone et l\'e-mail.'; exit;
}

// 1) Filet de sécurité : le lead est écrit AVANT l'envoi de l'e-mail
if (is_dir($PRIVE) || @mkdir($PRIVE, 0700, true)) {
  $fh=@fopen($CSV,'a');
  if($fh){ if(filesize($CSV)===0) fputcsv($fh,['date','nom','telephone','email','localite','besoin','message','page','origine','test','ip'],';');
    fputcsv($fh,[date('Y-m-d H:i:s'),$nom,$tel,$email,$ville,$besoin,str_replace(["\r","\n"],' ',$msg),$src,$origine,$TEST?'oui':'',$_SERVER['REMOTE_ADDR']??''],';');
    fclose($fh); @chmod($CSV,0600); }
}

// 2) CRM du client via Make (configuration hors docroot : {"make_url":..., "client":..., "cle":...})
$cfg = @json_decode(@file_get_contents($PRIVE . '/agence_arboritaille.json'), true);
if (is_array($cfg) && !empty($cfg['make_url']) && function_exists('curl_init')) {
  $lead = ['client'=>$cfg['client']??'', 'cle'=>$cfg['cle']??'', 'nom'=>($TEST?'TEST ':'').$nom, 'telephone'=>$tel, 'email'=>$email, 'localite'=>$ville, 'besoin'=>$besoin,
    'message'=>str_replace(["\r","\n"],' ',$msg), 'source'=>$origine, 'campagne'=>$src, 'id'=>'site-'.date('YmdHis').'-'.substr(md5($email.$tel),0,6)];
  $ch = curl_init($cfg['make_url']);
  curl_setopt_array($ch, [CURLOPT_POST=>true, CURLOPT_RETURNTRANSFER=>true, CURLOPT_CONNECTTIMEOUT=>2, CURLOPT_TIMEOUT=>4,
    CURLOPT_HTTPHEADER=>['Content-Type: application/json'], CURLOPT_POSTFIELDS=>json_encode($lead)]);
  @curl_exec($ch); @curl_close($ch);
}

// 3) E-mail
$subject = ($sujet!=='' ? $sujet : 'Nouvelle demande de devis – arboritaille.ch') . ($TEST ? ' [TEST]' : '');
$body  = ($TEST ? "*** TEST TECHNIQUE, à ignorer ***\n\n" : '');
$body .= "Nouvelle demande depuis arboritaille.ch\n\n";
$body .= "Nom        : $nom\nTéléphone  : $tel\nE-mail     : $email\nLocalité   : $ville\nBesoin     : $besoin\n";
$body .= "Origine    : $origine\nPage       : $src\n\nMessage :\n" . ($msg!=='' ? $msg : '(vide)') . "\n";
$headers  = "From: $FROM\r\nReply-To: $nom <$email>\r\n";
if (!$TEST) $headers .= "Bcc: $BCC\r\n";
$headers .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nX-Mailer: PHP/".phpversion();
$to = $TEST ? $BCC : $DEST;
@mail($to, '=?UTF-8?B?'.base64_encode($subject).'?=', $body, $headers);

// 4) Page de remerciement (le lead est déjà sauvegardé même si l'e-mail échoue)
header('Location: /merci?lp=' . urlencode($lp), true, 303);
exit;
