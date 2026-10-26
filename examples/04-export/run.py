# 04-export (kepler.gl) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# REQUIRED SETUP: wave11 venv must carry setuptools==80.9.0 (see 01).
# Exporting a standalone HTML map: one file, no server required to open
# it. The saved file embeds the kepler.gl bundle, so it is large by
# construction — the assertion is non-empty + mentions kepler, not an
# exact byte count (see README). Synthetic points ONLY.
# Writes standalone_map.html; prints a summary.
import pandas as pd
from keplergl import KeplerGl

ROWS = [
    {"lat": 10.010, "lon": 20.010, "value": 3},
    {"lat": 10.020, "lon": 20.030, "value": 7},
    {"lat": 10.030, "lon": 20.010, "value": 5},
    {"lat": 10.040, "lon": 20.040, "value": 9},
]

df = pd.DataFrame(ROWS)
kmap = KeplerGl(height=500)
kmap.add_data(data=df, name="synthetic_points")

out = "standalone_map.html"
kmap.save_to_html(file_name=out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "kepler" in html.lower()
print(f"Standalone file: {out}, bytes: {len(html)}, points: {len(df)}")
