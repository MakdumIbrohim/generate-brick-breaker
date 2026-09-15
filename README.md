# Generate Brick Breaker

<p align="center">
  <a href="https://brickbreaker-live.netlify.app" target="_blank">
    <img src="https://img.shields.io/badge/Live_Demo-brickbreaker--live.netlify.app-ff5964.svg?style=flat-square&logo=netlify" alt="Live Demo" />
  </a>
  <a href="https://github.com/marketplace/actions/generate-brick-breaker">
    <img src="https://img.shields.io/badge/Marketplace-v1.6.0-blue.svg?logo=github&style=flat-square" alt="Marketplace" />
  </a>
  <a href="https://github.com/MakdumIbrohim/generate-brick-breaker/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/MakdumIbrohim/generate-brick-breaker/generate.yml?branch=main&style=flat-square&label=build" alt="Build Status" />
  </a>
  <a href="https://github.com/MakdumIbrohim/generate-brick-breaker/stargazers">
    <img src="https://img.shields.io/github/stars/MakdumIbrohim/generate-brick-breaker?style=flat-square&logo=github" alt="Stars" />
  </a>
  <a href="https://github.com/MakdumIbrohim/generate-brick-breaker/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/MakdumIbrohim/generate-brick-breaker?style=flat-square" alt="License" />
  </a>
</p>

<p align="center">
  <img src="game.svg" alt="generate-brick-breaker" />
</p>

Turn your GitHub contribution graph into an automated retro Brick Breaker game animation (SVG or GIF) for your profile README.

[English](#english) • [Indonesia](#bahasa-indonesia)

---

## English

### Customization Options

#### Ball Skin Options (`ball_skin`)
| Option | Preview |
| :---: | :---: |
| `classic` (default) | <img src="assets/preview/sample_classic.svg" width="340" alt="classic" /> |
| `fire` | <img src="assets/preview/sample_fire.svg" width="340" alt="fire" /> |
| `ice` | <img src="assets/preview/sample_ice.svg" width="340" alt="ice" /> |
| `lightning` | <img src="assets/preview/sample_lightning.svg" width="340" alt="lightning" /> |
| `poison` | <img src="assets/preview/sample_poison.svg" width="340" alt="poison" /> |

#### Paddle Skin Options (`paddle_skin`)
| Option | Preview |
| :---: | :---: |
| `classic` (default) | Primary theme color |
| `laser` | <img src="assets/preview/sample_paddle_laser.svg" width="340" alt="paddle laser" /> |
| `retro` | <img src="assets/preview/sample_paddle_retro.svg" width="340" alt="paddle retro" /> |
| `mecha` | <img src="assets/preview/sample_paddle_mecha.svg" width="340" alt="paddle mecha" /> |
| `cyber` | <img src="assets/preview/sample_paddle_cyber.svg" width="340" alt="paddle cyber" /> |

#### Board Theme Options (`theme`)
| Option | Preview |
| :---: | :---: |
| `classic` (default) | <img src="assets/preview/sample_theme_classic.svg" width="340" alt="classic theme" /> |
| `sky` | <img src="assets/preview/sample_theme_sky.svg" width="340" alt="sky theme" /> |
| `sky-night` | <img src="assets/preview/sample_theme_sky_night.svg" width="340" alt="sky night theme" /> |
| `synthwave` | <img src="assets/preview/sample_theme_synthwave.svg" width="340" alt="synthwave theme" /> |
| `matrix` | <img src="assets/preview/sample_theme_matrix.svg" width="340" alt="matrix theme" /> |
| `sakura` | <img src="assets/preview/sample_theme_sakura.svg" width="340" alt="sakura theme" /> |

#### Custom Brick Color (`brick_color` / `--brick-color` )
*Applies to the `classic` board theme only.*
- **Single HEX (Auto-Gradient)**: Pass 1 HEX color (e.g. `'#00b4d8'`) to automatically generate all 4 brightness levels.
- **Combined Multi-HEX**: Pass 4 comma-separated HEX colors (e.g. `'#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF'`) from lowest to highest level.

#### Ball Speed Options (`ball_speed` / `--speed`)
- **Presets**: `slow` (8.0), `normal` (10.5), `fast` (14.0), `turbo` (18.0).
- **Custom Value**: Any numeric speed from `4.0` to `30.0` (e.g. `12.5`).
- *Default*: If omitted, ball speed automatically adapts to your total contribution commits so the animation finishes in 50–80s.

---

### Live Web Studio

Customize skins, test themes, and download your generated game SVG/GIF online without any installation:
#### [https://brickbreaker-live.netlify.app](https://brickbreaker-live.netlify.app)

<video src="https://github.com/user-attachments/assets/9c0854c2-1ca4-4367-9408-904013870ef9" width="50%" autoplay loop muted playsinline></video>

---

### Installation & Usage

#### 1. GitHub Profile Integration (Automated)

1. In your GitHub profile repository (`username/username`), create `.github/workflows/brick-breaker.yml`:

```yaml
name: Generate Brick Breaker

on:
  schedule:
    # Runs automatically every hour to sync new commits
    - cron: "0 * * * *"
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - uses: MakdumIbrohim/generate-brick-breaker@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          github_user: ${{ github.repository_owner }}

          # Options: game.svg (recommended) or game.gif
          output_path: game.svg

          # Options: classic | fire | ice | lightning | poison
          ball_skin: classic

          # Options: classic | sky | sky-night | synthwave | matrix | sakura
          theme: classic

          # Options: classic | laser | retro | mecha | cyber
          paddle_skin: classic

          # Optional: Custom brick color (applies to classic theme only).
          # - Single HEX (auto-gradient): '#00b4d8'
          # - Combined Multi-HEX (levels 1-4): '#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF'
          # brick_color: '#00b4d8'

          # Optional: Custom ball speed: slow | normal | fast | turbo or number (e.g. '14.0').
          # If omitted, speed adapts automatically based on your total commit count.
          # ball_speed: normal

      - name: Commit and Push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git diff --staged --quiet || git commit -m "chore: update brick breaker assets"
          git pull --rebase --autostash origin main || true
          git push origin main
```

2. Enable workflow permissions: Repo **Settings** > **Actions** > **General** > **Workflow permissions** > select **Read and write permissions** > **Save**.

3. Add image to your profile `README.md` (use `.svg` or `.gif` matching your `output_path`):
```markdown
<p align="center">
  <img src="game.svg" alt="Brick Breaker Game" />
</p>
```

> **Note on Image Caching:** GitHub caches profile images through its Camo CDN. If you update settings and the animation does not change immediately, do a hard refresh (`Ctrl + F5` or `Cmd + Shift + R`), open your profile in an Incognito window, or allow 5–15 minutes for the CDN cache to clear.

#### 2. Local Usage

**Using Python:**
```bash
git clone https://github.com/MakdumIbrohim/generate-brick-breaker.git
cd generate-brick-breaker
pip install pillow

# Show help and available options
python generate.py --help
```

Examples:
```bash
# Flexible flag-based syntax (single HEX or 4 combined HEX, fast speed)
python generate.py YourGithubUsername --skin fire --theme classic --paddle mecha --brick-color "#00b4d8" --speed fast
# or with 4 combined HEX colors:
python generate.py YourGithubUsername --skin fire --theme classic --paddle mecha --brick-color "#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF" --speed fast

# Or classic positional syntax
python generate.py YourGithubUsername game.svg fire classic laser "#00b4d8" 14.0
# or with 4 combined HEX colors:
python generate.py YourGithubUsername game.svg fire classic laser "#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF" 14.0
```

**Using Docker (Without installing Python):**
```bash
# Run with Docker Compose (outputs to current folder)
docker compose up

# Build Docker image
docker build -t generate-brick-breaker .

# Run directly with flags (supports all skins, themes, custom colors, and speed)
docker run --rm -v $(pwd):/output generate-brick-breaker YourGithubUsername -o /output/game.svg --skin fire --theme classic --paddle mecha --brick-color "#00b4d8" --speed fast

# Optional: pass GITHUB_TOKEN for real-time GraphQL API
docker run --rm -e GITHUB_TOKEN="ghp_xxx" -v $(pwd):/output generate-brick-breaker YourGithubUsername -o /output/game.svg
```

---

## Bahasa Indonesia

### Pilihan Kustomisasi

#### Pilihan Skin Bola (`ball_skin`)
| Opsi | Preview |
| :---: | :---: |
| `classic` (default) | <img src="assets/preview/sample_classic.svg" width="340" alt="classic" /> |
| `fire` | <img src="assets/preview/sample_fire.svg" width="340" alt="fire" /> |
| `ice` | <img src="assets/preview/sample_ice.svg" width="340" alt="ice" /> |
| `lightning` | <img src="assets/preview/sample_lightning.svg" width="340" alt="lightning" /> |
| `poison` | <img src="assets/preview/sample_poison.svg" width="340" alt="poison" /> |

#### Pilihan Skin Paddle (`paddle_skin`)
| Opsi | Preview |
| :---: | :---: |
| `classic` (default) | Warna primer tema aktif |
| `laser` | <img src="assets/preview/sample_paddle_laser.svg" width="340" alt="paddle laser" /> |
| `retro` | <img src="assets/preview/sample_paddle_retro.svg" width="340" alt="paddle retro" /> |
| `mecha` | <img src="assets/preview/sample_paddle_mecha.svg" width="340" alt="paddle mecha" /> |
| `cyber` | <img src="assets/preview/sample_paddle_cyber.svg" width="340" alt="paddle cyber" /> |

#### Pilihan Tema Papan (`theme`)
| Opsi | Preview |
| :---: | :---: |
| `classic` (default) | <img src="assets/preview/sample_theme_classic.svg" width="340" alt="classic theme" /> |
| `sky` | <img src="assets/preview/sample_theme_sky.svg" width="340" alt="sky theme" /> |
| `sky-night` | <img src="assets/preview/sample_theme_sky_night.svg" width="340" alt="sky night theme" /> |
| `synthwave` | <img src="assets/preview/sample_theme_synthwave.svg" width="340" alt="synthwave theme" /> |
| `matrix` | <img src="assets/preview/sample_theme_matrix.svg" width="340" alt="matrix theme" /> |
| `sakura` | <img src="assets/preview/sample_theme_sakura.svg" width="340" alt="sakura theme" /> |

#### Opsi Kustom Warna Balok (`brick_color`)
*Hanya berlaku untuk tema papan `classic`.*
- **Satu HEX (Otomatis Gradasi)**: Masukkan 1 kode HEX (contoh `'#00b4d8'`), sistem otomatis menghitung 4 tingkatan kecerahan.
- **Gabungan Multi-HEX**: Masukkan 4 kode HEX dipisah koma (contoh `'#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF'`) berurutan dari level terendah ke tertinggi.

#### Opsi Kecepatan Bola (`ball_speed` / `--speed`)
- **Preset**: `slow` (8.0), `normal` (10.5), `fast` (14.0), `turbo` (18.0).
- **Nilai Kustom**: Angka kecepatan bebas dari `4.0` hingga `30.0` (contoh `12.5`).
- *Default*: Jika tidak diisi, kecepatan bola otomatis menyesuaikan dengan banyaknya kontribusi commit agar durasi animasi tetap ideal (50–80 detik).

---

### Studio Web Interaktif (Live Demo Online)

Kustomisasi skin, uji tema, dan unduh aset game SVG/GIF langsung di browser tanpa perlu instalasi apa pun:  
[https://brickbreaker-live.netlify.app](https://brickbreaker-live.netlify.app)

---

### Panduan Instalasi & Penggunaan

#### 1. Pasang di Profil GitHub (Otomatis)

1. Di repo profil GitHub Anda (`username/username`), buat file `.github/workflows/brick-breaker.yml`:

```yaml
name: Generate Brick Breaker

on:
  schedule:
    # Berjalan otomatis setiap jam untuk menyinkronkan commit baru
    - cron: "0 * * * *"
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - uses: MakdumIbrohim/generate-brick-breaker@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          github_user: ${{ github.repository_owner }}

          # Opsi: game.svg (disarankan) atau game.gif
          output_path: game.svg

          # Opsi: classic | fire | ice | lightning | poison
          ball_skin: classic

          # Opsi: classic | sky | sky-night | synthwave | matrix | sakura
          theme: classic

          # Opsi: classic | laser | retro | mecha | cyber
          paddle_skin: classic

          # Opsional: Kustom warna balok (hanya untuk tema classic).
          # - Satu HEX (otomatis gradasi): '#00b4d8'
          # - Gabungan Multi-HEX (level 1-4): '#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF'
          # brick_color: '#00b4d8'

          # Opsional: Kustom kecepatan bola: slow | normal | fast | turbo atau angka (contoh '14.0').
          # Jika tidak diisi, kecepatan bola otomatis menyesuaikan dengan banyaknya commit Anda.
          # ball_speed: normal

      - name: Commit and Push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git diff --staged --quiet || git commit -m "chore: update brick breaker assets"
          git pull --rebase --autostash origin main || true
          git push origin main
```

2. Beri izin write: buka repo **Settings** > **Actions** > **General** > **Workflow permissions** > pilih **Read and write permissions** > **Save**.

3. Tampilkan di `README.md` profil Anda (sesuaikan ekstensi `.svg` atau `.gif` dengan `output_path` Anda):
```markdown
<p align="center">
  <img src="game.svg" alt="Brick Breaker Game" />
</p>
```

> **Catatan Cache Gambar:** GitHub menyimpan cache gambar profil melalui server Camo CDN. Jika Anda baru saja mengubah pengaturan tema/skin dan animasinya belum langsung berubah di profil, lakukan *hard refresh* (`Ctrl + F5` atau `Cmd + Shift + R`), buka lewat tab *Incognito*, atau tunggu 5–15 menit hingga cache CDN GitHub terperbarui otomatis.

#### 2. Penggunaan di Lokal

**Menggunakan Python:**
```bash
git clone https://github.com/MakdumIbrohim/generate-brick-breaker.git
cd generate-brick-breaker
pip install pillow

# Tampilkan menu bantuan dan opsi yang tersedia
python generate.py --help
```

Contoh pemakaian:
```bash
# Menggunakan flags modern (satu HEX atau gabungan 4 HEX, kecepatan bola)
python generate.py YourGithubUsername --skin fire --theme classic --paddle mecha --brick-color "#00b4d8" --speed fast
# atau dengan gabungan 4 HEX:
python generate.py YourGithubUsername --skin fire --theme classic --paddle mecha --brick-color "#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF" --speed fast

# Atau sintaks posisi klasik
python generate.py YourGithubUsername game.svg fire classic laser "#00b4d8" 14.0
# atau dengan gabungan 4 HEX:
python generate.py YourGithubUsername game.svg fire classic laser "#FFADAD,#FFD6A5,#FDFFB6,#9BF6FF" 14.0
```

**Menggunakan Docker (Tanpa perlu instalasi Python):**
```bash
# Jalankan dengan Docker Compose (output ke folder saat ini)
docker compose up

# Build Docker image
docker build -t generate-brick-breaker .

# Jalankan langsung dengan flags (mendukung semua skin, tema, warna kustom, dan kecepatan)
docker run --rm -v $(pwd):/output generate-brick-breaker YourGithubUsername -o /output/game.svg --skin fire --theme classic --paddle mecha --brick-color "#00b4d8" --speed fast

# Opsional: sertakan GITHUB_TOKEN untuk API GraphQL real-time
docker run --rm -e GITHUB_TOKEN="ghp_xxx" -v $(pwd):/output generate-brick-breaker YourGithubUsername -o /output/game.svg
```
