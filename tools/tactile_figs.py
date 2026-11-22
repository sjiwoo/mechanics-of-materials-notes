"""Custom SVG figures for the Tactile Sensing book.

T   : section-card figures, key 't-<ch>-<sec>'  -> <template id="sf-t-<ch>-<sec>">
ART : chapter-header icons, key '<ch>'          -> <template id="art-t-<ch>">
Both are injected into index.html by  python tools/section_figs.py  (which imports this module).
Drawing helpers and CSS class conventions are those of section_figs.py.
"""
from section_figs import *

T = {}
ART = {}

# ======================= Chapters 1-4 =======================
import math
def ell(cx, cy, rx, ry, c='ah'):
    return (f'<ellipse class="{c}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>')

def spring(x, y0, y1, n=5, amp=4):
    """vertical zigzag spring from y0 (bottom) to y1 (top)"""
    d = f'M{x:.1f} {y0:.1f}'
    L = y0 - y1
    d += f'L{x:.1f} {y0 - L*0.12:.1f}'
    for i in range(n):
        yy = y0 - L * (0.12 + 0.76 * (i + 0.5) / n)
        d += f'L{x + (amp if i % 2 == 0 else -amp):.1f} {yy:.1f}'
    d += f'L{x:.1f} {y0 - L*0.88:.1f}L{x:.1f} {y1:.1f}'
    return path(d, 'k')

def block(x, y, w, h, d):
    """oblique box: front face at (x,y) size w x h, depth d up-right"""
    b = path(f'M{x} {y}L{x+d} {y-d*0.8:.1f}L{x+w+d} {y-d*0.8:.1f}L{x+w} {y}Z', 'kb')
    b += path(f'M{x+w} {y}L{x+w+d} {y-d*0.8:.1f}L{x+w+d} {y+h-d*0.8:.1f}L{x+w} {y+h}Z', 'kb')
    b += rect(x, y, w, h, 'ah')
    return b

# ---- 1-1 robot hand
b = ''
for x in (120, 146, 172, 198):
    b += rect(x, 26, 22, 62, 'kb', 10)
b += rect(116, 74, 108, 62, 'kb', 8)
b += rect(78, 90, 46, 22, 'kb', 10)
b += rect(122, 28, 18, 24, 'ah', 8)       # index patch
b += rect(80, 92, 20, 18, 'ah', 8)        # thumb patch
b += rect(138, 96, 66, 30, 'ah', 6)       # palm patch
for i in range(3):
    for j in range(2):
        b += circ(147 + i * 22, 105 + j * 12, 2, 'af')
b += line(122, 36, 100, 36, 'g') + text(96, 40, 'index', 's', 'end')
b += line(80, 102, 66, 102, 'g') + text(62, 106, 'thumb', 's', 'end')
b += line(204, 111, 232, 111, 'g') + text(236, 115, 'palm', 's', 'start')
b += text(262, 46, 'patch', 's') + text(262, 58, '= taxel array', 's')
T['t-1-1'] = svg(b)

# ---- 1-2 rigid vs formed
b = ''
cy, R = 88, 38
b += circ(80, cy, R, 'k')
b += rect(36, cy - R - 8, 88, 8, 'kb', 2)
b += circ(240, cy, R, 'k')
def arcband(cx, cy, r1, r2, a0, a1, n=24):
    p1 = [(cx + r2 * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy - r2 * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    p2 = [(cx + r1 * math.cos(math.radians(a1 - (a1 - a0) * i / n)), cy - r1 * math.sin(math.radians(a1 - (a1 - a0) * i / n))) for i in range(n + 1)]
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in p1 + p2) + 'Z'
b += path(arcband(240, cy, R, R + 8, 20, 160), 'ah')
b += arrow(80, 12, 80, cy - R - 12, 'k') + text(90, 24, 'P', '', 'start')
b += arrow(240, 12, 240, cy - R - 12, 'k') + text(250, 24, 'P', '', 'start')
b += text(80, 143, 'rigid: line contact', 's') + text(240, 143, 'formed: full contact', 's')
b += line(160, 20, 160, 140, 'g')
T['t-1-2'] = svg(b)

# ---- 1-3 layer stack
b = ''
x0, x1 = 100, 230
b += arrow(165, 8, 165, 30, 'k') + text(175, 22, 'p', '', 'start')
b += rect(x0, 32, x1 - x0, 16, 'kb') + text(238, 44, 'cover', 's', 'start')
b += rect(x0, 48, x1 - x0, 10, 'ah') + text(238, 56, 'substrate', 's', 'start')
for ex in (108, 180):
    b += rect(ex, 58, 42, 5, 'af')
b += rect(x0, 63, x1 - x0, 28, 'kb') + text(238, 80, 'separator', 's', 'start')
for ex in (108, 180):
    b += rect(ex, 91, 42, 5, 'af')
b += rect(x0, 96, x1 - x0, 10, 'ah') + text(238, 104, 'substrate', 's', 'start')
b += rect(x0, 106, x1 - x0, 18, 'kb') + text(238, 118, 'backing', 's', 'start')
b += line(96, 60, 104, 60, 'g') + text(92, 64, 'electrode', 's', 'end')
b += line(96, 93, 104, 93, 'g') + text(92, 97, 'electrode', 's', 'end')
T['t-1-3'] = svg(b, 150)

# ---- 2-1 substrate map
b = axes(44, 128, 262, 30, 'stretch', 'heat limit')
b += ell(210, 104, 40, 16) + text(210, 108, 'TPU')
b += ell(92, 92, 34, 15) + text(92, 96, 'PET')
b += ell(92, 52, 34, 15) + text(92, 56, 'PI')
T['t-2-1'] = svg(b)

# ---- 2-2 flake vs liquid metal
b = line(160, 24, 160, 140, 'g')
b += text(80, 18, 'flake ink', 't') + text(240, 18, 'liquid metal', 't')
b += rect(14, 36, 132, 26, 'kb', 3)
for i in range(4):
    b += rect(22 + i * 24, 42 + (i % 2) * 6, 30, 7, 'ah', 2)
b += text(80, 78, 'relaxed: touching', 's')
b += rect(14, 98, 144, 26, 'kb', 3)
for i in range(4):
    b += rect(22 + i * 32, 104 + (i % 2) * 6, 28, 7, 'ah', 2)
b += text(80, 140, 'stretched: gaps open', 's')
b += rect(172, 36, 124, 26, 'kb', 3) + rect(176, 44, 116, 10, 'ah', 4)
b += text(234, 78, 'relaxed', 's')
b += rect(172, 98, 142, 26, 'kb', 3) + rect(176, 108, 134, 6, 'ah', 3)
b += text(243, 140, 'stretched: flows', 's')
T['t-2-2'] = svg(b)

# ---- 2-3 percolation
xc = 150
def perc(x):
    if x < xc:
        return 121 - 2 * (x - 50) / (xc - 50)
    return 119 - 88 * ((x - xc) / (280 - xc)) ** 2
b = axes(50, 125, 285, 22, 'φ', 'σ')
b += line(xc, 125, xc, 40, 'g') + text(xc, 140, 'φc')
b += path(curve(perc, 50, 280, 60), 'a')
b += text(98, 106, 'insulating', 's') + text(196, 52, 'conducting', 's')
T['t-2-3'] = svg(b)

# ---- 2-4 modulus ladder
b = ''
ax = 112
b += arrow(20, ax, 300, ax, 'k', 6, 3)
def lx(e): return 30 + (e - 4) * 36
for e in range(4, 12):
    b += line(lx(e), ax - 3, lx(e), ax + 3, 'k')
for e, s in ((4, '10 kPa'), (6, '1 MPa'), (8, '100 MPa'), (10, '10 GPa')):
    b += text(lx(e), ax + 16, s, 's')
for e, s, y in ((4, 'foam', 74), (6, 'silicone', 74), (7.5, 'TPU', 74), (9.5, 'PET/PI', 74), (11, 'metal', 74)):
    b += circ(lx(e), ax, 4, 'af') + line(lx(e), y + 6, lx(e), ax - 5, 'g') + text(lx(e), y, s)
b += arrow(156, 38, lx(4), 38, 'a') + arrow(156, 38, lx(11), 38, 'a') + text(156, 30, 'seven decades', 's')
b += text(160, 146, 'E (log scale)', 's')
T['t-2-4'] = svg(b)

# ---- 2-5 process window
b = rect(110, 30, 110, 82, 'zr')
b += line(110, 30, 110, 112, 'g') + line(220, 30, 220, 112, 'a')
b += arrow(24, 112, 298, 112, 'k', 6, 3) + text(300, 116, 'T', '', 'start')
b += text(165, 66, 'window', 't') + text(165, 82, 'cure + form', 's')
b += text(62, 66, 'no cure', 's') + text(268, 66, 'distorts', 's')
b += text(110, 130, 'ink cures', 's') + text(220, 130, 'substrate limit', 's')
T['t-2-5'] = svg(b)

# ---- 3-1 pressure profiles
b = ''
b += arrow(80, 10, 80, 52, 'k') + text(90, 26, 'F', '', 'start')
b += rect(30, 54, 100, 16, 'kb', 2) + rect(30, 70, 100, 18, 'ah')
b += circ(240, 52, 20, 'ah') + arrow(240, 10, 240, 30, 'k') + text(250, 22, 'F', '', 'start')
b += rect(190, 72, 100, 16, 'ah')
base = 138
b += line(24, base, 136, base, 'k') + line(184, base, 296, base, 'k')
b += path(f'M30 {base}L30 114L130 114L130 {base}Z', 'zr') + path(f'M30 114L130 114', 'a')
fn = lambda x: base - 44 * math.sqrt(max(0, 1 - ((x - 240) / 38) ** 2))
b += path(curve(fn, 202, 278, 50) + f'L278 {base}L202 {base}Z', 'zr') + path(curve(fn, 202, 278, 50), 'a')
b += text(80, 152, 'uniform p', 's') + text(240, 152, 'peak at centre', 's')
T['t-3-1'] = svg(b, 158)

# ---- 3-2 Hertz
b = ''
cx, cy, R = 105, 80, 40
b += rect(20, 108, 170, 36, 'kb') + line(20, 108, 190, 108, 'g')
b += circ(cx, cy, R, 'ah') 
b += arrow(cx, 8, cx, cy - R - 2, 'k') + text(cx + 10, 22, 'F', '', 'start')
b += circ(cx, cy, 2, 'kf') + line(cx, cy, cx - 28, cy - 28, 'k') + text(cx - 24, cy - 8, 'R', '', 'end')
b += line(cx, 120, 168, 120, 'g')
b += arrow(160, 97, 160, 108, 'k') + arrow(160, 131, 160, 120, 'k') + text(170, 118, 'δ', '', 'start')
b += line(cx - 31, 108, cx - 31, 140, 'g') + line(cx + 31, 108, cx + 31, 140, 'g')
b += arrow(cx, 136, cx + 31, 136, 'k', 5, 2.6) + arrow(cx, 136, cx - 31, 136, 'k', 5, 2.6)
b += text(cx, 131, 'a', 's')
# pressure plot
pb = 126; pcx = 256; pa = 36
fn = lambda x: pb - 50 * math.sqrt(max(0, 1 - ((x - pcx) / pa) ** 2))
b += line(212, pb, 300, pb, 'k')
b += path(curve(fn, pcx - pa, pcx + pa, 50) + f'L{pcx+pa} {pb}L{pcx-pa} {pb}Z', 'zr') + path(curve(fn, pcx - pa, pcx + pa, 50), 'a')
b += text(pcx, 68, 'p₀') + text(pcx, 48, 'p(r)', 't')
b += arrow(pcx, 138, pcx + pa, 138, 'k', 5, 2.6) + arrow(pcx, 138, pcx - pa, 138, 'k', 5, 2.6) + text(pcx, 148, 'a', 's')
T['t-3-2'] = svg(b, 152)

# ---- 3-3 Winkler
b = ''
cx, cy, R = 160, 70, 40
b += arrow(cx, 8, cx, cy - R - 2, 'k') + text(cx + 10, 20, 'F', '', 'start')
b += wall_h(60, 250, 128, +1)
topy = lambda x: max(96, cy + math.sqrt(max(0, R * R - (x - cx) ** 2))) if abs(x - cx) < R else 96
for xs in range(94, 227, 11):
    b += spring(xs, 128, topy(xs), 5, 4)
b += circ(cx, cy, R, 'ah')
b += text(86, 116, 'p=k″u', 's', 'end')
b += arrow(252, 112, 252, 128, 'k', 5, 2.6) + arrow(252, 112, 252, 96, 'k', 5, 2.6) + text(262, 116, 'h', '', 'start')
b += line(cx - 30, 100, cx - 30, 144, 'g') + line(cx + 30, 100, cx + 30, 144, 'g')
b += arrow(cx, 144, cx + 30, 144, 'k', 5, 2.6) + arrow(cx, 144, cx - 30, 144, 'k', 5, 2.6) + text(cx, 155, '2a > h', 's')
b += text(288, 132, 'backing', 's')
T['t-3-3'] = svg(b, 160)

# ---- 3-4 load spreading
b = ''
h = 40
b += arrow(160, 8, 160, 32, 'k') + text(170, 20, 'F', '', 'start')
b += rect(40, 34, 240, h, 'ah')
b += line(160, 34, 137, 74, 'g') + line(160, 34, 183, 74, 'g')
for k in range(-4, 5):
    b += rect(160 + 28 * k - 9, 76, 18, 7, 'kb')
b += arrow(296, 54, 296, 74, 'k', 5, 2.6) + arrow(296, 54, 296, 34, 'k', 5, 2.6) + text(306, 58, 'h', '', 'end')
b += text(60, 28, 'cover', 's')
base = 142; sg = 17
fn = lambda x: base - 36 * math.exp(-((x - 160) ** 2) / (2 * sg * sg))
b += line(60, base, 260, base, 'k')
b += path(curve(fn, 60, 260, 80) + f'L260 {base}L60 {base}Z', 'zr') + path(curve(fn, 60, 260, 80), 'a')
b += arrow(160, 124, 183, 124, 'k', 4, 2.4) + arrow(160, 124, 137, 124, 'k', 4, 2.4)
b += text(160, 99, '≈ h', 's') + text(262, 124, 'p at taxels', 's', 'start')
T['t-3-4'] = svg(b, 150)

# ---- 4-1 stretch
b = ''
b += block(30, 60, 56, 56, 14)
lam = 1.8; s = 1 / math.sqrt(lam)
b += block(150, 116 - round(56 * s), round(56 * lam), round(56 * s), round(14 * s))
b += arrow(262, 98, 292, 98, 'k') + arrow(148, 98, 120, 98, 'k')
b += text(58, 134, 'L₀') + text(200, 134, 'λL₀')
b += text(160, 20, 'volume unchanged', 't') + text(206, 52, 'thinner both ways', 's')
T['t-4-1'] = svg(b)

# ---- 4-2 neo-Hookean
X = lambda l: 40 + (l - 0.6) / 1.2 * 240
Y = lambda s_: 75 - 24 * s_
b = arrow(20, 75, 292, 75, 'k', 6, 3) + text(296, 79, 'λ', '', 'start')
b += arrow(X(1), 130, X(1), 14, 'k', 6, 3) + text(X(1) + 8, 20, 's/μ', '', 'start')
b += line(X(1), 72, X(1), 78, 'k')
b += path(f'M{X(0.6):.1f} {Y(-1.2):.1f}L{X(1.8):.1f} {Y(2.4):.1f}', 'g')
b += path(curve(lambda x: Y((0.6 + (x - 40) / 240 * 1.2) - (0.6 + (x - 40) / 240 * 1.2) ** -2), 40, 280, 60), 'a')
b += text(205, 28, '3μ(λ−1)', 's') + text(222, 66, 'neo-Hookean', 't', 'start')
b += text(88, 128, 'stiffer', 's') + text(X(1) - 30, 72, '1', 's', 'end')
T['t-4-2'] = svg(b)

# ---- 4-3 bulk vs shear
b = ''
b += arrow(80, 8, 80, 28, 'k') + text(90, 22, 'F', '', 'start')
b += rect(44, 30, 72, 8, 'kb') + wall_h(30, 130, 100, +1)
b += rect(50, 40, 60, 60, 'g')
b += path('M52 40Q38 70 52 100L108 100Q122 70 108 40Z', 'ah')
b += arrow(240, 8, 240, 28, 'k') + text(250, 22, 'F', '', 'start')
b += wall_v(180, 40, 100, -1) + wall_v(260, 40, 100, +1) + wall_h(176, 264, 100, +1)
b += rect(182, 30, 76, 8, 'kb') + rect(181, 40, 78, 60, 'ah')
b += text(80, 128, 'free to bulge', 's') + text(80, 142, 'soft: shear G', 's')
b += text(220, 128, 'confined', 's') + text(220, 142, 'stiff: bulk K', 's')
T['t-4-3'] = svg(b)

# ---- 4-4 shape factor
b = ''
b += arrow(80, 12, 80, 40, 'k') + text(90, 26, 'F', '', 'start')
b += rect(55, 42, 50, 8, 'kb') + rect(55, 100, 50, 8, 'kb')
b += path('M58 50Q48 75 58 100L102 100Q112 75 102 50Z', 'ah')
b += arrow(240, 12, 240, 76, 'k') + text(250, 26, 'F', '', 'start')
b += rect(190, 78, 100, 8, 'kb') + rect(190, 100, 100, 8, 'kb')
b += path('M194 86Q191 93 194 100L286 100Q289 93 286 86Z', 'ah')
b += text(80, 126, 'thick: S small', 's') + text(80, 142, 'bulges freely', 's')
b += text(240, 126, 'thin: S large', 's') + text(240, 142, 'no room to bulge', 's')
b += line(160, 20, 160, 146, 'g')
T['t-4-4'] = svg(b)

# ---- 4-5 separators
b = ''
for i, (x0, lab, sub) in enumerate(((14, 'solid', 'stiffest'), (120, 'pillars', 'softer'), (226, 'foam', 'softest'))):
    cxm = x0 + 40
    b += arrow(cxm, 8, cxm, 36, 'k')
    b += rect(x0 - 4, 38, 88, 8, 'kb') + rect(x0 - 4, 100, 88, 8, 'kb')
    if i == 0:
        b += rect(x0, 46, 80, 54, 'ah')
    elif i == 1:
        for k in range(4):
            b += rect(x0 + k * 22, 46, 14, 54, 'ah')
    else:
        b += rect(x0, 46, 80, 54, 'ah')
        for r_, yy in enumerate((58, 73, 88)):
            for k in range(5):
                xx = x0 + 10 + k * 15 + (7 if r_ % 2 else 0)
                if xx < x0 + 74:
                    b += circ(xx, yy, 5, 'a')
    b += text(cxm, 128, lab) + text(cxm, 142, sub, 's')
T['t-4-5'] = svg(b)

# ======================= Chapters 5-8 =======================
import math

# ---------- local helpers ----------
def _dir(x1, y1, x2, y2):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return L, ux, uy, -uy, ux

def spring(x1, y1, x2, y2, n=5, amp=6, c='a'):
    L, ux, uy, vx, vy = _dir(x1, y1, x2, y2)
    lead = L * 0.18
    pts = [(0, 0), (lead, 0)]
    span = L - 2 * lead
    for i in range(n * 2):
        s = lead + span * (i + 0.5) / (n * 2)
        pts.append((s, amp if i % 2 == 0 else -amp))
    pts += [(L - lead, 0), (L, 0)]
    d = 'M' + 'L'.join(f'{x1 + ux*s + vx*t:.1f} {y1 + uy*s + vy*t:.1f}' for s, t in pts)
    return path(d, c)

def dashpot(x1, y1, x2, y2, w=7, c='k'):
    L, ux, uy, vx, vy = _dir(x1, y1, x2, y2)
    P = lambda s, t: f'{x1 + ux*s + vx*t:.1f} {y1 + uy*s + vy*t:.1f}'
    d = f'M{P(0,0)}L{P(L*.3,0)}'
    d += f'M{P(L*.7,-w)}L{P(L*.3,-w)}L{P(L*.3,w)}L{P(L*.7,w)}'
    d += f'M{P(L*.5,-w+3)}L{P(L*.5,w-3)}'
    d += f'M{P(L*.5,0)}L{P(L,0)}'
    return path(d, c)

def vline(x, y1, y2, c='k'):
    return line(x, y1, x, y2, c)

# ---------------- 5-1 ----------------
b = ''
b += rect(60, 38, 140, 7, 'ah') + rect(60, 45, 140, 38, 'kb') + rect(60, 83, 140, 7, 'ah')
for x in (90, 130, 170):
    b += arrow(x, 12, x, 34, 'k')
b += text(205, 24, 'F', '', 'start')
b += arrow(216, 45, 216, 83, 'a', 5, 2.6) + arrow(216, 83, 216, 45, 'a', 5, 2.6)
b += text(226, 68, 'd', 't', 'start')
b += text(130, 68, 'dielectric', 's')
b += text(52, 70, 'A', 't', 'end') + line(56, 38, 56, 90, 'g')
b += text(130, 108, 'electrodes: area A', 's')
b += text(160, 138, 'C = ε₀εᵣA / d', 't')
T['t-5-1'] = svg(b)

# ---------------- 5-2 ----------------
b = ''
x0, y0 = 50, 125
b += axes(x0, y0, 280, 20, 'p', 'ΔC/C₀')
soft = lambda x: y0 - 92 * (1 - math.exp(-(x - x0) / 28))
stiff = lambda x: y0 - 0.2 * (x - x0)
b += path(curve(soft, x0, 270), 'a') + path(curve(stiff, x0, 270), 'k')
b += text(190, 62, 'soft: steep, saturates', 't')
b += text(235, 112, 'stiff: shallow', 's')
T['t-5-2'] = svg(b)

# ---------------- 5-3 ----------------
b = ''
def box(x, top, bot, rows, cols):
    s = rect(x, top - 6, 70, 6, 'ah') + rect(x, top, 70, bot - top, 'kb') + rect(x, bot, 70, 6, 'ah')
    for (px, py) in [(x + cx, ry) for cx in cols for ry in rows]:
        s += circ(px, py, 5, 'af')
    return s
b += box(10, 42, 104, [52, 70, 88], [14, 35, 56])
b += box(95, 52, 94, [57, 67, 77, 87], [14, 35, 56])
b += arrow(130, 14, 130, 44, 'k') + text(138, 28, 'p', '', 'start')
b += text(45, 126, 'far apart', 's') + text(130, 126, 'touching', 's')
b += text(45, 142, 'high R', 't') + text(130, 142, 'low R', 't')
ox, oy = 205, 118
b += axes(ox, oy, 296, 28, 'p', 'R')
b += path(curve(lambda x: oy - (12 + 78 * math.exp(-(x - ox) / 28)), ox, 290), 'a')
T['t-5-3'] = svg(b)

# ---------------- 5-4 ----------------
b = ''
b += text(80, 20, 'Capacitive', 't') + text(240, 20, 'Resistive', 't')
for x in (20, 180):
    b += rect(x, 34, 120, 7, 'ah') + rect(x, 41, 120, 46, 'kb') + rect(x, 87, 120, 7, 'ah')
for x in (40, 120):
    b += line(x, 48, x, 80, 'g')
b += text(80, 68, 'C', 't')
for i, (px, py) in enumerate([(200,52),(228,50),(256,54),(284,51),(206,74),(236,70),(262,76),(288,72),(222,62),(272,63)]):
    b += circ(px, py, 3.5, 'af')
b += text(240, 100, '', '')
b += text(80, 114, 'repeatable, low power', 's') + text(80, 128, 'small signal, stray C', 's')
b += text(240, 114, 'large, simple readout', 's') + text(240, 128, 'creep, hysteresis', 's')
b += line(160, 30, 160, 136, 'g')
T['t-5-4'] = svg(b)

# ---------------- 5-5 ----------------
b = ''
rows = [44, 78, 112]
cols = [70, 110, 150, 190]
for i, y in enumerate(rows):
    b += rect(34, y, 206, 12, 'kb')
    b += text(26, y + 10, f'R{"₁₂₃"[i]}', 's', 'end')
for j, x in enumerate(cols):
    b += rect(x, 26, 12, 110, 'ah')
    b += text(x + 6, 20, f'C{"₁₂₃₄"[j]}', 's')
for y in rows:
    for x in cols:
        b += rect(x, y, 12, 12, 'zr')
b += arrow(268, 34, 205, 46, 'a')
b += text(284, 30, 'taxel', 't')
b += text(280, 108, 'm + n wires', 's') + text(279, 122, 'm × n taxels', 's')
T['t-5-5'] = svg(b)

# ---------------- 6-1 ----------------
b = ''
oy = 118
def plot(x0):
    return axes(x0, oy, x0 + 82, 36, 't', '')
# creep
x0 = 14
b += text(x0 + 45, 18, 'creep', 't') + axes(x0, oy, x0 + 82, 36, 't', 'ε')
b += path(curve(lambda x: oy - 14 - 48 * (1 - math.exp(-(x - x0) / 20)), x0, x0 + 80), 'a')
b += line(x0, oy - 62, x0 + 80, oy - 62, 'g')
b += text(x0 + 41, 138, 'σ held', 's')
# relaxation
x0 = 118
b += text(x0 + 45, 18, 'relaxation', 't') + axes(x0, oy, x0 + 82, 36, 't', 'σ')
b += path(curve(lambda x: oy - 12 - 50 * math.exp(-(x - x0) / 22), x0, x0 + 80), 'a')
b += line(x0, oy - 12, x0 + 80, oy - 12, 'g')
b += text(x0 + 41, 138, 'ε held', 's')
# hysteresis
x0 = 222
b += text(x0 + 45, 18, 'hysteresis', 't') + axes(x0, oy, x0 + 82, 36, 'ε', 'σ')
Lw, Hh = 74, 62
n = 30
up = [(x0 + Lw * i / n, oy - Hh * (i / n) ** 0.7) for i in range(n + 1)]
dn = [(x0 + Lw * i / n, oy - Hh * (i / n) ** 1.6) for i in range(n, -1, -1)]
d = 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in up + dn) + 'Z'
b += path(d, 'ah')
b += text(x0 + 41, 138, 'loop area = loss', 's')
T['t-6-1'] = svg(b)

# ---------------- 6-2 ----------------
b = ''
top, bot = 30, 133
def bars(xa, xb):
    return line(xa, top, xb, top, 'k') + line(xa, bot, xb, bot, 'k') + line(xa, top - 4, xb, top - 4, 'k') * 0
# Maxwell
cx = 55
b += line(cx - 20, top, cx + 20, top, 'k') + line(cx - 20, bot, cx + 20, bot, 'k')
b += spring(cx, top, cx, 80) + dashpot(cx, 80, cx, bot)
b += text(cx + 12, 58, 'E', '', 'start') + text(cx + 12, 112, 'η', '', 'start')
b += text(cx, 154, 'Maxwell', 't') + text(cx, 168, 'series', 's')
# Kelvin-Voigt
cx = 160
b += line(cx - 32, top, cx + 32, top, 'k') + line(cx - 32, bot, cx + 32, bot, 'k')
b += spring(cx - 20, top, cx - 20, bot) + dashpot(cx + 20, top, cx + 20, bot)
b += text(cx - 10, 84, 'E', '', 'start') + text(cx + 30, 84, 'η', '', 'start')
b += text(cx, 154, 'Kelvin-Voigt', 't') + text(cx, 168, 'parallel', 's')
# SLS
cx = 265
b += line(cx - 38, top, cx + 38, top, 'k') + line(cx - 38, bot, cx + 38, bot, 'k')
b += spring(cx - 24, top, cx - 24, bot)
b += spring(cx + 20, top, cx + 20, 80) + dashpot(cx + 20, 80, cx + 20, bot)
b += text(cx - 14, 84, 'E₁', '', 'start') + text(cx + 30, 58, 'E₂', '', 'start') + text(cx + 30, 112, 'η', '', 'start')
b += text(cx, 154, 'Standard solid', 't') + text(cx, 168, 'spring ∥ Maxwell', 's')
T['t-6-2'] = svg(b, 175)

# ---------------- 6-3 ----------------
b = ''
mid = 82
per = 120
sh = 14
b += arrow(20, mid, 256, mid, 'k', 6, 3) + arrow(20, 132, 20, 26, 'k', 6, 3)
b += text(262, mid + 4, 't', '', 'start')
A = 36
fs = lambda x: mid - A * math.sin(2 * math.pi * (x - 20) / per)
fe = lambda x: mid - A * math.sin(2 * math.pi * (x - 20 - sh) / per)
b += path(curve(fs, 20, 245, 90), 'a') + path(curve(fe, 20, 245, 90), 'k')
px = 20 + per / 4
b += line(px, 38, px, mid - A + 0, 'g') + line(px + sh, 38, px + sh, mid - A + 0, 'g')
b += arrow(px - 14, 42, px, 42, 'a', 5, 2.6) + arrow(px + sh + 14, 42, px + sh, 42, 'a', 5, 2.6)
b += text(px + sh / 2, 32, 'δ', 't')
b += text(284, 52, 'σ', 't') + text(284, 72, 'ε')
b += line(266, 48, 278, 48, 'a') + line(266, 68, 278, 68, 'k')
b += text(160, 146, 'strain lags stress by δ', 's')
T['t-6-3'] = svg(b)

# ---------------- 6-4 ----------------
b = ''
x0, y0, L, H = 46, 125, 170, 90
b += axes(x0, y0, x0 + L + 14, 20, 'p', 'output')
up = lambda x: y0 - H * ((x - x0) / L) ** 0.7
dn = lambda x: y0 - H * ((x - x0) / L) ** 1.4
b += path(curve(dn, x0, x0 + L), 'a') + path(curve(up, x0, x0 + L), 'k')
u = 0.5 ** (1 / 0.7)
gx = x0 + L * u
b += arrow(gx, dn(gx) - 1, gx, up(gx) + 1, 'a', 5, 2.6) + arrow(gx, up(gx) + 1, gx, dn(gx) - 1, 'a', 5, 2.6)
b += text(60, 48, 'max gap', 't', 'start') + line(104, 52, gx - 2, up(gx) + 8, 'g')
b += text(140, 38, 'unloading', 's', 'start')
b += text(150, 110, 'loading', 's', 'start')
T['t-6-4'] = svg(b)

# ---------------- 7-1 ----------------
b = ''
cx, cy, Rm, tt = 160, 160, 95, 24
def pol(r, a):
    return cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a))
ro, ri = Rm + tt / 2, Rm - tt / 2
a0 = 35
p1, p2, p3, p4 = pol(ro, -a0), pol(ro, a0), pol(ri, a0), pol(ri, -a0)
d = (f'M{p1[0]:.1f} {p1[1]:.1f}A{ro} {ro} 0 0 1 {p2[0]:.1f} {p2[1]:.1f}L{p3[0]:.1f} {p3[1]:.1f}'
     f'A{ri} {ri} 0 0 0 {p4[0]:.1f} {p4[1]:.1f}Z')
b += path(d, 'ah')
n1, n2 = pol(Rm, -a0 - 6), pol(Rm, a0 + 6)
b += path(f'M{n1[0]:.1f} {n1[1]:.1f}A{Rm} {Rm} 0 0 1 {n2[0]:.1f} {n2[1]:.1f}', 'g')
b += text(160, 44, 'tension', 't')
b += text(160, 100, 'compression', 's')
b += text(n2[0] + 8, n2[1] + 6, 'neutral axis', 's', 'start')
r1 = pol(Rm, -35)
b += line(cx, cy, r1[0], r1[1], 'g') + circ(cx, cy, 2.5, 'kf')
b += text((cx + r1[0]) / 2 - 8, (cy + r1[1]) / 2 - 2, 'ρ', 't', 'end')
b += text(262, 150, 'ε = y / ρ', 't')
T['t-7-1'] = svg(b, 170)

# ---------------- 7-2 ----------------
b = ''
b += text(160, 22, 'ȳ = ΣEᵢtᵢyᵢ / ΣEᵢtᵢ', 't')
b += rect(56, 40, 170, 56, 'kb') + rect(56, 96, 170, 28, 'ah')
b += text(141, 58, 'soft layer', 's') + text(141, 121, 'stiff layer', 's')
b += line(48, 68, 232, 68, 'g') + text(238, 72, 'mid-plane', 's', 'start')
b += line(48, 110, 226, 110, 'a') + text(232, 114, 'neutral axis', 't', 'start')
b += arrow(40, 68, 40, 108, 'k') + text(34, 92, 'shift', 's', 'end')
T['t-7-2'] = svg(b)

# ---------------- 7-3 ----------------
b = ''
b += text(100, 20, 'on the surface', 't') + text(240, 20, 'buried', 't')
b += rect(56, 50, 90, 48, 'kb') + rect(88, 44, 26, 6, 'af')
b += line(50, 74, 152, 74, 'g') + text(154, 78, 'N.A.', 's', 'start')
b += arrow(40, 74, 40, 47, 'k') + text(34, 64, 'y', '', 'end')
b += arrow(74, 46, 56, 46, 'a', 5, 2.6) + arrow(128, 46, 146, 46, 'a', 5, 2.6)
b += text(101, 36, 'trace', 's')
b += text(100, 118, 'ε = y / ρ', 't') + text(100, 134, 'full bending strain', 's')
b += rect(190, 50, 110, 24, 'kb') + rect(190, 74, 110, 24, 'kb') + rect(228, 71, 34, 6, 'af')
b += line(184, 74, 306, 74, 'g')
b += text(245, 40, 'trace', 's') + line(245, 43, 245, 70, 'g')
b += text(245, 118, 'y = 0, ε ≈ 0', 't') + text(245, 134, 'on neutral plane', 's')
T['t-7-3'] = svg(b)

# ---------------- 7-4 ----------------
b = ''
def band(xc, hw, y_top, thick, k=22, hwn=60, n=30):
    f = lambda x: y_top - k * ((x - xc) / hwn) ** 2
    xs = [xc - hw + 2 * hw * i / n for i in range(n + 1)]
    top = [(x, f(x)) for x in xs]
    bt = [(x, f(x) + thick) for x in reversed(xs)]
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in top + bt) + 'Z'
b += text(80, 20, 'bonded', 't') + text(240, 20, 'free to slide', 't')
b += path(band(80, 60, 92, 20), 'ah')
b += path(band(240, 66, 92, 10), 'ah') + path(band(240, 58, 102, 10, hwn=60), 'kb')
b += arrow(80, 34, 80, 62, 'k') + text(88, 46, 'F', '', 'start')
b += arrow(240, 34, 240, 62, 'k') + text(248, 46, 'F', '', 'start')
b += text(292, 112, 'slip', 's')
b += text(80, 138, 'D ∝ (n t)³', '') + text(240, 138, 'D ∝ n t³', '')
T['t-7-4'] = svg(b)

# ---------------- 8-1 ----------------
b = ''
x0, y0 = 46, 125
sg = lambda z: 1 / (1 + math.exp(-z))
fy = lambda x: 38 + 56 * sg((x - 135) / 5) + 30 * sg((x - 250) / 7)
b += rect(148, 28, 90, 97, 'zr')
b += axes(x0, y0, 290, 20, 'T', 'log E')
b += path(curve(fy, x0, 280, 100), 'a')
b += line(135, 125, 135, 60, 'g') + text(135, 138, 'Tg', 't')
b += text(85, 27, 'glassy', 't')
b += text(195, 86, 'rubbery', 't')
b += text(268, 112, 'flow', 't')
b += arrow(160, 42, 160, 92, 'k') + arrow(160, 92, 160, 42, 'k')
b += text(166, 70, '~10³×', 's', 'start')
b += text(193, 106, 'forming', 's') + text(193, 117, 'window', 's')
T['t-8-1'] = svg(b)

# ---------------- 8-2 ----------------
b = ''
b += rect(70, 100, 180, 34, 'kb') + path('M130 100A30 30 0 0 1 190 100Z', 'kb')
d = 'M70 96L126.3 96A34 34 0 0 1 193.7 96L250 96L250 100L190 100A30 30 0 0 0 130 100L70 100Z'
b += path(d, 'ah')
def top_y(x):
    dx = x - 160
    return 100 - math.sqrt(34 ** 2 - dx ** 2) if abs(dx) < 34 else 96
for x in (118, 142, 160, 178, 202, 230):
    b += arrow(x, 28, x, top_y(x) - 5, 'a', 6, 3)
b += text(174, 18, 'pressure p', 't')
b += text(8, 82, 'heated stack', 's', 'start')
b += text(100, 122, 'mould', 's')
for x in (145, 175):
    b += arrow(x, 104, x, 152, 'k', 6, 3)
b += text(184, 150, 'vents', 's', 'start')
T['t-8-2'] = svg(b, 165)

# ---------------- 8-3 ----------------
b = ''
b += rect(30, 100, 80, 10, 'ah') + text(118, 109, 't₀', '', 'start')
b += path('M200 110A40 40 0 0 1 280 110L275 110A35 35 0 0 0 205 110Z', 'ah') + text(286, 108, 't₀/2', '', 'start')
b += arrow(122, 90, 190, 90, 'k') + text(156, 82, 'form', 's')
b += arrow(70, 122, 110, 122, 'k', 5, 2.6) + text(90, 136, 'R', 's')
b += arrow(240, 122, 280, 122, 'k', 5, 2.6) + text(260, 136, 'R', 's')
b += text(70, 152, 'A₀ = πR²', 't') + text(240, 152, 'A = 2πR²', 't')
T['t-8-3'] = svg(b, 160)

# ---------------- 8-4 ----------------
b = ''
b += text(70, 18, 'Trace', 't') + text(244, 18, 'Taxel', 't')
b += rect(20, 38, 60, 12, 'ah') + text(88, 48, 'R₀', '', 'start')
b += arrow(50, 56, 50, 90, 'k') + text(58, 76, 'λ', '', 'start')
b += rect(20, 94, 90, 8, 'ah') + text(116, 102, 'λ²R₀', 't', 'start')
b += text(70, 128, 'L × λ, A ÷ λ', 's')
b += rect(222, 28, 44, 6, 'ah') + rect(222, 56, 44, 6, 'ah') + text(272, 48, 'C₀', '', 'start') + text(216, 48, 'd', 's', 'end')
b += arrow(244, 66, 244, 84, 'k') + text(252, 78, 'λ', '', 'start')
b += rect(212, 88, 64, 6, 'ah') + rect(212, 103, 64, 6, 'ah') + text(282, 102, 'λ⁴C₀', 't', 'start') + text(208, 102, 'd/λ²', 's', 'end')
b += text(244, 128, 'A × λ², d ÷ λ²', 's')
T['t-8-4'] = svg(b)

# ======================= Chapters 9-11 and chapter art =======================
import math
def bez(p0, p1, p2, t):
    return ((1-t)**2*p0[0] + 2*t*(1-t)*p1[0] + t*t*p2[0],
            (1-t)**2*p0[1] + 2*t*(1-t)*p1[1] + t*t*p2[1])

def poly(pts, c='ah'):
    return f'<path class="{c}" d="M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'z"/>'

def band(p, q, th):
    """polygon for a strip from p to q with thickness th (offset to the left of travel)"""
    dx, dy = q[0]-p[0], q[1]-p[1]
    L = math.hypot(dx, dy)
    nx, ny = dy/L*th, -dx/L*th
    return [p, q, (q[0]+nx, q[1]+ny), (p[0]+nx, p[1]+ny)]

# ---------------- 9-1 wetting ----------------
b = ''
sy = 104
b += wall_h(14, 306, sy, 1)
# beaded, theta = 110
a, th = 30, math.radians(110)
r = a/math.sin(th); cx = 82
b += path(f'M{cx-a} {sy}A{r:.1f} {r:.1f} 0 1 1 {cx+a} {sy}z', 'ah')
ux, uy = math.cos(math.radians(70)), -math.sin(math.radians(70))
b += line(cx+a, sy, cx+a+44*ux, sy+44*uy, 'g') + line(cx+a, sy, cx+a+40, sy, 'g')
b += path(f'M{cx+a+16} {sy}A16 16 0 0 0 {cx+a+16*ux:.1f} {sy+16*uy:.1f}', 'k')
b += text(cx+a+22, sy-8, 'θ', 't', 'start')
b += text(cx, sy+30, 'untreated') + text(cx, sy+44, 'low surface energy', 's')
# spread, theta = 35
a, th = 52, math.radians(35)
r = a/math.sin(th); cx = 232
b += path(f'M{cx-a} {sy}A{r:.1f} {r:.1f} 0 0 1 {cx+a} {sy}z', 'ah')
ux, uy = -math.cos(th), -math.sin(th)
b += line(cx+a, sy, cx+a-50*ux*0.0+ -ux*46, sy-uy*46*0 + 0, 'g') if False else ''
b += line(cx+a, sy, cx+a+ux*52, sy+uy*52, 'g') + line(cx+a, sy, cx+a+30, sy, 'g')
b += path(f'M{cx+a-26} {sy}A26 26 0 0 1 {cx+a+26*ux:.1f} {sy+26*uy:.1f}', 'k')
b += text(cx+a-36, sy-5, 'θ', 't', 'end')
b += text(cx, sy+30, 'plasma treated') + text(cx, sy+44, 'high surface energy', 's')
T['t-9-1'] = svg(b, 156)

# ---------------- 9-2 peel ----------------
b = ''
sy, fx = 112, 160
b += wall_h(14, 306, sy, 1)
b += rect(30, sy-6, fx-30, 6, 'ah')
th = math.radians(60)
ex, ey = fx + 62*math.cos(th), sy - 3 - 62*math.sin(th)
b += poly(band((fx, sy-6), (fx+62*math.cos(th), sy-6-62*math.sin(th)), 6)[0:4][::1], 'ah') if False else ''
pa = (fx, sy-6); pb = (fx+64*math.cos(th), sy-6-64*math.sin(th))
dx, dy = pb[0]-pa[0], pb[1]-pa[1]; L = math.hypot(dx, dy); nx, ny = dy/L*6, -dx/L*6
b += poly([pa, pb, (pb[0]-nx*-1*-1, pb[1]-ny*-1*-1)] , 'ah') if False else ''
b += poly([pa, pb, (pb[0]+ny*0+0, pb[1]), (pa[0], pa[1])], 'ah') if False else ''
# peeled arm as a strip of thickness 6 whose lower face starts at the front
q = [(fx, sy), (fx+64*math.cos(th), sy-64*math.sin(th)),
     (fx+64*math.cos(th)+6*math.sin(th), sy-64*math.sin(th)-6*math.cos(th)),
     (fx+6*math.sin(th), sy-6*math.cos(th))]
b += poly(q, 'ah')
tipx, tipy = fx+64*math.cos(th)+3*math.sin(th), sy-64*math.sin(th)-3*math.cos(th)
b += arrow(tipx, tipy, tipx+34*math.cos(th), tipy-34*math.sin(th), 'a')
b += text(tipx+34*math.cos(th)+8, tipy-34*math.sin(th)+6, 'F', 't', 'start')
b += line(fx, sy, fx+70, sy, 'g')
b += path(f'M{fx+32} {sy}A32 32 0 0 0 {fx+32*math.cos(th):.1f} {sy-32*math.sin(th):.1f}', 'k')
b += text(fx+40, sy-14, 'θ', 't', 'start')
b += text(92, sy-14, 'bonded', 's') + text(92, sy+30, 'substrate', 's')
b += text(20, 40, 'width b', 's', 'start')
b += text(20, 58, 'G = (F/b)(1 − cosθ)', 't', 'start')
b += text(20, 74, 'peels when G ≥ Γ', 's', 'start')
T['t-9-2'] = svg(b, 150)

# ---------------- 9-3 bilayer curl ----------------
b = ''
x0, x1, y = 16, 126, 92
b += rect(x0, y-10, x1-x0, 10, 'ah') + rect(x0, y, x1-x0, 10, 'kb')
b += text(x1+6, y-1, 'α₁', 't', 'start') + text(x1+6, y+12, 'α₂', '', 'start')
b += text(71, 140, 'at T₀')
b += arrow(150, 88, 184, 88, 'a') + text(167, 80, 'ΔT', 't')
ccx, ccy, R = 246, 132, 52
phi = 1.0
def arcpts(r):
    return [(ccx + r*math.sin(-phi+2*phi*i/30), ccy - r*math.cos(-phi+2*phi*i/30)) for i in range(31)]
outer, mid, inner = arcpts(R+10), arcpts(R), arcpts(R-10)
b += poly(outer + mid[::-1], 'ah') + poly(mid + inner[::-1], 'kb')
b += text(ccx, 144, 'after ΔT: curls')
b += text(ccx, 56, 'α₁ > α₂', 's')
T['t-9-3'] = svg(b, 152)

# ---------------- 9-4 fatigue ----------------
b = ''
ox, oy = 40, 126
b += axes(ox, oy, 268, 16, 'cycles', 'R / R₀')
def rr(x):
    u = (x-ox)/226
    return oy - (14 + 18*u + 76*u**9)
b += path(curve(rr, ox, ox+226, 60), 'a')
b += line(ox, oy-14, ox+226, oy-14, 'g') + text(ox-4, oy-10, 'R₀', 's', 'end')
b += line(ox+226, oy, ox+226, rr(ox+226), 'g') + circ(ox+226, rr(ox+226), 3.5, 'af')
b += text(ox+226, oy+14, 'failure', 's')
b += text(110, 84, 'micro-cracks grow', 's')
b += path(f'M{ox+158} 95L{ox+120} {rr(ox+120)-6:.1f}', 'g') if False else ''
b += text(214, 46, 'sharp rise', 's', 'end')
T['t-9-4'] = svg(b, 152)

# ---------------- 10-1 two routes ----------------
b = ''
def flow(y, title, steps, hl):
    s = text(8, y, title, 't', 'start')
    for i, st in enumerate(steps):
        x = 8 + i*80
        s += rect(x, y+10, 64, 34, 'ah' if i == hl else 'kb', 3)
        lines = st.split('\n')
        for j, ln in enumerate(lines):
            yy = y+10+17+4 + (j-(len(lines)-1)/2)*12
            s += text(x+32, yy, ln, 's')
        if i < 3:
            s += arrow(x+64, y+27, x+80, y+27, 'k', 5, 2.6)
    return s
b += flow(20, 'A: build flat, then form (method 300)', ['substrate', 'pattern', 'laminate\nstack', 'form'], 3)
b += flow(88, 'B: form, then build (method 800)', ['form', 'pattern', 'separator', 'second\nlayer'], 0)
T['t-10-1'] = svg(b, 150)

# ---------------- 10-2 screen printing ----------------
b = ''
my = 96
b += line(20, my, 248, my, 'k')
segs = [(20, 60), (80, 100), (125, 200), (225, 248)]
for s0, s1 in segs:
    b += rect(s0, my, s1-s0, 6, 'kb')
for s0, s1 in [(60, 80), (100, 125)]:
    b += rect(s0, my, s1-s0, 6, 'af')
b += rect(20, my+6, 228, 8, 'ah') + rect(20, my+14, 228, 16, 'kb')
b += text(134, my+26, 'chuck', 's')
b += poly([(120, 40), (131, 40), (158, my), (148, my)], 'kb')
b += text(112, 52, 'blade', '', 'end')
b += path(f'M{cx} 0', 'k') if False else ''
b += path('M160 96A15 9 0 0 1 190 96z', 'ah') + text(194, 84, 'ink', 's', 'start')
b += arrow(168, 26, 214, 26, 'a') + text(222, 30, 'v', 't', 'start')
b += text(256, my-1, 'stencil', 's', 'start')
b += text(256, my+13, 'substrate', 's', 'start')
b += text(256, my+27, 'chuck', 's', 'start') if False else ''
b += text(212, 80, '', 's')
b += text(212, 124, 'openings', 's', 'middle') if False else ''
T['t-10-2'] = svg(b, 140)

# ---------------- 10-3 three methods ----------------
b = ''
def dome(cx):
    x0, x1, y0, yc = cx-44, cx+44, 116, 60
    return (x0, x1, y0, yc)
def ypos(cx, x):
    x0, x1, y0, yc = dome(cx)
    t = (x-x0)/(x1-x0)
    return bez((x0, y0), (cx, yc), (x1, y0), t)[1]
def surf(cx):
    x0, x1, y0, yc = dome(cx)
    return path(f'M{x0} 132L{x0} {y0}Q{cx} {yc} {x1} {y0}L{x1} 132z', 'kb')
def sub(cx, s0, s1, c='a'):
    x0, x1, y0, yc = dome(cx)
    P0, P1, P2 = (x0, y0), (cx, yc), (x1, y0)
    ps = [bez(P0, P1, P2, s0+(s1-s0)*i/20) for i in range(21)]
    return path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in ps), c)
# panel 1
cx = 56
b += surf(cx) + sub(cx, 0, .5)
px, py = bez(*[(cx-44, 116), (cx, 60), (cx+44, 116)], .5)
b += poly([(px-6, py-52), (px+6, py-52), (px+6, py-26), (px+1.5, py-5), (px-1.5, py-5), (px-6, py-26)], 'kb')
b += arrow(px, py-62, px, py-54, 'k', 4, 2.4) if False else ''
b += arrow(px+12, py-20, px+30, py-20, 'k', 5, 2.6) + text(px+32, py-17, 'v', '', 'start')
b += text(cx, 148, 'nozzle')
# panel 2
cx = 160
b += surf(cx) + sub(cx, 0, .45, 'g') + sub(cx, .55, 1, 'a')
lx, ly = bez(*[(cx-44, 116), (cx, 60), (cx+44, 116)], .27)
b += rect(lx-9, 26, 18, 14, 'kb', 2) + arrow(lx, 40, lx, ly-3, 'a', 6, 3)
b += text(lx+14, 36, 'laser', 's', 'start') if False else ''
b += text(cx+6, 46, 'laser', 's', 'start')
b += text(cx+30, 82, 'plated', 's', 'start')
b += text(cx, 148, 'laser + plate')
# panel 3
cx = 264
b += surf(cx)
yl, yr = ypos(cx, cx-26), ypos(cx, cx+26)
pts = [(cx-26+52*i/20, ypos(cx, cx-26+52*i/20)-3) for i in range(21)]
b += path(f'M{cx-26} 46L{cx+26} 46L{cx+26} {yr-3:.1f}' + ''.join(f'L{x:.1f} {y:.1f}' for x, y in pts[::-1]) + 'z', 'ah')
b += rect(cx-26, 28, 52, 18, 'kb') + sub(cx, .2, .8, 'a')
b += text(cx, 148, 'soft pad')
T['t-10-3'] = svg(b, 156)

# ---------------- 10-4 alignment ----------------
b = ''
b += line(160, 20, 160, 150, 'g')
b += rect(24, 40, 60, 60, 'kb') + rect(44, 40, 60, 60, 'ah') + rect(44, 40, 40, 60, 'zr')
b += line(24, 30, 44, 30, 'k') + text(34, 24, 'e', 't')
b += line(24, 110, 104, 110, 'k') if False else ''
b += line(44, 112, 104, 112, 'k') + text(74, 126, 'w', 't')
b += text(94, 22, 'overlap shrinks', 's') if False else ''
b += text(84, 146, 'ΔA/A = −e/w', 't')
# crossed strips
b += rect(176, 66, 132, 22, 'kb') + rect(228, 30, 22, 90, 'ah') + rect(228, 66, 22, 22, 'zr')
b += rect(244, 30, 22, 90, 'g') if False else ''
b += text(182, 60, 'row', 's', 'start') + text(256, 40, 'column', 's', 'start')
b += arrow(262, 100, 282, 100, 'k', 5, 2.6) + text(288, 104, 'e', '', 'start')
b += text(240, 134, 'overlap is constant', 's')
b += text(240, 150, 'ΔA = 0', 't')
T['t-10-4'] = svg(b, 160)

# ---------------- 11-1 backing ----------------
b = ''
def panel(cx, soft):
    s = ''
    top, d = 90, 14
    if not soft:
        sep = [(cx-60, top), (cx-18, top), (cx-18, top+d), (cx+18, top+d), (cx+18, top), (cx+60, top), (cx+60, 110), (cx-60, 110)]
        back = [(cx-60, 110), (cx+60, 110), (cx+60, 136), (cx-60, 136)]
    else:
        sep = [(cx-60, top), (cx-18, top), (cx-18, top+d), (cx+18, top+d), (cx+18, top), (cx+60, top), (cx+60, 110),
               (cx+30, 110), (cx+20, 118), (cx-20, 118), (cx-30, 110), (cx-60, 110)]
        back = [(cx-60, 110), (cx-30, 110), (cx-20, 118), (cx+20, 118), (cx+30, 110), (cx+60, 110), (cx+60, 136), (cx-60, 136)]
    s += poly(sep, 'ah') + poly(back, 'kb')
    s += rect(cx-18, 52, 36, top+d-52, 'kb')
    s += arrow(cx, 22, cx, 48, 'k')
    s += line(cx-60, top, cx-24, top, 'g')
    s += text(cx-40, top+d+14 if False else top-4, 'δ', 't') if False else ''
    return s
b += panel(82, False) + panel(238, True)
for cx in (82, 238):
    b += text(cx-40, 80, 'δ', 't') + arrow(cx-40, 84, cx-40, 90+14, 'k', 5, 2.6) if False else ''
b += text(82, 152, 'hard backing') + text(82, 166, 'separator takes all of δ', 's')
b += text(238, 152, 'soft backing') + text(238, 166, 'backing takes most of δ', 's')
b += text(36, 103, 'δ', 't', 'end') + text(192, 103, 'δ', 't', 'end')
T['t-11-1'] = svg(b, 172)

# ---------------- 11-2 flex tail ----------------
b = ''
b += rect(8, 64, 62, 34, 'ah', 3) + text(39, 85, 'sensor', 's')
b += rect(230, 64, 76, 34, 'kb', 3) + text(268, 85, 'connector', 's')
b += path('M70 81H98C124 81 122 40 152 40C182 40 178 81 204 81H230', 'a')
b += line(70, 81, 230, 81, 'g') if False else ''
b += text(152, 28, 'service loop', 's')
b += text(112, 66, 'flex tail', 's') if False else ''
for x in (70, 230):
    b += circ(x, 81, 8, 'a')
    b += line(x, 89, x, 112, 'g')
b += text(70, 126, 'stiffness step', 's') + text(230, 126, 'stiffness step', 's')
b += text(150, 74, 'tail', 's') if False else ''
T['t-11-2'] = svg(b, 140)

# ---------------- 11-3 cover resolution ----------------
b = ''
def gauss(x, c, s, a):
    return a*math.exp(-0.5*((x-c)/s)**2)
def cover(cx, h, label):
    s = ''
    base = 144
    top = 78-h
    s += rect(cx-60, top, 120, h, 'ah') + rect(cx-60, 78, 120, 7, 'kb')
    for dx in (-18, 18):
        s += arrow(cx+dx, 14, cx+dx, top-1, 'k', 5, 2.6)
    s += line(cx-72, top, cx-72, 78, 'k') + text(cx-76, (top+78)/2+4, 'h', 't', 'end')
    sg = h*0.55
    amp = 44*6/sg if sg > 6 else 44
    fn = lambda x: base - (gauss(x, cx-18, sg, amp) + gauss(x, cx+18, sg, amp))
    s += line(cx-60, base, cx+60, base, 'k')
    s += path(curve(fn, cx-60, cx+60, 60), 'a')
    s += text(cx, 160, label)
    return s
b += cover(86, 11, 'thin: two peaks') + cover(238, 36, 'thick: one blur')
T['t-11-3'] = svg(b, 168)

# ---------------- 11-4 matrix scan ----------------
b = ''
rows = [44, 70, 96]; cols = [70, 110, 150]
for i, y in enumerate(rows):
    b += line(34, y, 180, y, 'a' if i == 1 else 'k')
for x in cols:
    b += line(x, 30, x, 112, 'k') + arrow(x, 112, x, 126, 'k', 5, 2.6)
for i, y in enumerate(rows):
    for x in cols:
        b += circ(x, y, 5, 'af' if i == 1 else 'kb')
b += arrow(6, 70, 34, 70, 'a') + text(20, 60, 'drive', 's')
b += rect(54, 128, 112, 20, 'ah', 3) + text(110, 142, 'read')
b += text(190, 74, 'driven row', 't', 'start')
b += text(190, 48, 'held', 's', 'start') + text(190, 100, 'held', 's', 'start')
b += text(190, 142, 'columns read', 's', 'start')
T['t-11-4'] = svg(b, 156)

# ================= ART =================
S = 'stroke="currentColor"'
ART['1'] = ('<svg viewBox="0 0 150 84"><path d="M75 1v9m-4-5 4 5 4-5" stroke="currentColor" stroke-width="2" fill="none"/>'
  '<rect x="26" y="12" width="98" height="10" rx="2" fill="currentColor" opacity=".25" stroke="currentColor" stroke-width="2"/>'
  '<path d="M26 30h98M26 62h98" stroke="currentColor" stroke-width="4"/>'
  '<rect x="26" y="36" width="98" height="20" fill="currentColor" opacity=".12" stroke="currentColor" stroke-dasharray="4 3"/>'
  '<path d="M44 38v16M62 38v16M80 38v16M98 38v16M114 38v16" stroke="currentColor" opacity=".5"/>'
  '<rect x="26" y="68" width="98" height="12" rx="2" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/></svg>')
ART['2'] = ('<svg viewBox="0 0 150 84"><rect x="30" y="6" width="90" height="20" rx="3" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
  '<rect x="30" y="32" width="90" height="20" rx="3" fill="none" stroke="currentColor" stroke-width="2"/>'
  '<g fill="currentColor"><circle cx="44" cy="42" r="2.6"/><circle cx="58" cy="38" r="2.6"/><circle cx="70" cy="45" r="2.6"/><circle cx="84" cy="39" r="2.6"/><circle cx="98" cy="45" r="2.6"/><circle cx="110" cy="39" r="2.6"/></g>'
  '<rect x="30" y="58" width="90" height="20" rx="3" fill="currentColor" opacity=".3" stroke="currentColor" stroke-width="2"/>'
  '<path d="M44 78l14-20M64 78l14-20M84 78l14-20M104 78l14-20" stroke="currentColor" opacity=".6"/></svg>')
ART['3'] = ('<svg viewBox="0 0 150 84"><path d="M8 48h42a25 25 0 0 0 50 0h42" fill="none" stroke="currentColor" stroke-width="2"/>'
  '<circle cx="75" cy="28" r="20" fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="2"/>'
  '<path d="M50 48a25 25 0 0 0 50 0z" fill="currentColor" opacity=".15"/>'
  '<path d="M75 54v14m-4-5 4 5 4-5" stroke="currentColor" opacity=".5" fill="none"/></svg>')
ART['3'] = ('<svg viewBox="0 0 150 84"><path d="M8 46h40M102 46h40" stroke="currentColor" stroke-width="2"/>'
  '<path d="M48 46a27 26 0 0 0 54 0" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
  '<circle cx="75" cy="28" r="19" fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="2"/>'
  '<path d="M75 54v12m-4-5 4 5 4-5" stroke="currentColor" opacity=".5" fill="none"/></svg>')
ART['4'] = ('<svg viewBox="0 0 150 84"><path d="M30 16h90M30 70h90" stroke="currentColor" stroke-width="4"/>'
  '<path d="M46 16C32 34 32 52 46 70H104C118 52 118 34 104 16z" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
  '<path d="M46 16v54M104 16v54" stroke="currentColor" stroke-dasharray="3 3" opacity=".6"/>'
  '<path d="M75 1v9m-4-5 4 5 4-5" stroke="currentColor" stroke-width="2" fill="none"/></svg>')
ART['5'] = ('<svg viewBox="0 0 150 84"><rect x="30" y="14" width="90" height="7" fill="currentColor" opacity=".3" stroke="currentColor" stroke-width="2"/>'
  '<rect x="30" y="63" width="90" height="7" fill="currentColor" opacity=".3" stroke="currentColor" stroke-width="2"/>'
  '<g stroke="currentColor" stroke-width="1.5" fill="none"><path d="M44 24v34m-3-5 3 5 3-5M62 24v34m-3-5 3 5 3-5M80 24v34m-3-5 3 5 3-5M98 24v34m-3-5 3 5 3-5M114 24v34m-3-5 3 5 3-5" /></g>'
  '<path d="M30 22C16 34 16 50 30 62M120 22C134 34 134 50 120 62" stroke="currentColor" fill="none" stroke-dasharray="3 3"/>'
  '<text x="6" y="22" font-size="12" fill="currentColor" font-family="JetBrains Mono">+</text><text x="6" y="74" font-size="12" fill="currentColor" font-family="JetBrains Mono">−</text></svg>')
ART['6'] = ('<svg viewBox="0 0 150 84"><path d="M14 74h124M14 74V6" stroke="currentColor" opacity=".5"/>'
  '<path d="M24 68C70 66 114 54 130 14C100 24 50 34 24 68z" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2.5"/>'
  '<path d="M84 50l8-4M84 50l2 7" stroke="currentColor" stroke-width="1.6" fill="none" opacity="0"/>'
  '<path d="M78 36l8-1m-8 1 3 7" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>')
ART['7'] = ('<svg viewBox="0 0 150 84"><path d="M14 66Q75 -2 136 66L126 72Q75 18 24 72z" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
  '<path d="M19 69Q75 8 131 69" fill="none" stroke="currentColor" stroke-dasharray="4 3"/>'
  '<path d="M75 44v30" stroke="currentColor" opacity=".35" stroke-dasharray="2 3"/><path d="M44 18l-8 6m8-6-2 8M106 18l8 6m-8-6 2 8" stroke="currentColor" fill="none" opacity=".6"/></svg>')
ART['8'] = ('<svg viewBox="0 0 150 84"><path d="M4 78h142" stroke="currentColor" opacity=".5"/>'
  '<path d="M48 78a27 32 0 0 1 54 0z" fill="currentColor" opacity=".25" stroke="currentColor" stroke-width="2"/>'
  '<path d="M6 74h38a31 34 0 0 1 62 0h38" fill="none" stroke="currentColor" stroke-width="3"/>'
  '<path d="M75 2v14m-4-5 4 5 4-5" stroke="currentColor" stroke-width="2" fill="none"/>'
  '<path d="M40 8q4-5 8 0t8 0M94 8q4-5 8 0t8 0" stroke="currentColor" fill="none" opacity=".6"/></svg>')
ART['9'] = ('<svg viewBox="0 0 150 84"><rect x="12" y="56" width="70" height="6" fill="currentColor" opacity=".25" stroke="currentColor" stroke-width="2"/>'
  '<path d="M82 59C100 59 108 52 114 32L120 12" fill="none" stroke="currentColor" stroke-width="5" opacity=".7"/>'
  '<path d="M113 18l7-12 7 12" stroke="currentColor" stroke-width="2" fill="none"/>'
  '<path d="M8 64h134" stroke="currentColor" stroke-width="2.5"/>'
  '<path d="M16 76l8-8M32 76l8-8M48 76l8-8M64 76l8-8M80 76l8-8M96 76l8-8M112 76l8-8M128 76l8-8" stroke="currentColor" opacity=".5"/>'
  '<path d="M96 52A16 16 0 0 0 100 40" stroke="currentColor" fill="none" stroke-dasharray="3 2"/></svg>')
ART['10'] = ('<svg viewBox="0 0 150 84"><path d="M8 78Q75 24 142 78z" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
  '<path d="M49 6h12v24l-4 16h-4l-4-16z" fill="currentColor" opacity=".3" stroke="currentColor" stroke-width="2"/>'
  '<path d="M8 78Q31.5 59.8 55 54.3" fill="none" stroke="currentColor" stroke-width="3.5"/>'
  '<path d="M66 40Q95 36 104 56" fill="none" stroke="currentColor" stroke-dasharray="3 3"/></svg>')
ART['11'] = ('<svg viewBox="0 0 150 84"><g fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="1.8">'
  '<rect x="18" y="14" width="14" height="14"/><rect x="38" y="14" width="14" height="14"/><rect x="58" y="14" width="14" height="14"/>'
  '<rect x="18" y="34" width="14" height="14"/><rect x="58" y="34" width="14" height="14"/><rect x="18" y="54" width="14" height="14"/><rect x="38" y="54" width="14" height="14"/><rect x="58" y="54" width="14" height="14"/></g>'
  '<rect x="38" y="34" width="14" height="14" fill="currentColor" opacity=".6"/>'
  '<path d="M74 41H104Q120 41 120 56V70" fill="none" stroke="currentColor" stroke-width="4"/>'
  '<rect x="110" y="70" width="20" height="9" fill="currentColor"/></svg>')
