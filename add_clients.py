# -*- coding: utf-8 -*-
import re

with open(r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\generate_bilingual.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect where Section 02 ends
sec2_marker = '<!-- ══════════════════════════════════════════\n     SECTION 03 — TWO CORE DIVISIONS'

clients_section_html = '''<!-- ══════════════════════════════════════════
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

'''

if sec2_marker in code:
    code = code.replace(sec2_marker, clients_section_html + sec2_marker)
    print("Clients section inserted before Section 03.")
else:
    print("Error: sec2_marker not found!")

# Translation keys to add to translations.en
en_keys = '''      clients_label: "Trusted By Leading Companies",
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
'''

ar_keys = '''      clients_label: "شركاء النجاح وثقة كبار المصنعين",
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
'''

# Add to en dict
code = code.replace('cred_4: "Full-Cycle<br/>Turnkey Delivery",', 'cred_4: "Full-Cycle<br/>Turnkey Delivery",\n\n' + en_keys)
# Add to ar dict
code = code.replace('cred_4: "تسليم مفتاح كامل<br/>ودعم فني مستمر",', 'cred_4: "تسليم مفتاح كامل<br/>ودعم فني مستمر",\n\n' + ar_keys)

with open(r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\generate_bilingual.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_bilingual.py successfully updated with clients data.")
