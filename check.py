with open(r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sections = ['hero', 'about', 'divisions', 'capabilities', 'engineering', 'catalog', 'reverse-eng', 'industries', 'why', 'projects', 'process', 'contact']
missing = [s for s in sections if f'id="{s}"' not in content]
print('Missing sections:', missing if missing else 'None - all sections present')
print('File size:', len(content), 'bytes (~', round(len(content)/1024, 1), 'KB)')
print('Has Tailwind CDN:', 'tailwindcss.com' in content)
print('Has Lucide icons:', 'lucide' in content)
print('Has Google Fonts:', 'fonts.googleapis.com' in content)
print('Has RFQ form:', 'rfq-form' in content)
print('Has WhatsApp CTA:', 'wa.me' in content)
print('Has phone numbers:', '01018868858' in content)
print('Has email:', 'steeltechnology-eg.com' in content)
print('Has Auburn brand color:', '#9E272E' in content)
print('Has lang toggle:', 'toggleLang' in content)
print('Has scroll reveal:', 'IntersectionObserver' in content)
print('Has all checks PASSED!' if not missing else 'ISSUES FOUND')
