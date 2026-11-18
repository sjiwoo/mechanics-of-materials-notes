"""Generate the custom section-card figures (inline SVG <template>s) and inject them into index.html.

Run from the repo root:  python tools/section_figs.py
Each figure becomes <template id="sf-<ch>-<sec>"> between the SECTION-FIGS markers in index.html.
Styling comes from the .sf CSS classes in index.html, so figures follow the chapter accent + theme:
  a  = accent stroke     af = accent fill     ah = accent tinted area
  k  = ink stroke        kf = ink fill        g  = dashed guide
  text default = ink,  text.t = accent,  text.s = small muted label
"""
import math, re, pathlib

W, H = 320, 150

def arrow(x1, y1, x2, y2, c='a', hl=7, hw=3.6):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    bx, by = x2 - ux * hl, y2 - uy * hl
    px, py = -uy * hw, ux * hw
    f = 'af' if c == 'a' else 'kf'
    return (f'<path class="{c}" d="M{x1:.1f} {y1:.1f}L{bx:.1f} {by:.1f}"/>'
            f'<path class="{f}" d="M{x2:.1f} {y2:.1f}L{bx+px:.1f} {by+py:.1f}L{bx-px:.1f} {by-py:.1f}z"/>')

def line(x1, y1, x2, y2, c='k'):
    return f'<path class="{c}" d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}"/>'

def path(d, c='a'):
    return f'<path class="{c}" d="{d}"/>'

def rect(x, y, w, h, c='ah', rx=0):
    return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'

def circ(x, y, r, c='a'):
    return f'<circle class="{c}" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>'

def text(x, y, s, c='', a='middle'):
    cls = f' class="{c}"' if c else ''
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text{cls} x="{x:.1f}" y="{y:.1f}" text-anchor="{a}">{s}</text>'

def wall_v(x, y1, y2, side=-1):
    """vertical wall at x, hatch on `side` (-1 left, +1 right)"""
    s = line(x, y1, x, y2, 'k')
    for y in range(int(y1) + 4, int(y2), 7):
        s += line(x, y, x + 6 * side, y - 5, 'k')
    return s

def wall_h(x1, x2, y, side=-1):
    """horizontal wall at y, hatch above (-1) or below (+1)"""
    s = line(x1, y, x2, y, 'k')
    for x in range(int(x1) + 2, int(x2), 7):
        s += line(x, y, x + 5, y + 6 * side, 'k')
    return s

def pin(x, y):
    return path(f'M{x} {y}l-6 10h12z', 'k') + line(x - 9, y + 10, x + 9, y + 10, 'k')

def roller(x, y):
    return circ(x, y + 4.5, 4.5, 'k') + line(x - 9, y + 9, x + 9, y + 9, 'k')

def curve(fn, x0, x1, n=40):
    pts = [(x0 + (x1 - x0) * i / n) for i in range(n + 1)]
    return 'M' + 'L'.join(f'{x:.1f} {fn(x):.1f}' for x in pts)

def axes(x0, y0, x1, y1, xl, yl):
    """origin (x0,y0); x axis to x1, y axis up to y1"""
    return (arrow(x0, y0, x1, y0, 'k', 6, 3) + arrow(x0, y0, x0, y1, 'k', 6, 3)
            + text(x1 + 2, y0 + 4, xl, '', 'start') + text(x0, y1 - 5, yl))

def svg(body, h=H):
    return f'<svg viewBox="0 0 {W} {h}" role="img">{body}</svg>'

F = {}

# ---------------- Ch 1 ----------------
b = ''
b += rect(40, 52, 110, 34, 'ah', 3)
b += arrow(40, 69, 12, 69, 'k') + text(18, 62, 'P')
for y in range(56, 86, 7):
    b += arrow(150, y, 170, y, 'a', 5, 2.6)
b += text(184, 73, 'σ', 't', 'start')
b += line(150, 52, 150, 86, 'a')
b += text(95, 104, 'cut: internal force', 's') + text(95, 116, 'spread over area', 's')
b += text(95, 40, 'external load', 's')
# element
b += rect(232, 54, 30, 30, 'g')
b += rect(226, 56, 42, 26, 'ah')
b += text(247, 104, 'element deforms', 's') + text(247, 116, '→ strain ε', 's')
b += text(247, 40, 'at a point', 's')
F['1-1'] = (svg(b), 'Loads produce internal stress (strength) and strain (deformation).')

b = ''
def bar(y, x0, ln, c, lab, val):
    return rect(x0, y, ln, 14, c, 2) + text(x0 - 6, y + 11, lab, '', 'end') + text(x0 + ln + 6, y + 11, val, 's', 'start')
b += text(160, 18, 'LRFD: design strength ≥ factored load', 's')
b += bar(32, 72, 80, 'kb', 'R', 'nominal load')
b += bar(52, 72, 115, 'ah', 'ΣγR', 'factored (γ>1)')
b += bar(92, 72, 175, 'kb', 'Pₙ', 'nominal')
b += bar(112, 72, 140, 'ah', 'φPₙ', 'design (φ≤1)')
b += line(187, 70, 187, 110, 'g') + line(212, 70, 212, 110, 'g')
b += text(200, 142, 'design ≥ factored', 's')
F['1-7'] = (svg(b), 'Loads are scaled up, strength is scaled down; the scaled strength must still exceed the scaled load.')

# ---------------- Ch 2 ----------------
b = ''
b += wall_v(18, 40, 90)
b += rect(18, 52, 100, 26, 'g') + rect(18, 52, 124, 26, 'ah')
b += arrow(142, 65, 162, 65, 'k') + text(166, 69, 'P', '', 'start')
b += line(18, 96, 118, 96, 'k') + text(68, 108, 'L', '')
b += line(118, 90, 118, 100, 'k') + line(142, 90, 142, 100, 'k') + text(130, 108, 'δ', 't')
b += text(80, 132, 'ε = δ / L', 't')
# shear
x0, y0, s = 220, 98, 52
b += rect(x0, y0 - s, s, s, 'g')
off = 16
b += path(f'M{x0} {y0}L{x0+s} {y0}L{x0+s+off} {y0-s}L{x0+off} {y0-s}z', 'ah')
b += path(f'M{x0+12} {y0}A12 12 0 0 0 {x0+12*math.cos(math.atan2(s,off))+0.5:.1f} {y0-12*math.sin(math.atan2(s,off)):.1f}', 'a')
b += text(x0 + 22, y0 - 16, 'θ′', 't', 'start')
b += text(x0 + 34, 132, 'γ = π/2 − θ′', 't')
b += text(x0 + 34, 30, '', 's')
F['2-2'] = (svg(b), 'Normal strain = stretch per unit length; shear strain = loss of a right angle.')

# ---------------- Ch 3 ----------------
b = ''
y = 75
b += path(f'M40 {y-20}h40l14 12h96l14 -12h40v40h-40l-14 -12h-96l-14 12h-40z', 'ah')
b += arrow(40, y, 12, y, 'k') + arrow(244, y, 272, y, 'k')
b += text(18, y - 8, 'P') + text(266, y - 8, 'P')
b += line(112, y - 14, 112, y + 14, 'a') + line(172, y - 14, 172, y + 14, 'a')
b += line(112, y + 30, 172, y + 30, 'k') + text(142, y + 44, 'L₀  (gauge length)', 's')
b += text(142, y - 26, 'A₀', 't')
b += text(160, 138, 'σ = P/A₀,   ε = δ/L₀', 't')
F['3-1'] = (svg(b), 'Record load and gauge elongation, then divide by the original area and length.')

b = ''
ox, oy = 34, 128
b += axes(ox, oy, 300, 12, 'ε', 'σ')
# brittle: steep, nearly linear, early fracture
b += path(curve(lambda x: oy - (x - ox) * 4.2, ox, ox + 24), 'k')
b += text(ox + 24, oy - 24 * 4.2 + 4, '✕', '') + text(ox + 32, oy - 24 * 4.2 + 4, 'brittle', '', 'start')
# ductile
d = f'M{ox} {oy}L{ox+18} {oy-62}L{ox+40} {oy-60}C{ox+90} {oy-96} {ox+160} {oy-104} {ox+205} {oy-88}L{ox+235} {oy-66}'
b += path(d, 'a')
b += text(ox + 238, oy - 58, '✕', 't', 'start')
b += text(ox + 140, oy - 108, 'ductile', 't')
b += text(ox + 150, oy - 20, 'large plastic strain before fracture', 's')
F['3-3'] = (svg(b), 'Ductile metals stretch a lot before breaking; brittle materials fracture with almost no yielding.')

b = ''
ox, oy = 40, 128
b += axes(ox, oy, 296, 12, 'ε', 'σ')
b += path(f'M{ox} {oy}L{ox+80} {oy-80}', 'a')
b += path(f'M{ox+80} {oy-80}C{ox+110} {oy-104} {ox+170} {oy-110} {ox+230} {oy-112}', 'g')
b += path(f'M{ox+40} {oy-40}h30v-30', 'k') + text(ox + 76, oy - 50, 'E', 't', 'start')
b += line(ox, oy - 80, ox + 80, oy - 80, 'g') + text(ox - 4, oy - 76, 'σpl', 's', 'end')
b += text(ox + 150, oy - 30, 'σ = Eε  (linear-elastic)', 't')
b += text(ox + 150, oy - 14, 'slope E = stiffness', 's')
F['3-4'] = (svg(b), 'Below the proportional limit, stress is proportional to strain; the slope is E.')

# ---------------- Ch 4 ----------------
b = ''
def axrow(y, loads, dl, lab):
    s = wall_v(26, y - 10, y + 14) + rect(26, y - 4, 150, 12, 'ah', 2)
    for (x, t) in loads:
        s += arrow(x, y + 2, x + 22, y + 2, 'a', 6, 3) + text(x + 12, y - 8, t, 't')
    s += text(198, y + 6, lab, '', 'start')
    return s
b += axrow(26, [(100, 'P₁'), (176, 'P₂')], 0, 'δ')
b += text(150, 54, '=', '')
b += axrow(72, [(100, 'P₁')], 0, 'δ₁')
b += text(150, 100, '+', '')
b += axrow(118, [(176, 'P₂')], 0, 'δ₂')
b += text(270, 78, 'δ = δ₁ + δ₂', 't')
b += text(270, 94, 'linear, small δ', 's')
F['4-3'] = (svg(b), 'With linear-elastic behavior, the response to several loads is the sum of the separate responses.')

b = ''
def col(x, top_fix=True, bot_sup=True, load=True, red=False, dlab=''):
    s = wall_h(x - 14, x + 14, 22, -1)
    s += rect(x - 5, 22, 10, 96, 'ah', 1)
    if bot_sup:
        s += wall_h(x - 14, x + 14, 118, 1)
    if load:
        s += arrow(x + 30, 60, x + 8, 60, 'a') + text(x + 34, 64, 'P', 't', 'start')
    if red:
        s += arrow(x, 146, x, 122, 'a') + text(x + 9, 142, 'F_B', 't', 'start')
    if dlab:
        s += text(x + 12, 112, dlab, '', 'start')
    return s
b += col(40) + text(40, 140, 'actual', 's')
b += text(96, 74, '=', '')
b += col(150, bot_sup=False, dlab='δ_P ↓') + text(150, 140, 'support removed', 's')
b += text(206, 74, '+', '')
b += col(260, bot_sup=False, load=False, red=True, dlab='δ_B ↑') + text(250, 22 - 6, '', 's')
b += text(160, 12, 'compatibility:  δ_P − δ_B = 0', 't')
F['4-5'] = (svg(b, 152), 'Release the redundant support, then size the redundant force so the displacement there returns to zero.')

b = ''
b += wall_v(30, 20, 56) + rect(30, 30, 160, 16, 'ah', 2) + rect(190, 30, 18, 16, 'g')
b += text(199, 22, 'δ_T', 't') + text(226, 42, 'free end', 's', 'start')
b += text(110, 66, 'δ_T = α ΔT L', '')
b += wall_v(30, 88, 124) + wall_v(190, 88, 124, 1) + rect(30, 98, 160, 16, 'ah', 2)
b += arrow(80, 106, 58, 106, 'k', 6, 3) + arrow(140, 106, 162, 106, 'k', 6, 3)
b += text(226, 110, 'restrained', 's', 'start')
b += text(110, 140, 'σ = E α ΔT  (compression)', 't')
F['4-6'] = (svg(b), 'A bar that cannot expand freely develops stress proportional to the temperature change.')

b = ''
ox, oy = 40, 120
b += axes(ox, oy, 230, 14, 'ε', 'σ')
b += path(f'M{ox} {oy}L{ox+50} {oy-80}L{ox+180} {oy-80}', 'a')
b += line(ox, oy - 80, ox + 50, oy - 80, 'g') + text(ox - 4, oy - 76, 'σY', 't', 'end')
b += line(ox + 50, oy, ox + 50, oy - 80, 'g') + text(ox + 50, oy + 14, 'εY', 's')
b += text(ox + 120, oy - 88, 'perfectly plastic', 's')
b += text(ox + 22, oy - 30, 'E', 's')
# section fully yielded
b += rect(262, 48, 36, 36, 'ah')
for yy in range(52, 84, 8):
    b += arrow(298, yy + 2, 312, yy + 2, 'a', 4, 2.2)
b += text(280, 104, 'P_p = σY A', 't')
F['4-8'] = (svg(b), 'Elastic–perfectly plastic model: once at σY, stress stays there; the plastic load is σY A.')

# ---------------- Ch 5 ----------------
b = ''
b += rect(20, 46, 60, 52, 'kb', 4) + text(50, 77, 'motor', 's')
b += rect(80, 64, 190, 16, 'ah', 2)
b += path('M226 54 A10 18 0 1 1 222 90', 'a') + arrow(222, 90, 216, 88, 'a', 6, 3)
b += text(238, 48, 'T, ω', 't', 'start')
b += text(160, 120, 'P = T ω = 2π f T', 't')
b += text(160, 136, 'given P and speed → torque → size shaft', 's')
F['5-3'] = (svg(b), 'Power is torque times angular speed, so the torque a shaft must carry follows from power and rpm.')

b = ''
cx, cy, R, ry = 80, 66, 50, 22
b += circ(cx, cy, R, 'ah') + circ(cx, cy, ry, 'kb')
b += text(cx, cy + 4, 'core', 's') + text(cx, cy + R + 16, 'plastic annulus', 't')
b += line(cx, cy, cx + R * .7071, cy - R * .7071, 'k') + text(cx + R * .7071 + 6, cy - R * .7071, 'c', 's', 'start')
ox, oy = 180, 128
b += axes(ox, oy, 310, 20, 'ρ', 'τ')
b += path(f'M{ox} {oy}L{ox+50} {oy-70}L{ox+110} {oy-70}', 'a')
b += line(ox + 50, oy, ox + 50, oy - 70, 'g') + text(ox + 50, oy + 14, 'ρY', 's')
b += text(ox + 110, oy + 14, 'c', 's')
b += line(ox, oy - 70, ox + 50, oy - 70, 'g') + text(ox - 4, oy - 66, 'τY', 't', 'end')
b += text(ox + 82, oy - 78, 'yielded', 's')
F['5-9'] = (svg(b), 'Partly yielded shaft: linear stress in the elastic core, constant τY in the outer annulus.')

# ---------------- Ch 6 ----------------
b = ''
x0, x1 = 40, 280
xm = (x0 + x1) / 2
b += rect(x0, 22, x1 - x0, 8, 'ah', 1) + pin(x0, 30) + roller(x1, 30)
b += arrow(xm, 2, xm, 20, 'a') + text(xm + 8, 12, 'P', 't', 'start')
# V
yv = 76
b += line(x0, yv, x1, yv, 'k') + text(x0 - 8, yv + 4, 'V', '', 'end')
b += path(f'M{x0} {yv}V{yv-16}H{xm}V{yv+16}H{x1}V{yv}z', 'ah')
b += text(x0 + 40, yv - 18, '+P/2', 's') + text(x1 - 40, yv + 26, '−P/2', 's')
# M
ym = 158
b += line(x0, ym, x1, ym, 'k') + text(x0 - 8, ym + 4, 'M', '', 'end')
b += path(f'M{x0} {ym}L{xm} {ym-40}L{x1} {ym}z', 'ah')
b += text(xm, ym - 46, 'PL/4', 's')
F['6-1'] = (svg(b, 170), 'Cut the beam at x to get V(x) and M(x); the moment peaks where the shear changes sign.')

b = ''
cx, cy = 120, 76
b += rect(cx - 26, cy - 46, 52, 92, 'ah')
b += line(cx, cy + 62, cx, cy - 62, 'k') + text(cx, cy - 66, 'y')
b += line(cx - 62, cy, cx + 62, cy, 'k') + text(cx + 68, cy + 4, 'z', '', 'start')
th = math.radians(30)
ex, ey = cx + 60 * math.cos(th), cy - 60 * math.sin(th)
b += arrow(cx, cy, ex, ey, 'a') + arrow(cx, cy, cx + 52 * math.cos(th), cy - 52 * math.sin(th), 'a')
b += text(ex + 6, ey, 'M', 't', 'start')
al = math.atan(4 * math.tan(th))  # Iz/Iy ~ 4 for 2:1 rectangle... illustrative
nx, ny = 70 * math.cos(al), 70 * math.sin(al)
b += path(f'M{cx-nx:.1f} {cy+ny:.1f}L{cx+nx:.1f} {cy-ny:.1f}', 'g')
b += text(cx + nx + 4, cy - ny + 4, 'N.A.', 's', 'start')
b += path(f'M{cx+26} {cy}A26 26 0 0 0 {cx+26*math.cos(th):.1f} {cy-26*math.sin(th):.1f}', 'k')
b += text(cx + 32, cy - 4, 'θ', 's', 'start')
b += text(252, 64, 'tan α = (Iz/Iy) tan θ', 't')
b += text(250, 82, 'N.A. tilts toward', 's') + text(250, 94, 'the weak axis', 's')
F['6-5'] = (svg(b, 152), 'When the moment is not about a principal axis, the neutral axis tilts away from the moment axis.')

b = ''
x, y, w, h = 40, 34, 60, 40
b += rect(x, y, w, h, 'ah') + rect(x, y + h, w, h, 'kb')
b += text(x + w / 2, y + 24, 'E₁', 't') + text(x + w / 2, y + h + 24, 'E₂', 's')
b += text(x + w / 2, y - 8, 'b', 's')
b += arrow(120, 74, 168, 74, 'k') + text(144, 66, 'n = E₁/E₂', 's')
x2 = 190
b += rect(x2, y, 110, h, 'ah') + rect(x2 + 25, y + h, w, h, 'kb')
b += text(x2 + 55, y - 8, 'nb', 't') + text(x2 + 55, y + h + 24, 'b', 's')
b += text(160, 136, 'scale width only; σ₁ = n σ′', 't')
F['6-6'] = (svg(b), 'Transformed section: widen the stiffer material by n so the whole beam acts as one material.')

b = ''
def prof(x, yc, hh, kind, lab):
    s = line(x, yc - hh, x, yc + hh, 'k')
    S = 34
    if kind == 0:
        d = f'M{x} {yc-hh}L{x+S} {yc-hh}L{x-S} {yc+hh}L{x} {yc+hh}'
    elif kind == 1:
        e = hh * 0.45
        d = f'M{x} {yc-hh}H{x+S}V{yc-e}L{x-S} {yc+e}V{yc+hh}H{x}'
    else:
        d = f'M{x} {yc-hh}H{x+S}V{yc}H{x-S}V{yc+hh}H{x}'
    s += path(d + 'z', 'ah')
    s += text(x, yc + hh + 18, lab, 't')
    return s
yc, hh = 70, 44
b += prof(60, yc, hh, 0, 'M_Y') + prof(160, yc, hh, 1, 'M_Y<M<M_p') + prof(260, yc, hh, 2, 'M_p')
b += text(60, 18, 'elastic', 's') + text(160, 18, 'elastic core', 's') + text(260, 18, 'fully plastic', 's')
b += text(160, 146, 'k = M_p / M_Y  (1.5 for a rectangle)', 's')
F['6-10'] = (svg(b, 152), 'As the moment grows, yielding spreads inward from the outer fibers until the whole section is at σY.')

# ---------------- Ch 8 ----------------
b = ''
def dist(x, kind, lab):
    yt, yb = 30, 110
    s = line(x, yt, x, yb, 'k')
    if kind == 0:
        d = f'M{x} {yt}H{x+18}V{yb}H{x}z'
    elif kind == 1:
        d = f'M{x} {yt}L{x+26} {yt}L{x-26} {yb}L{x} {yb}z'
    else:
        d = f'M{x} {yt}L{x+44} {yt}L{x-8} {yb}L{x} {yb}z'
    return s + path(d, 'ah') + text(x, 132, lab, 't')
b += dist(48, 0, 'N/A') + text(98, 74, '+', '')
b += dist(150, 1, 'My/I') + text(206, 74, '=', '')
b += dist(250, 2, 'σ')
b += text(160, 16, 'compute each load effect, then add at the point', 's')
F['8-2'] = (svg(b), 'Find each internal load’s stress separately, then superpose them at the point.')

# ---------------- Ch 9 / 10 Mohr ----------------
b = ''
ox, oy = 40, 82
k = 1.0
s2, s1 = 64, 136
b += arrow(ox - 14, oy, 306, oy, 'k', 6, 3) + text(308, oy + 4, 'σ', '', 'start')
b += arrow(ox, 8, ox, 150, 'k', 6, 3) + text(ox - 8, 150, 'τ', '', 'end')
b += circ(ox + (s1) / 2, oy, s1 / 2, 'ah')
b += circ(ox + s2 / 2, oy, s2 / 2, 'kb') + circ(ox + (s1 + s2) / 2, oy, (s1 - s2) / 2, 'kb')
b += text(ox - 3, oy + 14, 'σ₃=0', 's', 'end')
b += text(ox + s2, oy + 14, 'σ₂', 's') + text(ox + s1 + 4, oy + 14, 'σ₁', 's', 'start')
cx = ox + s1 / 2
b += arrow(cx, oy, cx, oy - s1 / 2 + 2, 'a', 6, 3)
b += text(ox + s1 + 10, oy - 40, 'τ_abs max', 't', 'start') + text(ox + s1 + 10, oy - 26, '= σ₁/2', 't', 'start')
F['9-5'] = (svg(b, 156), 'Draw all three Mohr’s circles; when σ₁ and σ₂ share a sign, the largest circle includes σ₃ = 0.')

b = ''
cx, cy = 74, 92
b += arrow(cx - 10, cy, cx + 70, cy, 'k', 6, 3) + text(cx + 74, cy + 4, 'x', '', 'start')
b += arrow(cx, cy + 10, cx, cy - 70, 'k', 6, 3) + text(cx, cy - 74, 'y')
th = math.radians(30)
def rot(u, v):
    return cx + u * math.cos(th) - v * math.sin(th), cy - (u * math.sin(th) + v * math.cos(th))
p = [rot(0, 0), rot(40, 0), rot(40, 40), rot(0, 40)]
b += path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in p) + 'z', 'ah')
ax_ = rot(78, 0); ay_ = rot(0, 70)
b += arrow(cx, cy, *ax_, 'a', 6, 3) + text(ax_[0] + 4, ax_[1], "x′", 't', 'start')
b += arrow(cx, cy, *ay_, 'a', 6, 3) + text(ay_[0] - 4, ay_[1], "y′", 't', 'end')
b += path(f'M{cx+30} {cy}A30 30 0 0 0 {rot(30,0)[0]:.1f} {rot(30,0)[1]:.1f}', 'k') + text(cx + 36, cy - 6, 'θ', 's', 'start')
tx = 236
b += text(tx, 40, 'stress → strain', 's')
b += text(tx, 66, 'σ  →  ε', 't')
b += text(tx, 90, 'τ  →  γ/2', 't')
b += text(tx, 120, 'same equations,', 's') + text(tx, 132, 'same Mohr’s circle', 's')
F['10-2'] = (svg(b), 'Strain transforms exactly like stress once τ is replaced by γ/2.')

b = ''
ox, oy = 30, 76
b += arrow(ox - 10, oy, 306, oy, 'k', 6, 3) + text(308, oy + 4, 'ε', '', 'start')
b += arrow(ox + 20, 10, ox + 20, 146, 'k', 6, 3) + text(ox + 12, 146, 'γ/2', '', 'end')
C, R = 170, 58
b += circ(C, oy, R, 'ah')
ang = math.radians(35)
Ax, Ay = C + R * math.cos(ang), oy + R * math.sin(ang)
Bx, By = C - R * math.cos(ang), oy - R * math.sin(ang)
b += line(Bx, By, Ax, Ay, 'a') + circ(Ax, Ay, 3, 'af') + circ(C, oy, 2.5, 'kf')
b += text(Ax + 6, Ay + 10, 'A(εx, γxy/2)', 't', 'start')
b += circ(C + R, oy, 3, 'af') + circ(C - R, oy, 3, 'af')
b += text(C + R + 4, oy - 6, 'ε₁', 't', 'start') + text(C - R - 4, oy - 6, 'ε₂', 't', 'end')
b += text(C, oy - 6, 'ε_avg', 's')
b += line(C, oy, C, oy - R, 'g') + text(C + 4, oy - R + 14, 'R', 's', 'start')
F['10-3'] = (svg(b, 152), 'Strain Mohr’s circle: ε horizontal, γ/2 vertical (positive down), centered at ε_avg.')

# ---------------- Ch 12 ----------------
b = ''
def beamrow(y, udl, pt, lab, sag):
    x0, x1 = 30, 200
    s = rect(x0, y, x1 - x0, 6, 'ah', 1) + pin(x0, y + 6) + roller(x1, y + 6)
    if udl:
        for xx in range(x0 + 6, x1, 14):
            s += arrow(xx, y - 12, xx, y - 1, 'k', 4, 2)
        s += line(x0 + 6, y - 12, x1 - 6, y - 12, 'k')
    if pt:
        s += arrow(150, y - 20, 150, y - 1, 'a', 6, 3)
    s += path(curve(lambda x: y + 3 + sag * math.sin(math.pi * (x - x0) / (x1 - x0)), x0, x1), 'g')
    s += text(212, y + 8, lab, 't', 'start')
    return s
b += beamrow(24, True, True, 'v', 10) + text(115, 56, '=', '')
b += beamrow(78, True, False, 'v₁', 7) + text(115, 108, '+', '')
b += beamrow(130, False, True, 'v₂', 5)
b += text(276, 110, 'v = v₁ + v₂', 't')
F['12-5'] = (svg(b, 156), 'Split the loading into table cases and add their deflections and slopes.')

b = ''
x0, x1, y = 40, 250, 50
b += wall_v(x0, y - 20, y + 26) + rect(x0, y, x1 - x0, 7, 'ah', 1) + roller(x1, y + 7)
for xx in range(x0 + 8, x1, 14):
    b += arrow(xx, y - 16, xx, y - 1, 'k', 4, 2)
b += line(x0 + 8, y - 16, x1 - 6, y - 16, 'k') + text(150, y - 22, 'w', '')
L = x1 - x0
b += path(curve(lambda x: y + 3 + 28 * ((x - x0) / L) ** 2 * (1 - (x - x0) / L) * 1.9, x0, x1), 'a')
b += arrow(x1, y + 44, x1, y + 22, 'a') + text(x1 + 8, y + 40, 'B_y', 't', 'start') + text(x1 + 8, y + 54, 'redundant', 's', 'start')
b += text(x0 + 6, y + 50, 'A:  v = 0,  dv/dx = 0', 's', 'start')
b += text(x1 - 6, y + 66, 'B:  v = 0', 's', 'end')
b += text(150, 140, 'M(x) contains B_y;  3 BCs fix C₁, C₂, B_y', 't')
F['12-7'] = (svg(b), 'Write M(x) with the redundant kept as an unknown; the extra boundary condition solves for it.')

# ---------------- Ch 13 ----------------
b = ''
def column(x, kind, K):
    top, bot = 20, 120
    Lh = bot - top
    A = 10
    if kind == 'pp':
        f = lambda t: A * math.sin(math.pi * t)
    elif kind == 'ff':  # fixed bottom, free top
        f = lambda t: A * 1.6 * (1 - math.cos(math.pi * t / 2))
    elif kind == 'xx':  # fixed-fixed
        f = lambda t: A * 0.5 * (1 - math.cos(2 * math.pi * t))
    else:  # fixed bottom, pinned top: exact mode shape, tan(K)=K
        K_ = 4.4934
        g = lambda t: math.sin(K_ * t) - K_ * math.cos(K_ * t) - K_ * t + K_
        gm = max(g(i / 200) for i in range(201))
        f = lambda t: A * 1.3 * g(t) / gm
    pts = []
    for i in range(41):
        t = i / 40  # t from bottom (0) to top (1)
        pts.append((x + f(t), bot - Lh * t))
    s = path('M' + 'L'.join(f'{a:.1f} {c:.1f}' for a, c in pts), 'a')
    s += line(x, top, x, bot, 'g')
    # supports
    if kind in ('ff', 'xx', 'fp'):
        s += wall_h(x - 12, x + 12, bot + 1, 1)
    else:
        s += pin(x, bot)
    if kind == 'xx':
        s += wall_h(x - 12, x + 12, top - 1, -1)
    elif kind in ('pp', 'fp'):
        s += path(f'M{x} {top}l-6 -10h12z', 'k')
    tx = pts[-1][0]
    s += arrow(tx, top - 18 if kind != 'xx' else top - 22, tx, top - 2 if kind != 'xx' else top - 4, 'k', 5, 2.6) if kind != 'xx' else ''
    s += text(x, 144, f'K = {K}', 't')
    return s
b += column(46, 'pp', '1') + column(124, 'ff', '2') + column(200, 'xx', '0.5') + column(276, 'fp', '0.7')
F['13-3'] = (svg(b, 152), 'End conditions change the buckled shape; Le = KL is the length of one half sine wave.')

# ---------------- Ch 14 ----------------
b = ''
A_, B_, C_ = (40, 112), (240, 112), (140, 36)
b += line(*A_, *B_, 'a') + line(*A_, *C_, 'a') + line(*C_, *B_, 'a')
for p_ in (A_, B_, C_):
    b += circ(*p_, 3.5, 'kb')
b += pin(*A_) + roller(*B_)
b += arrow(140, 2, 140, 30, 'a') + text(148, 14, 'P', 't', 'start')
b += path(f'M{A_[0]} {A_[1]}L{C_[0]} {C_[1]+10}L{B_[0]} {B_[1]}', 'g')
b += text(124, 54, 'Δ', 's')
b += text(160, 142, 'Δ = Σ N (∂N/∂P) L / AE', 't')
F['14-9'] = (svg(b, 150), 'For each member, multiply its force by how fast it changes with P; sum to get the joint displacement.')

b = ''
x0, x1, y = 40, 250, 44
b += wall_v(x0, y - 20, y + 26) + rect(x0, y, x1 - x0, 7, 'ah', 1)
for xx in range(x0 + 8, x1, 14):
    b += arrow(xx, y - 16, xx, y - 1, 'k', 4, 2)
b += line(x0 + 8, y - 16, x1 - 6, y - 16, 'k') + text(140, y - 22, 'w', '')
L = x1 - x0
b += path(curve(lambda x: y + 3 + 34 * ((x - x0) / L) ** 2, x0, x1), 'g')
b += arrow(x1 + 14, y - 22, x1 + 14, y + 2, 'a') + text(x1 + 22, y - 10, "P′", 't', 'start')
b += line(x1, y + 7, x1, y + 37, 'k') + text(x1 + 6, y + 30, 'Δ', 's', 'start')
b += text(150, 112, 'Δ = ∫ M (∂M/∂P′) dx / EI', 't')
b += text(150, 130, 'add fictitious P′ where Δ is wanted, then set P′ = 0', 's')
F['14-10'] = (svg(b), 'Put a fictitious force where the deflection is wanted, differentiate M, then set it to zero.')

# ================= GD&T (Krulikowski ch 26 — pages missing from the scan) =================
def band(d, w=12):
    """tolerance-zone band along path d (wide translucent stroke)"""
    return f'<path class="zb" d="{d}" stroke-width="{w}"/>'

def bbox_text(x, y, s):
    """basic dimension: text in a box"""
    w = 7 * len(s) + 8
    return rect(x - w / 2, y - 11, w, 15, 'k') + text(x, y, s)

def fcfbox(x, y, cells):
    """draw a feature control frame; first cell is an svg glyph path string"""
    out = ''; cx = x
    widths = [22] + [8 * len(c) + 12 for c in cells[1:]]
    for i, wd in enumerate(widths):
        out += rect(cx, y, wd, 20, 'kfr')
        if i == 0:
            out += f'<g transform="translate({cx+3},{y+2})"><path class="k" d="{cells[0]}"/></g>'
        else:
            out += text(cx + wd / 2, y + 14, cells[i])
        cx += wd
    return out, cx

PSURF = 'M2.5 13a6.5 6.5 0 0 1 13 0z'

# 26.1 true profile
b = ''
d = 'M40 120V60H110A40 40 0 0 1 150 20H250V120'
b += band(d, 12) + path(d, 'g')
b += bbox_text(75, 52, '70') + bbox_text(200, 14, '100') + bbox_text(128, 36, 'R40')
b += text(176, 82, 'true profile', 't') + text(176, 97, 'exact, from basic dims', 's')
b += text(150, 140, 'zone straddles the true profile (equal bilateral by default)', 's')
F['g-26-1'] = (svg(b), 'The true profile is defined exactly by basic dimensions; the zone follows it.')

# 26.2 surface vs line
b = ''
def slab(x0, curved_band, slices):
    s = ''
    top = f'M{x0} 60C{x0+30} 30 {x0+70} 30 {x0+100} 60'
    s += path(f'M{x0} 60V110H{x0+100}V60', 'k')
    s += path(f'M{x0+100} 60l24 -18v50l-24 18', 'k')
    s += path(f'M{x0} 60l24 -18C{x0+54} 12 {x0+94} 12 {x0+124} 42', 'k')
    s += path(top, 'k')
    if curved_band:
        s += f'<path class="zfill" d="M{x0} 60l24 -18C{x0+54} 12 {x0+94} 12 {x0+124} 42L{x0+100} 60C{x0+70} 30 {x0+30} 30 {x0} 60z"/>'
    for t in slices:
        xs = x0 + 24 * t
        ys = 60 - 18 * t
        s += band(f'M{xs} {ys}C{xs+30} {ys-30} {xs+70} {ys-30} {xs+100} {ys}', 6)
    return s
b += slab(20, True, []) + text(80, 132, 'profile of a surface', 't') + text(80, 146, 'one 3D zone, whole surface', 's')
b += slab(176, False, [0.15, 0.5, 0.85]) + text(236, 132, 'profile of a line', 't') + text(236, 146, '2D zone at each cross section', 's')
F['g-26-2'] = (svg(b, 152), 'Surface profile is one 3D zone over the whole surface; line profile checks each cross section separately.')

# 26.3 five zone types
b = ''
def zpanel(x, kind, lab, sub):
    s = ''
    y = 56
    if kind == 'eq':
        s += rect(x, y - 8, 52, 16, 'zr')
    elif kind == 'uneq':
        s += rect(x, y - 12, 52, 16, 'zr')
    elif kind == 'out':
        s += rect(x, y - 16, 52, 16, 'zr')
    elif kind == 'in':
        s += rect(x, y, 52, 16, 'zr')
    else:
        s += f'<path class="zr" d="M{x} {y-4}L{x+52} {y-14}V{y+14}L{x} {y+4}z"/>'
    s += line(x - 2, y, x + 54, y, 'a')
    s += text(x + 26, 98, lab, 't') + text(x + 26, 112, sub, 's')
    return s
b += zpanel(8, 'eq', 'equal', 'bilateral')
b += zpanel(70, 'uneq', 'unequal', 'bilateral Ⓤ')
b += zpanel(132, 'out', 'outside', 'unilateral')
b += zpanel(194, 'in', 'inside', 'unilateral')
b += zpanel(256, 'non', 'varies', 'non-uniform')
b += text(160, 20, 'solid line = true profile;  shaded = tolerance zone', 's')
b += text(160, 140, 'outside = away from material (part material below the line)', 's')
F['g-26-3'] = (svg(b), 'Where the zone sits relative to the true profile: centered, offset with Ⓤ, all outside, all inside, or varying.')

# 26.4 between / all around / all over
b = ''
d = 'M40 112V44H120L160 24H260V112z'
b += path(d, 'ah')
b += circ(40, 44, 3, 'af') + text(30, 40, 'X', 't', 'end') + circ(260, 112, 3, 'af') + text(268, 120, 'Y', 't', 'start')
f, xe = fcfbox(120, 116, [PSURF, '0.4', 'A'])
b += f + text(xe + 8, 130, 'X ↔ Y', 't', 'start')
b += line(120, 126, 104, 126, 'k') + line(104, 126, 96, 112, 'k')
b += circ(214, 52, 0, 'k')
# all around on a second leader
b += line(260, 64, 290, 40, 'k') + circ(290, 40, 5, 'k') + line(290, 40, 306, 40, 'k')
b += text(306, 26, 'all around', 's', 'end')
b += circ(70, 20, 5, 'k') + circ(70, 20, 8.5, 'k') + line(78, 20, 100, 20, 'k') + text(104, 24, 'all over', 's', 'start')
b += text(160, 150, 'between: control applies only from X to Y', 's')
F['g-26-4'] = (svg(b, 152), 'Between (X↔Y) limits the extent; a circle on the leader means all around; a double circle, all over.')


def build():
    root = pathlib.Path(__file__).resolve().parent.parent
    html = (root / 'index.html').read_text(encoding='utf-8')
    out = '\n'.join(f'<template id="sf-{k}">{v[0]}</template>' for k, v in F.items())
    start, end = '<!-- SECTION-FIGS:START -->', '<!-- SECTION-FIGS:END -->'
    block = f'{start}\n{out}\n{end}'
    if start in html:
        html = re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda m: block, html, flags=re.S)
    else:
        html = html.replace('<!--\n  CONTENT FORMAT', block + '\n\n<!--\n  CONTENT FORMAT', 1)
    (root / 'index.html').write_text(html, encoding='utf-8')
    print(f'{len(F)} figures written')

if __name__ == '__main__':
    build()
