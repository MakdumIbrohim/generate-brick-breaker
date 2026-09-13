# Contributing to Generate Brick Breaker

Thank you for your interest in contributing to Generate Brick Breaker! We welcome contributions for new elemental ball skins, paddle models, animated board themes, bug fixes, and performance improvements.

## Code of Conduct
Please be respectful, constructive, and collaborative in all issues and pull requests.

## How to Contribute

### 1. Fork & Clone
Fork this repository to your GitHub account and clone it locally:
```bash
git clone https://github.com/<your-username>/generate-brick-breaker.git
cd generate-brick-breaker
pip install pillow
```

### 2. Architecture & Guidelines
- **Adding Ball Skins:** Add a new module in `src/skins/ball/<name>.py` containing `SKIN`, `spawn_particles()`, and `update_particle()`, then register it in `src/skins/ball/__init__.py`.
- **Adding Paddle Skins:** Add a new module in `src/skins/paddle/<name>.py` containing `SKIN` and `spawn_impact()`, register it in `src/skins/paddle/__init__.py`, and implement custom geometry in `src/gif_generator/` and `src/svg_generator/`.
- **Adding Board Themes:** Add a new module in `src/themes/<name>.py` containing `THEME`, `init_ambient()`, and `update_ambient()`, then register it in `src/themes/__init__.py`.
- **Lightweight Dependencies:** Keep the project minimal. `Pillow` is the only allowed external dependency. Do not introduce heavy libraries.
- **Local Testing:** Always test the generated SVG/GIF locally across different accounts, themes, and skins before opening a PR:
  ```bash
  python generate.py <username> test.svg [skin] [theme] [paddle_skin]
  ```

### 3. Commit Messages
Follow the Conventional Commits specification:
- `feat: ...` for new features, skins, or themes
- `fix: ...` for bug fixes and physics corrections
- `docs: ...` for documentation updates
- `refactor: ...` for code cleanup without functional changes

### 4. Submitting a Pull Request
1. Push your changes to your fork.
2. Open a Pull Request directly to the `main` branch.
3. Provide a clear description of your changes and attach a sample preview GIF if you introduced visual modifications.
