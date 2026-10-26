# 03-config (kepler.gl) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# REQUIRED SETUP: wave11 venv must carry setuptools==80.9.0 (see 01).
# Saving a map configuration and reusing it in a second map.
# The round-trip assertion covers a key WE set (mapState latitude),
# never library internals. Synthetic points ONLY.
# Writes config_map.html + config.json; prints a summary.
import json

import pandas as pd
from keplergl import KeplerGl

ROWS = [
    {"lat": 10.010, "lon": 20.010, "value": 3},
    {"lat": 10.020, "lon": 20.030, "value": 7},
    {"lat": 10.030, "lon": 20.010, "value": 5},
]

CONFIG = {
    "version": "v1",
    "config": {
        "mapState": {"latitude": 10.025, "longitude": 20.020, "zoom": 12},
        "mapStyle": {},
        "visState": {"layers": []},
    },
}

df = pd.DataFrame(ROWS)
kmap = KeplerGl(height=500, config=CONFIG)
kmap.add_data(data=df, name="synthetic_points")

# Persist the configuration we set, then reuse it verbatim.
with open("config.json", "w", encoding="utf-8") as fh:
    json.dump(CONFIG, fh, indent=2)
with open("config.json", encoding="utf-8") as fh:
    reloaded = json.load(fh)
assert reloaded["config"]["mapState"]["latitude"] == 10.025

kmap2 = KeplerGl(height=500, config=reloaded)
kmap2.add_data(data=df, name="synthetic_points")
kmap2.save_to_html(file_name="config_map.html")
html = open("config_map.html", encoding="utf-8").read()
assert len(html) > 0
print(f"Config latitude round-trip: {reloaded['config']['mapState']['latitude']}, points: {len(df)}")
