# 02-trip-layers (kepler.gl) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# REQUIRED SETUP: wave11 venv must carry setuptools==80.9.0 (see 01).
# Two synthetic trips (timestamped coordinate sequences) + a trip-layer
# config dict. The config dict is THIS pattern's artifact: the assertions
# cover row counts and the config keys we set, never library internals.
# The exact trip-layer schema rendering is a validation item (see README).
# Synthetic trips ONLY. Writes trip_layers.html; prints a summary.
import pandas as pd
from keplergl import KeplerGl

# Two trips x four timestamps = 8 rows. Timestamps are synthetic
# ordinals (0..3), not real datetimes, so no clock or timezone claim.
ROWS = [
    {"trip_id": "T1", "t": 0, "lat": 10.010, "lon": 20.010},
    {"trip_id": "T1", "t": 1, "lat": 10.020, "lon": 20.020},
    {"trip_id": "T1", "t": 2, "lat": 10.030, "lon": 20.030},
    {"trip_id": "T1", "t": 3, "lat": 10.040, "lon": 20.040},
    {"trip_id": "T2", "t": 0, "lat": 10.050, "lon": 20.010},
    {"trip_id": "T2", "t": 1, "lat": 10.040, "lon": 20.020},
    {"trip_id": "T2", "t": 2, "lat": 10.030, "lon": 20.030},
    {"trip_id": "T2", "t": 3, "lat": 10.020, "lon": 20.040},
]

df = pd.DataFrame(ROWS)
assert len(df) == 8 and df["trip_id"].nunique() == 2

CONFIG = {
    "version": "v1",
    "config": {
        "mapState": {"latitude": 10.030, "longitude": 20.025, "zoom": 13},
        "mapStyle": {},
        "visState": {
            "layers": [
                {
                    "id": "synthetic-trips",
                    "type": "trip",
                    "config": {
                        "dataId": "synthetic_trips",
                        "label": "Synthetic trips",
                        "columns": {"lat": "lat", "lng": "lon"},
                    },
                }
            ]
        },
    },
}

kmap = KeplerGl(height=500, config=CONFIG)
kmap.add_data(data=df, name="synthetic_trips")

out = "trip_layers.html"
kmap.save_to_html(file_name=out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0
assert CONFIG["config"]["visState"]["layers"][0]["type"] == "trip"
print(f"Trips: {df['trip_id'].nunique()}, rows: {len(df)}, layer type: trip")
