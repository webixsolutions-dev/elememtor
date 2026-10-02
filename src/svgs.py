"""Inline SVG artwork used by the templates (leaf branches + line icons).

Everything is vector so it stays crisp, needs no media upload and picks up
the global colors through CSS custom properties where it matters.
"""
import math


def _leaf(x, y, length, width, angle, light, dark, rib):
    """One pointed leaf whose base sits at (x, y), rotated by angle (deg)."""
    L, W = length, width
    path = (f"M0 0 C {L*0.25:.1f} {-W:.1f} {L*0.7:.1f} {-W*0.95:.1f} {L:.1f} 0 "
            f"C {L*0.7:.1f} {W*0.95:.1f} {L*0.25:.1f} {W:.1f} 0 0 Z")
    half = (f"M0 0 C {L*0.25:.1f} {-W:.1f} {L*0.7:.1f} {-W*0.95:.1f} {L:.1f} 0 Z")
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({angle:.1f})">'
            f'<path d="{path}" fill="{dark}"/>'
            f'<path d="{half}" fill="{light}"/>'
            f'<path d="M2 0 Q {L*0.5:.1f} {-W*0.08:.1f} {L*0.96:.1f} 0" stroke="{rib}" '
            f'stroke-width="1.1" fill="none" stroke-linecap="round"/></g>')


def leaf_branch(width=260, flip=False, rotate=0, seed=0):
    """A soft botanical sprig (stem + alternating leaves), photo-style tones."""
    light, dark, rib, stem = "#7E9A57", "#56743A", "#B9C99A", "#6B7F45"
    leaves = []
    # Stem: gentle curve from the left edge into the canvas.
    pts = [(0, 40), (80, 70), (160, 110), (230, 160)]
    stem_d = "M0 40 C 70 55 150 95 235 165"
    spec = [  # t along stem, side, length, width, extra angle
        (0.10, -1, 70, 20, -8), (0.22, 1, 78, 22, 6), (0.38, -1, 84, 24, -4),
        (0.52, 1, 86, 25, 10), (0.66, -1, 80, 23, 2), (0.80, 1, 70, 21, 14),
        (0.97, 0, 64, 19, 0),
    ]
    for t, side, L, Wd, extra in spec:
        # cubic bezier point + tangent
        p0, p1, p2, p3 = (0, 40), (70, 55), (150, 95), (235, 165)
        mt = 1 - t
        x = mt**3*p0[0] + 3*mt*mt*t*p1[0] + 3*mt*t*t*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt*mt*t*p1[1] + 3*mt*t*t*p2[1] + t**3*p3[1]
        dx = 3*mt*mt*(p1[0]-p0[0]) + 6*mt*t*(p2[0]-p1[0]) + 3*t*t*(p3[0]-p2[0])
        dy = 3*mt*mt*(p1[1]-p0[1]) + 6*mt*t*(p2[1]-p1[1]) + 3*t*t*(p3[1]-p2[1])
        base = math.degrees(math.atan2(dy, dx))
        ang = base + side * 48 + extra
        leaves.append(_leaf(x, y, L, Wd, ang, light, dark, rib))
    t = ""
    if flip:
        t = 'transform="translate(300 0) scale(-1 1)"'
    inner = (f'<g {t}><g transform="rotate({rotate} 150 120)">'
             f'<path d="{stem_d}" stroke="{stem}" stroke-width="3" fill="none" stroke-linecap="round"/>'
             + "".join(leaves) + "</g></g>")
    return (f'<svg class="bo-leaf-art" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 240" '
            f'width="{width}" aria-hidden="true" focusable="false">'
            f'<defs><filter id="bo-soft{seed}" x="-10%" y="-10%" width="130%" height="140%">'
            f'<feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#2b3a1f" flood-opacity=".18"/>'
            f'</filter></defs><g filter="url(#bo-soft{seed})">{inner}</g></svg>')


def sprig_icon(size=26, color="currentColor", stroke=1.6):
    """Small hand-drawn style sprig used next to the logo and in sidebar boxes."""
    return (f'<svg class="bo-sprig" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 40" '
            f'width="{size}" height="{size*1.25:.0f}" fill="none" stroke="{color}" '
            f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M6 38 C 12 28 16 18 26 3"/>'
            '<path d="M24 6 C 18 6 15 10 16 14 C 21 13 24 10 24 6 Z"/>'
            '<path d="M19 15 C 13 15 10 19 11 23 C 16 22 19 19 19 15 Z"/>'
            '<path d="M21 13 C 27 13 30 16 29 20 C 24 20 21 17 21 13 Z"/>'
            '<path d="M15 23 C 21 23 24 26 23 30 C 18 30 15 27 15 23 Z"/>'
            '</svg>')


def leaf_outline_art(width=120, color="currentColor"):
    """Large line-art leaves (newsletter strip on the single post)."""
    return (f'<svg class="bo-leaf-outline" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 110" '
            f'width="{width}" fill="none" stroke="{color}" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M30 105 C 40 80 52 58 70 38"/>'
            '<path d="M60 48 C 52 30 58 12 78 4 C 84 24 78 40 60 48 Z"/><path d="M60 48 C 66 32 72 18 78 4"/>'
            '<path d="M70 38 C 86 28 104 30 116 42 C 100 54 82 52 70 38 Z"/><path d="M70 38 C 86 40 100 42 116 42"/>'
            '<path d="M42 72 C 26 64 10 68 2 80 C 18 90 34 86 42 72 Z"/><path d="M42 72 C 30 76 16 78 2 80"/>'
            '</svg>')
