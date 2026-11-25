/* ══════════════════════════════════════════════
   STEEL TECHNOLOGY — APPLICATION CONTROLLER
══════════════════════════════════════════════ */

(function () {
  const DATA = window.ST_DATA;
  let currentLang = localStorage.getItem('st_lang') || 'en';
  let activePortfolioFilter = 'all';
  let activeCatalogModalCat = 'storage';
  let activeProjectSeries = null;
  let activeProjectPhotoIdx = 0;

  function t(key) {
    const dict = DATA.translations[currentLang] || DATA.translations.en;
    return dict[key] !== undefined ? dict[key] : (DATA.translations.en[key] || key);
  }

  function refreshIcons() {
    if (window.lucide) window.lucide.createIcons();
  }

  /* ─── LANGUAGE SWITCHING ─── */
  window.applyLanguage = function (lang) {
    currentLang = lang === 'ar' ? 'ar' : 'en';
    localStorage.setItem('st_lang', currentLang);
    const isAr = currentLang === 'ar';

    document.documentElement.lang = currentLang;
    document.documentElement.dir = isAr ? 'rtl' : 'ltr';

    const toggleLabel = document.getElementById('lang-label');
    const toggleLabelMobile = document.getElementById('lang-label-mobile');
    if (toggleLabel) toggleLabel.textContent = isAr ? 'English' : 'عربي';
    if (toggleLabelMobile) toggleLabelMobile.textContent = isAr ? 'English' : 'عربي';

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const val = t(key);
      if (val.includes('<br/>')) {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    });

    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
      const key = el.getAttribute('data-i18n-ph');
      el.setAttribute('placeholder', t(key));
    });

    const select = document.getElementById('project-type-select');
    if (select) {
      const selectedVal = select.value;
      select.innerHTML = '';
      DATA.projectOptions.forEach(opt => {
        const optionEl = document.createElement('option');
        optionEl.value = opt.val;
        optionEl.textContent = opt[currentLang];
        select.appendChild(optionEl);
      });
      if (selectedVal) select.value = selectedVal;
    }

    renderPortfolioGrid();
    refreshOpenModalsOnLangChange();
    refreshIcons();
  };

  window.toggleLang = function () {
    window.applyLanguage(currentLang === 'en' ? 'ar' : 'en');
  };

  /* ─── PORTFOLIO RENDERING & FILTERING ─── */
  window.setPortfolioFilter = function (cat) {
    activePortfolioFilter = cat;
    document.querySelectorAll('.filter-pill').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-filter') === cat);
    });
    renderPortfolioGrid();
    refreshIcons();
  };

  function renderPortfolioGrid() {
    const grid = document.getElementById('portfolio-grid');
    if (!grid) return;

    const items = activePortfolioFilter === 'all'
      ? DATA.portfolioSeries
      : DATA.portfolioSeries.filter(s => s.cat === activePortfolioFilter);

    grid.innerHTML = items.map((series, idx) => {
      const photoCountLabel = currentLang === 'ar'
        ? `${series.photos.length} صور`
        : `${series.photos.length} Photos`;
      return `
        <article class="proj-card group cursor-pointer flex flex-col justify-between" onclick="openProjectModal('${series.id}')">
          <div>
            <div class="h-56 bg-gunmetal border-b border-silver/10 relative overflow-hidden">
              <img src="${series.thumb}" alt="${series.title[currentLang]}" loading="lazy"
                class="w-full h-full object-cover proj-card-img" style="filter: brightness(0.82);" />
              <div class="absolute inset-0 bg-gradient-to-t from-rich-black/80 via-transparent to-transparent"></div>
              <span class="absolute top-3 start-3 bg-rich-black/85 border border-silver/20 px-2.5 py-1 font-heading text-[0.7rem] text-silver tracking-widest uppercase">
                ${photoCountLabel}
              </span>
            </div>
            <div class="p-6">
              <div class="flex gap-2 mb-3">
                <span class="tag text-bluebell" style="border-color: rgba(153,160,203,0.35); color: #99A0CB;">
                  ${series.catLabel[currentLang]}
                </span>
              </div>
              <h4 class="font-heading font-bold text-xl text-off-white mb-2 tracking-wide">
                ${series.title[currentLang]}
              </h4>
              <p class="text-silver/65 text-xs leading-relaxed mb-4">
                ${series.summary[currentLang]}
              </p>
            </div>
          </div>
          <div class="px-6 pb-6 pt-0">
            <button type="button" class="btn-ghost text-xs">
              <span>${t('proj_btn')}</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5 flip-rtl"></i>
            </button>
          </div>
        </article>
      `;
    }).join('');
  }

  /* ─── MODALS HELPER ─── */
  function openModal(modalId) {
    const el = document.getElementById(modalId);
    if (!el) return;
    el.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  window.closeAllModals = function () {
    document.querySelectorAll('.st-modal-backdrop').forEach(m => m.classList.remove('open'));
    document.body.style.overflow = '';
    activeProjectSeries = null;
  };

  /* ─── 1. EQUIPMENT CATALOG MODAL ─── */
  window.openCatalogModal = function (catId) {
    activeCatalogModalCat = catId || 'all';
    renderCatalogModal();
    openModal('catalog-modal');
    refreshIcons();
  };

  window.switchCatalogModalCat = function (catId) {
    activeCatalogModalCat = catId;
    renderCatalogModal();
    refreshIcons();
  };

  function renderCatalogModal() {
    const tabsEl = document.getElementById('catalog-modal-tabs');
    const bodyEl = document.getElementById('catalog-modal-body');
    if (!tabsEl || !bodyEl) return;

    const allLabel = t('modal_all_cats');
    const tabs = [
      `<button type="button" onclick="switchCatalogModalCat('all')" class="filter-pill ${activeCatalogModalCat === 'all' ? 'active' : ''}">${allLabel}</button>`,
      ...DATA.catalogCategories.map(c =>
        `<button type="button" onclick="switchCatalogModalCat('${c.id}')" class="filter-pill ${activeCatalogModalCat === c.id ? 'active' : ''}">${c.num} · ${c.title[currentLang]}</button>`
      )
    ];
    tabsEl.innerHTML = tabs.join('');

    const cats = activeCatalogModalCat === 'all'
      ? DATA.catalogCategories
      : DATA.catalogCategories.filter(c => c.id === activeCatalogModalCat);

    bodyEl.innerHTML = cats.map(cat => `
      <div class="mb-8 last:mb-0">
        <div class="flex flex-col sm:flex-row sm:items-center gap-4 mb-5 pb-4 border-b border-silver/15">
          <img src="${cat.img}" alt="${cat.title[currentLang]}" class="w-20 h-16 object-cover border border-silver/20 flex-shrink-0" />
          <div>
            <div class="font-heading text-xs text-auburn font-bold tracking-widest uppercase">${cat.num}</div>
            <h3 class="font-heading font-bold text-2xl text-off-white">${cat.title[currentLang]}</h3>
            <p class="text-silver/65 text-xs mt-1">${cat.summary[currentLang]}</p>
          </div>
        </div>
        <div class="grid sm:grid-cols-2 gap-4">
          ${cat.items.map(item => `
            <div class="bg-gunmetal/60 border border-silver/10 p-5 flex flex-col justify-between hover:border-auburn/40 transition-colors">
              <div>
                <div class="font-heading text-[0.7rem] text-bluebell tracking-widest uppercase mb-1">${item.sub[currentLang]}</div>
                <h4 class="font-heading font-bold text-base text-off-white mb-2">${item.name[currentLang]}</h4>
                <p class="text-silver/65 text-xs leading-relaxed mb-4">${item.desc[currentLang]}</p>
              </div>
              <button type="button" onclick="prefillRFQ('${cat.rfqType}', '${item.name[currentLang].replace(/'/g, "\\'")}')" class="btn-ghost text-xs self-start">
                <span>${t('modal_req_quote')}</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 flip-rtl"></i>
              </button>
            </div>
          `).join('')}
        </div>
      </div>
    `).join('');
  }

  /* ─── 2. PROJECT SERIES MODAL ─── */
  window.openProjectModal = function (seriesId) {
    const series = DATA.portfolioSeries.find(s => s.id === seriesId);
    if (!series) return;
    activeProjectSeries = series;
    activeProjectPhotoIdx = 0;
    renderProjectModal();
    openModal('project-modal');
    refreshIcons();
  };

  window.setProjectPhoto = function (idx) {
    if (!activeProjectSeries) return;
    const total = activeProjectSeries.photos.length;
    activeProjectPhotoIdx = ((idx % total) + total) % total;
    renderProjectModal();
    refreshIcons();
  };

  function renderProjectModal() {
    if (!activeProjectSeries) return;
    const series = activeProjectSeries;
    const photo = series.photos[activeProjectPhotoIdx];

    document.getElementById('pm-cat').textContent = series.catLabel[currentLang];
    document.getElementById('pm-title').textContent = series.title[currentLang];
    document.getElementById('pm-summary').textContent = series.summary[currentLang];
    document.getElementById('pm-img').src = photo.src;
    document.getElementById('pm-img').alt = photo.cap[currentLang];
    document.getElementById('pm-ref').textContent = `${photo.ref} (${activeProjectPhotoIdx + 1}/${series.photos.length})`;
    document.getElementById('pm-cap').textContent = photo.cap[currentLang];

    const thumbsEl = document.getElementById('pm-thumbs');
    thumbsEl.innerHTML = series.photos.map((p, idx) => `
      <button type="button" onclick="setProjectPhoto(${idx})"
        class="w-20 h-16 flex-shrink-0 overflow-hidden border-2 transition-all ${idx === activeProjectPhotoIdx ? 'border-auburn opacity-100' : 'border-silver/20 opacity-55 hover:opacity-90'}">
        <img src="${p.src}" alt="${p.ref}" class="w-full h-full object-cover" />
      </button>
    `).join('');

    const ctaBtn = document.getElementById('pm-cta');
    ctaBtn.onclick = function () {
      window.prefillRFQ(series.rfqType, series.title[currentLang]);
    };
  }

  /* ─── 3. CAPABILITY / DIVISION MODAL ─── */
  window.openCapabilityModal = function (capKey) {
    const cap = DATA.capabilitiesDetail[capKey];
    if (!cap) return;
    document.getElementById('cm-tag').textContent = cap.tag[currentLang];
    document.getElementById('cm-title').textContent = cap.title[currentLang];
    document.getElementById('cm-img').src = cap.img;
    document.getElementById('cm-img').alt = cap.title[currentLang];
    document.getElementById('cm-desc').textContent = cap.desc[currentLang];
    document.getElementById('cm-bullets').innerHTML = cap.bullets[currentLang].map(b => `
      <li class="flex items-start gap-3 text-sm text-silver/80">
        <span class="w-1.5 h-1.5 rounded-full bg-auburn mt-2 flex-shrink-0"></span>
        <span>${b}</span>
      </li>
    `).join('');

    document.getElementById('cm-cta').onclick = function () {
      window.prefillRFQ(cap.rfqType, cap.title[currentLang]);
    };

    openModal('capability-modal');
    refreshIcons();
  };

  /* ─── 4. LEGAL MODAL (Privacy / Terms) ─── */
  window.openLegalModal = function (type) {
    const isAr = currentLang === 'ar';
    const titleEl = document.getElementById('lm-title');
    const bodyEl = document.getElementById('lm-body');
    if (type === 'privacy') {
      titleEl.textContent = isAr ? 'سياسة الخصوصية وحماية البيانات' : 'Privacy Policy';
      bodyEl.innerHTML = isAr
        ? '<p class="mb-3">تلتزم شركة ستيل تكنولوجي بحماية سرية جميع الرسومات الهندسية (PDF/DXF/DWG/STEP) وبيانات التواصل المقدمة عبر نموذج طلب عرض الأسعار.</p><p>تُستخدم البيانات المقدمة حصراً لدراسة الجدوى الفنية وتقديم عروض الأسعار الهندسية ولن يتم مشاركتها مع أي أطراف خارجية.</p>'
        : '<p class="mb-3">Steel Technology respects the confidentiality of all engineering drawings (PDF, DXF, DWG, STEP) and corporate contact details submitted through our quotation portal.</p><p>Submitted information is used strictly for technical feasibility evaluation and preparing engineering quotations, and is never shared with third parties.</p>';
    } else {
      titleEl.textContent = isAr ? 'شروط الاستخدام والمواصفات الفنية' : 'Terms of Use & Technical Notice';
      bodyEl.innerHTML = isAr
        ? '<p class="mb-3">تعرض هذه المنصة قدرات ستيل تكنولوجي التصنيعية والهندسية. تخضع كافة السعات والأبعاد ودرجات الخامات للمراجعة والاعتماد الهندسي الرسمي لكل مشروع.</p><p>جميع الصور المعروضة في أرشيف المشروعات تعود لأعمال ستيل تكنولوجي الفعلية.</p>'
        : '<p class="mb-3">This website presents Steel Technology\'s manufacturing and engineering capabilities. All equipment capacities, tolerances, and material grades are subject to formal engineering review and confirmation per project specification.</p><p>All workshop and equipment photography shown in the Project Portfolio is sourced from Steel Technology\'s fabrication archive.</p>';
    }
    openModal('legal-modal');
    refreshIcons();
  };

  function refreshOpenModalsOnLangChange() {
    if (document.getElementById('catalog-modal')?.classList.contains('open')) renderCatalogModal();
    if (document.getElementById('project-modal')?.classList.contains('open') && activeProjectSeries) renderProjectModal();
  }

  /* ─── PRE-FILL RFQ FORM FROM ANY MODAL/CARD ─── */
  window.prefillRFQ = function (rfqType, itemName) {
    window.closeAllModals();
    const select = document.getElementById('project-type-select');
    const desc = document.getElementById('rfq-desc');
    const form = document.getElementById('rfq-form');
    const success = document.getElementById('form-success');

    if (form && success) {
      form.classList.remove('hidden');
      success.classList.add('hidden');
    }
    if (select && rfqType) {
      select.value = rfqType;
    }
    if (desc && itemName) {
      desc.value = currentLang === 'ar'
        ? `استفسار وطلب عرض أسعار بخصوص: ${itemName}\nالمواصفات المطلوبة / السعة / الأبعاد: `
        : `Quotation inquiry regarding: ${itemName}\nRequired capacity / dimensions / specs: `;
    }

    const contactSec = document.getElementById('contact');
    if (contactSec) contactSec.scrollIntoView({ behavior: 'smooth' });
    setTimeout(() => desc && desc.focus(), 450);
  };

  /* ─── WHATSAPP COMPOSER FROM RFQ FORM ─── */
  function buildWhatsAppURL() {
    const name = document.getElementById('rfq-name')?.value.trim() || '-';
    const comp = document.getElementById('rfq-comp')?.value.trim() || '-';
    const phone = document.getElementById('rfq-phone')?.value.trim() || '-';
    const email = document.getElementById('rfq-email')?.value.trim() || '-';
    const type = document.getElementById('project-type-select')?.value || '-';
    const desc = document.getElementById('rfq-desc')?.value.trim() || '-';
    const mat = document.getElementById('rfq-mat')?.value.trim() || '-';
    const qty = document.getElementById('rfq-qty')?.value.trim() || '-';

    const msg = currentLang === 'ar'
      ? `مرحباً ستيل تكنولوجي، أرغب في طلب عرض أسعار:\n• الاسم: ${name}\n• الشركة: ${comp}\n• الهاتف: ${phone}\n• البريد: ${email}\n• نوع المشروع: ${type}\n• الخامة: ${mat}\n• الكمية/السعة: ${qty}\n• التفاصيل: ${desc}`
      : `Hello Steel Technology, I would like to request a quote:\n• Name: ${name}\n• Company: ${comp}\n• Phone: ${phone}\n• Email: ${email}\n• Project Type: ${type}\n• Material: ${mat}\n• Quantity/Volume: ${qty}\n• Description: ${desc}`;

    return `https://wa.me/201018868858?text=${encodeURIComponent(msg)}`;
  }

  window.sendViaWhatsApp = function () {
    window.open(buildWhatsAppURL(), '_blank', 'noopener,noreferrer');
  };

  window.updateFileLabel = function (input) {
    const label = document.getElementById('file-label');
    if (!label) return;
    const isAr = currentLang === 'ar';
    if (input.files.length === 0) {
      label.textContent = isAr ? 'اضغط لرفع ملفات PDF, DXF, DWG, STEP' : 'Upload PDF, DXF, DWG, STEP files';
    } else if (input.files.length === 1) {
      label.textContent = input.files[0].name;
    } else {
      label.textContent = isAr ? `${input.files.length} ملفات مختارة` : `${input.files.length} files selected`;
    }
  };

  window.handleFormSubmit = function (e) {
    e.preventDefault();
    const waLink = document.getElementById('form-success-wa');
    if (waLink) waLink.href = buildWhatsAppURL();
    document.getElementById('rfq-form').classList.add('hidden');
    document.getElementById('form-success').classList.remove('hidden');
    refreshIcons();
  };

  window.resetRFQForm = function () {
    const form = document.getElementById('rfq-form');
    const success = document.getElementById('form-success');
    if (form) form.reset();
    window.updateFileLabel({ files: [] });
    if (form) form.classList.remove('hidden');
    if (success) success.classList.add('hidden');
    refreshIcons();
  };

  /* ─── INIT ON DOM READY ─── */
  document.addEventListener('DOMContentLoaded', () => {
    window.applyLanguage(currentLang);

    // Sticky Navbar
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      navbar && navbar.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });

    // Scroll Reveal (respects prefers-reduced-motion)
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const revealEls = document.querySelectorAll('.reveal');
    if (prefersReduced || !('IntersectionObserver' in window)) {
      revealEls.forEach(el => el.classList.add('visible'));
    } else {
      const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            revealObserver.unobserve(e.target);
          }
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
      revealEls.forEach(el => revealObserver.observe(el));
    }

    // Active Nav Highlight (accurate on tall sections)
    const navMap = {
      hero: 'hero',
      about: 'about',
      clients: 'clients',
      divisions: 'divisions',
      capabilities: 'divisions',
      engineering: 'engineering',
      catalog: 'catalog',
      'reverse-eng': 'engineering',
      industries: 'engineering',
      why: 'about',
      projects: 'projects',
      process: 'projects',
      contact: 'contact'
    };
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          const targetId = navMap[e.target.id] || e.target.id;
          navLinks.forEach(l => {
            l.classList.toggle('active-nav', l.getAttribute('href') === `#${targetId}`);
          });
        }
      });
    }, { rootMargin: '-25% 0px -60% 0px', threshold: 0 });
    sections.forEach(s => sectionObserver.observe(s));

    // Keyboard shortcuts for modals
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') window.closeAllModals();
      if (activeProjectSeries) {
        if (e.key === 'ArrowRight') window.setProjectPhoto(activeProjectPhotoIdx + (currentLang === 'ar' ? -1 : 1));
        if (e.key === 'ArrowLeft') window.setProjectPhoto(activeProjectPhotoIdx + (currentLang === 'ar' ? 1 : -1));
      }
    });
  });

  window.addEventListener('load', () => {
    refreshIcons();
    const bg = document.getElementById('hero-bg');
    if (bg) bg.classList.add('loaded');
  });
})();
