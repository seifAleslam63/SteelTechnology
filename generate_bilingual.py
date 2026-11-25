# -*- coding: utf-8 -*-
import os

new_html_content = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Steel Technology — Stainless Steel Precision. Industrial Power. | استيل تكنولوجي</title>
  <link rel="icon" type="image/png" href="logo.png" />
  <meta name="description" content="Steel Technology delivers custom metal fabrication, stainless steel equipment, and integrated industrial engineering solutions designed around your manufacturing requirements." />

  <!-- Fonts: Barlow Condensed (EN Heading), Inter (EN Body), IBM Plex Sans Arabic (AR All) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700&family=Inter:wght@300;400;500;600&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            auburn:        '#9E272E',
            'auburn-dark': '#7a1e23',
            'auburn-light':'#b8323a',
            bluebell:      '#99A0CB',
            silver:        '#A5A5A7',
            gunmetal:      '#262A32',
            'rich-black':  '#0D0D0D',
            'off-white':   '#F5F4F0',
            'light-gray':  '#E8E7E3',
          },
          fontFamily: {
            heading: ['Barlow Condensed', 'sans-serif'],
            body:    ['Inter', 'sans-serif'],
            arabic:  ['IBM Plex Sans Arabic', 'sans-serif'],
          },
          letterSpacing: {
            widest2: '0.25em',
          },
        }
      }
    }
  </script>

  <style>
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Inter', sans-serif;
      background: #0D0D0D;
      color: #F5F4F0;
      overflow-x: hidden;
      transition: direction 0.3s ease;
    }

    /* ─── RTL & ARABIC STYLING ─── */
    [dir="rtl"] {
      font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    }
    [dir="rtl"] .font-heading {
      font-family: 'IBM Plex Sans Arabic', sans-serif !important;
      letter-spacing: normal !important;
    }
    [dir="rtl"] .font-body {
      font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    }
    [dir="rtl"] .why-card {
      border-left: none !important;
      border-right: 2px solid rgba(158,39,46,0.3) !important;
      padding-left: 0 !important;
      padding-right: 24px !important;
    }
    [dir="rtl"] .why-card:hover {
      border-right-color: #9E272E !important;
    }
    [dir="rtl"] .btn-ghost svg,
    [dir="rtl"] .btn-outline svg,
    [dir="rtl"] .btn-primary svg {
      transform: scaleX(-1);
    }
    [dir="rtl"] .btn-ghost:hover svg {
      transform: scaleX(-1) translateX(4px);
    }
    [dir="rtl"] .section-label::before {
      display: none !important;
    }
    [dir="rtl"] .section-label::after {
      content: '';
      display: inline-block;
      width: 24px;
      height: 1px;
      background: #9E272E;
      margin-right: 10px;
    }
    [dir="rtl"] .nav-link::after {
      transform-origin: right !important;
    }
    [dir="rtl"] .hero-eyebrow .w-8:first-child {
      display: none;
    }
    [dir="rtl"] .hero-eyebrow .w-8:last-child {
      display: block;
    }

    /* ─── GRID OVERLAY ─── */
    .tech-grid {
      background-image:
        linear-gradient(rgba(153,160,203,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(153,160,203,0.04) 1px, transparent 1px);
      background-size: 60px 60px;
    }
    .tech-grid-fine {
      background-image:
        linear-gradient(rgba(153,160,203,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(153,160,203,0.03) 1px, transparent 1px);
      background-size: 20px 20px;
    }

    /* ─── HERO ─── */
    #hero {
      position: relative;
      min-height: 100vh;
      background: #0D0D0D;
      overflow: hidden;
    }
    .hero-bg {
      position: absolute; inset: 0;
      background:
        linear-gradient(135deg, rgba(13,13,13,0.95) 40%, rgba(38,42,50,0.7) 100%),
        url('https://images.unsplash.com/photo-1565793298595-6a879b1d9492?w=1800&q=80') center/cover no-repeat;
      transform: scale(1.05);
      transition: transform 8s ease-out;
    }
    .hero-bg.loaded { transform: scale(1); }
    .hero-scanlines {
      position: absolute; inset: 0;
      background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,0,0,0.03) 2px,
        rgba(0,0,0,0.03) 4px
      );
      pointer-events: none;
    }
    .hero-vignette {
      position: absolute; inset: 0;
      background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.6) 100%);
      pointer-events: none;
    }

    /* ─── NAV ─── */
    #navbar {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      transition: background 0.4s, backdrop-filter 0.4s, border-color 0.4s;
    }
    #navbar.scrolled {
      background: rgba(13,13,13,0.95);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(158,39,46,0.3);
    }
    .nav-link {
      position: relative;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.9rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(245,244,240,0.75);
      transition: color 0.2s;
    }
    [dir="rtl"] .nav-link {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      font-size: 0.95rem;
      letter-spacing: normal;
      text-transform: none;
    }
    .nav-link::after {
      content: '';
      position: absolute; bottom: -4px; left: 0; right: 0;
      height: 1px; background: #9E272E;
      transform: scaleX(0); transform-origin: left;
      transition: transform 0.3s ease;
    }
    .nav-link:hover { color: #F5F4F0; }
    .nav-link:hover::after { transform: scaleX(1); }

    /* ─── BUTTONS ─── */
    .btn-primary {
      display: inline-flex; align-items: center; gap: 10px;
      background: #9E272E; color: #fff;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.85rem; font-weight: 600;
      letter-spacing: 0.15em; text-transform: uppercase;
      padding: 14px 32px;
      border: 1px solid #9E272E;
      transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
    }
    [dir="rtl"] .btn-primary {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
      text-transform: none;
    }
    .btn-primary:hover {
      background: #7a1e23;
      box-shadow: 0 0 24px rgba(158,39,46,0.35);
      transform: translateY(-1px);
    }
    .btn-outline {
      display: inline-flex; align-items: center; gap: 10px;
      background: transparent; color: #F5F4F0;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.85rem; font-weight: 600;
      letter-spacing: 0.15em; text-transform: uppercase;
      padding: 13px 32px;
      border: 1px solid rgba(245,244,240,0.35);
      transition: border-color 0.2s, background 0.2s, transform 0.2s;
    }
    [dir="rtl"] .btn-outline {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
      text-transform: none;
    }
    .btn-outline:hover {
      border-color: #F5F4F0;
      background: rgba(245,244,240,0.05);
      transform: translateY(-1px);
    }
    .btn-ghost {
      display: inline-flex; align-items: center; gap: 8px;
      background: transparent; color: #9E272E;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.8rem; font-weight: 600;
      letter-spacing: 0.12em; text-transform: uppercase;
      padding: 8px 0;
      border: none; border-bottom: 1px solid rgba(158,39,46,0.4);
      transition: border-color 0.2s, gap 0.2s;
      cursor: pointer;
    }
    [dir="rtl"] .btn-ghost {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
      text-transform: none;
    }
    .btn-ghost:hover { gap: 14px; border-color: #9E272E; }
    .btn-ghost svg { transition: transform 0.2s; }
    .btn-ghost:hover svg { transform: translateX(4px); }
    [dir="rtl"] .btn-ghost:hover svg { transform: scaleX(-1) translateX(4px); }

    /* ─── SECTION LABELS ─── */
    .section-label {
      display: inline-flex; align-items: center; gap: 10px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.8rem; font-weight: 700;
      letter-spacing: 0.25em; text-transform: uppercase;
      color: #9E272E;
    }
    [dir="rtl"] .section-label {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
    }
    .section-label::before {
      content: '';
      display: block; width: 24px; height: 1px;
      background: #9E272E;
    }

    /* ─── STAT STRIP ─── */
    .stat-sep { width: 1px; height: 56px; background: rgba(165,165,167,0.25); }

    /* ─── CAPABILITY CARDS ─── */
    .cap-card {
      position: relative; overflow: hidden;
      border: 1px solid rgba(165,165,167,0.12);
      background: rgba(38,42,50,0.4);
      transition: border-color 0.3s, background 0.3s, transform 0.3s;
      cursor: pointer;
    }
    .cap-card::before {
      content: '';
      position: absolute; bottom: 0; left: 0; right: 0;
      width: 0; height: 2px;
      background: #9E272E;
      transition: width 0.4s ease;
    }
    .cap-card:hover { border-color: rgba(158,39,46,0.4); background: rgba(38,42,50,0.7); transform: translateY(-3px); }
    .cap-card:hover::before { width: 100%; }
    .cap-icon { color: #9E272E; }

    /* ─── DIVISION CARDS ─── */
    .div-card {
      position: relative; overflow: hidden;
      transition: transform 0.4s;
    }
    .div-card-bg {
      position: absolute; inset: 0;
      background: center/cover no-repeat;
      transition: transform 0.6s;
    }
    .div-card:hover .div-card-bg { transform: scale(1.05); }
    .div-card-overlay {
      position: absolute; inset: 0;
      background: linear-gradient(to top, rgba(13,13,13,0.92) 30%, rgba(13,13,13,0.3) 100%);
      transition: background 0.4s;
    }
    .div-card:hover .div-card-overlay {
      background: linear-gradient(to top, rgba(13,13,13,0.97) 30%, rgba(13,13,13,0.4) 100%);
    }

    /* ─── EQUIPMENT CATALOG ─── */
    .eq-card {
      position: relative; overflow: hidden;
      background: rgba(38,42,50,0.5);
      border: 1px solid rgba(165,165,167,0.1);
      transition: border-color 0.3s, transform 0.3s;
    }
    .eq-card:hover { border-color: rgba(158,39,46,0.35); transform: translateY(-4px); }
    .eq-card-img { transition: transform 0.5s; }
    .eq-card:hover .eq-card-img { transform: scale(1.06); }

    /* ─── INDUSTRY GRID ─── */
    .ind-card {
      position: relative; overflow: hidden;
      aspect-ratio: 4/3;
    }
    .ind-card-bg { position: absolute; inset: 0; background: center/cover no-repeat; transition: transform 0.5s; }
    .ind-card:hover .ind-card-bg { transform: scale(1.08); }
    .ind-card-overlay {
      position: absolute; inset: 0;
      background: linear-gradient(to top, rgba(13,13,13,0.9) 0%, rgba(13,13,13,0.2) 100%);
      transition: background 0.4s;
    }
    .ind-card:hover .ind-card-overlay {
      background: linear-gradient(to top, rgba(158,39,46,0.85) 0%, rgba(13,13,13,0.3) 100%);
    }

    /* ─── SCROLL REVEAL ─── */
    .reveal {
      opacity: 0;
      transform: translateY(32px);
      transition: opacity 0.7s ease, transform 0.7s ease;
    }
    .reveal.visible { opacity: 1; transform: translateY(0); }
    .reveal-delay-1 { transition-delay: 0.1s; }
    .reveal-delay-2 { transition-delay: 0.2s; }
    .reveal-delay-3 { transition-delay: 0.3s; }
    .reveal-delay-4 { transition-delay: 0.4s; }
    .reveal-delay-5 { transition-delay: 0.5s; }

    /* ─── SCROLL INDICATOR ─── */
    .scroll-indicator {
      display: flex; flex-direction: column; align-items: center; gap: 8px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase;
      color: rgba(245,244,240,0.4);
    }
    [dir="rtl"] .scroll-indicator {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
    }
    .scroll-line {
      width: 1px; height: 48px;
      background: linear-gradient(to bottom, rgba(245,244,240,0.4), transparent);
      animation: scrollPulse 2s ease-in-out infinite;
    }
    @keyframes scrollPulse {
      0%, 100% { opacity: 0.4; transform: scaleY(1); }
      50% { opacity: 1; transform: scaleY(1.1); }
    }

    /* ─── HERO TEXT ANIMATION ─── */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(24px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .hero-eyebrow { animation: fadeUp 0.8s ease 0.2s both; }
    .hero-h1-line1 { animation: fadeUp 0.8s ease 0.4s both; }
    .hero-h1-line2 { animation: fadeUp 0.8s ease 0.55s both; }
    .hero-h1-line3 { animation: fadeUp 0.8s ease 0.70s both; }
    .hero-sub   { animation: fadeUp 0.8s ease 0.9s both; }
    .hero-ctas  { animation: fadeUp 0.8s ease 1.1s both; }

    /* ─── RFQ FORM ─── */
    .rfq-input {
      width: 100%; background: rgba(38,42,50,0.6);
      border: 1px solid rgba(165,165,167,0.2);
      color: #F5F4F0; padding: 12px 16px;
      font-size: 0.875rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .rfq-input:focus { border-color: #9E272E; }
    .rfq-input::placeholder { color: rgba(165,165,167,0.5); }
    .rfq-label {
      display: block;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.75rem; font-weight: 600;
      letter-spacing: 0.15em; text-transform: uppercase;
      color: #A5A5A7; margin-bottom: 6px;
    }
    [dir="rtl"] .rfq-label {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
    }
    .rfq-select {
      width: 100%; background: rgba(38,42,50,0.6);
      border: 1px solid rgba(165,165,167,0.2);
      color: #F5F4F0; padding: 12px 16px;
      font-size: 0.875rem;
      outline: none; cursor: pointer;
      transition: border-color 0.2s;
      -webkit-appearance: none;
    }
    .rfq-select:focus { border-color: #9E272E; }
    .rfq-select option { background: #262A32; }

    /* ─── MOBILE MENU ─── */
    #mobile-menu {
      display: none;
      position: fixed; inset: 0; z-index: 200;
      background: rgba(13,13,13,0.98);
      backdrop-filter: blur(16px);
      flex-direction: column;
      align-items: center; justify-content: center;
      gap: 2rem;
    }
    #mobile-menu.open { display: flex; }
    .mobile-nav-link {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 2.2rem; font-weight: 700;
      letter-spacing: 0.08em; text-transform: uppercase;
      color: rgba(245,244,240,0.7);
      transition: color 0.2s;
    }
    [dir="rtl"] .mobile-nav-link {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
    }
    .mobile-nav-link:hover { color: #9E272E; }

    /* ─── WHATSAPP BTN ─── */
    .wa-btn {
      display: inline-flex; align-items: center; gap: 8px;
      background: #25D366; color: #fff;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.85rem; font-weight: 600;
      letter-spacing: 0.12em; text-transform: uppercase;
      padding: 13px 24px;
      transition: background 0.2s;
    }
    [dir="rtl"] .wa-btn {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
    }
    .wa-btn:hover { background: #1da851; }

    /* ─── FOOTER ─── */
    .footer-link {
      font-size: 0.85rem; color: rgba(165,165,167,0.7);
      transition: color 0.2s;
    }
    .footer-link:hover { color: #9E272E; }

    /* ─── WHY US PILLAR ─── */
    .why-card {
      border-left: 2px solid rgba(158,39,46,0.3);
      padding-left: 24px;
      transition: border-color 0.3s;
    }
    .why-card:hover { border-color: #9E272E; }

    /* ─── REVERSE ENG ─── */
    .re-grid {
      background-image:
        linear-gradient(rgba(153,160,203,0.06) 1px, transparent 1px),
        linear-gradient(90deg, rgba(153,160,203,0.06) 1px, transparent 1px),
        linear-gradient(rgba(153,160,203,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(153,160,203,0.03) 1px, transparent 1px);
      background-size: 80px 80px, 80px 80px, 20px 20px, 20px 20px;
    }

    /* TAG */
    .tag {
      display: inline-block;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 0.7rem; font-weight: 700;
      letter-spacing: 0.2em; text-transform: uppercase;
      padding: 4px 10px;
      border: 1px solid rgba(158,39,46,0.4);
      color: #9E272E;
    }
    [dir="rtl"] .tag {
      font-family: 'IBM Plex Sans Arabic', sans-serif;
      letter-spacing: normal;
    }

    /* Project placeholder */
    .proj-card {
      position: relative; overflow: hidden;
      border: 1px solid rgba(165,165,167,0.1);
      background: rgba(38,42,50,0.4);
      transition: border-color 0.3s, transform 0.3s;
    }
    .proj-card:hover { border-color: rgba(158,39,46,0.4); transform: translateY(-3px); }

    /* Language Switcher Badge */
    .lang-btn {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 6px 14px;
      border: 1px solid rgba(165,165,167,0.3);
      border-radius: 2px;
      font-size: 0.85rem; font-weight: 600;
      color: #F5F4F0;
      background: rgba(38,42,50,0.6);
      transition: all 0.2s ease;
      cursor: pointer;
    }
    .lang-btn:hover {
      border-color: #9E272E;
      background: rgba(158,39,46,0.15);
      color: #FFF;
    }

    @media (max-width: 768px) {
      .hero-h1 { font-size: clamp(2.5rem, 9vw, 4.5rem) !important; }
      .stat-sep { display: none; }
    }
  </style>
</head>
<body>

<!-- ══════════════════════════════════════════
     NAVIGATION
══════════════════════════════════════════ -->
<nav id="navbar" class="px-6 py-5">
  <div class="max-w-7xl mx-auto flex items-center justify-between">

    <!-- Logo -->
    <a href="#hero" class="flex items-center gap-3 group">
<img src="logo.png" alt="Steel Technology Official Logo" class="w-12 h-12 object-contain drop-shadow-[0_0_12px_rgba(158,39,46,0.35)] group-hover:scale-105 transition-transform duration-300" />
      <div>
        <div class="font-heading font-bold text-off-white text-base tracking-wide leading-none" data-i18n="logo_title">STEEL</div>
        <div class="font-heading font-light text-silver text-xs tracking-widest2 leading-none" data-i18n="logo_sub">TECHNOLOGY</div>
      </div>
    </a>

    <!-- Desktop Nav -->
    <div class="hidden lg:flex items-center gap-8">
      <a href="#hero"         class="nav-link" data-i18n="nav_home">Home</a>
      <a href="#about"        class="nav-link" data-i18n="nav_about">About</a>
      <a href="#divisions"    class="nav-link" data-i18n="nav_fab">Metal Fabrication</a>
      <a href="#engineering"  class="nav-link" data-i18n="nav_eng">Industrial Solutions</a>
      <a href="#catalog"      class="nav-link" data-i18n="nav_equip">Equipment</a>
      <a href="#projects"     class="nav-link" data-i18n="nav_proj">Projects</a>
      <a href="#contact"      class="nav-link" data-i18n="nav_contact">Contact</a>
    </div>

    <!-- Right CTA + Lang Switcher -->
    <div class="hidden lg:flex items-center gap-4">
      <button onclick="toggleLang()" class="lang-btn" id="lang-toggle" title="Switch Language">
        <i data-lucide="languages" class="w-4 h-4 text-auburn"></i>
        <span id="lang-label">عربي</span>
      </button>
      <a href="#contact" class="btn-primary text-sm py-2.5 px-6" data-i18n="btn_quote">Request a Quote</a>
    </div>

    <!-- Mobile Hamburger + Mobile Lang -->
    <div class="flex items-center gap-3 lg:hidden">
      <button onclick="toggleLang()" class="lang-btn text-xs py-1.5 px-2.5" id="lang-toggle-mobile">
        <span id="lang-label-mobile">عربي</span>
      </button>
      <button class="text-off-white" onclick="document.getElementById('mobile-menu').classList.add('open')" aria-label="Open menu">
        <i data-lucide="menu" class="w-6 h-6"></i>
      </button>
    </div>
  </div>
</nav>

<!-- Mobile Menu -->
<div id="mobile-menu">
  <button class="absolute top-6 right-6 text-off-white" onclick="document.getElementById('mobile-menu').classList.remove('open')" aria-label="Close menu">
    <i data-lucide="x" class="w-7 h-7"></i>
  </button>
  <a href="#hero"        class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_home">Home</a>
  <a href="#about"       class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_about">About</a>
  <a href="#divisions"   class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_fab">Fabrication</a>
  <a href="#engineering" class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_eng">Engineering</a>
  <a href="#catalog"     class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_equip">Equipment</a>
  <a href="#projects"    class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_proj">Projects</a>
  <a href="#contact"     class="mobile-nav-link" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="nav_contact">Contact</a>
  <a href="#contact"     class="btn-primary mt-4" onclick="document.getElementById('mobile-menu').classList.remove('open')" data-i18n="btn_quote">Request a Quote</a>
</div>


<!-- ══════════════════════════════════════════
     SECTION 01 — CINEMATIC HERO
══════════════════════════════════════════ -->
<section id="hero" class="tech-grid-fine">
  <div class="hero-bg" id="hero-bg"></div>
  <div class="hero-scanlines"></div>
  <div class="hero-vignette"></div>

  <!-- Decorative horizontal rule -->
  <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-auburn/40 to-transparent z-10"></div>

  <div class="relative z-10 max-w-7xl mx-auto px-6 pt-32 pb-20 min-h-screen flex flex-col justify-between">
    <div class="flex-1 flex flex-col justify-center max-w-4xl pt-8">
      <!-- Eyebrow -->
      <div class="hero-eyebrow flex items-center gap-3 mb-6">
        <div class="w-8 h-px bg-auburn"></div>
        <span class="font-heading text-xs font-semibold tracking-widest2 uppercase text-auburn" data-i18n="hero_eyebrow">20 Years of Industrial Expertise</span>
        <div class="w-8 h-px bg-auburn/30"></div>
      </div>

      <!-- Headline -->
      <h1 class="hero-h1 font-heading font-black leading-none mb-6" style="font-size: clamp(3.2rem, 6.8vw, 6.2rem); line-height: 0.98;">
        <span class="hero-h1-line1 block text-off-white" data-i18n="hero_title_1">STAINLESS STEEL</span>
        <span class="hero-h1-line2 block text-off-white" data-i18n="hero_title_2">PRECISION.</span>
        <span class="hero-h1-line3 block text-auburn" data-i18n="hero_title_3">INDUSTRIAL POWER.</span>
      </h1>
      <div class="font-heading font-light text-silver/80 text-xl tracking-widest mb-8" data-i18n="hero_title_4">ENGINEERED FOR YOUR PROCESS.</div>

      <!-- Subtext -->
      <p class="hero-sub text-silver/80 font-body text-base leading-relaxed max-w-2xl mb-10" data-i18n="hero_desc">
        Steel Technology delivers custom metal fabrication, stainless steel equipment, and integrated industrial engineering solutions designed around your manufacturing requirements.
      </p>

      <!-- CTAs -->
      <div class="hero-ctas flex flex-wrap gap-4">
        <a href="#contact" class="btn-primary">
          <i data-lucide="file-text" class="w-4 h-4"></i>
          <span data-i18n="hero_btn_quote">Request a Quote</span>
        </a>
        <a href="#divisions" class="btn-outline">
          <span data-i18n="hero_btn_explore">Explore Our Capabilities</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </div>

    <!-- Bottom row: stats preview + scroll -->
    <div class="flex items-end justify-between pt-12 flex-wrap gap-8 border-t border-silver/10">
      <div class="flex items-center gap-8 flex-wrap">
        <div>
          <div class="font-heading font-black text-3xl text-off-white">20+</div>
          <div class="font-heading text-xs tracking-widest uppercase text-silver/60" data-i18n="stat_exp">Years Experience</div>
        </div>
        <div class="stat-sep"></div>
        <div>
          <div class="font-heading font-black text-3xl text-off-white">304 / 316L</div>
          <div class="font-heading text-xs tracking-widest uppercase text-silver/60" data-i18n="stat_grades">Stainless Steel</div>
        </div>
        <div class="stat-sep"></div>
        <div>
          <div class="font-heading font-black text-3xl text-off-white">2</div>
          <div class="font-heading text-xs tracking-widest uppercase text-silver/60" data-i18n="stat_divs">Business Divisions</div>
        </div>
      </div>
      <div class="scroll-indicator">
        <span data-i18n="scroll_text">Scroll</span>
        <div class="scroll-line"></div>
      </div>
    </div>
  </div>

  <!-- Side brand tagline -->
  <div class="absolute right-8 top-1/2 -translate-y-1/2 hidden xl:flex flex-col items-center gap-3 z-10 pointer-events-none">
    <div class="w-px h-16 bg-gradient-to-b from-transparent to-auburn/40"></div>
    <span class="font-heading text-xs tracking-widest uppercase text-silver/40" style="writing-mode: vertical-lr; transform: rotate(180deg);" data-i18n="side_slogan">Where Strength Meets Innovation</span>
    <div class="w-px h-16 bg-gradient-to-t from-transparent to-auburn/40"></div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 02 — INDUSTRIAL CREDENTIALS
══════════════════════════════════════════ -->
<section id="about" class="bg-gunmetal border-y border-silver/10">
  <div class="max-w-7xl mx-auto px-6 py-16">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-0 divide-x divide-silver/10">
      <div class="reveal px-6 md:px-8 py-6 flex flex-col items-center text-center group">
        <div class="font-heading font-black text-5xl md:text-6xl text-off-white group-hover:text-auburn transition-colors duration-300">20<span class="text-auburn">+</span></div>
        <div class="font-heading font-semibold text-xs md:text-sm tracking-widest uppercase text-silver/70 mt-2" data-i18n="cred_1">Years of<br/>Experience</div>
      </div>
      <div class="reveal reveal-delay-1 px-6 md:px-8 py-6 flex flex-col items-center text-center group">
        <div class="font-heading font-black text-3xl md:text-4xl text-off-white group-hover:text-auburn transition-colors duration-300 leading-tight">304 &<br/>316L</div>
        <div class="font-heading font-semibold text-xs md:text-sm tracking-widest uppercase text-silver/70 mt-2" data-i18n="cred_2">Certified Stainless<br/>Steel Grades</div>
      </div>
      <div class="reveal reveal-delay-2 px-6 md:px-8 py-6 flex flex-col items-center text-center group">
        <div class="font-heading font-black text-3xl md:text-4xl text-off-white group-hover:text-auburn transition-colors duration-300 leading-tight" data-i18n="cred_3_title">Custom<br/>Engineering</div>
        <div class="font-heading font-semibold text-xs md:text-sm tracking-widest uppercase text-silver/70 mt-2" data-i18n="cred_3">Solutions<br/>Tailored to You</div>
      </div>
      <div class="reveal reveal-delay-3 px-6 md:px-8 py-6 flex flex-col items-center text-center group">
        <div class="font-heading font-black text-3xl md:text-4xl text-off-white group-hover:text-auburn transition-colors duration-300 leading-tight" data-i18n="cred_4_title">Fab to<br/>Install</div>
        <div class="font-heading font-semibold text-xs md:text-sm tracking-widest uppercase text-silver/70 mt-2" data-i18n="cred_4">Full-Cycle<br/>Turnkey Delivery</div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION: TRUSTED BY LEADING COMPANIES (CLIENTS)
══════════════════════════════════════════ -->
<section id="clients" class="py-20 bg-rich-black border-b border-silver/10 tech-grid relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal flex flex-col md:flex-row md:items-end justify-between mb-14 gap-6">
      <div>
        <div class="section-label mb-3" data-i18n="clients_label">Trusted By Leading Companies</div>
        <h2 class="font-heading font-black text-4xl md:text-5xl text-off-white leading-none">
          <span data-i18n="clients_h2_1">TRUSTED BY</span><br/>
          <span class="text-auburn" data-i18n="clients_h2_2">INDUSTRY LEADERS</span>
        </h2>
      </div>
      <p class="text-silver/65 text-sm leading-relaxed max-w-md" data-i18n="clients_desc">
        We are proud to engineer, fabricate, and commission mission-critical stainless steel systems for Egypt's leading multinational and national corporations.
      </p>
    </div>

    <!-- 4 Industrial Categories Grid -->
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">

      <!-- Category 1: Food & Beverage -->
      <div class="reveal bg-gunmetal/50 border border-silver/10 p-6 flex flex-col justify-between group hover:border-auburn/40 transition-all duration-300">
        <div>
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-silver/10">
            <div class="flex items-center gap-2.5">
              <i data-lucide="utensils" class="w-5 h-5 text-auburn"></i>
              <h3 class="font-heading font-bold text-lg text-off-white tracking-wide" data-i18n="cat_fb">FOOD & BEVERAGE</h3>
            </div>
            <span class="tag text-[0.65rem] py-0.5 px-2">5 Clients</span>
          </div>
          <ul class="space-y-3.5">
            <li class="flex items-center gap-3 text-sm text-silver/80 group-hover:text-off-white transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-auburn"></span>
              <span class="font-semibold text-off-white" data-i18n="c_nestle">Nestlé</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/80 group-hover:text-off-white transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-auburn"></span>
              <span class="font-semibold text-off-white" data-i18n="c_heinz">Heinz</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_marbella">Marbella Food Industries</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_technotaste">Techno Taste</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_albawadi">Al Bawadi Food Industries</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Category 2: Pharma & Medical -->
      <div class="reveal reveal-delay-1 bg-gunmetal/50 border border-silver/10 p-6 flex flex-col justify-between group hover:border-auburn/40 transition-all duration-300">
        <div>
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-silver/10">
            <div class="flex items-center gap-2.5">
              <i data-lucide="pill" class="w-5 h-5 text-auburn"></i>
              <h3 class="font-heading font-bold text-lg text-off-white tracking-wide" data-i18n="cat_pharma">PHARMA & MEDICAL</h3>
            </div>
            <span class="tag text-[0.65rem] py-0.5 px-2">3 Clients</span>
          </div>
          <ul class="space-y-3.5">
            <li class="flex items-center gap-3 text-sm text-silver/80 group-hover:text-off-white transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-auburn"></span>
              <span class="font-semibold text-off-white" data-i18n="c_sedico">Sedico Pharmaceuticals</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/80 group-hover:text-off-white transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-auburn"></span>
              <span class="font-semibold text-off-white" data-i18n="c_october">October Pharma</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_arabpack">Arab Pharmaceutical Packaging</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Category 3: Chemicals & Industrial -->
      <div class="reveal reveal-delay-2 bg-gunmetal/50 border border-silver/10 p-6 flex flex-col justify-between group hover:border-auburn/40 transition-all duration-300">
        <div>
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-silver/10">
            <div class="flex items-center gap-2.5">
              <i data-lucide="flask-conical" class="w-5 h-5 text-auburn"></i>
              <h3 class="font-heading font-bold text-lg text-off-white tracking-wide" data-i18n="cat_chem">CHEMICALS & INDUSTRIAL</h3>
            </div>
            <span class="tag text-[0.65rem] py-0.5 px-2">3 Clients</span>
          </div>
          <ul class="space-y-3.5">
            <li class="flex items-center gap-3 text-sm text-silver/80 group-hover:text-off-white transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-auburn"></span>
              <span class="font-semibold text-off-white" data-i18n="c_henkel">Henkel</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_evergrow">EverGrow</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_intlpaints">International Paints</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Category 4: Engineering Services -->
      <div class="reveal reveal-delay-3 bg-gunmetal/50 border border-silver/10 p-6 flex flex-col justify-between group hover:border-auburn/40 transition-all duration-300">
        <div>
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-silver/10">
            <div class="flex items-center gap-2.5">
              <i data-lucide="building-2" class="w-5 h-5 text-auburn"></i>
              <h3 class="font-heading font-bold text-lg text-off-white tracking-wide" data-i18n="cat_eng_serv">ENGINEERING SERVICES</h3>
            </div>
            <span class="tag text-[0.65rem] py-0.5 px-2">2 Clients</span>
          </div>
          <ul class="space-y-3.5">
            <li class="flex items-center gap-3 text-sm text-silver/80 group-hover:text-off-white transition-colors">
              <span class="w-1.5 h-1.5 rounded-full bg-auburn"></span>
              <span class="font-semibold text-off-white" data-i18n="c_tmg">Talaat Moustafa Group (TMG)</span>
            </li>
            <li class="flex items-center gap-3 text-sm text-silver/70">
              <span class="w-1.5 h-1.5 rounded-full bg-silver/30"></span>
              <span data-i18n="c_emco">EMCO</span>
            </li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════
     SECTION 03 — TWO CORE DIVISIONS
══════════════════════════════════════════ -->
<section id="divisions" class="py-24 bg-rich-black tech-grid">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal mb-16">
      <div class="section-label mb-4" data-i18n="div_label">Our Two Business Divisions</div>
      <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
        <span data-i18n="div_h2_1">TWO STRENGTHS.</span><br/>
        <span class="text-auburn" data-i18n="div_h2_2">ONE INTEGRATED PARTNER.</span>
      </h2>
    </div>

    <div class="grid md:grid-cols-2 gap-8">
      <!-- Division A -->
      <div class="div-card h-96 md:h-[520px] reveal group cursor-pointer border border-silver/10 hover:border-auburn/50 transition-colors">
        <div class="div-card-bg"
          style="background-image: linear-gradient(135deg, rgba(13,13,13,0.3) 0%, rgba(13,13,13,0.1) 100%), url('https://images.unsplash.com/photo-1587293852726-70cdb56c2866?w=900&q=80'); background-size: cover; background-position: center;"></div>
        <div class="div-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-8 md:p-12 z-10">
          <div class="tag mb-4" data-i18n="div_a_tag">Division A</div>
          <h3 class="font-heading font-black text-3xl md:text-4xl text-off-white leading-tight mb-3" data-i18n="div_a_title">
            PRECISION<br/>METAL FABRICATION
          </h3>
          <p class="text-silver/75 text-sm leading-relaxed mb-6 max-w-sm" data-i18n="div_a_desc">
            Laser & plasma cutting, stainless steel fabrication, argon welding, orbital welding, metal forming, surface finishing, and custom industrial assemblies.
          </p>
          <button class="btn-ghost" data-i18n="div_btn">
            <span>Explore Division</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>
        <div class="absolute top-6 right-6 w-10 h-10 border-t border-r border-auburn/40 group-hover:border-auburn transition-colors z-10"></div>
      </div>

      <!-- Division B -->
      <div class="div-card h-96 md:h-[520px] reveal reveal-delay-2 group cursor-pointer border border-silver/10 hover:border-auburn/50 transition-colors">
        <div class="div-card-bg"
          style="background-image: linear-gradient(135deg, rgba(13,13,13,0.3) 0%, rgba(13,13,13,0.1) 100%), url('https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=900&q=80'); background-size: cover; background-position: center;"></div>
        <div class="div-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-8 md:p-12 z-10">
          <div class="tag mb-4" data-i18n="div_b_tag">Division B</div>
          <h3 class="font-heading font-black text-3xl md:text-4xl text-off-white leading-tight mb-3" data-i18n="div_b_title">
            INDUSTRIAL<br/>ENGINEERING SOLUTIONS
          </h3>
          <p class="text-silver/75 text-sm leading-relaxed mb-6 max-w-sm" data-i18n="div_b_desc">
            Stainless steel tanks, process vessels, industrial piping, heat exchangers, production lines, CIP/SIP systems, and custom machinery from engineering to installation.
          </p>
          <button class="btn-ghost" data-i18n="div_btn">
            <span>Explore Division</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>
        <div class="absolute top-6 right-6 w-10 h-10 border-t border-r border-auburn/40 group-hover:border-auburn transition-colors z-10"></div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 04 — MANUFACTURING CAPABILITIES
══════════════════════════════════════════ -->
<section id="capabilities" class="py-24 bg-gunmetal/60 tech-grid-fine">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
      <div>
        <div class="section-label mb-4" data-i18n="cap_label">What We Do</div>
        <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
          <span data-i18n="cap_h2_1">MANUFACTURING</span><br/>
          <span class="text-auburn" data-i18n="cap_h2_2">CAPABILITIES</span>
        </h2>
      </div>
      <p class="text-silver/70 text-sm leading-relaxed max-w-sm" data-i18n="cap_intro">
        A complete manufacturing and engineering capability set built on two decades of industrial experience with certified stainless steel materials.
      </p>
    </div>

    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 8 Cap Cards -->
      <div class="cap-card p-6 reveal group">
        <div class="cap-icon mb-4"><i data-lucide="zap" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_1_t">LASER & PLASMA CUTTING</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_1_d">High-precision cutting for complex profiles in carbon steel, stainless steel, and aluminum sheets.</p>
      </div>

      <div class="cap-card p-6 reveal reveal-delay-1 group">
        <div class="cap-icon mb-4"><i data-lucide="box" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_2_t">STAINLESS STEEL FABRICATION</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_2_d">Custom stainless fabrication in 304 and 316L — hoppers, furniture, panels, platforms, and assemblies.</p>
      </div>

      <div class="cap-card p-6 reveal reveal-delay-2 group">
        <div class="cap-icon mb-4"><i data-lucide="git-branch" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_3_t">METAL FORMING & BENDING</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_3_d">Sheet metal forming and CNC bending for custom structural and functional components.</p>
      </div>

      <div class="cap-card p-6 reveal reveal-delay-3 group">
        <div class="cap-icon mb-4"><i data-lucide="flame" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_4_t">SPECIALIZED WELDING</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_4_d">Manual argon welding and automated orbital welding for hygienic, zero-defect joints in critical applications.</p>
      </div>

      <div class="cap-card p-6 reveal group">
        <div class="cap-icon mb-4"><i data-lucide="sparkles" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_5_t">SURFACE FINISHING</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_5_d">Mechanical polishing, mirror finishing, pickling, and passivation for maximum corrosion resistance and hygiene.</p>
      </div>

      <div class="cap-card p-6 reveal reveal-delay-1 group">
        <div class="cap-icon mb-4"><i data-lucide="cylinder" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_6_t">TANKS & VESSELS</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_6_d">Storage tanks, mixing vessels, process containers, and CIP units for pharmaceutical, food, and industrial use.</p>
      </div>

      <div class="cap-card p-6 reveal reveal-delay-2 group">
        <div class="cap-icon mb-4"><i data-lucide="workflow" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_7_t">INDUSTRIAL PIPING</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_7_d">Sanitary and industrial piping networks including purified water, WFI, pure steam, and CIP/SIP systems.</p>
      </div>

      <div class="cap-card p-6 reveal reveal-delay-3 group">
        <div class="cap-icon mb-4"><i data-lucide="settings" class="w-7 h-7"></i></div>
        <h4 class="font-heading font-bold text-lg text-off-white mb-2 tracking-wide" data-i18n="cap_8_t">PRODUCTION LINES & CONVEYORS</h4>
        <p class="text-silver/60 text-xs leading-relaxed" data-i18n="cap_8_d">Custom conveyor systems, material handling equipment, and complete production line integration and installation.</p>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 05 — INDUSTRIAL ENGINEERING FEATURE
══════════════════════════════════════════ -->
<section id="engineering" class="py-24 bg-rich-black overflow-hidden">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid lg:grid-cols-2 gap-16 items-center">
      <!-- Text -->
      <div class="reveal">
        <div class="section-label mb-6" data-i18n="eng_label">Division B — Industrial Engineering</div>
        <h2 class="font-heading font-black leading-none mb-8 text-off-white" style="font-size: clamp(2.5rem, 5vw, 4.5rem);">
          <span data-i18n="eng_h2_1">ENGINEERED AROUND</span><br/>
          <span class="text-auburn" data-i18n="eng_h2_2">YOUR PROCESS.</span>
        </h2>
        <p class="text-silver/75 leading-relaxed mb-8 text-sm" data-i18n="eng_p">
          Steel Technology designs, fabricates, and installs complete industrial engineering systems. From single process vessels to fully integrated production lines, every solution is engineered to your exact process requirements.
        </p>
        <div class="grid grid-cols-2 gap-4 mb-10">
          <div class="why-card py-2">
            <div class="font-heading font-semibold text-sm text-off-white tracking-wide mb-1" data-i18n="eng_item1_t">Tanks & Process Vessels</div>
            <div class="text-silver/55 text-xs" data-i18n="eng_item1_d">Storage, mixing, jacketed, pressure</div>
          </div>
          <div class="why-card py-2">
            <div class="font-heading font-semibold text-sm text-off-white tracking-wide mb-1" data-i18n="eng_item2_t">Heat Exchangers</div>
            <div class="text-silver/55 text-xs" data-i18n="eng_item2_d">Thermal processing & energy efficiency</div>
          </div>
          <div class="why-card py-2">
            <div class="font-heading font-semibold text-sm text-off-white tracking-wide mb-1" data-i18n="eng_item3_t">Piping & Utilities</div>
            <div class="text-silver/55 text-xs" data-i18n="eng_item3_d">WFI, pure steam, CIP/SIP networks</div>
          </div>
          <div class="why-card py-2">
            <div class="font-heading font-semibold text-sm text-off-white tracking-wide mb-1" data-i18n="eng_item4_t">Production Lines</div>
            <div class="text-silver/55 text-xs" data-i18n="eng_item4_d">Custom machinery & conveyors</div>
          </div>
          <div class="why-card py-2">
            <div class="font-heading font-semibold text-sm text-off-white tracking-wide mb-1" data-i18n="eng_item5_t">CIP/SIP Systems</div>
            <div class="text-silver/55 text-xs" data-i18n="eng_item5_d">Hygienic cleaning-in-place units</div>
          </div>
          <div class="why-card py-2">
            <div class="font-heading font-semibold text-sm text-off-white tracking-wide mb-1" data-i18n="eng_item6_t">Installation & Maintenance</div>
            <div class="text-silver/55 text-xs" data-i18n="eng_item6_d">Site commissioning & long-term support</div>
          </div>
        </div>
        <a href="#contact" class="btn-primary">
          <span data-i18n="eng_btn">Discuss Your Project</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>

      <!-- Image collage -->
      <div class="reveal reveal-delay-2 relative">
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1565793298595-6a879b1d9492?w=700&q=80"
            alt="Industrial engineering — stainless steel tanks"
            class="w-full h-80 object-cover"
            style="filter: brightness(0.75) saturate(0.9);"
          />
          <div class="absolute inset-0 border border-auburn/20"></div>
          <div class="absolute bottom-0 left-0 bg-gunmetal border border-auburn/30 px-5 py-3">
            <div class="font-heading font-black text-2xl text-auburn">SS 304 / 316L</div>
            <div class="font-heading text-xs tracking-widest uppercase text-silver/60" data-i18n="badge_cert">Certified Materials</div>
          </div>
        </div>
        <div class="absolute -bottom-8 -right-6 w-48 h-36 overflow-hidden border-2 border-gunmetal shadow-2xl hidden md:block">
          <img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=400&q=80"
            alt="Industrial piping"
            class="w-full h-full object-cover"
            style="filter: brightness(0.6);"
          />
        </div>
        <div class="absolute -top-4 -left-4 w-20 h-20 border-t-2 border-l-2 border-auburn/30"></div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 06 — EQUIPMENT CATALOG
══════════════════════════════════════════ -->
<section id="catalog" class="py-24 bg-gunmetal/40 tech-grid">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
      <div>
        <div class="section-label mb-4" data-i18n="cat_label">Equipment Catalog</div>
        <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
          <span data-i18n="cat_h2_1">INDUSTRIAL</span><br/>
          <span class="text-auburn" data-i18n="cat_h2_2">EQUIPMENT SHOWCASE</span>
        </h2>
      </div>
      <a href="#contact" class="btn-outline self-start md:self-auto">
        <span data-i18n="cat_btn_all">Browse Full Catalog</span>
        <i data-lucide="arrow-right" class="w-4 h-4"></i>
      </a>
    </div>

    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- 5 Categories + CTA Tile -->
      <div class="eq-card reveal overflow-hidden group">
        <div class="overflow-hidden h-52">
          <img src="https://images.unsplash.com/photo-1565793298595-6a879b1d9492?w=600&q=80" alt="Storage Tanks"
            class="w-full h-full object-cover eq-card-img" style="filter: brightness(0.6);" />
        </div>
        <div class="p-6">
          <div class="tag mb-3" data-i18n="cat_tag_1">Category 01</div>
          <h4 class="font-heading font-bold text-xl text-off-white mb-2 tracking-wide" data-i18n="cat_1_t">STORAGE & TRANSPORT TANKS</h4>
          <p class="text-silver/60 text-xs leading-relaxed mb-5" data-i18n="cat_1_d">IBC totes, cylindrical storage tanks, vertical tanks, and eccentric-bottom tanks for liquid products, hazardous materials, and thick liquids.</p>
          <button class="btn-ghost text-xs"><span data-i18n="cat_card_btn">Explore Products</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <div class="eq-card reveal reveal-delay-1 overflow-hidden group">
        <div class="overflow-hidden h-52">
          <img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=600&q=80" alt="Mixing Equipment"
            class="w-full h-full object-cover eq-card-img" style="filter: brightness(0.5);" />
        </div>
        <div class="p-6">
          <div class="tag mb-3" data-i18n="cat_tag_2">Category 02</div>
          <h4 class="font-heading font-bold text-xl text-off-white mb-2 tracking-wide" data-i18n="cat_2_t">MIXING & HEATING EQUIPMENT</h4>
          <p class="text-silver/60 text-xs leading-relaxed mb-5" data-i18n="cat_2_d">Liquid mixing tanks, electric heating tanks, agitator vessels, and pneumatic mixer tanks from 100L to 2000L for food, chemical, and pharma applications.</p>
          <button class="btn-ghost text-xs"><span data-i18n="cat_card_btn">Explore Products</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <div class="eq-card reveal reveal-delay-2 overflow-hidden group">
        <div class="overflow-hidden h-52">
          <img src="https://images.unsplash.com/photo-1587293852726-70cdb56c2866?w=600&q=80" alt="Food Processing"
            class="w-full h-full object-cover eq-card-img" style="filter: brightness(0.5);" />
        </div>
        <div class="p-6">
          <div class="tag mb-3" data-i18n="cat_tag_3">Category 03</div>
          <h4 class="font-heading font-bold text-xl text-off-white mb-2 tracking-wide" data-i18n="cat_3_t">FOOD, DAIRY & COSMETIC PROCESSING</h4>
          <p class="text-silver/60 text-xs leading-relaxed mb-5" data-i18n="cat_3_d">Sanitary mixing tanks, steam-jacketed kettles, planetary mixers, cheese vats, and specialized production lines for hygiene-critical sectors.</p>
          <button class="btn-ghost text-xs"><span data-i18n="cat_card_btn">Explore Products</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <div class="eq-card reveal overflow-hidden group">
        <div class="overflow-hidden h-52">
          <img src="https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=600&q=80" alt="Conveyors"
            class="w-full h-full object-cover eq-card-img" style="filter: brightness(0.5);" />
        </div>
        <div class="p-6">
          <div class="tag mb-3" data-i18n="cat_tag_4">Category 04</div>
          <h4 class="font-heading font-bold text-xl text-off-white mb-2 tracking-wide" data-i18n="cat_4_t">CONVEYORS & MATERIAL HANDLING</h4>
          <p class="text-silver/60 text-xs leading-relaxed mb-5" data-i18n="cat_4_d">Screw feeders, screw conveyors, tubular and U-type designs, shaftless configurations for bulk material handling in clean and industrial environments.</p>
          <button class="btn-ghost text-xs"><span data-i18n="cat_card_btn">Explore Products</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <div class="eq-card reveal reveal-delay-1 overflow-hidden group">
        <div class="overflow-hidden h-52">
          <img src="https://images.unsplash.com/photo-1573164574001-518958d9baa2?w=600&q=80" alt="Process Equipment"
            class="w-full h-full object-cover eq-card-img" style="filter: brightness(0.5);" />
        </div>
        <div class="p-6">
          <div class="tag mb-3" data-i18n="cat_tag_5">Category 05</div>
          <h4 class="font-heading font-bold text-xl text-off-white mb-2 tracking-wide" data-i18n="cat_5_t">PROCESS EQUIPMENT</h4>
          <p class="text-silver/60 text-xs leading-relaxed mb-5" data-i18n="cat_5_d">Chemical storage tanks, FRP tanks, powder storage, dry bulk containers, and chemical mixing units for industrial and manufacturing applications.</p>
          <button class="btn-ghost text-xs"><span data-i18n="cat_card_btn">Explore Products</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <!-- CTA Tile -->
      <div class="eq-card reveal reveal-delay-2 p-8 flex flex-col justify-between" style="background: linear-gradient(135deg, rgba(158,39,46,0.15) 0%, rgba(38,42,50,0.85) 100%); border-color: rgba(158,39,46,0.35);">
        <div>
          <div class="font-heading font-black text-3xl text-off-white mb-4 leading-tight" data-i18n="cat_custom_t">CUSTOM INDUSTRIAL EQUIPMENT?</div>
          <p class="text-silver/70 text-sm leading-relaxed mb-6" data-i18n="cat_custom_d">Don't see what you need? Steel Technology specializes in bespoke industrial equipment designed and engineered to your exact factory specifications.</p>
        </div>
        <a href="#contact" class="btn-primary self-start text-sm">
          <span data-i18n="cat_custom_btn">Request Custom Build</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 07 — REVERSE ENGINEERING
══════════════════════════════════════════ -->
<section id="reverse-eng" class="py-24 bg-rich-black re-grid overflow-hidden border-y border-silver/10">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid lg:grid-cols-2 gap-16 items-center">
      <!-- Visual side -->
      <div class="reveal relative order-2 lg:order-1">
        <div class="relative bg-gunmetal border border-bluebell/20 p-1">
          <img src="https://images.unsplash.com/photo-1518432031352-d6fc5c10da5a?w=700&q=80"
            alt="3D scanning and reverse engineering"
            class="w-full h-72 object-cover"
            style="filter: brightness(0.5) saturate(0.4);"
          />
          <div class="absolute inset-1 border border-bluebell/15 pointer-events-none"></div>
          <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
            <div class="relative w-32 h-32">
              <div class="absolute inset-0 border border-bluebell/30 rotate-45"></div>
              <div class="absolute top-1/2 left-0 right-0 h-px bg-bluebell/25"></div>
              <div class="absolute left-1/2 top-0 bottom-0 w-px bg-bluebell/25"></div>
              <div class="absolute inset-6 border border-auburn/40 rounded-full"></div>
            </div>
          </div>
          <div class="absolute top-3 left-3 font-heading text-xs text-bluebell/60 tracking-widest">SCAN.001</div>
          <div class="absolute top-3 right-3 font-heading text-xs text-bluebell/60 tracking-widest">∅ ±0.01mm</div>
          <div class="absolute bottom-3 left-3 font-heading text-xs text-silver/50 tracking-widest" data-i18n="re_scan_tag">3D GEOMETRY CAPTURE</div>
        </div>
        <div class="absolute -bottom-6 -left-6 w-24 h-24 border-b-2 border-l-2 border-auburn/30"></div>
      </div>

      <!-- Text -->
      <div class="reveal reveal-delay-2 order-1 lg:order-2">
        <div class="section-label mb-6" style="color: #99A0CB;">
          <span style="background: #99A0CB; width: 24px; height: 1px; display: inline-block; margin-right: 10px; vertical-align: middle;"></span>
          <span data-i18n="re_label">Strategic Innovation Capability</span>
        </div>
        <h2 class="font-heading font-black leading-none mb-6 text-off-white" style="font-size: clamp(2.2rem, 4.5vw, 4rem);">
          <span data-i18n="re_h2_1">REVERSE ENGINEERING.</span><br/>
          <span style="color: #99A0CB;" data-i18n="re_h2_2">REAL-WORLD SOLUTIONS.</span>
        </h2>
        <p class="text-silver/75 leading-relaxed mb-8 text-sm" data-i18n="re_p">
          When imported machinery requires localization or legacy equipment needs replacement components, Steel Technology captures exact geometries to reverse-engineer and locally manufacture critical parts — eliminating supply chain delays and foreign currency burdens.
        </p>
        <div class="space-y-4 mb-10">
          <div class="flex items-start gap-4">
            <div class="w-6 h-px bg-bluebell/60 mt-3 flex-shrink-0"></div>
            <div>
              <div class="font-heading font-semibold text-sm text-off-white tracking-wide" data-i18n="re_item1_t">3D Measurement & Geometry Capture</div>
              <div class="text-silver/60 text-xs mt-1" data-i18n="re_item1_d">High-fidelity dimensional scanning of existing complex parts in minutes.</div>
            </div>
          </div>
          <div class="flex items-start gap-4">
            <div class="w-6 h-px bg-bluebell/60 mt-3 flex-shrink-0"></div>
            <div>
              <div class="font-heading font-semibold text-sm text-off-white tracking-wide" data-i18n="re_item2_t">CAD Modeling & Engineering Modifications</div>
              <div class="text-silver/60 text-xs mt-1" data-i18n="re_item2_d">Translation of physical geometry to digital twins with structural stress optimizations.</div>
            </div>
          </div>
          <div class="flex items-start gap-4">
            <div class="w-6 h-px bg-bluebell/60 mt-3 flex-shrink-0"></div>
            <div>
              <div class="font-heading font-semibold text-sm text-off-white tracking-wide" data-i18n="re_item3_t">Local Manufacturing & Equipment Localization</div>
              <div class="text-silver/60 text-xs mt-1" data-i18n="re_item3_d">Flawless, zero-tolerance fit when components integrate into legacy production lines.</div>
            </div>
          </div>
        </div>
        <a href="#contact" class="btn-outline" style="border-color: rgba(153,160,203,0.4); color: #99A0CB;">
          <span data-i18n="re_btn">Discuss Reverse Engineering Project</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 08 — INDUSTRIES WE SERVE
══════════════════════════════════════════ -->
<section id="industries" class="py-24 bg-gunmetal/50 tech-grid">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal mb-14">
      <div class="section-label mb-4" data-i18n="ind_label">Sectors & Applications</div>
      <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
        <span data-i18n="ind_h2_1">INDUSTRIES</span><br/>
        <span class="text-auburn" data-i18n="ind_h2_2">WE EMPOWER</span>
      </h2>
    </div>

    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- 6 Industry cards -->
      <div class="ind-card reveal group cursor-pointer border border-silver/10">
        <div class="ind-card-bg" style="background-image: url('https://images.unsplash.com/photo-1587017539504-67cfbddac569?w=600&q=80');"></div>
        <div class="ind-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-6 z-10">
          <div class="font-heading font-black text-xl text-off-white tracking-wide mb-1" data-i18n="ind_1_t">PHARMACEUTICALS</div>
          <p class="text-silver/70 text-xs leading-relaxed" data-i18n="ind_1_d">WFI, pure steam, purified water piping, clean room equipment, and hygienic stainless fabrication meeting GMP requirements.</p>
        </div>
      </div>

      <div class="ind-card reveal reveal-delay-1 group cursor-pointer border border-silver/10">
        <div class="ind-card-bg" style="background-image: url('https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?w=600&q=80');"></div>
        <div class="ind-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-6 z-10">
          <div class="font-heading font-black text-xl text-off-white tracking-wide mb-1" data-i18n="ind_2_t">FOOD PROCESSING</div>
          <p class="text-silver/70 text-xs leading-relaxed" data-i18n="ind_2_d">Sanitary piping, mixing tanks, cooking kettles, hoppers, and CIP/SIP systems designed for maximum food safety standards.</p>
        </div>
      </div>

      <div class="ind-card reveal reveal-delay-2 group cursor-pointer border border-silver/10">
        <div class="ind-card-bg" style="background-image: url('https://images.unsplash.com/photo-1563178406-4cdc2923acbc?w=600&q=80');"></div>
        <div class="ind-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-6 z-10">
          <div class="font-heading font-black text-xl text-off-white tracking-wide mb-1" data-i18n="ind_3_t">DAIRY</div>
          <p class="text-silver/70 text-xs leading-relaxed" data-i18n="ind_3_d">Cheese vats, pasteurization tanks, milk storage tanks, and dairy processing equipment with triple-wall insulation and orbital welds.</p>
        </div>
      </div>

      <div class="ind-card reveal group cursor-pointer border border-silver/10">
        <div class="ind-card-bg" style="background-image: url('https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=600&q=80');"></div>
        <div class="ind-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-6 z-10">
          <div class="font-heading font-black text-xl text-off-white tracking-wide mb-1" data-i18n="ind_4_t">COSMETICS</div>
          <p class="text-silver/70 text-xs leading-relaxed" data-i18n="ind_4_d">Specialized mixing tanks for shampoos, gels, creams, and hygiene products. Mirror-finish interiors for hygienic production.</p>
        </div>
      </div>

      <div class="ind-card reveal reveal-delay-1 group cursor-pointer border border-silver/10">
        <div class="ind-card-bg" style="background-image: url('https://images.unsplash.com/photo-1565793298595-6a879b1d9492?w=600&q=80');"></div>
        <div class="ind-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-6 z-10">
          <div class="font-heading font-black text-xl text-off-white tracking-wide mb-1" data-i18n="ind_5_t">INDUSTRIAL MANUFACTURING</div>
          <p class="text-silver/70 text-xs leading-relaxed" data-i18n="ind_5_d">Custom fabrication, industrial platforms, structural steel, ducting, skids, and mechanical assemblies for heavy industrial facilities.</p>
        </div>
      </div>

      <div class="ind-card reveal reveal-delay-2 group cursor-pointer border border-silver/10">
        <div class="ind-card-bg" style="background-image: url('https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=600&q=80');"></div>
        <div class="ind-card-overlay"></div>
        <div class="relative h-full flex flex-col justify-end p-6 z-10">
          <div class="font-heading font-black text-xl text-off-white tracking-wide mb-1" data-i18n="ind_6_t">WATER & UTILITY SYSTEMS</div>
          <p class="text-silver/70 text-xs leading-relaxed" data-i18n="ind_6_d">Multimedia filters, heat exchangers, utility piping networks, and water treatment skids for industrial and utility applications.</p>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 09 — WHY STEEL TECHNOLOGY
══════════════════════════════════════════ -->
<section id="why" class="py-24 bg-rich-black tech-grid-fine">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal mb-14 text-center max-w-2xl mx-auto">
      <div class="section-label mb-4 justify-center" data-i18n="why_label">Why Partner With Us</div>
      <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
        <span data-i18n="why_h2_1">WHY STEEL</span><br/>
        <span class="text-auburn" data-i18n="why_h2_2">TECHNOLOGY</span>
      </h2>
    </div>

    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="why-card reveal py-4">
        <div class="text-auburn font-heading font-black text-4xl mb-3">01</div>
        <h4 class="font-heading font-bold text-xl text-off-white tracking-wide mb-2" data-i18n="why_1_t">20 YEARS OF EXPERTISE</h4>
        <p class="text-silver/65 text-sm leading-relaxed" data-i18n="why_1_d">Two decades of industrial manufacturing experience across Egypt's most demanding sectors — pharmaceutical, food, dairy, and heavy industry.</p>
      </div>
      <div class="why-card reveal reveal-delay-1 py-4">
        <div class="text-auburn font-heading font-black text-4xl mb-3">02</div>
        <h4 class="font-heading font-bold text-xl text-off-white tracking-wide mb-2" data-i18n="why_2_t">CUSTOM-BUILT SOLUTIONS</h4>
        <p class="text-silver/65 text-sm leading-relaxed" data-i18n="why_2_d">Every project is designed around your specific process requirements. No off-the-shelf answers — only engineered solutions built for your application.</p>
      </div>
      <div class="why-card reveal reveal-delay-2 py-4">
        <div class="text-auburn font-heading font-black text-4xl mb-3">03</div>
        <h4 class="font-heading font-bold text-xl text-off-white tracking-wide mb-2" data-i18n="why_3_t">ENGINEERING UNDER ONE ROOF</h4>
        <p class="text-silver/65 text-sm leading-relaxed" data-i18n="why_3_d">From precision fabrication to complete industrial systems, Steel Technology unifies engineering, manufacturing, and installation in a single, accountable partner.</p>
      </div>
      <div class="why-card reveal py-4">
        <div class="text-auburn font-heading font-black text-4xl mb-3">04</div>
        <h4 class="font-heading font-bold text-xl text-off-white tracking-wide mb-2" data-i18n="why_4_t">CERTIFIED MATERIALS ONLY</h4>
        <p class="text-silver/65 text-sm leading-relaxed" data-i18n="why_4_d">All fabrication uses certified stainless steel 304 and 316L grades, ensuring corrosion resistance, longevity, and regulatory compliance for hygienic applications.</p>
      </div>
      <div class="why-card reveal reveal-delay-1 py-4">
        <div class="text-auburn font-heading font-black text-4xl mb-3">05</div>
        <h4 class="font-heading font-bold text-xl text-off-white tracking-wide mb-2" data-i18n="why_5_t">FROM FABRICATION TO INSTALLATION</h4>
        <p class="text-silver/65 text-sm leading-relaxed" data-i18n="why_5_d">Steel Technology handles full project delivery — from initial engineering design through fabrication, site installation, commissioning, and ongoing maintenance support.</p>
      </div>
      <div class="why-card reveal reveal-delay-2 py-4">
        <div class="text-auburn font-heading font-black text-4xl mb-3">06</div>
        <h4 class="font-heading font-bold text-xl text-off-white tracking-wide mb-2" data-i18n="why_6_t">KNOWLEDGE OF DEMANDING APPLICATIONS</h4>
        <p class="text-silver/65 text-sm leading-relaxed" data-i18n="why_6_d">Deep technical understanding of GMP manufacturing, hygienic process design, pharmaceutical-grade piping, and clean room-compatible fabrication requirements.</p>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 10 — PROJECT PORTFOLIO
══════════════════════════════════════════ -->
<section id="projects" class="py-24 bg-gunmetal/60 tech-grid">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal flex flex-col md:flex-row md:items-end justify-between mb-14 gap-6">
      <div>
        <div class="section-label mb-4" data-i18n="proj_label">Our Track Record</div>
        <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
          <span data-i18n="proj_h2_1">PROJECT</span><br/>
          <span class="text-auburn" data-i18n="proj_h2_2">PORTFOLIO</span>
        </h2>
      </div>
      <p class="text-silver/65 text-sm max-w-sm leading-relaxed" data-i18n="proj_intro">
        A selection of manufacturing and engineering projects delivered for clients across Egypt's industrial sectors.
      </p>
    </div>

    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
      <!-- Project placeholder cards -->
      <div class="proj-card reveal group">
        <div class="h-56 bg-gunmetal flex items-center justify-center border-b border-silver/10 relative overflow-hidden">
          <div class="absolute inset-0 tech-grid opacity-50"></div>
          <div class="relative text-center">
            <i data-lucide="image" class="w-10 h-10 text-silver/20 mx-auto mb-2"></i>
            <div class="font-heading text-xs text-silver/40 tracking-widest uppercase" data-i18n="proj_ph">Verified Project Asset</div>
          </div>
        </div>
        <div class="p-6">
          <div class="flex gap-2 mb-3">
            <span class="tag text-bluebell/80" style="border-color: rgba(153,160,203,0.3);" data-i18n="proj_1_tag">Pharmaceutical</span>
          </div>
          <h4 class="font-heading font-bold text-lg text-off-white mb-1 tracking-wide" data-i18n="proj_1_t">WFI & PURIFIED WATER PIPING</h4>
          <p class="text-silver/60 text-xs mb-4 leading-relaxed" data-i18n="proj_1_d">Sanitary piping network with automated orbital welding, passivation, and full qualification support.</p>
          <button class="btn-ghost text-xs"><span data-i18n="proj_btn">View Project</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <div class="proj-card reveal reveal-delay-1 group">
        <div class="h-56 bg-gunmetal flex items-center justify-center border-b border-silver/10 relative overflow-hidden">
          <div class="absolute inset-0 tech-grid opacity-50"></div>
          <div class="relative text-center">
            <i data-lucide="image" class="w-10 h-10 text-silver/20 mx-auto mb-2"></i>
            <div class="font-heading text-xs text-silver/40 tracking-widest uppercase" data-i18n="proj_ph">Verified Project Asset</div>
          </div>
        </div>
        <div class="p-6">
          <div class="flex gap-2 mb-3">
            <span class="tag text-bluebell/80" style="border-color: rgba(153,160,203,0.3);" data-i18n="proj_2_tag">Food & Dairy</span>
          </div>
          <h4 class="font-heading font-bold text-lg text-off-white mb-1 tracking-wide" data-i18n="proj_2_t">MIXING TANKS & CIP SKID UNIT</h4>
          <p class="text-silver/60 text-xs mb-4 leading-relaxed" data-i18n="proj_2_d">Insulated stainless steel mixing vessels and automatic clean-in-place unit engineered for dairy processing.</p>
          <button class="btn-ghost text-xs"><span data-i18n="proj_btn">View Project</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>

      <div class="proj-card reveal reveal-delay-2 group">
        <div class="h-56 bg-gunmetal flex items-center justify-center border-b border-silver/10 relative overflow-hidden">
          <div class="absolute inset-0 tech-grid opacity-50"></div>
          <div class="relative text-center">
            <i data-lucide="image" class="w-10 h-10 text-silver/20 mx-auto mb-2"></i>
            <div class="font-heading text-xs text-silver/40 tracking-widest uppercase" data-i18n="proj_ph">Verified Project Asset</div>
          </div>
        </div>
        <div class="p-6">
          <div class="flex gap-2 mb-3">
            <span class="tag text-bluebell/80" style="border-color: rgba(153,160,203,0.3);" data-i18n="proj_3_tag">Industrial</span>
          </div>
          <h4 class="font-heading font-bold text-lg text-off-white mb-1 tracking-wide" data-i18n="proj_3_t">CUSTOM PLATFORMS & VENTILATION DUCTING</h4>
          <p class="text-silver/60 text-xs mb-4 leading-relaxed" data-i18n="proj_3_d">Custom structural stainless steel platforms, handrails, motorized gates, and heavy industrial ducting.</p>
          <button class="btn-ghost text-xs"><span data-i18n="proj_btn">View Project</span> <i data-lucide="arrow-right" class="w-3 h-3"></i></button>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 11 — HOW WE WORK
══════════════════════════════════════════ -->
<section id="process" class="py-24 bg-rich-black tech-grid-fine">
  <div class="max-w-7xl mx-auto px-6">
    <div class="reveal mb-16 text-center">
      <div class="section-label justify-center mb-4" data-i18n="proc_label">Our Engineering Methodology</div>
      <h2 class="font-heading font-black text-5xl md:text-6xl text-off-white leading-none">
        <span data-i18n="proc_h2_1">HOW WE</span><br/>
        <span class="text-auburn" data-i18n="proc_h2_2">DELIVER EXCELLENCE</span>
      </h2>
    </div>

    <div class="relative">
      <div class="hidden lg:block absolute top-9 left-[10%] right-[10%] h-px bg-silver/15 z-0"></div>

      <div class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-5 gap-8 relative z-10">
        <div class="reveal flex flex-col items-center text-center">
          <div class="w-16 h-16 rounded-full border-2 border-auburn/40 flex items-center justify-center mb-5 bg-rich-black">
            <i data-lucide="message-square" class="w-6 h-6 text-auburn"></i>
          </div>
          <div class="font-heading font-black text-auburn text-xs tracking-widest uppercase mb-2">01</div>
          <h4 class="font-heading font-bold text-base text-off-white tracking-wide mb-2" data-i18n="proc_1_t">CONSULTATION</h4>
          <p class="text-silver/60 text-xs leading-relaxed" data-i18n="proc_1_d">Share your requirements, drawings, or process brief. Our engineering team reviews feasibility and technical parameters.</p>
        </div>
        <div class="reveal reveal-delay-1 flex flex-col items-center text-center">
          <div class="w-16 h-16 rounded-full border-2 border-auburn/40 flex items-center justify-center mb-5 bg-rich-black">
            <i data-lucide="file-search" class="w-6 h-6 text-auburn"></i>
          </div>
          <div class="font-heading font-black text-auburn text-xs tracking-widest uppercase mb-2">02</div>
          <h4 class="font-heading font-bold text-base text-off-white tracking-wide mb-2" data-i18n="proc_2_t">TECHNICAL REVIEW</h4>
          <p class="text-silver/60 text-xs leading-relaxed" data-i18n="proc_2_d">Our engineers analyze your drawings and generate detailed engineering blueprints, material specs, and quotation.</p>
        </div>
        <div class="reveal reveal-delay-2 flex flex-col items-center text-center">
          <div class="w-16 h-16 rounded-full border-2 border-auburn/40 flex items-center justify-center mb-5 bg-rich-black">
            <i data-lucide="settings-2" class="w-6 h-6 text-auburn"></i>
          </div>
          <div class="font-heading font-black text-auburn text-xs tracking-widest uppercase mb-2">03</div>
          <h4 class="font-heading font-bold text-base text-off-white tracking-wide mb-2" data-i18n="proc_3_t">FABRICATION</h4>
          <p class="text-silver/60 text-xs leading-relaxed" data-i18n="proc_3_d">Precision manufacturing using certified stainless steel 304/316L, controlled welding, and rigorous QA inspections.</p>
        </div>
        <div class="reveal reveal-delay-3 flex flex-col items-center text-center">
          <div class="w-16 h-16 rounded-full border-2 border-auburn/40 flex items-center justify-center mb-5 bg-rich-black">
            <i data-lucide="truck" class="w-6 h-6 text-auburn"></i>
          </div>
          <div class="font-heading font-black text-auburn text-xs tracking-widest uppercase mb-2">04</div>
          <h4 class="font-heading font-bold text-base text-off-white tracking-wide mb-2" data-i18n="proc_4_t">INSTALLATION</h4>
          <p class="text-silver/60 text-xs leading-relaxed" data-i18n="proc_4_d">On-site mechanical and piping installation, equipment assembly, pressure testing, and final plant commissioning.</p>
        </div>
        <div class="reveal reveal-delay-4 flex flex-col items-center text-center">
          <div class="w-16 h-16 rounded-full border-2 border-auburn/40 flex items-center justify-center mb-5 bg-rich-black">
            <i data-lucide="headphones" class="w-6 h-6 text-auburn"></i>
          </div>
          <div class="font-heading font-black text-auburn text-xs tracking-widest uppercase mb-2">05</div>
          <h4 class="font-heading font-bold text-base text-off-white tracking-wide mb-2" data-i18n="proc_5_t">SUPPORT</h4>
          <p class="text-silver/60 text-xs leading-relaxed" data-i18n="proc_5_d">Ongoing maintenance partnerships, equipment modifications, efficiency enhancement, and prompt technical support.</p>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 12 — CONTACT / RFQ
══════════════════════════════════════════ -->
<section id="contact" class="py-24 bg-gunmetal relative overflow-hidden tech-grid">
  <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-auburn/50 to-transparent"></div>
  <div class="absolute -top-32 -right-32 w-96 h-96 rounded-full bg-auburn/5 blur-3xl pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-6">
    <div class="grid lg:grid-cols-2 gap-16">
      <!-- Left — Headline & contact info -->
      <div class="reveal">
        <div class="section-label mb-6" data-i18n="rfq_label">Start a Project</div>
        <h2 class="font-heading font-black leading-none mb-6 text-off-white" style="font-size: clamp(2.5rem, 5vw, 4.5rem);">
          <span data-i18n="rfq_h2_1">LET'S ENGINEER</span><br/>
          <span class="text-auburn" data-i18n="rfq_h2_2">YOUR NEXT</span><br/>
          <span data-i18n="rfq_h2_3">INDUSTRIAL SOLUTION.</span>
        </h2>
        <p class="text-silver/70 leading-relaxed mb-10 text-sm max-w-sm" data-i18n="rfq_p">
          From precision metal components to complete industrial systems, share your requirements and let our engineering team help bring your project to life.
        </p>

        <!-- Direct Channels -->
        <div class="space-y-5 mb-10">
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 border border-auburn/30 flex items-center justify-center flex-shrink-0">
              <i data-lucide="phone" class="w-4 h-4 text-auburn"></i>
            </div>
            <div>
              <div class="font-heading text-xs tracking-widest uppercase text-silver/50 mb-0.5" data-i18n="rfq_phone_label">Sales & Technical Inquiries</div>
              <div class="font-body text-off-white text-sm font-semibold">01018868858 &nbsp;|&nbsp; 01070772356</div>
            </div>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 border border-auburn/30 flex items-center justify-center flex-shrink-0">
              <i data-lucide="mail" class="w-4 h-4 text-auburn"></i>
            </div>
            <div>
              <div class="font-heading text-xs tracking-widest uppercase text-silver/50 mb-0.5" data-i18n="rfq_email_label">Official Engineering Email</div>
              <a href="mailto:info@steeltechnology-eg.com" class="font-body text-off-white text-sm hover:text-auburn transition-colors">info@steeltechnology-eg.com</a>
            </div>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-10 h-10 border border-auburn/30 flex items-center justify-center flex-shrink-0">
              <i data-lucide="map-pin" class="w-4 h-4 text-auburn"></i>
            </div>
            <div>
              <div class="font-heading text-xs tracking-widest uppercase text-silver/50 mb-0.5" data-i18n="rfq_loc_label">Headquarters & Plant</div>
              <div class="font-body text-off-white text-sm" data-i18n="rfq_loc_val">Cairo, Egypt — Serving all governorates</div>
            </div>
          </div>
        </div>

        <!-- Quick contact action buttons -->
        <div class="flex flex-wrap gap-3">
          <a href="https://wa.me/201018868858?text=Hello%2C%20I%27d%20like%20to%20request%20a%20quote%20for%20Steel%20Technology%20services." target="_blank" class="wa-btn">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
              <path d="M12 0C5.373 0 0 5.373 0 12c0 2.124.555 4.118 1.528 5.845L0 24l6.336-1.504A11.945 11.945 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.822 9.822 0 01-5.011-1.37l-.36-.213-3.76.892.942-3.665-.234-.376A9.818 9.818 0 012.182 12C2.182 6.569 6.569 2.182 12 2.182S21.818 6.569 21.818 12 17.431 21.818 12 21.818z"/>
            </svg>
            <span data-i18n="rfq_btn_wa">Direct WhatsApp</span>
          </a>
          <a href="tel:+201018868858" class="btn-outline text-sm py-2.5">
            <i data-lucide="phone" class="w-4 h-4"></i>
            <span data-i18n="rfq_btn_call">Call Sales</span>
          </a>
        </div>
      </div>

      <!-- Right — RFQ Form -->
      <div class="reveal reveal-delay-2">
        <div class="bg-rich-black border border-silver/10 p-8">
          <div class="font-heading font-bold text-xl text-off-white tracking-wide mb-6" data-i18n="form_title">REQUEST FOR QUOTATION</div>

          <form id="rfq-form" class="space-y-5" onsubmit="handleFormSubmit(event)">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="rfq-label" data-i18n="f_name">Full Name *</label>
                <input type="text" class="rfq-input" data-i18n-ph="f_name_ph" placeholder="Your name" required />
              </div>
              <div>
                <label class="rfq-label" data-i18n="f_comp">Company *</label>
                <input type="text" class="rfq-input" data-i18n-ph="f_comp_ph" placeholder="Company name" required />
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="rfq-label" data-i18n="f_phone">Phone *</label>
                <input type="tel" class="rfq-input" placeholder="+20 1XX XXX XXXX" required />
              </div>
              <div>
                <label class="rfq-label" data-i18n="f_email">Email *</label>
                <input type="email" class="rfq-input" placeholder="you@company.com" required />
              </div>
            </div>
            <div>
              <label class="rfq-label" data-i18n="f_type">Project Type *</label>
              <select class="rfq-select" required id="project-type-select">
                <!-- Dynamically localized options -->
              </select>
            </div>
            <div>
              <label class="rfq-label" data-i18n="f_desc">Project Description *</label>
              <textarea class="rfq-input" rows="4" data-i18n-ph="f_desc_ph" placeholder="Describe your project, required quantities, materials, dimensions, and specifications..." required style="resize: vertical;"></textarea>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="rfq-label" data-i18n="f_mat">Material Required</label>
                <input type="text" class="rfq-input" data-i18n-ph="f_mat_ph" placeholder="e.g. SS 316L, 304, Carbon Steel" />
              </div>
              <div>
                <label class="rfq-label" data-i18n="f_qty">Quantity / Volume</label>
                <input type="text" class="rfq-input" data-i18n-ph="f_qty_ph" placeholder="e.g. 5 units, 1000L" />
              </div>
            </div>
            <div>
              <label class="rfq-label" data-i18n="f_draw">Technical Drawings</label>
              <div class="rfq-input border-dashed flex items-center gap-3 cursor-pointer hover:border-auburn/40 transition-colors" onclick="document.getElementById('file-upload').click()">
                <i data-lucide="upload" class="w-4 h-4 text-silver/40"></i>
                <span class="text-silver/50 text-sm" id="file-label" data-i18n="f_draw_ph">Upload PDF, DXF, DWG, STEP files</span>
                <input type="file" id="file-upload" class="hidden" accept=".pdf,.dxf,.dwg,.step,.stp,.iges,.igs" multiple onchange="updateFileLabel(this)" />
              </div>
            </div>

            <button type="submit" class="btn-primary w-full justify-center py-4 mt-2">
              <i data-lucide="send" class="w-4 h-4"></i>
              <span data-i18n="f_submit">Submit Request for Quotation</span>
            </button>
          </form>

          <div id="form-success" class="hidden text-center py-8">
            <i data-lucide="check-circle" class="w-12 h-12 text-auburn mx-auto mb-4"></i>
            <div class="font-heading font-bold text-xl text-off-white mb-2" data-i18n="f_success_t">Request Received</div>
            <p class="text-silver/70 text-sm" data-i18n="f_success_d">Our engineering team will review your specifications and respond with a technical evaluation within 24 hours.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════
     SECTION 13 — FOOTER
══════════════════════════════════════════ -->
<footer class="bg-rich-black border-t border-silver/10">
  <div class="max-w-7xl mx-auto px-6 py-16">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
      <!-- Brand -->
      <div class="lg:col-span-1">
        <div class="flex items-center gap-3 mb-4">
<img src="logo.png" alt="Steel Technology Official Logo" class="w-12 h-12 object-contain drop-shadow-[0_0_14px_rgba(158,39,46,0.25)]" />
          <div>
            <div class="font-heading font-bold text-off-white text-base tracking-wide leading-none" data-i18n="logo_title">STEEL</div>
            <div class="font-heading font-light text-silver text-xs tracking-widest2 leading-none" data-i18n="logo_sub">TECHNOLOGY</div>
          </div>
        </div>
        <p class="text-silver/60 text-xs leading-relaxed mb-5" data-i18n="footer_bio">
          Where Strength Meets Innovation. Twenty years of custom industrial manufacturing, precision stainless steel fabrication, and engineering solutions across Egypt.
        </p>
        <div class="font-heading text-xs text-silver/40 tracking-widest uppercase" data-i18n="footer_est">Egypt — 20+ Years of Excellence</div>
      </div>

      <!-- Manufacturing Services -->
      <div>
        <div class="font-heading font-semibold text-sm tracking-widest uppercase text-silver/60 mb-5" data-i18n="foot_col1_t">Manufacturing Services</div>
        <ul class="space-y-2.5">
          <li><a href="#capabilities" class="footer-link" data-i18n="cap_1_t">Laser & Plasma Cutting</a></li>
          <li><a href="#capabilities" class="footer-link" data-i18n="cap_2_t">Stainless Steel Fabrication</a></li>
          <li><a href="#capabilities" class="footer-link" data-i18n="cap_3_t">Metal Forming & Bending</a></li>
          <li><a href="#capabilities" class="footer-link" data-i18n="cap_4_t">Specialized Welding</a></li>
          <li><a href="#capabilities" class="footer-link" data-i18n="cap_5_t">Surface Finishing</a></li>
          <li><a href="#reverse-eng"  class="footer-link" data-i18n="nav_re">Reverse Engineering</a></li>
        </ul>
      </div>

      <!-- Industrial Solutions -->
      <div>
        <div class="font-heading font-semibold text-sm tracking-widest uppercase text-silver/60 mb-5" data-i18n="foot_col2_t">Industrial Solutions</div>
        <ul class="space-y-2.5">
          <li><a href="#engineering" class="footer-link" data-i18n="eng_item1_t">Tanks & Process Vessels</a></li>
          <li><a href="#engineering" class="footer-link" data-i18n="cap_7_t">Industrial Piping Networks</a></li>
          <li><a href="#engineering" class="footer-link" data-i18n="eng_item2_t">Heat Exchangers</a></li>
          <li><a href="#engineering" class="footer-link" data-i18n="eng_item4_t">Production Lines</a></li>
          <li><a href="#engineering" class="footer-link" data-i18n="eng_item5_t">CIP/SIP Systems</a></li>
          <li><a href="#catalog"    class="footer-link" data-i18n="nav_equip">Equipment Catalog</a></li>
        </ul>
      </div>

      <!-- Contact -->
      <div>
        <div class="font-heading font-semibold text-sm tracking-widest uppercase text-silver/60 mb-5" data-i18n="foot_col3_t">Contact & Inquiries</div>
        <div class="space-y-3">
          <div class="text-silver/60 text-xs">
            <div class="font-heading text-silver/40 tracking-widest uppercase text-xs mb-0.5" data-i18n="foot_phone_t">Phone</div>
            01018868858<br/>01070772356
          </div>
          <div class="text-silver/60 text-xs">
            <div class="font-heading text-silver/40 tracking-widest uppercase text-xs mb-0.5" data-i18n="foot_email_t">Email</div>
            <a href="mailto:info@steeltechnology-eg.com" class="hover:text-auburn transition-colors">info@steeltechnology-eg.com</a>
          </div>
          <div class="text-silver/60 text-xs">
            <div class="font-heading text-silver/40 tracking-widest uppercase text-xs mb-0.5" data-i18n="foot_web_t">Official Website</div>
            <a href="https://steeltechnology-eg.com" class="hover:text-auburn transition-colors">steeltechnology-eg.com</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom bar -->
  <div class="border-t border-silver/8">
    <div class="max-w-7xl mx-auto px-6 py-5 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div class="text-silver/40 text-xs font-heading tracking-wide" data-i18n="copy_right">
        © 2024 Steel Technology Egypt. All rights reserved. Where Strength Meets Innovation.
      </div>
      <div class="flex items-center gap-6">
        <a href="#contact" class="text-auburn/80 hover:text-auburn text-xs font-heading tracking-wide transition-colors" data-i18n="back_top">↑ Back to Top</a>
      </div>
    </div>
  </div>
</footer>


<!-- ══════════════════════════════════════════
     TRANSLATIONS & JAVASCRIPT
══════════════════════════════════════════ -->
<script>
  // ─── COMPLETE I18N DICTIONARY ───
  const translations = {
    en: {
      logo_title: "STEEL",
      logo_sub: "TECHNOLOGY",
      nav_home: "Home",
      nav_about: "About",
      nav_fab: "Metal Fabrication",
      nav_eng: "Industrial Solutions",
      nav_equip: "Equipment",
      nav_proj: "Projects",
      nav_contact: "Contact",
      nav_re: "Reverse Engineering",
      btn_quote: "Request a Quote",
      side_slogan: "Where Strength Meets Innovation",

      hero_eyebrow: "20 Years of Industrial Expertise",
      hero_title_1: "STAINLESS STEEL",
      hero_title_2: "PRECISION.",
      hero_title_3: "INDUSTRIAL POWER.",
      hero_title_4: "ENGINEERED FOR YOUR PROCESS.",
      hero_desc: "Steel Technology delivers custom metal fabrication, stainless steel equipment, and integrated industrial engineering solutions designed around your manufacturing requirements.",
      hero_btn_quote: "Request a Quote",
      hero_btn_explore: "Explore Our Capabilities",
      stat_exp: "Years Experience",
      stat_grades: "Stainless Steel",
      stat_divs: "Business Divisions",
      scroll_text: "Scroll",

      cred_1: "Years of<br/>Experience",
      cred_2: "Certified Stainless<br/>Steel Grades",
      cred_3_title: "Custom<br/>Engineering",
      cred_3: "Solutions<br/>Tailored to You",
      cred_4_title: "Fab to<br/>Install",
      cred_4: "Full-Cycle<br/>Turnkey Delivery",

      clients_label: "Trusted By Leading Companies",
      clients_h2_1: "TRUSTED BY",
      clients_h2_2: "INDUSTRY LEADERS",
      clients_desc: "We are proud to engineer, fabricate, and commission mission-critical stainless steel systems for Egypt's leading multinational and national corporations.",
      cat_fb: "FOOD & BEVERAGE",
      cat_pharma: "PHARMA & MEDICAL",
      cat_chem: "CHEMICALS & INDUSTRIAL",
      cat_eng_serv: "ENGINEERING SERVICES",
      c_marbella: "Marbella Food Industries",
      c_technotaste: "Techno Taste",
      c_albawadi: "Al Bawadi Food Industries",
      c_heinz: "Heinz",
      c_nestle: "Nestlé",
      c_sedico: "Sedico Pharmaceuticals",
      c_october: "October Pharma",
      c_arabpack: "Arab Pharmaceutical Packaging",
      c_henkel: "Henkel",
      c_evergrow: "EverGrow",
      c_intlpaints: "International Paints",
      c_emco: "EMCO",
      c_tmg: "Talaat Moustafa Group (TMG)",


      div_label: "Our Two Business Divisions",
      div_h2_1: "TWO STRENGTHS.",
      div_h2_2: "ONE INTEGRATED PARTNER.",
      div_a_tag: "Division A",
      div_a_title: "PRECISION<br/>METAL FABRICATION",
      div_a_desc: "Laser & plasma cutting, stainless steel fabrication, argon welding, orbital welding, metal forming, surface finishing, and custom industrial assemblies.",
      div_b_tag: "Division B",
      div_b_title: "INDUSTRIAL<br/>ENGINEERING SOLUTIONS",
      div_b_desc: "Stainless steel tanks, process vessels, industrial piping, heat exchangers, production lines, CIP/SIP systems, and custom machinery from engineering to installation.",
      div_btn: "Explore Division",

      cap_label: "What We Do",
      cap_h2_1: "MANUFACTURING",
      cap_h2_2: "CAPABILITIES",
      cap_intro: "A complete manufacturing and engineering capability set built on two decades of industrial experience with certified stainless steel materials.",
      cap_1_t: "LASER & PLASMA CUTTING",
      cap_1_d: "High-precision cutting for complex profiles in carbon steel, stainless steel, and aluminum sheets.",
      cap_2_t: "STAINLESS STEEL FABRICATION",
      cap_2_d: "Custom stainless fabrication in 304 and 316L — hoppers, furniture, panels, platforms, and assemblies.",
      cap_3_t: "METAL FORMING & BENDING",
      cap_3_d: "Sheet metal forming and CNC bending for custom structural and functional components.",
      cap_4_t: "SPECIALIZED WELDING",
      cap_4_d: "Manual argon welding and automated orbital welding for hygienic, zero-defect joints in critical applications.",
      cap_5_t: "SURFACE FINISHING",
      cap_5_d: "Mechanical polishing, mirror finishing, pickling, and passivation for maximum corrosion resistance and hygiene.",
      cap_6_t: "TANKS & VESSELS",
      cap_6_d: "Storage tanks, mixing vessels, process containers, and CIP units for pharmaceutical, food, and industrial use.",
      cap_7_t: "INDUSTRIAL PIPING",
      cap_7_d: "Sanitary and industrial piping networks including purified water, WFI, pure steam, and CIP/SIP systems.",
      cap_8_t: "PRODUCTION LINES & CONVEYORS",
      cap_8_d: "Custom conveyor systems, material handling equipment, and complete production line integration and installation.",

      eng_label: "Division B — Industrial Engineering",
      eng_h2_1: "ENGINEERED AROUND",
      eng_h2_2: "YOUR PROCESS.",
      eng_p: "Steel Technology designs, fabricates, and installs complete industrial engineering systems. From single process vessels to fully integrated production lines, every solution is engineered to your exact process requirements.",
      eng_item1_t: "Tanks & Process Vessels",
      eng_item1_d: "Storage, mixing, jacketed, pressure",
      eng_item2_t: "Heat Exchangers",
      eng_item2_d: "Thermal processing & energy efficiency",
      eng_item3_t: "Piping & Utilities",
      eng_item3_d: "WFI, pure steam, CIP/SIP networks",
      eng_item4_t: "Production Lines",
      eng_item4_d: "Custom machinery & conveyors",
      eng_item5_t: "CIP/SIP Systems",
      eng_item5_d: "Hygienic cleaning-in-place units",
      eng_item6_t: "Installation & Maintenance",
      eng_item6_d: "Site commissioning & long-term support",
      eng_btn: "Discuss Your Project",
      badge_cert: "Certified Materials",

      cat_label: "Equipment Catalog",
      cat_h2_1: "INDUSTRIAL",
      cat_h2_2: "EQUIPMENT SHOWCASE",
      cat_btn_all: "Browse Full Catalog",
      cat_tag_1: "Category 01",
      cat_1_t: "STORAGE & TRANSPORT TANKS",
      cat_1_d: "IBC totes, cylindrical storage tanks, vertical tanks, and eccentric-bottom tanks for liquid products, hazardous materials, and thick liquids.",
      cat_tag_2: "Category 02",
      cat_2_t: "MIXING & HEATING EQUIPMENT",
      cat_2_d: "Liquid mixing tanks, electric heating tanks, agitator vessels, and pneumatic mixer tanks from 100L to 2000L for food, chemical, and pharma applications.",
      cat_tag_3: "Category 03",
      cat_3_t: "FOOD, DAIRY & COSMETIC PROCESSING",
      cat_3_d: "Sanitary mixing tanks, steam-jacketed kettles, planetary mixers, cheese vats, and specialized production lines for hygiene-critical sectors.",
      cat_tag_4: "Category 04",
      cat_4_t: "CONVEYORS & MATERIAL HANDLING",
      cat_4_d: "Screw feeders, screw conveyors, tubular and U-type designs, shaftless configurations for bulk material handling in clean and industrial environments.",
      cat_tag_5: "Category 05",
      cat_5_t: "PROCESS EQUIPMENT",
      cat_5_d: "Chemical storage tanks, FRP tanks, powder storage, dry bulk containers, and chemical mixing units for industrial and manufacturing applications.",
      cat_card_btn: "Explore Products",
      cat_custom_t: "CUSTOM INDUSTRIAL EQUIPMENT?",
      cat_custom_d: "Don't see what you need? Steel Technology specializes in bespoke industrial equipment designed and engineered to your exact factory specifications.",
      cat_custom_btn: "Request Custom Build",

      re_label: "Strategic Innovation Capability",
      re_h2_1: "REVERSE ENGINEERING.",
      re_h2_2: "REAL-WORLD SOLUTIONS.",
      re_p: "When imported machinery requires localization or legacy equipment needs replacement components, Steel Technology captures exact geometries to reverse-engineer and locally manufacture critical parts — eliminating supply chain delays and foreign currency burdens.",
      re_item1_t: "3D Measurement & Geometry Capture",
      re_item1_d: "High-fidelity dimensional scanning of existing complex parts in minutes.",
      re_item2_t: "CAD Modeling & Engineering Modifications",
      re_item2_d: "Translation of physical geometry to digital twins with structural stress optimizations.",
      re_item3_t: "Local Manufacturing & Equipment Localization",
      re_item3_d: "Flawless, zero-tolerance fit when components integrate into legacy production lines.",
      re_btn: "Discuss Reverse Engineering Project",
      re_scan_tag: "3D GEOMETRY CAPTURE",

      ind_label: "Sectors & Applications",
      ind_h2_1: "INDUSTRIES",
      ind_h2_2: "WE EMPOWER",
      ind_1_t: "PHARMACEUTICALS",
      ind_1_d: "WFI, pure steam, purified water piping, clean room equipment, and hygienic stainless fabrication meeting GMP requirements.",
      ind_2_t: "FOOD PROCESSING",
      ind_2_d: "Sanitary piping, mixing tanks, cooking kettles, hoppers, and CIP/SIP systems designed for maximum food safety standards.",
      ind_3_t: "DAIRY",
      ind_3_d: "Cheese vats, pasteurization tanks, milk storage tanks, and dairy processing equipment with triple-wall insulation and orbital welds.",
      ind_4_t: "COSMETICS",
      ind_4_d: "Specialized mixing tanks for shampoos, gels, creams, and hygiene products. Mirror-finish interiors for hygienic production.",
      ind_5_t: "INDUSTRIAL MANUFACTURING",
      ind_5_d: "Custom fabrication, industrial platforms, structural steel, ducting, skids, and mechanical assemblies for heavy industrial facilities.",
      ind_6_t: "WATER & UTILITY SYSTEMS",
      ind_6_d: "Multimedia filters, heat exchangers, utility piping networks, and water treatment skids for industrial and utility applications.",

      why_label: "Why Partner With Us",
      why_h2_1: "WHY STEEL",
      why_h2_2: "TECHNOLOGY",
      why_1_t: "20 YEARS OF EXPERTISE",
      why_1_d: "Two decades of industrial manufacturing experience across Egypt's most demanding sectors — pharmaceutical, food, dairy, and heavy industry.",
      why_2_t: "CUSTOM-BUILT SOLUTIONS",
      why_2_d: "Every project is designed around your specific process requirements. No off-the-shelf answers — only engineered solutions built for your application.",
      why_3_t: "ENGINEERING UNDER ONE ROOF",
      why_3_d: "From precision fabrication to complete industrial systems, Steel Technology unifies engineering, manufacturing, and installation in a single, accountable partner.",
      why_4_t: "CERTIFIED MATERIALS ONLY",
      why_4_d: "All fabrication uses certified stainless steel 304 and 316L grades, ensuring corrosion resistance, longevity, and regulatory compliance for hygienic applications.",
      why_5_t: "FROM FABRICATION TO INSTALLATION",
      why_5_d: "Steel Technology handles full project delivery — from initial engineering design through fabrication, site installation, commissioning, and ongoing maintenance support.",
      why_6_t: "KNOWLEDGE OF DEMANDING APPLICATIONS",
      why_6_d: "Deep technical understanding of GMP manufacturing, hygienic process design, pharmaceutical-grade piping, and clean room-compatible fabrication requirements.",

      proj_label: "Our Track Record",
      proj_h2_1: "PROJECT",
      proj_h2_2: "PORTFOLIO",
      proj_intro: "A selection of manufacturing and engineering projects delivered for clients across Egypt's industrial sectors.",
      proj_ph: "Verified Project Asset",
      proj_1_tag: "Pharmaceutical",
      proj_1_t: "WFI & PURIFIED WATER PIPING",
      proj_1_d: "Sanitary piping network with automated orbital welding, passivation, and full qualification support.",
      proj_2_tag: "Food & Dairy",
      proj_2_t: "MIXING TANKS & CIP SKID UNIT",
      proj_2_d: "Insulated stainless steel mixing vessels and automatic clean-in-place unit engineered for dairy processing.",
      proj_3_tag: "Industrial",
      proj_3_t: "CUSTOM PLATFORMS & DUCTING",
      proj_3_d: "Custom structural stainless steel platforms, handrails, motorized gates, and heavy industrial ducting.",
      proj_btn: "View Project",

      proc_label: "Our Engineering Methodology",
      proc_h2_1: "HOW WE",
      proc_h2_2: "DELIVER EXCELLENCE",
      proc_1_t: "CONSULTATION",
      proc_1_d: "Share your requirements, drawings, or process brief. Our engineering team reviews feasibility and technical parameters.",
      proc_2_t: "TECHNICAL REVIEW",
      proc_2_d: "Our engineers analyze your drawings and generate detailed engineering blueprints, material specs, and quotation.",
      proc_3_t: "FABRICATION",
      proc_3_d: "Precision manufacturing using certified stainless steel 304/316L, controlled welding, and rigorous QA inspections.",
      proc_4_t: "INSTALLATION",
      proc_4_d: "On-site mechanical and piping installation, equipment assembly, pressure testing, and final plant commissioning.",
      proc_5_t: "SUPPORT",
      proc_5_d: "Ongoing maintenance partnerships, equipment modifications, efficiency enhancement, and prompt technical support.",

      rfq_label: "Start a Project",
      rfq_h2_1: "LET'S ENGINEER",
      rfq_h2_2: "YOUR NEXT",
      rfq_h2_3: "INDUSTRIAL SOLUTION.",
      rfq_p: "From precision metal components to complete industrial systems, share your requirements and let our engineering team help bring your project to life.",
      rfq_phone_label: "Sales & Technical Inquiries",
      rfq_email_label: "Official Engineering Email",
      rfq_loc_label: "Headquarters & Plant",
      rfq_loc_val: "Cairo, Egypt — Serving all governorates",
      rfq_btn_wa: "Direct WhatsApp",
      rfq_btn_call: "Call Sales",

      form_title: "REQUEST FOR QUOTATION",
      f_name: "Full Name *",
      f_name_ph: "Your name",
      f_comp: "Company *",
      f_comp_ph: "Company name",
      f_phone: "Phone *",
      f_email: "Email *",
      f_type: "Project Type *",
      f_desc: "Project Description *",
      f_desc_ph: "Describe your project, required quantities, materials, dimensions, and specifications...",
      f_mat: "Material Required",
      f_mat_ph: "e.g. SS 316L, 304, Carbon Steel",
      f_qty: "Quantity / Volume",
      f_qty_ph: "e.g. 5 units, 1000L",
      f_draw: "Technical Drawings",
      f_draw_ph: "Upload PDF, DXF, DWG, STEP files",
      f_submit: "Submit Request for Quotation",
      f_success_t: "Request Received",
      f_success_d: "Our engineering team will review your specifications and respond with a technical evaluation within 24 hours.",

      footer_bio: "Where Strength Meets Innovation. Twenty years of custom industrial manufacturing, precision stainless steel fabrication, and engineering solutions across Egypt.",
      footer_est: "Egypt — 20+ Years of Excellence",
      foot_col1_t: "Manufacturing Services",
      foot_col2_t: "Industrial Solutions",
      foot_col3_t: "Contact & Inquiries",
      foot_phone_t: "Phone",
      foot_email_t: "Email",
      foot_web_t: "Official Website",
      copy_right: "© 2024 Steel Technology Egypt. All rights reserved. Where Strength Meets Innovation.",
      back_top: "↑ Back to Top",
    },

    ar: {
      logo_title: "ستيل",
      logo_sub: "تكنولوجي",
      nav_home: "الرئيسية",
      nav_about: "من نحن",
      nav_fab: "تشكيل المعادن",
      nav_eng: "الحلول الهندسية",
      nav_equip: "المعدات والكتالوج",
      nav_proj: "المشروعات",
      nav_contact: "تواصل معنا",
      nav_re: "الهندسة العكسية",
      btn_quote: "طلب عرض أسعار",
      side_slogan: "القوة تلتقي بالابتكار — ستيل تكنولوجي",

      hero_eyebrow: "20 عاماً من الخبرة الصناعية والهندسية",
      hero_title_1: "دقة الاستانلس ستيل.",
      hero_title_2: "قوة صناعية.",
      hero_title_3: "صُممت لخطوط إنتاجك.",
      hero_title_4: "حلول تصنيعية وهندسية متكاملة",
      hero_desc: "في ستيل تكنولوجي، نقدم تصنيعاً مخصصاً للاستانلس ستيل، ومعدات صناعية متطورة، وحلول هندسية متكاملة مصممة خصيصاً لتلائم متطلبات خطوط إنتاجك ومصنعك بالملي.",
      hero_btn_quote: "اطلب عرض أسعار",
      hero_btn_explore: "استكشف قدراتنا التصنيعية",
      stat_exp: "سنة خبرة صناعية",
      stat_grades: "استانلس ستيل معتمد",
      stat_divs: "قطاعان رئيسيان للحلول",
      scroll_text: "تمرير للأسفل",

      cred_1: "سنة من الخبرة<br/>والريادة الصناعية",
      cred_2: "استانلس ستيل 304 و 316L<br/>بأعلى المعايير المعتمدة",
      cred_3_title: "حلول هندسية<br/>مخصصة بالملي",
      cred_3: "تصميم خصيصاً<br/>لحاجات مصنعك",
      cred_4_title: "من التصنيع<br/>إلى التركيب",
      cred_4: "تسليم مفتاح كامل<br/>ودعم فني مستمر",

      clients_label: "شركاء النجاح وثقة كبار المصنعين",
      clients_h2_1: "شركاء موثوقون",
      clients_h2_2: "لكبرى المؤسسات الصناعية",
      clients_desc: "نفخر بتصميم وتصنيع وتوريد أنظمة الاستانلس ستيل وخطوط الإنتاج لكبرى الشركات العالمية والمحلية الرائدة في مصر.",
      cat_fb: "الأغذية والمشروبات",
      cat_pharma: "الصناعات الدوائية والطبية",
      cat_chem: "الكيماويات والصناعات الثقيلة",
      cat_eng_serv: "الخدمات الهندسية والإنشائية",
      c_marbella: "ماربيلا للصناعات الغذائية (Marbella)",
      c_technotaste: "تكنو تيست (Techno Taste)",
      c_albawadi: "البوادي للصناعات الغذائية (Al Bawadi)",
      c_heinz: "هاينز (Heinz)",
      c_nestle: "نستله (Nestlé)",
      c_sedico: "سيديكو للأدوية (Sedico Pharmaceuticals)",
      c_october: "أكتوبر فارما (October Pharma)",
      c_arabpack: "العربية لتغليف الأدوية (Arab Packaging)",
      c_henkel: "هنكل (Henkel)",
      c_evergrow: "إيفر جرو للأسمدة المتخصصة (EverGrow)",
      c_intlpaints: "العالمية للدهانات (International Paints)",
      c_emco: "إمكو للمشروعات الهندسية (EMCO)",
      c_tmg: "مجموعة طلعت مصطفى (TMG)",


      div_label: "قطاعا أعمالنا الرئيسيان",
      div_h2_1: "قوتان صناعيتان.",
      div_h2_2: "شريك هندسي واحد متكامل.",
      div_a_tag: "القطاع الأول",
      div_a_title: "تشكيل وتصنيع<br/>المعادن بدقة",
      div_a_desc: "تقطيع ليزر وبالازما فائق الدقة، تشكيل الصاج والاستانلس، لحام أرجون ولحام مداري، معالجة وتلميع ميكانيكي وتشطيب لامع، ومنصات ومصنعات صناعية مخصصة.",
      div_b_tag: "القطاع الثاني",
      div_b_title: "حلول الهندسة<br/>الصناعية المتكاملة",
      div_b_desc: "تصنيع خزانات وأوعية الضغط، مبادلات حرارية، شبكات مواسير WFI وبخار نقي، خطوط إنتاج وسيور ناقلة، ووحدات CIP/SIP للغسيل والتعقيم الآلي.",
      div_btn: "استكشف تفاصيل القطاع",

      cap_label: "قدراتنا التصنيعية",
      cap_h2_1: "القدرات الهندسية",
      cap_h2_2: "والتصنيعية المتكاملة",
      cap_intro: "منظومة تصنيع شاملة مستندة إلى عقدين من الخبرة في خدمة أكثر القطاعات الصناعية والغذائية والدوائية حساسية في مصر.",
      cap_1_t: "تقطيع بالليزر والبالازما",
      cap_1_d: "تقطيع عالي الدقة لألواح ومقاطع الاستانلس ستيل، الحديد، والألومنيوم بأحدث تقنيات CNC.",
      cap_2_t: "تصنيع الاستانلس ستيل المخصص",
      cap_2_d: "تشكيل مصنعات 304 و 316L: هوبرات، وحدات ستانلس، منصات، بوابات، ولوحات مخصصة.",
      cap_3_t: "تشكيل وثني المعادن",
      cap_3_d: "تشكيل وثني ألواح الصاج والاستانلس بمكابس CNC للأشكال الهندسية المعقدة والهياكل الدقيقة.",
      cap_4_t: "لحام متخصص (أرجون ومداري)",
      cap_4_d: "لحام أرجون يدوي ولحام مداري آلي (Orbital Welding) للوصلات الصحية الخالية من أي عيوب.",
      cap_5_t: "معالجة وتلميع الأسطح",
      cap_5_d: "تلميع ميكانيكي، تشطيب مرآة (Mirror finish)، ومعالجة بالبكلينج والباسيفيشن (Pickling & Passivation).",
      cap_6_t: "تصنيع الخزانات والأوعية",
      cap_6_d: "تنكات تخزين، خلط، دابل جاكيت، معزولة، أوعية محطات المياه، ووحدات تعقيم متوافقة مع المواصفات.",
      cap_7_t: "شبكات المواسير الصناعية والصحية",
      cap_7_d: "شبكات مواسير WFI، بخار نقي، مياه منقاة، خطوط هواء مضغوط، خطوط حريق، وتجميع وحدات Skids.",
      cap_8_t: "خطوط الإنتاج والسيور الناقلة",
      cap_8_d: "سيور ناقلة مخصصة، طباخات، غراميل، وماكينات تعبئة وتغليف مع حلول تسليم مفتاح.",

      eng_label: "القطاع الثاني — الهندسة الصناعية",
      eng_h2_1: "صُممت خصيصاً",
      eng_h2_2: "لتلائم خطوات إنتاجك.",
      eng_p: "في ستيل تكنولوجي، لا نبيع معدات جاهزة من على الرف، بل نصمم وننفذ حلولاً هندسية تلبي بدقة طبيعة منتجك ومعايير مصنعك، من الخزان المنفرد إلى خط الإنتاج الآلي المتكامل.",
      eng_item1_t: "خزانات وأوعية تشغيل",
      eng_item1_d: "تخزين، خلط، تجانس، دابل جاكيت، معزولة",
      eng_item2_t: "المبادلات الحرارية",
      eng_item2_d: "إدارة حرارية عالية الكفاءة مع العزل التام",
      eng_item3_t: "شبكات المواسير والمرافق",
      eng_item3_d: "مياه منقاة WFI، بخار نقي، وهواء مضغوط",
      eng_item4_t: "خطوط الإنتاج والتعبئة",
      eng_item4_d: "سيور ناقلة وماكينات متوافقة مع خطك",
      eng_item5_t: "منظومات الغسيل والتعقيم CIP/SIP",
      eng_item5_d: "تعقيم موقوت آلي بالبخار النقي لبيئات العمل",
      eng_item6_t: "التركيب والصيانة الميدانية",
      eng_item6_d: "تشغيل ميداني وتطوير كفاءة مستمر للمعدات",
      eng_btn: "ناقش مشروعك الهندسي معنا",
      badge_cert: "خامات 304 و 316L معتمدة",

      cat_label: "كتالوج المعدات الصناعية",
      cat_h2_1: "معرض المعدات",
      cat_h2_2: "والأنظمة الصناعية",
      cat_btn_all: "استعراض كامل الكتالوج",
      cat_tag_1: "الفئة الأولى",
      cat_1_t: "تنكات التخزين والنقل",
      cat_1_d: "تنكات IBC للنقل والشحن، تنكات أسطوانية ورأسية، وتنكات بقاع لا مركزي لتسهيل تصريف السوائل اللزجة.",
      cat_tag_2: "الفئة الثانية",
      cat_2_t: "معدات الخلط والتسخين",
      cat_2_d: "تنكات خلط سوائل، تنكات تسخين كهربائي بجاكيت، تنكات بقلابات ميكانيكية، وخلط نيوماتيك من 100 إلى 2000 لتر.",
      cat_tag_3: "الفئة الثالثة",
      cat_3_t: "تصنيع الأغذية والألبان والتجميل",
      cat_3_d: "تنكات خلط صحية، غلايات طهي دابل جاكيت، خلاطات كوكير دائرية، تنكات تجبين الألبان، وماكينات تصنيع المنظفات والكريمات.",
      cat_tag_4: "الفئة الرابعة",
      cat_4_t: "السيور ومناولة المواد الخام",
      cat_4_d: "نواقل ومغذيات حلزونية (Screw Feeders/Conveyors)، تصميمات أنبوبية نظيفة، وسيور مخصصة للصناعات الغذائية والكيماوية.",
      cat_tag_5: "الفئة الخامسة",
      cat_5_t: "معدات المعالجة والتنكات الكيماوية",
      cat_5_d: "تنكات مقاومة للأحماض FRP، تنكات تخزين المساحيق والبودرة، ووحدات خلط المواد الكيماوية والمحاليل الصناعية.",
      cat_card_btn: "تفاصيل المنتجات",
      cat_custom_t: "هل تبحث عن معدات بمواصفات خاصة؟",
      cat_custom_d: "تتميز ستيل تكنولوجي بالقدرة على تصنيع معدات وحلول مصممة هندسياً خصيصاً لتطابق أبعاد ومواصفات منشأتك الصناعية.",
      cat_custom_btn: "اطلب تصنيعاً مخصصاً",

      re_label: "ابتكار استراتيجي لدعم توطين الصناعة",
      re_h2_1: "الهندسة العكسية.",
      re_h2_2: "والمسح ثلاثي الأبعاد 3D.",
      re_p: "في وقت تتطلب فيه الصناعة سرعة قصوى، لم يعد انتظار قطع الغيار المستوردة لشهور حلاً عملياً. نحن نسد هذه الفجوة عبر مسح القطع المعقدة بدقة ميكروسكوبية، وتحسين تصميمها، وتصنيعها محلياً بأعلى كفاءة لتركب بالملي في خطوط إنتاجك.",
      re_item1_t: "مسح 3D عالي الدقة",
      re_item1_d: "التقاط الأشكال الهندسية المعقدة والأسطح والتفاصيل الداخلية في دقائق معدودة.",
      re_item2_t: "تطوير ونمذجة على برامج CAD",
      re_item2_d: "تحليل التصميم، إنشاء توأم رقمي مطابق، وتعديل نقاط الضعف هندسياً للأفضل.",
      re_item3_t: "تصنيع وتجميع محلي بدون نسبة خطأ",
      re_item3_d: "إنتاج القطعة محلياً لتركب مباشرة بدون أي تأخير في سلاسل التوريد وبكفاءة تفوق الأصلية.",
      re_btn: "ناقش مشروع هندسة عكسية",
      re_scan_tag: "مسح رقمي ثلاثي الأبعاد",

      ind_label: "القطاعات والتطبيقات",
      ind_h2_1: "القطاعات الصناعية",
      ind_h2_2: "التي نخدمها",
      ind_1_t: "الصناعات الدوائية (فارما)",
      ind_1_d: "شبكات مياه الحقن WFI، البخار النقي، المياه المنقاة، ومصنعات غرف التعقيم النظيفة المطابقة لمواصفات GMP الصارمة.",
      ind_2_t: "الأغذية والمشروبات",
      ind_2_d: "مواسير صحية، تنكات خلط، غلايات طهي، هوبرات، ووحدات CIP/SIP مطابقة لأقصى معايير السلامة الغذائية.",
      ind_3_t: "صناعة الألبان ومشتقاتها",
      ind_3_d: "تنكات التجبين، وحدات البسترة، خزانات تبريد وحفظ الحليب ثلاثية الجدران المعزولة مع لحامات مدارية نقية.",
      ind_4_t: "مستحضرات التجميل والعناية",
      ind_4_d: "تنكات خلط الشامبو والجل والكريمات بأسطح داخلية تلميع مرآة مانعة للالتصاق ومحركات تقليب متغيرة السرعات.",
      ind_5_t: "المنشآت الصناعية العامة",
      ind_5_d: "منصات صلب واستانلس، مسارات، دكتات تهوية، بوابات أوتوماتيكية، ومصنعات ميكانيكية ثقيلة لمختلف المصانع.",
      ind_6_t: "محطات وشبكات المياه والمرافق",
      ind_6_d: "فلاتر مالتي ميديا، فلاتر كربون ومايكرون، مبادلات حرارية، وشبكات توزيع المرافق الصناعية ومحطات المعالجة.",

      why_label: "لماذا تختار ستيل تكنولوجي",
      why_h2_1: "لماذا يثق بنا",
      why_h2_2: "كبار المصنعين في مصر",
      why_1_t: "20 عاماً من الخبرة المتراكمة",
      why_1_d: "خبرة عميقة امتدت لعشرين عاماً في تصنيع وتشكيل الاستانلس ستيل وخدمة أكثر مصانع مصر حساسية ودقة.",
      why_2_t: "حلول مفصلة وليست منتجات رف",
      why_2_d: "كل قطعة ومعدة نصنعها تُدرس وتُصمم لتلائم تماماً ظروف تشغيل مصنعك وتحديات مساحتك وسرعة خطك.",
      why_3_t: "التصميم والتصنيع تحت سقف واحد",
      why_3_d: "نحن لسنا ورشة تقطيع، بل شريك هندسي متكامل يجمع بين الاستشارة الهندسية، التصنيع، والتركيب الميداني.",
      why_4_t: "خامات 304 و 316L معتمدة فقط",
      why_4_d: "نستخدم حصراً ألواح ومواسير استانلس ستيل أصلية معتمدة لضمان أقصى مقاومة للتآكل وعمر افتراضي طويل.",
      why_5_t: "من لوحة الرسم إلى التشغيل الفعلي",
      why_5_d: "نتولى كافة مراحل العمل: الرفع المساحي، التصميم الرقمي، التقطيع، اللحام، التشطيب، والتركيب والتشغيل الميداني.",
      why_6_t: "فهم دقيق لمتطلبات الصناعات الصحية",
      why_6_d: "دراية هندسية كاملة باشتراطات النظافة واللحام المداري والمعالجة الكيميائية المطلوبة في مصانع الأدوية والأغذية.",

      proj_label: "سابقة الأعمال",
      proj_h2_1: "مشروعات",
      proj_h2_2: "وقصص نجاح",
      proj_intro: "نماذج من المشروعات الهندسية والتصنيعية المنفذة لصالح كبرى المنشآت الصناعية في مختلف محافظات مصر.",
      proj_ph: "صورة المشروع موثقة",
      proj_1_tag: "الصناعات الدوائية",
      proj_1_t: "شبكة مواسير WFI وبخار نقي",
      proj_1_d: "تنفيذ شبكة مواسير استانلس 316L صحية بلحام مداري آلي ومعالجة Passivation شاملة لاختبارات الجودة.",
      proj_2_tag: "الأغذية والألبان",
      proj_2_t: "تنكات خلط معزولة ووحدة غسيل CIP",
      proj_2_d: "تصنيع خزانات دابل جاكيت معزولة حرارياً مع وحدة تنظيف مكاني أوتوماتيكية متصلة بخط التعبئة.",
      proj_3_tag: "منشآت صناعية",
      proj_3_t: "منصات تشغيل ودكتات تهوية عملاقة",
      proj_3_d: "تصنيع وتركيب منصات سلامة واستانلس ستيل وهاندريل مع دكتات تهوية صناعية وبوابات أوتوماتيكية.",
      proj_btn: "تفاصيل المشروع",

      proc_label: "منهجية العمل الهندسي",
      proc_h2_1: "كيف نعمل",
      proc_h2_2: "لضمان الجودة الفائقة",
      proc_1_t: "الاستشارة ودراسة الاحتياج",
      proc_1_d: "مراجعة متطلباتك أو رسوماتك الهندسية وتحديد المعايير الفنية والتشغيلية المناسبة لمنشأتك.",
      proc_2_t: "المراجعة الهندسية والمخطط",
      proc_2_d: "إعداد التصميمات التنفيذية الدقيقة وتحديد مواصفات الخامات وإصدار المقترح الفني والمالي.",
      proc_3_t: "التصنيع والتشغيل الدقيق",
      proc_3_d: "بدء التقطيع، التشكيل، واللحام المتخصص مع الفحص المرحلي لضمان مطابقة أدق التفاوتات الهندسية.",
      proc_4_t: "التركيب الميداني والتسليم",
      proc_4_d: "نقل وتركيب المنظومة داخل مصنعك، إجراء اختبارات الضغط والتشغيل، والتسليم النهائي المعتمد.",
      proc_5_t: "الدعم الفني والصيانة",
      proc_5_d: "شراكة ممتدة تشمل الصيانة الدورية، تطوير كفاءة الخطوط، وتوفير الدعم الهندسي الفوري.",

      rfq_label: "ابدأ مشروعك معنا",
      rfq_h2_1: "دعنا نصمم ونصنع",
      rfq_h2_2: "منظومتك",
      rfq_h2_3: "الهندسية القادمة.",
      rfq_p: "سواء كنت بحاجة إلى قطع معدنية دقيقة أو خطوط إنتاج وتنكات متكاملة، شاركنا تفاصيل مشروعك وسيقوم فريقنا الهندسي بدراستها وتقديم أفضل الحلول.",
      rfq_phone_label: "المبيعات والاستفسارات الفنية",
      rfq_email_label: "البريد الإلكتروني الهندسي المعتمد",
      rfq_loc_label: "المقر الرئيسي والمصنع",
      rfq_loc_val: "القاهرة، جمهورية مصر العربية — نخدم كافة المحافظات",
      rfq_btn_wa: "واتساب مباشر للمبيعات",
      rfq_btn_call: "اتصال بالمبيعات",

      form_title: "طلب عرض أسعار هندسي (RFQ)",
      f_name: "الاسم بالكامل *",
      f_name_ph: "اكتب اسمك هنا",
      f_comp: "اسم الشركة / المصنع *",
      f_comp_ph: "اسم المنشأة",
      f_phone: "رقم الهاتف / الواتساب *",
      f_email: "البريد الإلكتروني *",
      f_type: "نوع الخدمة أو المشروع *",
      f_desc: "وصف المشروع والمتطلبات *",
      f_desc_ph: "يرجى توضيح المواصفات المطلوبة، الأبعاد، السعات، أو أي اشتراطات فنية خاصة...",
      f_mat: "نوع الخامة المفضلة",
      f_mat_ph: "مثال: استانلس 316L، 304، حديد",
      f_qty: "الكمية أو السعة التقديرية",
      f_qty_ph: "مثال: 3 وحدات، سعة 2000 لتر",
      f_draw: "الملفات والرسومات الهندسية",
      f_draw_ph: "اضغط لرفع ملفات PDF, DXF, DWG, STEP",
      f_submit: "إرسال طلب عرض الأسعار",
      f_success_t: "تم استلام طلبكم بنجاح",
      f_success_d: "سيقوم مهندسونا بمراجعة المواصفات والرد عليكم بدراسة فنية وعرض أسعار خلال 24 ساعة.",

      footer_bio: "حيث تلتقي القوة بالابتكار. عشرون عاماً من الخبرة في التصنيع الهندسي، تشكيل الاستانلس ستيل، وتنفيذ المشروعات الصناعية المتكاملة في مصر.",
      footer_est: "مصر — أكثر من 20 عاماً من التميز",
      foot_col1_t: "خدمات التصنيع والتشكيل",
      foot_col2_t: "الحلول الهندسية الصناعية",
      foot_col3_t: "التواصل والاستفسارات",
      foot_phone_t: "الهاتف",
      foot_email_t: "البريد الإلكتروني",
      foot_web_t: "الموقع الرسمي",
      copy_right: "© 2024 ستيل تكنولوجي مصر. جميع الحقوق محفوظة. حيث تلتقي القوة بالابتكار.",
      back_top: "↑ العودة لأعلى الصفحة",
    }
  };

  const projectOptions = {
    en: [
      { val: "", text: "Select project type" },
      { val: "Stainless Steel Fabrication", text: "Stainless Steel Fabrication" },
      { val: "Industrial Tanks & Vessels", text: "Industrial Tanks & Vessels" },
      { val: "Laser / Plasma Cutting", text: "Laser / Plasma Cutting" },
      { val: "Industrial Piping (CIP/SIP/WFI)", text: "Industrial Piping (CIP/SIP/WFI)" },
      { val: "Production Line / Conveyor", text: "Production Line / Conveyor" },
      { val: "Heat Exchanger", text: "Heat Exchanger" },
      { val: "Reverse Engineering / 3D Scanning", text: "Reverse Engineering / 3D Scanning" },
      { val: "Surface Finishing", text: "Surface Finishing" },
      { val: "Equipment Supply", text: "Equipment Supply" },
      { val: "Other / Multiple Services", text: "Other / Multiple Services" }
    ],
    ar: [
      { val: "", text: "اختر نوع المشروع المطلوب" },
      { val: "تصنيع وتشكيل استانلس ستيل", text: "تصنيع وتشكيل استانلس ستيل مخصص" },
      { val: "تنكات وأوعية صناعية", text: "تصنيع خزانات وأوعية تشغيل (Tanks & Vessels)" },
      { val: "تقطيع ليزر وبالازما", text: "تقطيع ليزر وبالازما CNC" },
      { val: "شبكات مواسير صحية وصناعية", text: "شبكات مواسير صحية وصناعية (WFI / بخار)" },
      { val: "خطوط إنتاج وسيور ناقلة", text: "خطوط إنتاج وماكينات وسيور ناقلة" },
      { val: "مبادلات حرارية", text: "مبادلات حرارية وإدارة طاقة" },
      { val: "هندسة عكسية ومسح ثلاثي الأبعاد", text: "هندسة عكسية ومسح 3D Scanning" },
      { val: "معالجة وتلميع الأسطح", text: "معالجة وتلميع ميكانيكي (Mirror Finish)" },
      { val: "توريد معدات ومستلزمات", text: "توريد معدات ومستلزمات مصانع" },
      { val: "خدمات متعددة / مشروع مخصص", text: "خدمات متعددة / مشروع متكامل" }
    ]
  };

  // ─── LANGUAGE ENGINE ───
  let currentLang = localStorage.getItem('st_lang') || 'en';

  function applyLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('st_lang', lang);
    const isAr = lang === 'ar';

    // HTML root attributes
    document.documentElement.lang = lang;
    document.documentElement.dir = isAr ? 'rtl' : 'ltr';

    // Update Language Button labels
    const toggleLabel = document.getElementById('lang-label');
    const toggleLabelMobile = document.getElementById('lang-label-mobile');
    if (toggleLabel) toggleLabel.textContent = isAr ? 'English' : 'عربي';
    if (toggleLabelMobile) toggleLabelMobile.textContent = isAr ? 'English' : 'عربي';

    // Apply translations to all data-i18n elements
    const dict = translations[lang] || translations.en;
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) {
        if (dict[key].includes('<br/>')) {
          el.innerHTML = dict[key];
        } else {
          el.textContent = dict[key];
        }
      }
    });

    // Apply placeholders
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
      const key = el.getAttribute('data-i18n-ph');
      if (dict[key] !== undefined) {
        el.setAttribute('placeholder', dict[key]);
      }
    });

    // Populate select options
    const select = document.getElementById('project-type-select');
    if (select) {
      const selectedVal = select.value;
      select.innerHTML = '';
      projectOptions[lang].forEach(opt => {
        const optionEl = document.createElement('option');
        optionEl.value = opt.val;
        optionEl.textContent = opt.text;
        select.appendChild(optionEl);
      });
      select.value = selectedVal;
    }

    // Refresh icons
    if (window.lucide) {
      lucide.createIcons();
    }
  }

  function toggleLang() {
    applyLanguage(currentLang === 'en' ? 'ar' : 'en');
  }

  // ─── INITIALIZATION ───
  document.addEventListener('DOMContentLoaded', () => {
    applyLanguage(currentLang);
  });

  // ─── Lucide Icons ───
  window.addEventListener('load', () => {
    if (window.lucide) lucide.createIcons();
    document.getElementById('hero-bg').classList.add('loaded');
  });

  // ─── Sticky Nav ───
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  });

  // ─── Scroll Reveal ───
  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        revealObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  revealEls.forEach(el => revealObserver.observe(el));

  // ─── File Upload Label ───
  function updateFileLabel(input) {
    const label = document.getElementById('file-label');
    const isAr = currentLang === 'ar';
    if (input.files.length === 0) {
      label.textContent = isAr ? 'اضغط لرفع ملفات PDF, DXF, DWG, STEP' : 'Upload PDF, DXF, DWG, STEP files';
    } else if (input.files.length === 1) {
      label.textContent = input.files[0].name;
    } else {
      label.textContent = isAr ? `${input.files.length} ملفات مختارة` : `${input.files.length} files selected`;
    }
  }

  // ─── RFQ Form Handler ───
  function handleFormSubmit(e) {
    e.preventDefault();
    document.getElementById('rfq-form').classList.add('hidden');
    document.getElementById('form-success').classList.remove('hidden');
    if (window.lucide) lucide.createIcons();
  }

  // ─── Nav Active State ───
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        navLinks.forEach(l => l.classList.remove('text-off-white'));
        const active = document.querySelector(`.nav-link[href="#${e.target.id}"]`);
        if (active) active.classList.add('text-off-white');
      }
    });
  }, { threshold: 0.4 });
  sections.forEach(s => sectionObserver.observe(s));
</script>

</body>
</html>
'''

target_file = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\index.html'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_html_content.strip())

print(f"Successfully wrote {len(new_html_content)} characters to {target_file}")
