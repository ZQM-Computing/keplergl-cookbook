# 02 — Trip layers

Trip and arc-style movement data: two synthetic trips, four timestamped
positions each, plus a trip-layer config dict. Timestamps are synthetic
ordinals (0–3), not real datetimes.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv). The wave11 venv must carry `setuptools==80.9.0`
(see pattern 01).

## Expected output

```text
Trips: 2, rows: 8, layer type: trip
```

Derivation: 2 trip ids × 4 timestamps = 8 rows. The assertions that
must hold are: 8 rows, 2 distinct trips, the config's first layer
type is "trip", and the saved HTML is non-empty.

## Failure behavior

- A different trip or row count — the `ROWS` table was edited;
  restore it from `run.py`.
- The trip layer not rendering in the saved map — the config schema
  for trip layers is the open validation item below, not proof the
  data is wrong: the data table and config keys are this pattern's
  own artifacts and are asserted; how kepler.gl renders them is
  **to confirm at validation**, field by field.
- `ModuleNotFoundError: pkg_resources` — setuptools pin missing; see
  pattern 01.

## Versions and evidence

- Tool: kepler.gl 0.3.7 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked) with the setuptools 80.9.0 pin.
- Evidence level: design-only (gate 1 target). Trip/row counts and
  the config dict were derived during drafting; the exact trip-layer
  schema rendering against fleet kepler.gl is **to confirm at
  validation**.
