# kepler.gl Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **kepler.gl cookbook** — large-scale geospatial visualization in notebooks and apps. Installed in wave-11 (Node-1 wave11-venv, Wally spot-checked 2026-10-25). First pattern pass written below (design-only, gate 1 target). It is intended for Analysts who visualize millions of points and trips interactively. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** kepler.gl patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Analysts who visualize millions of points and trips interactively.

## Prerequisites

- kepler.gl 0.3.7 in Node-1's wave11-venv (`C:\geo-tools\wave11-venv`, Python 3.12.10) — invoke the venv Python by full path, never bare `python` (hermes venv)
- **setuptools==80.9.0 REQUIRED in the venv** (venv setuptools 84.2.1 dropped `pkg_resources` and kepler.gl fails to import without it — wave-11A proven fix)
- A point or trip dataset (synthetic data is used throughout)

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-first-map](examples/01-first-map) | A first kepler.gl map from a DataFrame | Written (design-only) |
| 02 | [examples/02-trip-layers](examples/02-trip-layers) | Trip and arc layers for movement data | Written (design-only) |
| 03 | [examples/03-config](examples/03-config) | Saving and reusing map configurations | Written (design-only) |
| 04 | [examples/04-export](examples/04-export) | Exporting standalone HTML maps | Written (design-only) |

## Repository layout

```text
keplergl-cookbook/
├── examples/
│   ├── 01-first-map/
│   ├── 02-trip-layers/
│   ├── 03-config/
│   └── 04-export/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (design-only, gate 1 target)
- Validation pass: run each pattern against the fleet environment and promote to gate 3

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [folium-cookbook](https://github.com/ZQM-Computing/folium-cookbook) — Interactive Leaflet maps from Python
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [plotly-cookbook](https://github.com/ZQM-Computing/plotly-cookbook) — Interactive charts and geo charts from Python
