def build_svg_keyframes(history, total_frames):
    ball_kf = []
    paddle_kf = []
    for i, h in enumerate(history):
        pct = round((i / (total_frames - 1)) * 100, 2)
        ball_kf.append(f"{pct}% {{ transform: translate({h['bx']}px, {h['by']}px); }}")
        paddle_kf.append(f"{pct}% {{ transform: translate({h['px']}px, {h['py']}px); }}")
    return ball_kf, paddle_kf

def build_trail_keyframes(history, total_frames, trail_count):
    trail_kfs = []
    for t_i in range(trail_count):
        tkf = []
        in_inactive = False
        start_pct = None
        prev_pct = None
        for f_i, h in enumerate(history):
            pct = round((f_i / (total_frames - 1)) * 100, 2)
            pts = h["trail"]
            if t_i < len(pts):
                if in_inactive:
                    span = f"{start_pct}%" if start_pct == prev_pct else f"{start_pct}%, {prev_pct}%"
                    tkf.append(f"{span} {{ opacity: 0; }}")
                    in_inactive = False
                pt = pts[t_i]
                tkf.append(f"{pct}% {{ transform: translate({pt[0]}px, {pt[1]}px); opacity: 0.7; }}")
            else:
                if not in_inactive:
                    in_inactive = True
                    start_pct = pct
            prev_pct = pct
        if in_inactive:
            span = f"{start_pct}%" if start_pct == prev_pct else f"{start_pct}%, {prev_pct}%"
            tkf.append(f"{span} {{ opacity: 0; }}")
        trail_kfs.append(f"@keyframes trail-{t_i} {{\n      " + "\n      ".join(tkf) + "\n    }")
    return trail_kfs

def build_particle_keyframes(history, total_frames, max_particles=14):
    particle_kfs = []
    particle_info = []
    for p_i in range(max_particles):
        pkf = []
        dominant_type = "debris"
        dominant_size = 1
        in_inactive = False
        start_pct = None
        prev_pct = None
        for f_i, h in enumerate(history):
            pct = round((f_i / (total_frames - 1)) * 100, 2)
            pts = h["particles"]
            if p_i < len(pts):
                if in_inactive:
                    span = f"{start_pct}%" if start_pct == prev_pct else f"{start_pct}%, {prev_pct}%"
                    pkf.append(f"{span} {{ opacity: 0; }}")
                    in_inactive = False
                pt = pts[p_i]
                dominant_type = pt["type"]
                dominant_size = pt["size"]
                pkf.append(f"{pct}% {{ transform: translate({pt['x']}px, {pt['y']}px); color: {pt['color']}; opacity: 1; }}")
            else:
                if not in_inactive:
                    in_inactive = True
                    start_pct = pct
            prev_pct = pct
        if in_inactive:
            span = f"{start_pct}%" if start_pct == prev_pct else f"{start_pct}%, {prev_pct}%"
            pkf.append(f"{span} {{ opacity: 0; }}")
        particle_kfs.append(f"@keyframes p-drift-{p_i} {{\n      " + "\n      ".join(pkf) + "\n    }")
        particle_info.append((dominant_type, dominant_size))
    return particle_kfs, particle_info
