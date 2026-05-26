import os
import re

base_dir = r'c:\Users\54375\Desktop\IT\my-projects-web\footstats'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract styles
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
styles = style_match.group(1)

# Write style.css
with open(os.path.join(base_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(styles)

# Update the HTML base structure by replacing style with link
content = content.replace(style_match.group(0), '<link rel="stylesheet" href="style.css">')

# Update Nav links
nav_replacements = {
    'href="#villalba"': 'href="index.html#villalba"',
    'href="#palmares-jugador"': 'href="index.html#palmares-jugador"',
    'href="#liga"': 'href="argentina.html#liga"',
    'href="#copa"': 'href="argentina.html#copa"',
    'href="#supercopa"': 'href="argentina.html#supercopa"',
    'href="#sudamericana"': 'href="sudamericano.html#sudamericana"',
    '>Copa Sudamericana</a>': '>Campeonato Sudamericano</a>'
}
for k, v in nav_replacements.items():
    content = content.replace(k, v)

# Update nav logo to point to index.html
content = content.replace('<span class="nav-logo">⚽ FootStats</span>', '<a href="index.html" class="nav-logo" style="text-decoration:none;">⚽ FootStats</a>')

# Update nav active script in all files
nav_script_old = """        window.addEventListener('scroll', () => {
            const sections = ['villalba', 'palmares-jugador', 'liga', 'copa', 'supercopa', 'sudamericana'];
            let current = '';
            sections.forEach(id => {
                const el = document.getElementById(id);
                if (el && window.scrollY >= el.offsetTop - 80) current = id;
            });
            document.querySelectorAll('.nav-links a').forEach(a => {
                a.classList.toggle('active', a.getAttribute('href') === '#' + current);
            });
        });"""

nav_script_new = """        window.addEventListener('scroll', () => {
            const sections = ['villalba', 'palmares-jugador', 'liga', 'copa', 'supercopa', 'sudamericana'];
            let current = '';
            sections.forEach(id => {
                const el = document.getElementById(id);
                if (el && window.scrollY >= el.offsetTop - 80) current = id;
            });
            document.querySelectorAll('.nav-links a').forEach(a => {
                const href = a.getAttribute('href');
                a.classList.toggle('active', current && href.endsWith('#' + current));
            });
        });"""

content = content.replace(nav_script_old, nav_script_new)

# Now extract sections
hero_section = re.search(r'<!-- ====== PLAYER HERO ====== -->.*?(?=<!-- ====== CAREER ====== -->)', content, re.DOTALL).group(0)
career_section = re.search(r'<!-- ====== CAREER ====== -->.*?(?=<!-- ====== PLAYER PALMARES ====== -->)', content, re.DOTALL).group(0)
palmares_section = re.search(r'<!-- ====== PLAYER PALMARES ====== -->.*?(?=<!-- ====== LIGA ARGENTINA ====== -->)', content, re.DOTALL).group(0)

liga_section = re.search(r'<!-- ====== LIGA ARGENTINA ====== -->.*?(?=<!-- ====== COPA ARGENTINA ====== -->)', content, re.DOTALL).group(0)
copa_section = re.search(r'<!-- ====== COPA ARGENTINA ====== -->.*?(?=<!-- ====== SUPERCOPA ====== -->)', content, re.DOTALL).group(0)
supercopa_section = re.search(r'<!-- ====== SUPERCOPA ====== -->.*?(?=<!-- ====== COPA SUDAMERICANA ====== -->)', content, re.DOTALL).group(0)

suda_section = re.search(r'<!-- ====== COPA SUDAMERICANA ====== -->.*?(?=<footer>)', content, re.DOTALL).group(0)
# Update name in suda_section
suda_section = suda_section.replace('Copa Sudamericana', 'Campeonato Sudamericano')

footer = re.search(r'<footer>.*?</footer>', content, re.DOTALL).group(0)
footer = footer.replace('Copa Sudamericana', 'Campeonato Sudamericano')

head_nav = re.search(r'<!DOCTYPE html>.*?</nav>', content, re.DOTALL).group(0)

career_data_js = re.search(r'\s*const careerData = \[.*?\];', content, re.DOTALL).group(0)
liga_data_js = re.search(r'\s*const ligaData = \[.*?\];', content, re.DOTALL).group(0)
copa_data_js = re.search(r'\s*const copaData = \[.*?\];', content, re.DOTALL).group(0)
supercopa_data_js = re.search(r'\s*const supercopaData = \[.*?\];', content, re.DOTALL).group(0)
sud_data_js = re.search(r'\s*const sudData = \[.*?\];', content, re.DOTALL).group(0)

career_cards_js = re.search(r'\s*// ==============================\n\s*// CAREER CARDS\n\s*// ==============================.*?(?=\s*// ==============================\n\s*// PLAYER PALMARES DATA)', content, re.DOTALL).group(0)
palmares_data_js = re.search(r'\s*// ==============================\n\s*// PLAYER PALMARES DATA\n\s*// ==============================.*?(?=\s*// ==============================\n\s*// BUILD PALMARES TABLE \(ARG\))', content, re.DOTALL).group(0)

build_palmares_js = re.search(r'\s*// ==============================\n\s*// BUILD PALMARES TABLE \(ARG\)\n\s*// ==============================.*?(?=\s*// ==============================\n\s*// BUILD COPA SUDAMERICANA TABLE)', content, re.DOTALL).group(0)
build_sud_js = re.search(r'\s*// ==============================\n\s*// BUILD COPA SUDAMERICANA TABLE\n\s*// ==============================.*?(?=        buildPalmaresTable)', content, re.DOTALL).group(0)

observer_nav_js = re.search(r'\s*// ==============================\n\s*// SCROLL OBSERVER.*?</script>', content, re.DOTALL).group(0)

def make_file(name, body_sections, script_sections):
    with open(os.path.join(base_dir, name), 'w', encoding='utf-8') as f:
        f.write(head_nav + '\n\n')
        for s in body_sections:
            f.write(s + '\n')
        f.write('    ' + footer + '\n\n')
        f.write('    <script>\n')
        for s in script_sections:
            f.write(s + '\n')
        f.write(observer_nav_js + '\n')
        f.write('</body>\n</html>')


make_file('index.html', 
          [hero_section, career_section, palmares_section],
          [career_data_js, career_cards_js, palmares_data_js])

make_file('argentina.html',
          [liga_section, copa_section, supercopa_section],
          [liga_data_js, copa_data_js, supercopa_data_js, build_palmares_js, "        buildPalmaresTable(ligaData, 'ligaTable');\n        buildPalmaresTable(copaData, 'copaTable');\n        buildPalmaresTable(supercopaData, 'supercopaTable');"])

make_file('sudamericano.html',
          [suda_section],
          [sud_data_js, build_sud_js, "        buildSudTable(sudData);"])

print("Successfully generated all files.")
