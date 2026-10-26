# 03 — Config

Saving and reusing map configurations: a config dict is written to
`config.json`, reloaded verbatim, and handed to a second map. The
round-trip assertion covers the latitude value this pattern set.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv). The wave11 venv must carry `setuptools==80.9.0`
(see pattern 01).

## Expected output

```text
Config latitude round-trip: 10.025, points: 3
```

The assertions that must hold are: the reloaded config's mapState
latitude is 10.025, the point count is 3, and the saved HTML is
non-empty.

## Failure behavior

- A different reloaded latitude — `config.json` was edited between
  write and read; restore `CONFIG` from `run.py`.
- The second map ignoring the config — whether kepler.gl applies a
  passed config verbatim or merges defaults is a validation item;
  the round-trip of our own file is asserted, not the renderer's
  merge behavior.
- `ModuleNotFoundError: pkg_resources` — setuptools pin missing; see
  pattern 01.

## Versions and evidence

- Tool: kepler.gl 0.3.7 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked) with the setuptools 80.9.0 pin.
- Evidence level: design-only (gate 1 target). The config dict and
  round-trip value were derived during drafting; config application
  behavior against fleet kepler.gl is **to confirm at validation**.
