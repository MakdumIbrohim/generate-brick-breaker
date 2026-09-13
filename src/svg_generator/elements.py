def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def get_heart_svg_path(cx, cy, size=5):
    coords = [
        (cx, cy + size),
        (cx - size, cy),
        (cx - size, cy - size // 2),
        (cx - size // 2, cy - size),
        (cx, cy - size // 2),
        (cx + size // 2, cy - size),
        (cx + size, cy - size // 2),
        (cx + size, cy),
    ]
    return f"M {coords[0][0]} {coords[0][1]} " + " ".join(f"L {x} {y}" for x, y in coords[1:]) + " Z"

def generate_particle_svg_node(ptype, sz=2):
    if ptype == "snowflake":
        # Cross snowflake shape (+)
        return f'<line x1="-{sz}" y1="0" x2="{sz}" y2="0" stroke="currentColor" stroke-width="1.6" /><line x1="0" y1="-{sz}" x2="0" y2="{sz}" stroke="currentColor" stroke-width="1.6" />'
    elif ptype == "crystal":
        # Diamond frost crystal
        return f'<polygon points="0,-{sz*1.2:.1f} {sz},0 0,{sz*1.2:.1f} -{sz},0" fill="currentColor" />'
    elif ptype == "ember":
        # Glowing round ember
        return f'<circle cx="0" cy="0" r="{sz}" fill="currentColor" />'
    elif ptype == "spark":
        # Sharp spark streak
        return f'<line x1="0" y1="0" x2="-{sz*1.5:.1f}" y2="-{sz*1.5:.1f}" stroke="currentColor" stroke-width="1.8" />'
    elif ptype == "bubble":
        # Hollow poison bubble
        return f'<circle cx="0" cy="0" r="{sz}" fill="none" stroke="currentColor" stroke-width="1.5" />'
    elif ptype == "zap":
        # Jagged electric zap line
        return f'<line x1="-{sz}" y1="-{sz}" x2="{sz}" y2="{sz}" stroke="currentColor" stroke-width="2" />'
    elif ptype == "thrust":
        # Rocket flame jet
        return f'<polygon points="-{sz},0 {sz},0 0,{sz*2.5:.1f}" fill="currentColor" />'
    elif ptype == "energy":
        return f'<circle cx="0" cy="0" r="{sz}" fill="currentColor" />'
    elif ptype == "pixel":
        return f'<rect x="-{sz}" y="-{sz}" width="{sz*2}" height="{sz*2}" fill="currentColor" />'
    else:
        return f'<rect x="-{sz}" y="-{sz}" width="{sz*2}" height="{sz*2}" fill="currentColor" />'

def generate_ambient_svg(theme, engine):
    elements = []
    effect = theme.get("bg_effect")
    if effect == "starfield":
        for i, s in enumerate(getattr(engine, "ambient_items", [])):
            dur = 1.5 + (i % 5) * 0.4
            delay = (i % 7) * 0.3
            elements.append(f'  <rect x="{s["x"]:.1f}" y="{s["y"]:.1f}" width="{s["size"]}" height="{s["size"]}" fill="#ffffff" style="animation: star-twinkle {dur:.1f}s ease-in-out infinite {delay:.1f}s;" />')
    elif effect == "mario_sky":
        # 4 distinct Mario puffy clouds cycling seamlessly from left to right
        clouds = [
            {"y": 140, "scale": 1.1, "dur": 24.0, "delay": 0.0},
            {"y": 180, "scale": 0.85, "dur": 30.0, "delay": -7.5},
            {"y": 150, "scale": 1.25, "dur": 20.0, "delay": -13.0},
            {"y": 172, "scale": 0.95, "dur": 27.0, "delay": -19.5}
        ]
        for c in clouds:
            cy = c["y"]
            sc = c["scale"]
            bw, bh = 54 * sc, 18 * sc
            dur = c["dur"]
            delay = c["delay"]
            cloud_g = [
                f'  <g style="animation: cloud-loop {dur:.1f}s linear infinite {delay:.1f}s;">',
                f'    <rect x="0" y="{cy + 8 * sc:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{bh/2:.1f}" fill="#ffffff" stroke="#000000" stroke-width="1" />',
                f'    <circle cx="{17 * sc:.1f}" cy="{cy + 13 * sc:.1f}" r="{11 * sc:.1f}" fill="#ffffff" stroke="#000000" stroke-width="1" />',
                f'    <circle cx="{34 * sc:.1f}" cy="{cy + 10 * sc:.1f}" r="{14 * sc:.1f}" fill="#ffffff" stroke="#000000" stroke-width="1" />',
                f'    <circle cx="{46 * sc:.1f}" cy="{cy + 14 * sc:.1f}" r="{10 * sc:.1f}" fill="#ffffff" stroke="#000000" stroke-width="1" />',
                f'    <rect x="{8 * sc:.1f}" y="{cy + 8 * sc:.1f}" width="{bw - 16 * sc:.1f}" height="{10 * sc:.1f}" fill="#ffffff" />',
                f'  </g>'
            ]
            elements.append("\n".join(cloud_g))
        # Flying pixel birds in open blue sky
        birds = [
            {"y": 132, "dur": 13.0, "delay": -2.0, "sc": 1.1},
            {"y": 162, "dur": 11.5, "delay": -8.0, "sc": 0.9}
        ]
        for b in birds:
            elements.append(
                f'  <path style="animation: cloud-loop {b["dur"]}s linear infinite {b["delay"]}s;" d="M 0,{b["y"]} Q 5,{b["y"]-6} 10,{b["y"]} Q 15,{b["y"]-6} 20,{b["y"]}" fill="none" stroke="#24292f" stroke-width="2" />'
            )
    elif effect == "mario_sky_night":
        # Glowing crescent moon in night sky
        elements.append('  <path d="M 45,28 A 16,16 0 1,0 72,55 A 20,20 0 1,1 45,28 Z" fill="#fff4bd" opacity="0.95" />')
        # Twinkling night stars
        for i, s in enumerate(getattr(engine, "ambient_items", [])):
            if s.get("type") == "star":
                dur = 1.6 + (i % 4) * 0.4
                delay = (i % 6) * 0.3
                elements.append(f'  <rect x="{s["x"]:.1f}" y="{s["y"]:.1f}" width="{s["size"]}" height="{s["size"]}" fill="#dbe7ff" style="animation: star-twinkle {dur:.1f}s ease-in-out infinite {delay:.1f}s;" />')
        # Translucent, dim night clouds floating under moon
        night_clouds = [
            {"y": 142, "scale": 1.1, "dur": 26.0, "delay": 0.0},
            {"y": 178, "scale": 0.85, "dur": 32.0, "delay": -8.5},
            {"y": 152, "scale": 1.2, "dur": 22.0, "delay": -15.0},
            {"y": 170, "scale": 0.95, "dur": 28.0, "delay": -21.0}
        ]
        for c in night_clouds:
            cy = c["y"]
            sc = c["scale"]
            bw, bh = 54 * sc, 18 * sc
            dur = c["dur"]
            delay = c["delay"]
            cloud_g = [
                f'  <g style="animation: cloud-loop {dur:.1f}s linear infinite {delay:.1f}s; opacity: 0.42;">',
                f'    <rect x="0" y="{cy + 8 * sc:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{bh/2:.1f}" fill="#334b82" stroke="#1c2d54" stroke-width="1" />',
                f'    <circle cx="{17 * sc:.1f}" cy="{cy + 13 * sc:.1f}" r="{11 * sc:.1f}" fill="#334b82" stroke="#1c2d54" stroke-width="1" />',
                f'    <circle cx="{34 * sc:.1f}" cy="{cy + 10 * sc:.1f}" r="{14 * sc:.1f}" fill="#334b82" stroke="#1c2d54" stroke-width="1" />',
                f'    <circle cx="{46 * sc:.1f}" cy="{cy + 14 * sc:.1f}" r="{10 * sc:.1f}" fill="#334b82" stroke="#1c2d54" stroke-width="1" />',
                f'    <rect x="{8 * sc:.1f}" y="{cy + 8 * sc:.1f}" width="{bw - 16 * sc:.1f}" height="{10 * sc:.1f}" fill="#334b82" />',
                f'  </g>'
            ]
            elements.append("\n".join(cloud_g))
        # Floating retro Boo ghosts drifting in night
        ghosts = [
            {"y": 136, "dur": 15.0, "delay": -3.0},
            {"y": 166, "dur": 13.5, "delay": -9.5}
        ]
        for gh in ghosts:
            gy = gh["y"]
            ghost_svg = [
                f'  <g style="animation: cloud-loop {gh["dur"]}s linear infinite {gh["delay"]}s; opacity: 0.85;">',
                f'    <circle cx="10" cy="{gy}" r="8" fill="#ffffff" stroke="#1c2d54" stroke-width="1" />',
                f'    <ellipse cx="6" cy="{gy - 2}" rx="1.5" ry="2" fill="#0d1b3e" />',
                f'    <ellipse cx="12" cy="{gy - 2}" rx="1.5" ry="2" fill="#0d1b3e" />',
                f'    <path d="M 6,{gy+3} Q 9,{gy+6} 12,{gy+3}" stroke="#0d1b3e" stroke-width="1" fill="none" />',
                f'    <polygon points="2,{gy+4} 0,{gy+2} 3,{gy+1}" fill="#ffffff" />',
                f'  </g>'
            ]
            elements.append("\n".join(ghost_svg))
    elif effect == "neon_grid":
        horizon_y = int(engine.canvas_h * 0.65)
        elements.append(f'  <g class="synthwave-grid">')
        elements.append(f'    <line x1="0" y1="{horizon_y}" x2="{engine.canvas_w}" y2="{horizon_y}" stroke="#961ec8" stroke-width="1.4" />')
        for y in range(horizon_y + 12, engine.canvas_h, 16):
            elements.append(f'    <line x1="0" y1="{y}" x2="{engine.canvas_w}" y2="{y}" stroke="#6e1496" stroke-width="1" />')
        center_x = engine.canvas_w / 2
        for offset in range(-int(engine.canvas_w), int(engine.canvas_w * 2), 48):
            elements.append(f'    <line x1="{center_x + (offset - center_x) * 0.15:.1f}" y1="{horizon_y}" x2="{offset}" y2="{engine.canvas_h}" stroke="#500a78" stroke-width="1" />')
        elements.append(f'  </g>')
    elif effect == "matrix_rain":
        cols = int(engine.canvas_w / 16)
        for c_i in range(cols):
            x = c_i * 16 + 8
            clen = 6 + (c_i % 4)
            dur = 2.2 + (c_i % 5) * 0.35
            delay = (c_i % 7) * -0.4

            stream_nodes = [f'  <g style="animation: matrix-stream {dur:.1f}s linear infinite {delay:.1f}s;">']
            for i in range(clen):
                py = -i * 9
                g_val = int(40 + ((clen - i) / clen) * 160)
                alpha = round(0.25 + ((clen - i) / clen) * 0.75, 2)
                col_hex = f"#00{g_val:02x}{int(g_val*0.4):02x}"
                stream_nodes.append(f'    <rect x="{x}" y="{py}" width="2" height="4" fill="{col_hex}" opacity="{alpha}" />')
            stream_nodes.append('  </g>')
            elements.append("\n".join(stream_nodes))
    elif effect == "sakura_drift":
        # 16 drifting cherry blossom petals across spring night
        petals = [
            {"x": 40, "y": -15, "dur": 8.5, "delay": 0.0, "sc": 1.1},
            {"x": 120, "y": -15, "dur": 10.0, "delay": -3.2, "sc": 0.9},
            {"x": 210, "y": -15, "dur": 9.0, "delay": -6.5, "sc": 1.2},
            {"x": 310, "y": -15, "dur": 11.2, "delay": -1.8, "sc": 0.85},
            {"x": 400, "y": -15, "dur": 9.6, "delay": -4.7, "sc": 1.05},
            {"x": 490, "y": -15, "dur": 8.8, "delay": -8.1, "sc": 1.15},
            {"x": 580, "y": -15, "dur": 10.5, "delay": -5.5, "sc": 0.95},
            {"x": 80, "y": -15, "dur": 9.2, "delay": -7.0, "sc": 1.0},
            {"x": 260, "y": -15, "dur": 11.5, "delay": -9.0, "sc": 0.8},
            {"x": 440, "y": -15, "dur": 8.6, "delay": -2.5, "sc": 1.1},
            {"x": 540, "y": -15, "dur": 10.2, "delay": -7.8, "sc": 0.9}
        ]
        for p in petals:
            x, y = p["x"], p["y"]
            sc = p["sc"]
            dur = p["dur"]
            delay = p["delay"]
            elements.append(
                f'  <g style="animation: sakura-flutter {dur:.1f}s linear infinite {delay:.1f}s;">'
                f'<path d="M {x},{y} C {x+6*sc:.1f},{y-4*sc:.1f} {x+10*sc:.1f},{y+2*sc:.1f} {x+6*sc:.1f},{y+8*sc:.1f} C {x+2*sc:.1f},{y+4*sc:.1f} {x-2*sc:.1f},{y+2*sc:.1f} {x},{y} Z" fill="#ffb7c5" opacity="0.85" />'
                f'</g>'
            )
    return elements

def generate_paddle_svg(pskin, engine, paddle_hex):
    style = pskin.get("style", "default")
    pw, ph = engine.paddle_w, engine.paddle_h
    mid_y = ph / 2
    svg_defs = []

    if style == "laser":
        cap_w = 7
        caps_hex = rgb_to_hex(pskin["caps"])
        prim_hex = rgb_to_hex(pskin["primary"])
        core_hex = rgb_to_hex(pskin["core"])
        svg_defs.append(f'    <g id="paddle-graphic">')
        svg_defs.append(f'      <rect x="0" y="-2" width="{cap_w}" height="{ph + 4}" fill="{caps_hex}" />')
        svg_defs.append(f'      <rect x="{pw - cap_w}" y="-2" width="{cap_w}" height="{ph + 4}" fill="{caps_hex}" />')
        svg_defs.append(f'      <rect x="{cap_w}" y="0" width="{pw - 2*cap_w}" height="{ph}" rx="2" fill="{prim_hex}" />')
        svg_defs.append(f'      <rect x="{cap_w + 3}" y="{mid_y - 1}" width="{pw - 2*cap_w - 6}" height="2" fill="{core_hex}" />')
        svg_defs.append(f'      <rect x="{cap_w/2 - 1}" y="{mid_y - 1}" width="2" height="2" fill="#ffffff" />')
        svg_defs.append(f'      <rect x="{pw - cap_w/2 - 1}" y="{mid_y - 1}" width="2" height="2" fill="#ffffff" />')
        svg_defs.append(f'    </g>')
    elif style == "mecha":
        bw = 6
        booster_hex = rgb_to_hex(pskin["booster"])
        prim_hex = rgb_to_hex(pskin["primary"])
        plate_hex = rgb_to_hex(pskin["plate"])
        cx = pw / 2
        svg_defs.append(f'    <g id="paddle-graphic">')
        svg_defs.append(f'      <polygon points="0,2 {bw},-1 {bw},{ph+1} 0,{ph-2}" fill="{booster_hex}" />')
        svg_defs.append(f'      <polygon points="{pw},2 {pw-bw},-1 {pw-bw},{ph+1} {pw},{ph-2}" fill="{booster_hex}" />')
        svg_defs.append(f'      <rect x="{bw}" y="0" width="{pw - 2*bw}" height="{ph}" fill="{prim_hex}" />')
        svg_defs.append(f'      <rect x="{cx - pw*0.22}" y="-1" width="{pw*0.44}" height="{ph+2}" rx="2" fill="{plate_hex}" />')
        # Dual multi-layer rocket exhaust flame cones
        # Outer red flame
        svg_defs.append(f'      <polygon points="1,{ph-1} {bw-1},{ph-1} {bw/2},{ph+8}" fill="#ff3c1e" style="animation: flame-flicker 0.16s linear infinite alternate; transform-box: fill-box; transform-origin: top;" />')
        svg_defs.append(f'      <polygon points="{pw-1},{ph-1} {pw-bw+1},{ph-1} {pw - bw/2},{ph+8}" fill="#ff3c1e" style="animation: flame-flicker 0.16s linear infinite alternate 0.08s; transform-box: fill-box; transform-origin: top;" />')
        # Inner yellow/white flame core
        svg_defs.append(f'      <polygon points="2,{ph-1} {bw-2},{ph-1} {bw/2},{ph+5}" fill="#ffeb3b" style="animation: flame-flicker 0.12s linear infinite alternate 0.04s; transform-box: fill-box; transform-origin: top;" />')
        svg_defs.append(f'      <polygon points="{pw-2},{ph-1} {pw-bw+2},{ph-1} {pw - bw/2},{ph+5}" fill="#ffeb3b" style="animation: flame-flicker 0.12s linear infinite alternate 0.09s; transform-box: fill-box; transform-origin: top;" />')
        # Rocket spark embers shooting downward
        svg_defs.append(f'      <circle cx="{bw/2}" cy="{ph+9}" r="1.5" fill="#ffa000" style="animation: spark-drift 0.35s linear infinite; transform-box: fill-box;" />')
        svg_defs.append(f'      <circle cx="{pw - bw/2}" cy="{ph+9}" r="1.5" fill="#ffa000" style="animation: spark-drift 0.35s linear infinite 0.17s; transform-box: fill-box;" />')
        svg_defs.append(f'    </g>')
    elif style == "retro":
        cap_w = 8
        prim_hex = rgb_to_hex(pskin["primary"])
        caps_hex = rgb_to_hex(pskin["caps"])
        stripes_hex = rgb_to_hex(pskin["stripes"])
        svg_defs.append(f'    <g id="paddle-graphic">')
        svg_defs.append(f'      <polygon points="0,{ph} {cap_w},0 {cap_w},{ph}" fill="{caps_hex}" />')
        svg_defs.append(f'      <polygon points="{pw},{ph} {pw-cap_w},0 {pw-cap_w},{ph}" fill="{caps_hex}" />')
        svg_defs.append(f'      <rect x="{cap_w}" y="0" width="{pw - 2*cap_w}" height="{ph}" fill="{prim_hex}" />')
        for sx in range(int(cap_w + 6), int(pw - cap_w - 6), 12):
            svg_defs.append(f'      <polygon points="{sx},{ph} {sx+4},0 {sx+8},0 {sx+4},{ph}" fill="{stripes_hex}" />')
        svg_defs.append(f'      <line x1="{cap_w}" y1="1" x2="{pw-cap_w}" y2="1" stroke="#ffffff" stroke-width="1.5" />')
        # Distinct, visible 8-bit golden pixel dust motes floating up (3x3 and 4x4)
        svg_defs.append(f'      <rect x="{pw/2 - 14}" y="-6" width="3.5" height="3.5" fill="#ffd700" style="animation: spark-drift 0.5s linear infinite;" />')
        svg_defs.append(f'      <rect x="{pw/2 - 2}" y="-8" width="4.5" height="4.5" fill="#fff59d" style="animation: spark-drift 0.45s linear infinite 0.15s;" />')
        svg_defs.append(f'      <rect x="{pw/2 + 12}" y="-6" width="3.5" height="3.5" fill="#ffb300" style="animation: spark-drift 0.5s linear infinite 0.3s;" />')
        svg_defs.append(f'    </g>')
    elif style == "cyber":
        prim_hex = rgb_to_hex(pskin["primary"])
        core_hex = rgb_to_hex(pskin["core"])
        caps_hex = rgb_to_hex(pskin["caps"])
        cx = pw / 2
        svg_defs.append(f'    <g id="paddle-graphic">')
        svg_defs.append(f'      <rect x="0" y="0" width="{pw}" height="{ph}" rx="4" fill="{caps_hex}" stroke="{prim_hex}" stroke-width="1.5" />')
        svg_defs.append(f'      <rect x="6" y="2" width="{pw - 12}" height="{ph - 4}" fill="{prim_hex}" />')
        svg_defs.append(f'      <circle cx="{cx}" cy="{mid_y}" r="4.5" fill="{core_hex}" style="animation: pulse-glow 0.4s ease-in-out infinite alternate;" />')
        # Big neon data bit blocks
        svg_defs.append(f'      <rect x="{cx - 16}" y="-6" width="3.5" height="3.5" fill="{core_hex}" style="animation: spark-drift 0.5s linear infinite;" />')
        svg_defs.append(f'      <rect x="{cx + 16}" y="-7" width="3.5" height="3.5" fill="{prim_hex}" style="animation: spark-drift 0.5s linear infinite 0.25s;" />')
        svg_defs.append(f'    </g>')
    else:
        svg_defs.append(f'    <g id="paddle-graphic">')
        svg_defs.append(f'      <rect x="0" y="0" width="{pw}" height="{ph}" rx="3" fill="{paddle_hex}" />')
        svg_defs.append(f'    </g>')

    return "\n".join(svg_defs)
