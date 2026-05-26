import os

base_dir = r'c:\Users\54375\Desktop\IT\my-projects-web\footstats'
files = ['index.html', 'argentina.html', 'sudamericano.html']

for f in files:
    path = os.path.join(base_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    target = '<ul class="nav-links">'
    replacement = '<div class="hamburger" onclick="document.querySelector(\'.nav-links\').classList.toggle(\'open\')">☰</div>\n        <ul class="nav-links">'
    
    if replacement not in content:
        content = content.replace(target, replacement)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print('Updated html files with hamburger menu.')
