/* Arboritaille — menu mobile, bandeau cookies (Mode Consentement v2), origine des demandes. Aucun suivi maison. */
(function () {
  'use strict';
  // Menu mobile
  var burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = document.body.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Consentement (choix conservé 6 mois)
  var KEY = 'arbo_consent', box = document.getElementById('consent');
  function read() { try { var v = JSON.parse(localStorage.getItem(KEY) || 'null'); return v && v.exp > Date.now() ? v.c : null; } catch (e) { return null; } }
  function apply(c) {
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    var s = c === 'yes' ? 'granted' : 'denied';
    gtag('consent', 'update', { ad_storage: s, ad_user_data: s, ad_personalization: s, analytics_storage: s });
    dataLayer.push({ event: 'consent_update', consent: c });
  }
  function choose(c) {
    try { localStorage.setItem(KEY, JSON.stringify({ c: c, exp: Date.now() + 1000 * 60 * 60 * 24 * 182 })); } catch (e) { }
    apply(c); if (box) box.classList.remove('show');
  }
  var saved = read();
  if (saved) apply(saved); else if (box) box.classList.add('show');
  document.querySelectorAll('[data-consent]').forEach(function (b) { b.addEventListener('click', function () { choose(b.getAttribute('data-consent')); }); });
  document.querySelectorAll('[data-consent-open]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); if (box) box.classList.add('show'); }); });

  // Origine de la visite (pour la colonne Source du CRM), mémorisée 90 jours, sans cookie
  var OK = 'arbo_origine';
  function origine() {
    var q = location.search, ref = document.referrer || '';
    if (/[?&](gclid|gbraid|wbraid)=/.test(q) || /utm_source=google.*utm_medium=cpc|utm_medium=cpc.*utm_source=google/.test(q)) return 'Google Ads';
    if (/[?&]fbclid=/.test(q) || /utm_source=(facebook|instagram|meta)/.test(q)) return 'Meta Ads';
    if (/^https?:\/\/([^/]*\.)?(google|bing|duckduckgo|qwant|ecosia|yahoo)\./.test(ref)) return 'SEO';
    if (ref && ref.indexOf(location.host) === -1) return 'Autre';
    return '';
  }
  var o = origine();
  try {
    if (o) localStorage.setItem(OK, JSON.stringify({ o: o, exp: Date.now() + 1000 * 60 * 60 * 24 * 90 }));
    var v = JSON.parse(localStorage.getItem(OK) || 'null'); if (v && v.exp > Date.now()) o = v.o;
  } catch (e) { }
  document.querySelectorAll('input[name="Origine"]').forEach(function (i) { i.value = o || 'Site'; });
})();
