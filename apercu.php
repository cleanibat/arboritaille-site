<?php
// Accès au site pendant la maintenance : vérifie le mot de passe saisi sur la page de maintenance
// et pose un cookie de 30 jours reconnu par .htaccess. Le mot de passe (haché) et la clé du cookie
// sont dans ../prive_arboritaille/maintenance.json (hors docroot, déposé par le déploiement), jamais dans le dépôt.
$PRIVE = dirname($_SERVER['DOCUMENT_ROOT']) . '/prive_arboritaille';
if (!is_dir($PRIVE)) { $PRIVE = __DIR__ . '/../prive_arboritaille'; }
$cfg = @json_decode(@file_get_contents($PRIVE . '/maintenance.json'), true);

$retour = isset($_POST['retour']) ? (string)$_POST['retour'] : '/';
if ($retour === '' || $retour[0] !== '/' || strpos($retour, '//') === 0 || strpbrk($retour, "\r\n\\") !== false) { $retour = '/'; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !is_array($cfg) || empty($cfg['hash']) || empty($cfg['token'])) {
  header('Location: /', true, 303); exit;
}

$mdp = isset($_POST['mdp']) ? (string)$_POST['mdp'] : '';
if (password_verify($mdp, $cfg['hash'])) {
  setcookie('arbo_apercu', $cfg['token'], ['expires' => time() + 30 * 86400, 'path' => '/', 'secure' => true, 'httponly' => true, 'samesite' => 'Lax']);
  header('Cache-Control: private, no-store');
  header('Location: ' . $retour, true, 303); exit;
}

sleep(2); // freine les essais en série
$sep = (strpos($retour, '?') === false) ? '?' : '&';
header('Cache-Control: private, no-store');
header('Location: ' . $retour . $sep . 'acces=refuse', true, 303);
