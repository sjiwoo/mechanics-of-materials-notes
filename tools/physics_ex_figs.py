"""Render the interviewer figures for the Physics for Mechanics problems (figures/physics/ex/ex<ch>-<n>.png).

Run from the repo root:  python tools/physics_ex_figs.py     (needs rsvg-convert)
Each problem in examples-ph.js reuses one section figure from tools/physics_figs.py; FIG maps problem id -> figure key.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import physics_figs
from tactile_ex_figs import render

FIG = { "1.1": "ph-1-1", "1.2": "ph-1-3", "1.3": "ph-1-4", "2.1": "ph-2-2", "2.2": "ph-2-3", "2.3": "ph-2-4", "3.1": "ph-3-4", "3.2": "ph-3-2", "3.3": "ph-3-3", "4.1": "ph-4-3", "4.2": "ph-4-4", "4.3": "ph-4-5", "5.1": "ph-5-1", "5.2": "ph-5-2", "5.3": "ph-5-3", "6.1": "ph-6-1", "6.2": "ph-6-4", "6.3": "ph-6-5", "7.1": "ph-7-2", "7.2": "ph-7-3", "7.3": "ph-7-4", "8.1": "ph-8-1", "8.2": "ph-8-3", "8.3": "ph-8-5", "9.1": "ph-9-2", "9.2": "ph-9-5", "9.3": "ph-9-6" }

if __name__ == '__main__':
    render(physics_figs.T, FIG, pathlib.Path(__file__).resolve().parent.parent / 'figures' / 'physics' / 'ex')
