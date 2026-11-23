# -*- coding: utf-8 -*-
path = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\index.html'

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# Add favicon
if 'rel="icon"' not in c:
    c = c.replace('<meta name="description"', '<link rel="icon" type="image/png" href="logo.png" />\n  <meta name="description"')

# Replace navbar placeholder
old_nav_logo = '''    <!-- Logo -->
    <a href="#hero" class="flex items-center gap-3 group">
      <div class="w-10 h-10 rounded-full bg-gunmetal border border-auburn/30 flex items-center justify-center group-hover:border-auburn/70 transition-colors">
        <span class="font-heading font-black text-auburn text-sm">ST</span>
      </div>'''

new_nav_logo = '''    <!-- Logo -->
    <a href="#hero" class="flex items-center gap-3.5 group">
      <img src="logo.png" alt="Steel Technology Official Logo" class="w-12 h-12 object-contain drop-shadow-[0_0_12px_rgba(158,39,46,0.35)] group-hover:scale-105 transition-transform duration-300" />'''

# Replace footer placeholder
old_foot_logo = '''      <!-- Brand -->
      <div class="lg:col-span-1">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-full bg-gunmetal border border-auburn/30 flex items-center justify-center">
            <span class="font-heading font-black text-auburn text-sm">ST</span>
          </div>'''

new_foot_logo = '''      <!-- Brand -->
      <div class="lg:col-span-1">
        <div class="flex items-center gap-3.5 mb-4">
          <img src="logo.png" alt="Steel Technology Official Logo" class="w-12 h-12 object-contain drop-shadow-[0_0_14px_rgba(158,39,46,0.25)]" />'''

if old_nav_logo in c:
    c = c.replace(old_nav_logo, new_nav_logo)
    print("Replaced navbar logo successfully.")
else:
    print("Warning: old_nav_logo pattern not found.")

if old_foot_logo in c:
    c = c.replace(old_foot_logo, new_foot_logo)
    print("Replaced footer logo successfully.")
else:
    print("Warning: old_foot_logo pattern not found.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated index.html. Total logo.png occurrences:", c.count('logo.png'))
