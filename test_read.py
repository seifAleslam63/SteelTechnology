# -*- coding: utf-8 -*-
import re

html_path = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's check the current content structure
print("Read successfully, length:", len(html))
