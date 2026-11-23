# -*- coding: utf-8 -*-
path = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\generate_bilingual.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old1 = '''      <div class="w-10 h-10 rounded-full bg-gunmetal border border-auburn/30 flex items-center justify-center group-hover:border-auburn/70 transition-colors">
        <span class="font-heading font-black text-auburn text-sm">ST</span>
      </div>'''

new1 = '''<img src="logo.png" alt="Steel Technology Official Logo" class="w-12 h-12 object-contain drop-shadow-[0_0_12px_rgba(158,39,46,0.35)] group-hover:scale-105 transition-transform duration-300" />'''

old2 = '''          <div class="w-10 h-10 rounded-full bg-gunmetal border border-auburn/30 flex items-center justify-center">
            <span class="font-heading font-black text-auburn text-sm">ST</span>
          </div>'''

new2 = '''<img src="logo.png" alt="Steel Technology Official Logo" class="w-12 h-12 object-contain drop-shadow-[0_0_14px_rgba(158,39,46,0.25)]" />'''

text = text.replace(old1, new1)
text = text.replace(old2, new2)

if 'rel="icon"' not in text:
    text = text.replace('<meta name="description"', '<link rel="icon" type="image/png" href="logo.png" />\n  <meta name="description"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated generate_bilingual.py successfully.")
