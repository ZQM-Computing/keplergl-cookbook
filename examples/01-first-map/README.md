# 01 — First map

A first kepler.gl map from a DataFrame: eight synthetic points with a
value column, saved as standalone HTML.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

**Setup prerequisite (fleet fact, do not skip):** the wave11 venv must
carry `setuptools==80.9.0`. Venv setuptools 84.2.1 dropped
`pkg_resources` and kepler.gl fails to import without it — wave-11A
proved the pin fixes it. If the import fails with
`ModuleNotFoundError: pkg_resources`, the pin is missing, not the
library.

## Expected output

```text
Points: 8, value sum: 44
```

Derivation: values 3 + 7 + 5 + 9 + 4 + 6 + 8 + 2 = 44. The assertions
that must hold are: the DataFrame has 8 rows, the value sum is 44,
and the saved HTML is non-empty and mentions kepler.

## Failure behavior

- `ModuleNotFoundError: pkg_resources` — setuptools pin missing; run
  `pip install setuptools==80.9.0` in the wave11 venv and retry.
- A different point count or sum — the `ROWS` table was edited;
  restore it from `run.py`, do not adjust the assertions.
- Empty HTML — the save step failed; check the `save_to_html` call
  before assuming a library defect.

## Versions and evidence

- Tool: kepler.gl 0.3.7 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked) with the setuptools 80.9.0 pin.
- Evidence level: design-only (gate 1 target). Row count and value
  sum were derived during drafting; running them against the fleet
  kepler.gl environment is **to confirm at validation**.
