# 04 — Export

Exporting a standalone HTML map: `save_to_html` writes one file that
opens in a browser with no server. Four synthetic points prove the
content survived the round trip.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv). The wave11 venv must carry `setuptools==80.9.0`
(see pattern 01).

## Expected output

```text
Standalone file: standalone_map.html, bytes: <positive integer>, points: 4
```

The byte count varies with the kepler.gl version because the saved
file embeds the kepler.gl bundle — it is large by construction. The
assertions that must hold are: the file exists, is non-empty, and
mentions kepler; the point count is 4.

## Failure behavior

- An unexpectedly small file (a few KB) — the bundle did not embed;
  check the `save_to_html` call before assuming a library defect.
- A missing kepler mention — the save step wrote something else;
  restore `run.py`.
- `ModuleNotFoundError: pkg_resources` — setuptools pin missing; see
  pattern 01.

## Versions and evidence

- Tool: kepler.gl 0.3.7 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked) with the setuptools 80.9.0 pin.
- Evidence level: design-only (gate 1 target). Point count and the
  bundle-size note were derived during drafting; the actual exported
  byte count against fleet kepler.gl is **to confirm at validation**.
