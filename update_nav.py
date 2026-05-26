import os

base_dir = r'c:\Users\54375\Desktop\IT\my-projects-web\footstats'
files = ['index.html', 'argentina.html', 'sudamericano.html']

for f in files:
    path = os.path.join(base_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We find the <ul class="nav-links">...</ul> block.
    # It might vary slightly per file if one has class="active" differently, but we can use regex.
    import re
    
    nav_links_pattern = r'<ul class="nav-links">.*?</ul>'
    
    new_nav_links = """<ul class="nav-links">
            <li><a href="index.html">VILLALBA</a></li>
            <li><a href="argentina.html">FUTBOL ARGENTINO</a></li>
            <li><a href="sudamericano.html">FUTBOL SUDAMERICANO</a></li>
        </ul>"""
    
    content = re.sub(nav_links_pattern, new_nav_links, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print('Updated navbar in all html files.')
