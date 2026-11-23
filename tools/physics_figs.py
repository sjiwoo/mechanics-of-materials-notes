"""Custom SVG figures for the Physics for Mechanics book.

T   : section-card figures, key 'ph-<ch>-<sec>' -> <template id="sf-ph-<ch>-<sec>">
ART : chapter-header icons, key '<ch>'          -> <template id="art-ph-<ch>">
Both are injected into index.html by  python tools/section_figs.py  (which imports this module).
Drawing helpers and CSS class conventions are those of section_figs.py.
"""
from section_figs import *

T = {}
ART = {}

# ======================= part A =======================
import math
# ---------------- 1-1 projectile ----------------
b = ''
x0, y0 = 30, 130
b += axes(x0, y0, 300, 20, 'x', 'y')
par = lambda x: 130 - 90 * (1 - ((x - 150) / 120) ** 2)
b += path(curve(par, 30, 270), 'a')
b += arrow(30, 130, 52, 97, 'k') + text(49, 84, 'v₀', '', 'end') + text(62, 124, 'θ', '', 'start')
b += line(150, 40, 150, 130, 'g') + text(144, 88, 'h', 't', 'end')
b += arrow(150, 40, 186, 40, 'k') + text(192, 44, 'vx', 's', 'start')
b += arrow(230, 72, 230, 100, 'a') + text(240, 90, 'g', 't', 'start')
b += arrow(30, 148, 270, 148, 'k') + arrow(270, 148, 30, 148, 'k') + text(150, 162, 'R', 't')
T['ph-1-1'] = svg(b, 170)

# ---------------- 1-2 free-body diagram ----------------
b = ''
b += rect(125, 55, 70, 40, 'ah', 3) + text(160, 80, 'm', 't')
b += rect(115, 45, 90, 60, 'g', 5)
b += arrow(160, 45, 160, 12, 'a') + text(170, 22, 'N', 't', 'start')
b += arrow(160, 105, 160, 140, 'a') + text(170, 134, 'W = mg', 't', 'start')
b += arrow(205, 75, 265, 75, 'k') + text(270, 79, 'F', '', 'start')
b += arrow(115, 75, 55, 75, 'k') + text(48, 79, 'f', '', 'end')
b += text(160, 156, 'only external forces on the isolated body', 's')
T['ph-1-2'] = svg(b, 162)

# ---------------- 1-3 incline and capstan ----------------
b = ''
b += path('M20 125L150 125L150 60z', 'kb')
b += path('M64.7 102.6L100.5 84.8L89.8 63.3L54 81.1z', 'ah')
b += arrow(77, 83, 105, 69, 'a') + text(112, 66, 'f', 't', 'start')
b += arrow(77, 83, 64, 55, 'a') + text(58, 52, 'N', 't', 'end')
b += path('M48 125A28 28 0 0 0 45 112.5', 'k') + text(56, 121, 'θ', '', 'start')
b += text(85, 148, 'slips when tanθ > μs', 's')
b += circ(240, 70, 28, 'kb')
b += path('M212 70A28 28 0 0 1 268 70', 'a')
b += line(212, 70, 212, 100, 'a') + line(268, 70, 268, 100, 'a')
b += arrow(212, 100, 212, 132, 'a') + text(205, 124, 'T₁', 't', 'end')
b += arrow(268, 100, 268, 116, 'k') + text(276, 114, 'T₂', '', 'start')
b += text(240, 78, 'θ', 't')
b += text(245, 148, 'T₁/T₂ = e^(μθ)', 's')
T['ph-1-3'] = svg(b, 156)

# ---------------- 1-4 circular motion and banking ----------------
b = ''
b += circ(110, 80, 50, 'g')
b += line(110, 80, 160, 80, 'g')
b += circ(160, 80, 8, 'ah')
b += arrow(160, 72, 160, 36, 'k') + text(168, 48, 'v', '', 'start')
b += arrow(152, 80, 120, 80, 'a') + text(136, 72, 'ac', 't')
b += circ(110, 80, 2.5, 'kf') + text(136, 98, 'r', 's')
b += text(110, 150, 'top view', 's')
b += path('M190 125L300 125L300 85z', 'kb')
b += path('M232.3 109.6L269.9 95.9L263.1 77.1L225.5 90.8z', 'ah')
b += arrow(247.7, 93.4, 235.4, 59.6, 'a') + text(242, 60, 'N', 't', 'start')
b += arrow(247.7, 93.4, 212, 93.4, 'k') + text(212, 84, 'N sinθ', 's', 'end')
b += path('M220 125A30 30 0 0 0 218.2 114.7', 'k') + text(224, 122, 'θ', '', 'start')
b += text(255, 150, 'centre on left', 's')
T['ph-1-4'] = svg(b, 158)

# ---------------- 2-1 work as area ----------------
b = ''
b += axes(40, 115, 290, 20, 'x', 'F')
b += path('M40 115L40 85L240 45L240 115z', 'zr')
b += line(40, 85, 240, 45, 'a')
b += line(240, 45, 240, 115, 'g')
b += text(140, 106, 'W = area', 't')
b += text(240, 128, 'x₂', 's') + text(40, 128, 'x₁', 's')
b += text(110, 36, 'W = ∫F dx', 't')
b += text(160, 146, 'net work = change in kinetic energy', 's')
T['ph-2-1'] = svg(b, 152)

# ---------------- 2-2 potential energy curve ----------------
b = ''
b += axes(30, 135, 300, 15, 'x', 'U')
U = lambda x: 75 + 9 * (-(((x - 165) / 50) ** 3) / 3 + 4 * ((x - 165) / 50))
b += path(curve(U, 40, 290), 'a')
b += circ(265, 123, 4, 'af') + text(262, 104, 'stable', 't')
b += circ(65, 27, 4, 'kf') + text(68, 18, 'unstable', 's')
b += arrow(140, 64, 180, 64, 'k') + text(160, 54, 'F', '', 'middle')
b += text(165, 153, 'F = −dU/dx pushes toward lower U', 's')
T['ph-2-2'] = svg(b, 160)

# ---------------- 2-3 incline with friction ----------------
b = ''
b += path('M30 50L200 130L30 130z', 'kb') + line(200, 130, 300, 130, 'k')
b += path('M43.6 56.4L79.8 73.4L87.5 57.1L51.3 40.1z', 'ah')
b += arrow(22, 50, 22, 130, 'a') + arrow(22, 130, 22, 50, 'a') + text(14, 94, 'h', 't', 'end')
b += text(125, 48, 'U = mgh', 's')
b += rect(225, 100, 34, 30, 'g') + arrow(262, 115, 292, 115, 'k') + text(296, 119, 'v', '', 'start')
b += text(160, 148, 'mgh = ½mv² + μk N s', 's')
T['ph-2-3'] = svg(b, 155)

# ---------------- 2-4 drive chain ----------------
b = ''
b += arrow(6, 70, 34, 70, 'a') + text(20, 56, 'Pin', 't')
b += rect(36, 50, 56, 40, 'ah', 3) + text(64, 75, 'motor')
b += line(92, 70, 130, 70, 'k') + text(111, 62, 'T, ω', 's')
b += rect(130, 50, 56, 40, 'ah', 3) + text(158, 75, 'gearbox')
b += line(186, 70, 228, 70, 'k') + text(207, 62, 'T↑ ω↓', 's')
b += circ(250, 70, 22, 'kb')
b += line(272, 70, 272, 118, 'k') + rect(258, 118, 28, 20, 'ah', 2) + text(272, 132, 'm')
b += arrow(296, 115, 296, 88, 'a') + text(300, 102, 'v', '', 'start')
b += text(250, 34, 'Pout = mgv', 't')
b += text(64, 108, 'η₁', 's') + text(158, 108, 'η₂', 's')
b += text(110, 148, 'η = η₁ × η₂', 't')
T['ph-2-4'] = svg(b, 160)

# ---------------- chapter icons ----------------
ART['1'] = ('<svg viewBox="0 0 150 84"><path d="M10 72h130" stroke="currentColor" opacity=".5"/>'
            '<path d="M18 72Q75 -20 132 72" fill="none" stroke="currentColor" stroke-width="2.5" stroke-dasharray="5 3"/>'
            '<circle cx="75" cy="25" r="6" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<path d="M18 72L30 53M30 53L29.4 60.9M30 53L23.2 57.1" stroke="currentColor" stroke-width="2" fill="none"/>'
            '<path d="M75 32v14m-4-6 4 6 4-6" stroke="currentColor" stroke-width="2" fill="none"/>'
            '<text x="60" y="68" font-size="12" fill="currentColor" font-family="JetBrains Mono">F=ma</text></svg>')
ART['2'] = ('<svg viewBox="0 0 150 84"><path d="M10 14v56" stroke="currentColor" stroke-width="3"/>'
            '<g stroke="currentColor" opacity=".5"><path d="M4 22l6-6M4 34l6-6M4 46l6-6M4 58l6-6M4 70l6-6"/></g>'
            '<path d="M10 42h8l4-10 8 20 8-20 8 20 8-20 4 10h6" fill="none" stroke="currentColor" stroke-width="2.5"/>'
            '<rect x="64" y="28" width="38" height="28" rx="3" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<path d="M106 42h34m-6-5 6 5-6 5" stroke="currentColor" stroke-width="2" fill="none"/>'
            '<text x="30" y="78" font-size="12" fill="currentColor" font-family="JetBrains Mono">U=½kx²</text></svg>')

# ======================= part B =======================
from math import sin, cos, pi, radians
# 3.1 impulse
b = ''
b += axes(40, 120, 290, 20, 't', 'F')
fn = lambda x: 120 - 80 * sin(pi * (x - 70) / 160)
b += path('M70 120L' + curve(fn, 70, 230)[1:] + 'L230 120z', 'zfill')
b += path(curve(fn, 70, 230), 'a')
b += line(70, 69, 230, 69, 'g')
b += text(236, 73, 'F_avg', 's', 'start')
b += text(150, 104, 'J = area', 't')
b += arrow(70, 136, 230, 136, 'k', 6, 3) + arrow(230, 136, 70, 136, 'k', 6, 3)
b += text(150, 152, 'Δt', '')
T['ph-3-1'] = svg(b, 160)

# 3.2 recoil
b = ''
b += rect(100, 66, 80, 20, 'ah', 3) + rect(180, 71, 24, 10, 'ah', 1)
b += circ(220, 76, 4, 'af')
b += arrow(230, 76, 292, 76, 'a') + text(262, 66, 'v', 't')
b += arrow(100, 76, 46, 76, 'k') + text(72, 66, 'V', '')
b += line(150, 46, 150, 112, 'g')
b += text(150, 126, 'centre of mass stays put', 's')
b += text(160, 30, 'm₁V = m₂v', 't')
T['ph-3-2'] = svg(b)

# 3.3 collision
b = ''
b += text(8, 47, 'before', 's', 'start') + text(8, 97, 'after', 's', 'start')
b += rect(70, 30, 44, 26, 'ah', 3) + text(92, 47, 'm₁')
b += rect(190, 30, 44, 26, 'kb', 3) + text(212, 47, 'm₂')
b += arrow(74, 22, 114, 22, 'a') + text(120, 26, 'v₁', '', 'start')
b += arrow(194, 22, 220, 22, 'k') + text(226, 26, 'v₂', '', 'start')
b += rect(130, 80, 44, 26, 'ah', 3) + text(152, 97, 'm₁')
b += rect(230, 80, 44, 26, 'kb', 3) + text(252, 97, 'm₂')
b += arrow(134, 72, 156, 72, 'a') + text(162, 76, "v₁'", '', 'start')
b += arrow(234, 72, 280, 72, 'k') + text(284, 76, "v₂'", '', 'start')
b += text(160, 136, "e = (v₂' − v₁') / (v₁ − v₂)", 't')
T['ph-3-3'] = svg(b, 150)

# 3.4 cushion
b = ''
b += rect(160, 96, 90, 28, 'kb') + wall_h(150, 260, 124, 1)
b += rect(180, 28, 50, 24, 'ah', 3) + text(205, 44, 'm')
b += arrow(205, 52, 205, 92, 'a')
b += line(120, 52, 120, 96, 'k')
b += arrow(120, 74, 120, 52, 'k', 5, 3) + arrow(120, 74, 120, 96, 'k', 5, 3)
b += text(112, 78, 'h', '', 'end')
b += line(160, 110, 250, 110, 'g')
b += text(150, 107, 'd', '', 'end')
b += arrow(262, 124, 262, 88, 'a') + text(270, 106, 'F', 't', 'start')
b += text(300, 60, 'F = ΔKE/d', 't', 'end')
T['ph-3-4'] = svg(b)

# 4.1 kinematics
b = ''
cx, cy, R = 100, 85, 50
a = radians(50)
px, py = cx + R * cos(a), cy - R * sin(a)
b += circ(cx, cy, R, 'a')
b += line(cx, cy, cx + 62, cy, 'g')
b += line(cx, cy, px, py, 'g')
b += path(f'M{cx+22} {cy} A22 22 0 0 0 {cx+22*cos(a):.1f} {cy-22*sin(a):.1f}', 'k')
b += text(cx + 31, cy - 6, 'θ', '')
b += circ(px, py, 3, 'kf')
b += arrow(px, py, px - 40 * sin(a), py - 40 * cos(a), 'a') + text(px - 40 * sin(a) - 4, py - 40 * cos(a) + 4, 'v', 't', 'end')
b += arrow(px, py, px - 28 * cos(a), py + 28 * sin(a), 'k') + text(px + 8, py + 16, 'aₙ', '', 'start')
b += text(cx + 10, cy - 28, 'r', '', 'end')
b += text(206, 48, 'v = rω', '', 'start') + text(206, 74, 'aₜ = rα', '', 'start') + text(206, 100, 'aₙ = rω²', '', 'start')
T['ph-4-1'] = svg(b)

# 4.2 torque and inertia
b = ''
b += rect(44, 84, 226, 12, 'ah', 2)
b += circ(60, 90, 5, 'k')
b += circ(110, 90, 5, 'kf') + circ(200, 90, 5, 'kf')
b += arrow(250, 40, 250, 84, 'a') + text(258, 62, 'F', 't', 'start')
b += arrow(60, 114, 250, 114, 'k', 6, 3) + arrow(250, 114, 60, 114, 'k', 6, 3)
b += text(155, 132, 'r', '')
b += text(70, 40, 'τ = r × F', 't', 'start') + text(70, 62, 'I = Σ m r²', '', 'start')
T['ph-4-2'] = svg(b)

# 4.3 rolling on incline
b = ''
b += path('M30 35L30 125L290 125z', 'kb')
tan = 90 / 260
d = (1 / (1 + tan ** 2) ** .5, tan / (1 + tan ** 2) ** .5)
n = (d[1], -d[0])
sx = 170; sy = 35 + (sx - 30) * tan
wx, wy = sx + 18 * n[0], sy + 18 * n[1]
b += circ(wx, wy, 18, 'ah') + line(wx, wy, wx + 18, wy)
b += circ(sx, sy, 3, 'kf')
b += arrow(wx, wy, wx + 45 * d[0], wy + 45 * d[1], 'a') + text(wx + 48, wy + 8, 'v = rω', 't', 'start')
b += text(150, 114, 'contact point: v = 0', 's')
b += text(22, 82, 'h', '', 'end')
T['ph-4-3'] = svg(b)

# 4.4 flywheel / angular momentum
b = ''
b += circ(100, 82, 50, 'ah') + circ(100, 82, 38, 'g')
b += circ(100, 82, 6, 'k') + circ(100, 82, 1.5, 'kf')
b += path('M162 82 A62 62 0 0 0 100 20', 'a') + arrow(115, 20, 98, 20, 'a', 6, 3)
b += text(160, 40, 'ω', 't', 'start')
b += text(200, 52, 'L = Iω', 't', 'start')
b += text(200, 76, 'L along axis', 's', 'start') + text(200, 92, '(out of page)', 's', 'start')
b += text(200, 118, 'mass at rim: I large', 's', 'start')
T['ph-4-4'] = svg(b)

# 4.5 gears
b = ''
b += circ(100, 82, 20, 'ah') + circ(100, 82, 23, 'g') + circ(100, 82, 3, 'kf')
b += circ(160, 82, 40, 'kb') + circ(160, 82, 43, 'g') + circ(160, 82, 3, 'kf')
b += text(100, 52, '1 motor', 's') + text(160, 22, '2 load', 's')
b += text(212, 56, 'ω₂ = ω₁/N', '', 'start') + text(212, 80, 'τ₂ = N τ₁', '', 'start') + text(212, 104, 'J₂/N² at motor', '', 'start')
b += text(160, 140, 'N = 2 shown', 's')
T['ph-4-5'] = svg(b)

ART['3'] = ('<svg viewBox="0 0 150 84"><circle cx="40" cy="42" r="14" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<circle cx="104" cy="42" r="14" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<path d="M4 42h18m-6-5 6 5-6 5M122 42h22m-6-5 6 5-6 5" stroke="currentColor" stroke-width="2" fill="none"/>'
            '<path d="M56 42h32" stroke="currentColor" stroke-dasharray="3 3"/>'
            '<text x="20" y="76" font-size="11" fill="currentColor" font-family="JetBrains Mono">Δp = FΔt</text></svg>')
ART['4'] = ('<svg viewBox="0 0 150 84"><circle cx="50" cy="42" r="22" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<circle cx="50" cy="42" r="28" fill="none" stroke="currentColor" stroke-dasharray="3 3" opacity=".6"/>'
            '<path d="M50 42l16-16M50 42l-18 6M50 42l4 20" stroke="currentColor" stroke-width="1.5"/>'
            '<circle cx="50" cy="42" r="3" fill="currentColor"/>'
            '<path d="M104 24a24 24 0 0 1 14 22m-3-7 3 7 7-4" stroke="currentColor" stroke-width="2" fill="none"/>'
            '<text x="80" y="74" font-size="11" fill="currentColor" font-family="JetBrains Mono">τ = Iα</text></svg>')

# ======================= part C =======================
import math

def spring(x1, y1, x2, y2, n=5, amp=6, c='a'):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    vx, vy = -uy, ux
    lead = L * 0.18
    pts = [(0, 0), (lead, 0)]
    span = L - 2 * lead
    for i in range(n * 2):
        s = lead + span * (i + 0.5) / (n * 2)
        pts.append((s, amp if i % 2 == 0 else -amp))
    pts += [(L - lead, 0), (L, 0)]
    d = 'M' + 'L'.join(f'{x1 + ux*s + vx*t:.1f} {y1 + uy*s + vy*t:.1f}' for s, t in pts)
    return path(d, c)

def pts_path(f, x0, x1, n=120):
    return 'M' + 'L'.join(f'{x:.1f} {f(x):.1f}' for x in [x0 + (x1 - x0) * i / n for i in range(n + 1)])

# ---------------- 5.1 SHM ----------------
b = ''
x0, y0, per, A = 40, 78, 130, 40
f = lambda x: y0 - A * math.cos(2 * math.pi * (x - x0) / per + math.pi / 3)
b += axes(x0, y0, 300, 12, 't', 'x')
b += path(pts_path(f, x0, 296), 'a')
b += line(x0, y0 - A, 270, y0 - A, 'g') + line(x0, y0 + A, 270, y0 + A, 'g')
b += arrow(24, y0, 24, y0 - A, 'k') + arrow(24, y0, 24, y0 + A, 'k') + text(12, y0 + 4, 'A')
pk1 = x0 + per * 5 / 6
b += line(pk1, y0 - A, pk1, 132, 'g') + line(pk1 + per, y0 - A, pk1 + per, 132, 'g')
b += arrow(pk1 + 50, 128, pk1, 128, 'k', 6, 3) + arrow(pk1 + 80, 128, pk1 + per, 128, 'k', 6, 3)
b += text(pk1 + 65, 132, 'T', 't')
b += circ(x0, f(x0), 2.5, 'kf') + text(x0 + 10, 30, 'φ = phase at t = 0', 's', 'start')
b += text(x0 + 50, 148, 'x = A cos(ωt + φ)', 's', 'start')
T['ph-5-1'] = svg(b, 155)

# ---------------- 5.2 spring-mass and cantilever ----------------
b = ''
b += wall_v(28, 12, 66, -1)
b += spring(28, 40, 120, 40, 6, 7, 'a')
b += rect(120, 22, 40, 36, 'ah', 3) + text(140, 44, 'm')
b += line(120, 62, 200, 62, 'g') + line(28, 62, 28, 62, 'g')
b += arrow(165, 40, 195, 40, 'k') + text(200, 44, 'x', '', 'start')
b += text(218, 28, 'ω = √(k/m)', 't', 'start') + text(218, 46, 'parallel: k₁+k₂', 's', 'start') + text(218, 60, 'series: 1/k = Σ 1/kᵢ', 's', 'start')
b += wall_v(28, 92, 160, -1)
dl = lambda x: 124 + 20 * ((x - 28) / 150) ** 2 * (3 - (x - 28) / 150) / 2
b += line(28, 124, 178, 124, 'g')
b += path(pts_path(dl, 28, 178, 40), 'a')
b += rect(168, dl(178) - 1, 24, 22, 'ah', 3) + text(180, dl(178) + 14, 'm')
b += arrow(205, 126, 205, 150, 'k') + text(214, 148, 'δ', '', 'start')
b += text(262, 120, 'k = 3EI/L³', 't') + text(262, 138, 'bar: EA/L', 's')
T['ph-5-2'] = svg(b, 170)

# ---------------- 5.3 pendulums ----------------
b = ''
b += line(40, 18, 120, 18, 'k')
px, py = 80, 18
bx, by = 80 + 70 * math.sin(0.5), 18 + 70 * math.cos(0.5)
b += line(px, py, px, 112, 'g')
b += line(px, py, bx, by, 'k') + circ(bx, by, 9, 'ah')
b += path(f'M{px} 46A28 28 0 0 1 {px + 28 * math.sin(0.5):.1f} {py + 28 * math.cos(0.5):.1f}', 'a')
b += text(px + 11, 66, 'θ', 't') + text(px + 36, 40, 'L') + text(bx + 20, by + 6, 'm')
b += arrow(bx, by + 9, bx, by + 36, 'a') + text(bx + 18, by + 36, 'mg', 't')
b += line(190, 18, 270, 18, 'k')
ox, oy = 230, 18
a = 0.35
ux, uy = math.sin(a), math.cos(a)
nx, ny = uy, -ux
L2, w2 = 98, 7
poly = [(ox + nx * w2, oy + ny * w2), (ox + ux * L2 + nx * w2, oy + uy * L2 + ny * w2),
        (ox + ux * L2 - nx * w2, oy + uy * L2 - ny * w2), (ox - nx * w2, oy - ny * w2)]
b += path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in poly) + 'z', 'ah')
gx, gy = ox + ux * 52, oy + uy * 52
b += line(ox, oy, ox, 120, 'g') + circ(ox, oy, 3, 'kf') + circ(gx, gy, 3.5, 'kf')
b += text(ox - 12, 13, 'O', '', 'end') + text(gx + 14, gy - 2, 'G', '', 'start')
b += text(ox - 7, 50, 'd', '', 'end') + arrow(gx, gy + 4, gx, gy + 34, 'a') + text(gx - 6, gy + 40, 'mg', 't', 'end')
b += text(80, 150, 'simple', 's') + text(230, 150, 'physical', 's')
T['ph-5-3'] = svg(b, 160)

# ---------------- 5.4 energy ----------------
b = ''
cx, base = 165, 128
sc = 105
par = lambda x: base - 78 * ((x - cx) / sc) ** 2
b += arrow(40, base, 295, base, 'k', 6, 3) + text(298, base + 4, 'x', '', 'start')
b += line(cx, base, cx, 14, 'k')
b += path(pts_path(par, cx - sc, cx + sc, 60), 'a')
b += line(cx - sc - 6, 50, cx + sc + 6, 50, 'g')
b += text(cx + 4, 28, 'E = ½kA²', 't', 'start')
b += text(cx - sc, base + 14, '−A') + text(cx + sc, base + 14, '+A')
xs = cx + 55
b += arrow(xs, par(xs) - 1, xs, 52, 'k', 6, 3) + text(xs + 6, 76, 'KE', '', 'start')
b += text(cx + 74, 108, 'PE = ½kx²', 't', 'start')
T['ph-5-4'] = svg(b, 150)

# ---------------- 6.1 decay ----------------
b = ''
x0, y0, per = 40, 80, 50
zeta = 0.1
env = lambda x: 56 * math.exp(-zeta * 2 * math.pi * (x - x0) / per)
f = lambda x: y0 - env(x) * math.cos(2 * math.pi * (x - x0) / per)
b += axes(x0, y0, 300, 12, 't', 'x')
b += path(pts_path(env and (lambda x: y0 - env(x)), x0, 296, 80), 'g') + path(pts_path(lambda x: y0 + env(x), x0, 296, 80), 'g')
b += path(pts_path(f, x0, 296, 240), 'a')
for k, lab in ((1, 'x₁'), (2, 'x₂')):
    px = x0 + per * k
    b += circ(px, y0 - env(px), 2.5, 'kf') + text(px, y0 - env(px) - 6, lab)
b += arrow(x0 + per + 18, 140, x0 + per, 140, 'k', 6, 3) + arrow(x0 + per + 32, 140, x0 + 2 * per, 140, 'k', 6, 3)
b += line(x0 + per, y0 - env(x0 + per), x0 + per, 144, 'g') + line(x0 + 2 * per, y0 - env(x0 + 2 * per), x0 + 2 * per, 144, 'g')
b += text(x0 + per + 25, 143, 'T', 't')
b += text(180, 28, 'δ = ln(x₁/x₂) ≈ 2πζ', 's', 'start') + text(180, 42, 'envelope e^(−ζωₙt)', 's', 'start')
T['ph-6-1'] = svg(b, 155)

# ---------------- 6.2 magnification ----------------
b = ''
x0, y0, sx, sy = 40, 132, 100, 20
Mf = lambda r, z: 1 / math.sqrt((1 - r * r) ** 2 + (2 * z * r) ** 2)
b += axes(x0, y0, 292, 14, 'r', 'M')
b += line(x0 + sx, y0, x0 + sx, 30, 'g') + text(x0 + sx, y0 + 13, '1')
b += line(x0, y0 - sy, 285, y0 - sy, 'g')
for z, c, lab, lx, ly in ((0.1, 'a', 'ζ = 0.1', 168, 38), (0.3, 'k', 'ζ = 0.3', 150, 88), (0.7, 'k', 'ζ = 0.7', 46, 96)):
    b += path(pts_path(lambda r, z=z: y0 - sy * Mf(r, z), 0, 2.5, 100).replace('M0', 'M0'), c) if False else ''
    pts = [(x0 + sx * r, y0 - sy * Mf(r, z)) for r in [i * 0.025 for i in range(101)]]
    b += path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts), c)
    ly = {0.1: 32, 0.3: 50, 0.7: 68}[z]
    b += line(215, ly - 4, 235, ly - 4, c) + text(240, ly, lab, 't' if c == 'a' else '', 'start')
b += text(x0 + sx + 3, 24, '≈ 1/(2ζ)', 's', 'start')
b += text(30, y0 - sy + 4, '1', '', 'end')
T['ph-6-2'] = svg(b, 160)

# ---------------- 6.3 half power ----------------
b = ''
x0, y0, sx, sy = 40, 135, 250, 20
z = 0.1
rmap = lambda r: x0 + sx * (r - 0.5)
b += axes(x0, y0, 296, 14, 'ω', '')
pts = [(rmap(0.5 + i * 0.01), y0 - sy * Mf(0.5 + i * 0.01, z)) for i in range(101)]
b += path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts), 'a')
pk = y0 - sy / (2 * z)
hp = y0 - sy / (2 * z) / math.sqrt(2)
r1 = 1 - z
r2 = 1 + z
b += line(x0, hp, rmap(1.28), hp, 'g')
b += line(rmap(1), pk, rmap(1), y0, 'g')
b += line(rmap(r1), hp, rmap(r1), y0, 'g') + line(rmap(r2), hp, rmap(r2), y0, 'g')
b += arrow(rmap(1) - 2, hp + 14, rmap(r1), hp + 14, 'k', 6, 3) + arrow(rmap(1) + 2, hp + 14, rmap(r2), hp + 14, 'k', 6, 3)
b += text(rmap(r1) - 4, y0 + 13, 'ω₁', '', 'end') + text(rmap(r2) + 4, y0 + 13, 'ω₂', '', 'start') + text(rmap(1), y0 + 13, 'ωₙ')
b += text(rmap(1), y0 + 30, 'Δω = ωₙ/Q', 't')
b += text(rmap(1.1), pk + 10, 'peak = Q', 's', 'start')
b += text(rmap(1.31), hp + 4, 'peak/√2', 's', 'start')
T['ph-6-3'] = svg(b, 172)

# ---------------- 6.4 transmissibility ----------------
b = ''
x0, y0, sx, sy = 40, 132, 70, 17
Tf = lambda r, z: math.sqrt(1 + (2 * z * r) ** 2) / math.sqrt((1 - r * r) ** 2 + (2 * z * r) ** 2)
b += axes(x0, y0, 290, 14, 'r', 'T')
xr = x0 + sx * math.sqrt(2)
b += rect(xr, y0 - sy, 285 - xr, sy, 'zr')
b += line(x0, y0 - sy, 285, y0 - sy, 'g') + line(xr, y0, xr, 30, 'g')
b += text(xr, y0 + 13, '√2') + text(x0 - 4, y0 - sy + 4, '1', '', 'end')
for z, c in ((0.1, 'a'), (0.5, 'k')):
    pts = [(x0 + sx * r, y0 - sy * Tf(r, z)) for r in [i * 0.02 for i in range(176)]]
    pts = [(x, y) for x, y in pts if y > 20]
    b += path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts), c)
b += line(185, 26, 205, 26, 'a') + text(210, 30, 'ζ = 0.1', 't', 'start')
b += line(185, 44, 205, 44, 'k') + text(210, 48, 'ζ = 0.5', '', 'start')
b += text(xr + 60, y0 - sy - 8, 'isolation, T < 1', 's')
T['ph-6-4'] = svg(b, 160)

# ---------------- 6.5 cantilever mode ----------------
b = ''
b += wall_v(30, 50, 130, -1)
dl = lambda x: 78 + 36 * ((x - 30) / 190) ** 2 * (3 - (x - 30) / 190) / 2
b += line(30, 78, 220, 78, 'k')
b += path(pts_path(dl, 30, 220, 50), 'g')
b += rect(208, 62, 28, 16, 'ah', 3) + text(222, 74, 'M')
b += rect(208, dl(220) - 1, 28, 16, 'kb', 3)
b += arrow(246, 80, 246, dl(220) - 2, 'k', 6, 3) + text(254, 100, 'δ', '', 'start')
b += arrow(222, 40, 222, 60, 'a') + text(232, 48, 'Mg', 't', 'start')
b += text(160, 140, 'ω₁ ≈ √(g/δ_st)', 't') + text(100, 38, 'm_eff ≈ 0.24 m_beam', 's')
b += text(120, 108, 'mode shape', 's')
T['ph-6-5'] = svg(b, 155)

# ---------------- icons ----------------
ART['5'] = ('<svg viewBox="0 0 150 84"><path d="M12 8v68" stroke="currentColor" stroke-width="3"/>'
            '<g stroke="currentColor" opacity=".5"><path d="M6 14l6-6M6 28l6-6M6 42l6-6M6 56l6-6M6 70l6-6"/></g>'
            '<path d="M12 42h10l4-10 8 20 8-20 8 20 8-20 4 10h8" fill="none" stroke="currentColor" stroke-width="2.5"/>'
            '<rect x="68" y="28" width="26" height="28" rx="3" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<path d="M100 42q10-24 20 0t20 0" fill="none" stroke="currentColor" stroke-width="2.5"/>'
            '<path d="M100 66h40" stroke="currentColor" stroke-dasharray="3 3" opacity=".5"/></svg>')
ART['6'] = ('<svg viewBox="0 0 150 84"><path d="M12 72h128M12 72V10" stroke="currentColor" opacity=".5"/>'
            '<path d="M12 42Q60 6 140 40M12 42Q60 78 140 44" fill="none" stroke="currentColor" stroke-dasharray="3 3" opacity=".6"/>'
            '<path d="M12 42c6-30 12-30 18 0s12 24 18 0 10-18 16 0 9 12 14 0 8-8 12 0 7 5 10 0 6-3 9 0 5 2 7 0" fill="none" stroke="currentColor" stroke-width="2.5"/>'
            '<text x="86" y="20" font-size="11" fill="currentColor" font-family="JetBrains Mono">ζ, Q</text></svg>')

# ======================= part D =======================
import math

def dim(x1, y1, x2, y2):
    return arrow(x1, y1, x2, y2, 'k', 6, 3) + arrow(x2, y2, x1, y1, 'k', 6, 3)

# ---------------- 7-1 travelling wave ----------------
b = ''
y0, A, lam, x0 = 88, 28, 120, 24
b += line(x0, y0, 270, y0, 'g')
b += path(curve(lambda x: y0 - A * math.sin(2 * math.pi * (x - x0) / lam), x0, x0 + 2 * lam, 120), 'a')
b += line(54, y0 - A - 2, 54, 36, 'g') + line(174, y0 - A - 2, 174, 36, 'g')
b += dim(54, 40, 174, 40) + text(114, 32, 'λ')
b += line(174, y0 - A, 280, y0 - A, 'g') + dim(282, y0, 282, y0 - A) + text(292, y0 - 10, 'A', '', 'start')
b += arrow(200, 140, 260, 140, 'a') + text(270, 144, 'v', 't', 'start')
b += text(30, 144, 'y = A sin(kx − ωt)', 's', 'start')
T['ph-7-1'] = svg(b)

# ---------------- 7-2 wave speeds ----------------
b = ''
rows = [('steel', 5050, 'ah'), ('water', 1480, 'kb'), ('air', 343, 'kb'), ('rubber', 95, 'ah')]
for i, (n, v, c) in enumerate(rows):
    y = 14 + i * 30
    w = (math.log10(v) - 1.5) * 90
    b += text(54, y + 13, n, '', 'end') + rect(60, y, round(w), 18, c, 2)
    b += text(60 + w + 5, y + 13, f'{v} m/s', 's', 'start')
b += line(60, 8, 60, 128, 'k')
b += text(160, 150, 'log scale: rods √(E/ρ), fluids √(B/ρ)', 's')
T['ph-7-2'] = svg(b, 160)

# ---------------- 7-3 string modes ----------------
b = ''
for n, yc in ((1, 28), (2, 70), (3, 112)):
    f = lambda x, n=n, yc=yc: yc - 16 * math.sin(n * math.pi * (x - 40) / 240)
    b += path(curve(f, 40, 280, 100), 'a')
    b += path(curve(lambda x, n=n, yc=yc: 2 * yc - f(x), 40, 280, 100), 'g')
    b += line(40, yc - 20, 40, yc + 20, 'k') + line(280, yc - 20, 280, yc + 20, 'k')
    for k in range(n + 1):
        b += circ(40 + 240 * k / n, yc, 2.8, 'kf')
    b += text(24, yc + 4, f'n={n}', '', 'end') + text(292, yc + 4, f'{n}f₁' if n > 1 else 'f₁', '', 'start')
b += dim(40, 140, 280, 140) + text(160, 156, 'L')
T['ph-7-3'] = svg(b, 162)

# ---------------- 7-4 beats ----------------
b = ''
y0, A = 78, 17
b += axes(30, y0, 292, y0, 't', '') + arrow(30, y0, 30, 22, 'k', 6, 3) + text(30, 16, 'y')
env = lambda x: y0 - 2 * A * math.cos(2 * math.pi * (x - 30) / 260)
b += path(curve(env, 30, 290, 120), 'g') + path(curve(lambda x: 2 * y0 - env(x), 30, 290, 120), 'g')
s = lambda x: y0 - A * (math.sin(2 * math.pi * 12 * (x - 30) / 260) + math.sin(2 * math.pi * 10 * (x - 30) / 260))
b += path(curve(s, 30, 290, 300), 'a')
b += line(95, y0 + 6, 95, 128, 'g') + line(225, y0 + 6, 225, 128, 'g')
b += dim(95, 124, 225, 124) + text(160, 146, 'T_beat = 1/|f₁ − f₂|', 's')
T['ph-7-4'] = svg(b, 156)

# ---------------- 8-1 hydrostatics and Pascal ----------------
b = ''
b += rect(30, 40, 80, 90, 'ah') + path('M30 34V130H110V34', 'k')
b += line(30, 40, 110, 40, 'a')
for y, L in ((60, 16), (85, 28), (110, 40)):
    b += arrow(110, y, 110 + L, y, 'a')
b += dim(18, 40, 18, 110) + text(10, 78, 'h')
b += text(70, 26, 'p₀ (atmosphere)', 's') + text(70, 148, 'p = p₀ + ρgh', 's')
b += path('M190 86H220V108H250V86H310V130H190Z', 'zr')
b += path('M188 72V132H312V72', 'k') + path('M221 72V107H249V72', 'k')
b += rect(190, 80, 30, 6, 'kb') + rect(250, 80, 60, 6, 'kb')
b += arrow(205, 44, 205, 78, 'k') + text(205, 38, 'F₁')
b += arrow(280, 76, 280, 44, 'a') + text(280, 38, 'F₂', 't')
b += text(205, 102, 'A₁', 's') + text(280, 102, 'A₂', 's')
b += text(250, 148, 'F₂ = F₁A₂/A₁', 's')
T['ph-8-1'] = svg(b)

# ---------------- 8-2 buoyancy ----------------
b = ''
b += rect(20, 64, 280, 76, 'zr') + line(20, 64, 300, 64, 'a')
b += rect(120, 34, 80, 62, 'kb')
b += arrow(148, 62, 148, 118, 'k') + text(138, 118, 'W', '', 'end')
b += arrow(172, 80, 172, 26, 'a') + text(184, 26, 'F_B', 't', 'start')
b += text(50, 100, 'ρ_f', 's') + text(250, 100, 'V_disp below line', 's')
b += text(160, 154, 'F_B = ρ_f g V_disp = W when floating', 's')
T['ph-8-2'] = svg(b, 160)

# ---------------- 8-3 venturi ----------------
b = ''
b += path('M20 46H90L130 66H190L230 46H300V114H230L190 94H130L90 114H20Z', 'zr')
b += path('M20 46H90L130 66H190L230 46H300', 'k') + path('M20 114H90L130 94H190L230 114H300', 'k')
b += rect(52, 22, 6, 24, 'ah') + rect(157, 44, 6, 22, 'ah')
b += line(58, 22, 176, 22, 'g') + dim(172, 22, 172, 44) + text(182, 37, 'Δh', '', 'start')
b += text(55, 15, 'p₁') + text(160, 37, 'p₂', '', 'end')
b += arrow(26, 80, 66, 80, 'a') + arrow(128, 80, 196, 80, 'a')
b += text(55, 134, 'v₁, A₁', 's') + text(160, 134, 'v₂, A₂', 's')
b += text(160, 154, 'A₁v₁ = A₂v₂,  p₂ < p₁', 's')
T['ph-8-3'] = svg(b, 162)

# ---------------- 8-4 viscosity and pipe flow ----------------
b = ''
b += rect(30, 24, 110, 8, 'kb') + wall_h(30, 140, 112, 1)
b += arrow(60, 14, 100, 14, 'k') + text(108, 18, 'U', '', 'start')
b += line(40, 32, 40, 112, 'g') + line(100, 32, 40, 112, 'g')
for y in (44, 60, 76, 92):
    b += arrow(40, y, 40 + 60 * (112 - y) / 80, y, 'a')
b += text(85, 136, 'τ = μ du/dy', 's')
b += wall_h(180, 300, 34, -1) + wall_h(180, 300, 114, 1)
b += line(200, 34, 200, 114, 'g')
pts = [(200 + 70 * (1 - ((y - 74) / 40) ** 2), y) for y in range(34, 115, 4)]
b += path('M' + 'L'.join(f'{x:.1f} {y}' for x, y in pts), 'a')
for y in (46, 60, 74, 88, 102):
    b += arrow(200, y, 200 + 70 * (1 - ((y - 74) / 40) ** 2), y, 'a')
b += text(240, 138, 'u_max = 2 × mean', 's')
T['ph-8-4'] = svg(b, 150)

# ---------------- 8-5 drag ----------------
b = ''
b += rect(60, 50, 8, 60, 'kb')
b += path('M68 50L135 32M68 110L135 128', 'g')
b += arrow(12, 80, 52, 80, 'k') + text(32, 70, 'v')
b += arrow(70, 80, 110, 80, 'a') + text(124, 84, 'F_D', 't', 'start')
b += path('M185 80C195 55 235 58 270 80C235 102 195 105 185 80Z', 'ah')
b += path('M270 80L306 74M270 80L306 86', 'g')
b += arrow(150, 80, 180, 80, 'k')
b += text(100, 150, 'C_D ≈ 1.2 (plate)') + text(245, 150, 'C_D ≈ 0.05')
T['ph-8-5'] = svg(b, 160)

# ---------------- chapter icons ----------------
pts = 'M' + 'L'.join(f'{10 + i*130/80:.1f} {40 - 20*math.sin(2*math.pi*i/40):.1f}' for i in range(81))
ART['7'] = ('<svg viewBox="0 0 150 84"><path d="M10 40H140" stroke="currentColor" stroke-dasharray="3 3" opacity=".5"/>'
            f'<path d="{pts}" fill="none" stroke="currentColor" stroke-width="2.5"/>'
            '<path d="M10 72h60m-6-4 6 4-6 4" fill="none" stroke="currentColor" stroke-width="1.5"/>'
                        '<text x="80" y="78" font-size="11" fill="currentColor" font-family="JetBrains Mono">v = fλ</text></svg>')
ART['8'] = ('<svg viewBox="0 0 150 84"><path d="M20 22V74H100V22" fill="none" stroke="currentColor" stroke-width="2"/>'
            '<path d="M20 30q10-6 20 0t20 0t20 0t20 0V74H20Z" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
            '<g stroke="currentColor" stroke-width="1.6" fill="none"><path d="M104 40h10m-4-3 4 3-4 3M104 54h22m-4-3 4 3-4 3M104 68h34m-4-3 4 3-4 3"/></g>'
            '<text x="34" y="58" font-size="11" fill="currentColor" font-family="JetBrains Mono">ρgh</text></svg>')

# ======================= part E =======================
import math

def zig(x1, x2, y, n=5, amp=7, c='a'):
    w = (x2 - x1)
    lead = w * 0.12
    pts = [(x1, y), (x1 + lead, y)]
    span = w - 2 * lead
    for i in range(n * 2):
        pts.append((x1 + lead + span * (i + 0.5) / (n * 2), y + (amp if i % 2 == 0 else -amp)))
    pts += [(x2 - lead, y), (x2, y)]
    return path('M' + 'L'.join(f'{x:.1f} {yy:.1f}' for x, yy in pts), c)

# ---------------- 9-1 ----------------
b = ''
b += rect(110, 50, 100, 54, 'ah', 4)
b += text(160, 72, 'part', 't') + text(160, 90, 'm, c, T', '')
b += arrow(20, 77, 108, 77, 'a') + text(62, 68, 'q in')
b += arrow(212, 77, 300, 77, 'a') + text(256, 68, 'q out')
b += arrow(160, 16, 160, 48, 'k') + text(160, 12, '', '') + text(168, 34, 'generated', 's', 'start')
b += text(160, 124, 'stored: m c dT/dt', 't')
b += text(160, 141, 'in − out + generated = stored', 's')
T['ph-9-1'] = svg(b, 150)

# ---------------- 9-2 ----------------
b = ''
b += rect(60, 100, 60, 30, 'kb') + rect(120, 100, 100, 30, 'ah')
b += text(90, 119, 'Al', '') + text(170, 119, 'polymer', '')
b += arrow(14, 115, 56, 115, 'a') + text(35, 108, 'q')
b += line(120, 30, 120, 135, 'g')
# temperature profile
b += path('M60 30L120 36', 'a') + path('M120 36L120 46', 'a') + path('M120 46L220 86', 'a')
b += text(60, 22, 'T₁', 's') + text(232, 90, 'T₂', 's', 'start')
b += text(90, 56, 'shallow', 's') + text(190, 52, 'steep', 's')
b += text(128, 26, 'contact jump', 's', 'start')
b += text(250, 119, 'ΔT ∝ R', 's', 'start')
T['ph-9-2'] = svg(b, 150)

# ---------------- 9-3 ----------------
b = ''
b += wall_h(30, 300, 112, 1)
b += text(32, 140, 'plate, Ts', 't', 'start')
# boundary layer edge
b += path(curve(lambda x: 112 - 5 - 36 * math.sqrt((x - 30) / 270), 30, 300, 40), 'g')
b += text(300, 54, 'δ edge', 's', 'end')
for x in (46, 70, 94):
    b += arrow(x, 36, x + 34, 36, 'k')
b += text(30, 30, 'U∞, T∞', '', 'start')
# velocity profile at x=210
x0 = 210
d = 36 * math.sqrt((x0 - 30) / 270)
for fr in (0.2, 0.45, 0.7, 0.95):
    y = 112 - fr * d
    L = 28 * math.sin(fr * math.pi / 2)
    b += arrow(x0, y, x0 + L, y, 'k', 5, 3)
b += line(x0, 112, x0, 112 - d, 'k')
# heat out
b += arrow(130, 108, 130, 78, 'a') + text(143, 92, 'q', 't', 'start')
b += text(165, 140, 'U = 0 at wall', 's', 'start')
T['ph-9-3'] = svg(b, 150)

# ---------------- 9-4 ----------------
b = ''
x0, y0 = 40, 128
b += axes(x0, y0, 290, 22, 'Ts', 'q')
sx = 200.0
conv = lambda x: y0 - 10 - 80 * (x - x0) / sx * 1.0
rad = lambda x: y0 - 8 - 0.186 * 80 * ((1 + 0.8 * (x - x0) / sx) ** 4 - 1) / 0.8 * 0.8 / 1.0
cx = lambda x: y0 - 80 * (x - x0) / sx
rx = lambda x: y0 - 80 * 0.186 * ((1 + 0.8 * (x - x0) / sx) ** 4 - 1) / 0.8
b += path(curve(cx, x0, 250, 30), 'k')
b += path(curve(rx, x0, 250, 40), 'a')
b += text(252, cx(250) - 4, 'convection', 's', 'start')
b += text(252, rx(250) + 2, '', 's')
b += text(150, 36, 'radiation ~ T⁴', 't', 'end')
b += line(x0 + sx * 0.25, y0, x0 + sx * 0.25, 40, 'g')
b += text(x0 + sx * 0.25, 143, 'crossover', 's')
b += text(200, 140, 'ε = 0.9, Ts and Tsur in K', 's', 'start')
T['ph-9-4'] = svg(b, 150)

# ---------------- 9-5 ----------------
b = ''
xs = (30, 110, 190, 270)
for x in xs:
    b += circ(x, 80, 3.5, 'af')
b += line(30, 80, 40, 80, 'a') + zig(40, 100, 80, 4, 7) + line(100, 80, 110, 80, 'a')
b += zig(120, 180, 80, 4, 7) + line(110, 80, 120, 80, 'a') + line(180, 80, 190, 80, 'a')
b += zig(200, 260, 80, 4, 16) + line(190, 80, 200, 80, 'a') + line(260, 80, 270, 80, 'a')
b += text(70, 58, 'R_jc', '') + text(150, 58, 'R_TIM', '') + text(230, 50, 'R_sink', 't')
for x, s in zip(xs, ('Tj', 'Tcase', 'Tpad', 'T∞')):
    b += text(x, 112, s, 's')
b += arrow(20, 26, 80, 26, 'k') + text(100, 30, 'q = 5 W', 's', 'start')
b += text(160, 140, 'ΔT = qR: biggest R, biggest drop', 's')
T['ph-9-5'] = svg(b, 150)

# ---------------- 9-6 ----------------
b = ''
x0, y0 = 50, 128
b += axes(x0, y0, 290, 20, 't', 'T')
Tinf, T0 = 112, 34
f = lambda x: Tinf + (T0 - Tinf) * math.exp(-(x - x0) / 70.0) * 1.0
f = lambda x: Tinf - (Tinf - T0) * math.exp(-(x - x0) / 70.0) if False else T0 + (Tinf - T0) * (1 - math.exp(-(x - x0) / 70.0))
# cooling curve from T0 (high) to Tinf (low): y larger = lower temperature
Ty0, Tyinf = 36, 112
g = lambda x: Tyinf - (Tyinf - Ty0) * math.exp(-(x - x0) / 70.0)
b += path(curve(g, x0, 280, 50), 'a')
b += line(x0, Tyinf, 285, Tyinf, 'g')
b += text(x0 - 4, Ty0 + 4, 'T₀', 's', 'end') + text(x0 - 4, Tyinf + 4, 'T∞', 's', 'end')
ty = Tyinf - (Tyinf - Ty0) * 0.368
b += line(x0, ty, x0 + 70, ty, 'g') + line(x0 + 70, ty, x0 + 70, y0, 'g')
b += circ(x0 + 70, ty, 3, 'af')
b += text(x0 + 70, 142, 'τ', 't')
b += text(x0 + 78, ty - 6, '37 % left at t = τ', 's', 'start')
T['ph-9-6'] = svg(b, 150)

# ---------------- 9-7 ----------------
b = ''
b += wall_v(60, 20, 70, -1)
b += rect(60, 34, 180, 16, 'ah')
for x in (110, 160, 210):
    b += arrow(x, 32, x, 12, 'k', 5, 3)
b += text(250, 46, 'fin', 't', 'start')
b += text(66, 28, '', '') 
b += text(200, 20, '', '')
b += text(262, 14, 'h, T∞', 's', 'end')
# profile
x0, y0 = 60, 150
b += line(60, 160, 240, 160, 'g')
mL = 1.2
prof = lambda x: 160 - 60 * math.cosh(mL * (1 - (x - 60) / 180.0)) / math.cosh(mL)
b += path(curve(prof, 60, 240, 40), 'a')
b += text(54, 104, 'θb', 's', 'end') + text(246, prof(240) + 4, 'tip', 's', 'start')
b += text(150, 86, 'excess temperature θ = T − T∞', 's')
b += text(54, 164, '0', 's', 'end')
T['ph-9-7'] = svg(b, 170)

# ---------------- icon ----------------
ART['9'] = ('<svg viewBox="0 0 150 84">'
 '<rect x="14" y="14" width="30" height="56" fill="currentColor" opacity=".15" stroke="currentColor" stroke-width="2"/>'
 '<g stroke="currentColor" stroke-width="2" fill="none"><path d="M44 24h24l4-6 6 12 6-12 6 12 4-6h28"/>'
 '<path d="M44 42h20l4-6 6 12 6-12 6 12 4-6h32"/><path d="M44 60h24l4-6 6 12 6-12 6 12 4-6h28"/></g>'
 '<path d="M132 18l10 6-10 6M136 36l10 6-10 6M132 54l10 6-10 6" stroke="currentColor" stroke-width="2" fill="none"/>'
 '<text x="16" y="44" font-size="11" fill="currentColor" font-family="JetBrains Mono">T</text></svg>')
