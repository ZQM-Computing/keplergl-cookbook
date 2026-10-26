# 01-first-map (kepler.gl) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# REQUIRED SETUP (fleet fact): the wave11 venv must carry
# setuptools==80.9.0 — venv setuptools 84.2.1 dropped pkg_resources and
# kepler.gl fails to import without it (wave-11A, proven fix).
# Synthetic points ONLY (a made-up grid, not a real place).
# Writes first_map.html in this directory; prints a summary.
import pandas as pd
from keplergl import KeplerGl

ROWS = [
    {"lat": 10.010, "lon": 20.010, "value": 3},
    {"lat": 10.020, "lon": 20.030, "value": 7},
    {"lat": 10.030, "lon": 20.010, "value": 5},
    {"lat": 10.040, "lon": 20.040, "value": 9},
    {"lat": 10.050, "lon": 20.020, "value": 4},
    {"lat": 10.015, "lon": 20.035, "value": 6},
    {"lat": 10.035, "lon": 20.015, "value": 8},
    {"lat": 10.045, "lon": 20.025, "value": 2},
]

df = pd.DataFrame(ROWS)
assert len(df) == 8 and df["value"].sum() == 44

kmap = KeplerGl(height=500)
kmap.add_data(data=df, name="synthetic_points")

out = "first_map.html"
kmap.save_to_html(file_name=out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "kepler" in html.lower()
print(f"Points: {len(df)}, value sum: {int(df['value'].sum())}")
