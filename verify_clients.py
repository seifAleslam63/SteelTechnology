# -*- coding: utf-8 -*-
import urllib.request
resp = urllib.request.urlopen('http://127.0.0.1:8080/')
html = resp.read().decode('utf-8')
print('Status:', resp.status)
print('Has clients section id:', 'id="clients"' in html)
print('Has Nestlé:', 'Nestlé' in html)
print('Has Henkel:', 'Henkel' in html)
print('Has Sedico:', 'Sedico' in html)
print('Has Talaat Moustafa Group:', 'Talaat Moustafa Group' in html)
print('Has Arabic translations:', 'نستله' in html and 'سيديكو' in html and 'هنكل' in html)
print('Total characters:', len(html))
