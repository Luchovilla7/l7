import os
import re

base_dir = r'c:\Users\54375\Desktop\IT\my-projects-web\footstats'
index_path = os.path.join(base_dir, 'index.html')
arg_2018_path = os.path.join(base_dir, 'arg_2018.html')

# 1. Update index.html
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update seleccionData to include links
old_data = """        const seleccionData = [
            { year: 2018, event: 'Amistosos', goals: '1', games: '1' },
            { year: 2019, event: 'Copa Sudamérica', goals: '1', games: '4' },
            { year: 2020, event: 'Copa Mundial', goals: '2', games: '4' },
            { year: 2021, event: 'Amistosos', goals: '1', games: '2' },
            { year: 2022, event: 'Copa Sudamérica', goals: '5', games: '6' },
            { year: 2023, event: 'Copa de las Américas', goals: '2', games: '1' },
            { year: 2023, event: 'Copa Mundial', goals: '8', games: '7' },
            { year: 2024, event: 'Amistosos', goals: '2', games: '3' },
            { year: 2025, event: 'Copa Sudamérica', goals: '4', games: '6' },
            { year: 2026, event: 'Copa de las Américas', goals: '1', games: '1' },
            { year: 2026, event: 'Copa Mundial', goals: '-', games: '-' },
        ];"""

new_data = """        const seleccionData = [
            { year: 2018, event: 'Amistosos', goals: '1', games: '1', link: 'arg_2018.html' },
            { year: 2019, event: 'Copa Sudamérica', goals: '1', games: '4', link: '#' },
            { year: 2020, event: 'Copa Mundial', goals: '2', games: '4', link: '#' },
            { year: 2021, event: 'Amistosos', goals: '1', games: '2', link: '#' },
            { year: 2022, event: 'Copa Sudamérica', goals: '5', games: '6', link: '#' },
            { year: 2023, event: 'Copa de las Américas', goals: '2', games: '1', link: '#' },
            { year: 2023, event: 'Copa Mundial', goals: '8', games: '7', link: '#' },
            { year: 2024, event: 'Amistosos', goals: '2', games: '3', link: '#' },
            { year: 2025, event: 'Copa Sudamérica', goals: '4', games: '6', link: '#' },
            { year: 2026, event: 'Copa de las Américas', goals: '1', games: '1', link: '#' },
            { year: 2026, event: 'Copa Mundial', goals: '-', games: '-', link: '#' },
        ];"""

content = content.replace(old_data, new_data)

# Update the render logic to be clickable
old_render = """        seleccionData.forEach((d, i) => {
            seleccionGrid.innerHTML += `
    <div class="career-card fade-in" data-age="${d.year}" style="animation-delay:${i * 0.04}s">"""

new_render = """        seleccionData.forEach((d, i) => {
            const clickAttr = (d.link && d.link !== '#') ? `onclick="window.location.href='${d.link}'" style="cursor:pointer; animation-delay:${i * 0.04}s"` : `style="animation-delay:${i * 0.04}s"`;
            seleccionGrid.innerHTML += `
    <div class="career-card fade-in" data-age="${d.year}" ${clickAttr}>"""

content = content.replace(old_render, new_render)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Generate arg_2018.html
html_2018 = """<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Argentina 2018 - Amistosos</title>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        .match-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            padding: 30px;
            margin-bottom: 20px;
            transition: all 0.3s;
        }
        .match-card:hover {
            border-color: rgba(201, 168, 76, 0.3);
            background: rgba(255, 255, 255, 0.05);
        }
        .match-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        .match-date {
            font-size: 0.8rem;
            color: var(--muted);
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .match-type {
            font-size: 0.75rem;
            color: var(--gold);
            letter-spacing: 1px;
            padding: 4px 12px;
            border: 1px solid var(--gold);
            border-radius: 20px;
        }
        .match-score {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 40px;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 4rem;
        }
        .team {
            display: flex;
            align-items: center;
            gap: 15px;
            width: 200px;
        }
        .team.home {
            justify-content: flex-end;
            text-align: right;
        }
        .team.away {
            justify-content: flex-start;
            text-align: left;
        }
        .team-name {
            font-size: 2.5rem;
            color: var(--text);
        }
        .score-box {
            color: var(--gold);
            background: rgba(201, 168, 76, 0.1);
            padding: 0 20px;
            border-radius: 8px;
        }
        .goal-scorers {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            font-size: 0.9rem;
            color: var(--muted);
        }
        .goal-scorers > div {
            width: 45%;
        }
        .home-scorers {
            text-align: right;
        }
        .away-scorers {
            text-align: left;
        }
        .scorer {
            margin-bottom: 5px;
        }
        .scorer strong {
            color: var(--text);
        }
        .highlight-goal {
            color: var(--green-light) !important;
        }
    </style>
</head>

<body>

    <nav>
        <a href="index.html" class="nav-logo" style="text-decoration:none;">⚽ FootStats</a>
        <div class="hamburger" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</div>
        <ul class="nav-links">
            <li><a href="index.html">VILLALBA</a></li>
            <li><a href="argentina.html">FUTBOL ARGENTINO</a></li>
            <li><a href="sudamericano.html">FUTBOL SUDAMERICANO</a></li>
        </ul>
    </nav>

    <section id="year-header">
        <div class="section-header fade-in">
            <div class="section-number">18</div>
            <div class="section-title-block">
                <div class="section-subtitle">Selección Argentina</div>
                <div class="section-title">Amistosos 2018</div>
            </div>
        </div>
        <p style="color:var(--muted); max-width:800px; line-height:1.6; margin-bottom: 40px;" class="fade-in">
            Resumen de los partidos amistosos disputados por la Selección Argentina en el año 2018. Este año marcó el debut absoluto de Luciano Villalba con la selección mayor, anotando su primer gol internacional en el encuentro frente a Malasia.
        </p>

        <!-- Match 1 -->
        <div class="match-card fade-in">
            <div class="match-header">
                <span class="match-date">Marzo 2018</span>
                <span class="match-type">Amistoso Internacional</span>
            </div>
            <div class="match-score">
                <div class="team home">
                    <span class="team-name">Argentina</span>
                </div>
                <div class="score-box">3 - 0</div>
                <div class="team away">
                    <span class="team-name">Estonia</span>
                </div>
            </div>
            <div class="goal-scorers">
                <div class="home-scorers">
                    <div class="scorer">⚽ <strong>B. Armoa</strong> 14'</div>
                    <div class="scorer">⚽ <strong>P. Sabatinni</strong> 42'</div>
                    <div class="scorer">⚽ <strong>E. Fernández</strong> 78'</div>
                </div>
                <div class="away-scorers"></div>
            </div>
        </div>

        <!-- Match 2 -->
        <div class="match-card fade-in">
            <div class="match-header">
                <span class="match-date">Junio 2018</span>
                <span class="match-type">Amistoso Internacional</span>
            </div>
            <div class="match-score">
                <div class="team home">
                    <span class="team-name">Argentina</span>
                </div>
                <div class="score-box">2 - 1</div>
                <div class="team away">
                    <span class="team-name">Dinamarca</span>
                </div>
            </div>
            <div class="goal-scorers">
                <div class="home-scorers">
                    <div class="scorer">⚽ <strong>P. Sabatinni</strong> 23'</div>
                    <div class="scorer">⚽ <strong>R. De Paul</strong> 65'</div>
                </div>
                <div class="away-scorers">
                    <div class="scorer">⚽ <strong>C. Eriksen</strong> 55'</div>
                </div>
            </div>
        </div>

        <!-- Match 3 -->
        <div class="match-card fade-in">
            <div class="match-header">
                <span class="match-date">Septiembre 2018</span>
                <span class="match-type">Amistoso Internacional</span>
            </div>
            <div class="match-score">
                <div class="team home">
                    <span class="team-name">Argentina</span>
                </div>
                <div class="score-box">3 - 1</div>
                <div class="team away">
                    <span class="team-name">Suiza</span>
                </div>
            </div>
            <div class="goal-scorers">
                <div class="home-scorers">
                    <div class="scorer">⚽ <strong>B. Armoa</strong> 12', 34'</div>
                    <div class="scorer">⚽ <strong>A. Mac Allister</strong> 82'</div>
                </div>
                <div class="away-scorers">
                    <div class="scorer">⚽ <strong>G. Xhaka</strong> 45'</div>
                </div>
            </div>
        </div>

        <!-- Match 4 -->
        <div class="match-card fade-in">
            <div class="match-header">
                <span class="match-date">Noviembre 2018</span>
                <span class="match-type">Amistoso Internacional</span>
            </div>
            <div class="match-score">
                <div class="team home">
                    <span class="team-name">Argentina</span>
                </div>
                <div class="score-box">4 - 1</div>
                <div class="team away">
                    <span class="team-name">Malasia</span>
                </div>
            </div>
            <div class="goal-scorers">
                <div class="home-scorers">
                    <div class="scorer">⚽ <strong>B. Armoa</strong> 10'</div>
                    <div class="scorer">⚽ <strong>P. Sabatinni</strong> 28'</div>
                    <div class="scorer">⚽ <strong class="highlight-goal">L. Villalba</strong> 60' <span style="color:var(--green-light); font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-left:4px;">(Debut en la Mayor)</span></div>
                    <div class="scorer">⚽ <strong>L. Paredes</strong> 85'</div>
                </div>
                <div class="away-scorers">
                    <div class="scorer">⚽ <strong>S. Rasid</strong> 75'</div>
                </div>
            </div>
        </div>

        <div style="text-align: center; margin-top: 40px;">
            <a href="index.html#seleccion" style="color: var(--gold); text-decoration: none; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; border: 1px solid var(--gold); padding: 10px 24px; border-radius: 4px; transition: all 0.3s;">
                ← Volver a Estadísticas
            </a>
        </div>
    </section>

    <footer>
        <span>⚽ FootStats — Estadísticas de Fútbol · Liga Argentina · Campeonato Sudamericano · 1965–2025</span>
    </footer>

    <script>
        // SCROLL OBSERVER
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) e.target.classList.add('visible');
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    </script>
</body>
</html>"""

with open(arg_2018_path, 'w', encoding='utf-8') as f:
    f.write(html_2018)

print('Updated index.html to support links and created arg_2018.html')
