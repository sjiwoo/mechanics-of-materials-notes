"""Render the interviewer figures for the Tactile Sensing examples (figures/tactile/ex/ex<ch>-<n>.png).

Run from the repo root:  python tools/tactile_ex_figs.py     (needs rsvg-convert)
Each worked example in examples-tactile.js reuses one of the section figures from tools/tactile_figs.py as its
schematic; FIG maps example id -> section figure key. The site styles those SVGs with CSS, so a fixed light
palette is embedded here to make them stand-alone images (also sent to Gemini as the problem figure).
"""
import pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tactile_figs

FIG = {'1.1': 't-1-1', '1.2': 't-1-3', '2.1': 't-2-2', '2.2': 't-2-1', '3.1': 't-3-2', '3.2': 't-3-4',
       '4.1': 't-4-1', '4.2': 't-4-4', '5.1': 't-5-1', '5.2': 't-5-2', '5.3': 't-5-3', '6.1': 't-6-2',
       '6.2': 't-6-3', '7.1': 't-7-1', '7.2': 't-7-2', '8.1': 't-8-3', '8.2': 't-8-4', '9.1': 't-9-2',
       '9.2': 't-9-3', '10.1': 't-10-3', '10.2': 't-10-3', '10.3': 't-10-4', '11.1': 't-11-1', '11.2': 't-11-4'}

ACC, INK, INK2, INK3 = '#0369a1', '#0f172a', '#475569', '#64748b'
STYLE = f"""<style>
.a{{stroke:{ACC};fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}}
.af{{fill:{ACC}}}
.ah{{fill:{ACC};fill-opacity:.16;stroke:{ACC};stroke-width:1.6;stroke-linejoin:round}}
.kb{{fill:{INK2};fill-opacity:.12;stroke:{INK2};stroke-width:1.3}}
.k{{stroke:{INK2};fill:none;stroke-width:1.4;stroke-linecap:round}}
.kf{{fill:{INK2}}}
.g{{stroke:{INK3};fill:none;stroke-width:1.2;stroke-dasharray:4 3}}
.zb{{fill:none;stroke:{ACC};stroke-opacity:.24;stroke-linejoin:round}}
.zfill,.zr{{fill:{ACC};fill-opacity:.22;stroke:none}}
.kfr{{fill:#fff;stroke:{INK};stroke-width:1.3}}
text{{fill:{INK};font:500 12px Inter,Arial,Helvetica,sans-serif}}
text.t{{fill:{ACC};font-weight:600}}
text.s{{fill:{INK3};font:500 10.5px Inter,Arial,Helvetica,sans-serif}}
</style>"""


def build():
    root = pathlib.Path(__file__).resolve().parent.parent
    out = root / 'figures' / 'tactile' / 'ex'
    out.mkdir(parents=True, exist_ok=True)
    for ex, key in FIG.items():
        svg = tactile_figs.T[key]
        head, body = svg.split('>', 1)
        vb = head.split('viewBox="')[1].split('"')[0].split()
        svg = (f'{head} xmlns="http://www.w3.org/2000/svg" width="{vb[2]}" height="{vb[3]}" color="{ACC}">'
               f'{STYLE}<rect width="100%" height="100%" fill="#fff"/>{body}')
        png = out / f"ex{ex.replace('.', '-')}.png"
        subprocess.run(['rsvg-convert', '-z', '3', '-o', str(png)], input=svg.encode('utf-8'), check=True)
    print(f'{len(FIG)} example figures written to {out}')


if __name__ == '__main__':
    build()
