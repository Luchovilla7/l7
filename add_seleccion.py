import os

base_dir = r'c:\Users\54375\Desktop\IT\my-projects-web\footstats'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# HTML to insert before <footer>
html_to_insert = """
    <!-- ====== SELECCION ARGENTINA ====== -->
    <section id="seleccion">
        <div class="section-header fade-in">
            <div class="section-number">03</div>
            <div class="section-title-block">
                <div class="section-subtitle">Carrera Internacional</div>
                <div class="section-title">Selección Argentina</div>
            </div>
        </div>
        
        <h3 style="color:var(--gold); font-family:'Bebas Neue',sans-serif; font-size:2rem; letter-spacing:1px; margin-bottom:20px; text-transform:uppercase;" class="fade-in">Estadísticas por Año</h3>
        <div class="career-grid fade-in" id="seleccionGrid" style="margin-bottom: 60px;"></div>

        <h3 style="color:var(--gold); font-family:'Bebas Neue',sans-serif; font-size:2rem; letter-spacing:1px; margin-bottom:20px; text-transform:uppercase;" class="fade-in">Palmarés Internacional</h3>
        <div class="palmares-clubs" id="seleccionPalmares"></div>
    </section>

    <footer>"""

if "<!-- ====== SELECCION ARGENTINA ====== -->" not in content:
    content = content.replace("    <footer>", html_to_insert)

# JS to insert before SCROLL OBSERVER
js_to_insert = """
        // ==============================
        // SELECCION DATA
        // ==============================
        const seleccionData = [
            { year: 2018, event: 'Amistosos (4 partidos)', goals: '-', games: '-' },
            { year: 2019, event: 'Copa Sudamérica', goals: '-', games: '-' },
            { year: 2020, event: 'Copa Mundial', goals: '-', games: '-' },
            { year: 2021, event: 'Amistosos (4 partidos)', goals: '-', games: '-' },
            { year: 2022, event: 'Copa Sudamérica', goals: '-', games: '-' },
            { year: 2023, event: 'Mundial / Copa Américas', goals: '-', games: '-' },
            { year: 2024, event: 'Amistosos (4 partidos)', goals: '-', games: '-' },
            { year: 2025, event: 'Copa Sudamérica', goals: '-', games: '-' },
            { year: 2026, event: 'Mundial / Copa Américas', goals: '-', games: '-' },
        ];

        const seleccionGrid = document.getElementById('seleccionGrid');
        seleccionData.forEach((d, i) => {
            seleccionGrid.innerHTML += `
    <div class="career-card fade-in" data-age="${d.year}" style="animation-delay:${i * 0.04}s">
      <div class="card-age">Año · ${d.year}</div>
      <div class="card-club" style="font-size: 1.15rem; color: #72b2e8;">${d.event}</div>
      <div class="card-number" style="margin-bottom: 24px;">Selección Mayor</div>
      <div class="card-stats">
        <div class="card-stat">
          <span class="val goals">${d.goals}</span>
          <span class="key">Goles</span>
        </div>
        <div class="card-stat">
          <span class="val">${d.games}</span>
          <span class="key">Partidos</span>
        </div>
      </div>
      <div class="goals-bar" style="width:0%"></div>
    </div>
  `;
        });

        const seleccionPalmaresData = [
            {
                club: 'Selección Argentina',
                period: '2018–2026 (Retiro a los 30 años)',
                titles: 5,
                trophies: [
                    { icon: '🏆', name: 'Copa Sudamérica', year: '2022' },
                    { icon: '🌟', name: 'Copa de las Américas', year: '2023' },
                    { icon: '🌍', name: 'Copa Mundial', year: '2023' },
                    { icon: '🏆', name: 'Copa Sudamérica', year: '2025' },
                    { icon: '🌟', name: 'Copa de las Américas', year: '2026' },
                    { icon: '🌍', name: 'Copa Mundial', year: '2026 (A definir)' },
                ]
            }
        ];

        const seleccionPalmaresEl = document.getElementById('seleccionPalmares');
        seleccionPalmaresData.forEach((club, ci) => {
            const trophiesHtml = club.trophies.map(t => `
    <div class="trophy-item">
      <div class="trophy-icon">${t.icon}</div>
      <div>
        <div class="trophy-name">${t.name}</div>
        <span class="trophy-year">${t.year}</span>
      </div>
    </div>
  `).join('');

            seleccionPalmaresEl.innerHTML += `
    <div class="club-palmares-block fade-in" style="border-left: 3px solid #72b2e8;">
      <div class="club-palmares-header">
        <div>
          <div class="club-name-big" style="color:#72b2e8;">${club.club}</div>
          <div class="club-period">${club.period}</div>
        </div>
        <div style="text-align:center; margin-left:auto;">
          <div class="club-title-count">${club.titles}</div>
          <div class="club-title-label">${club.titles === 1 ? 'título' : 'títulos'}</div>
        </div>
      </div>
      <div class="trophies-grid">${trophiesHtml}</div>
    </div>
  `;
        });


        // ==============================
        // SCROLL OBSERVER"""

if "// SELECCION DATA" not in content:
    content = content.replace("        // ==============================\n        // SCROLL OBSERVER", js_to_insert)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with Seleccion Argentina section.')
