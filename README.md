# Store Sales Analysis

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)](#)

A comprehensive Python project for analyzing store sales data to track performance, calculate profits, and generate actionable insights. This system integrates a billing module, inventory management, and advanced analytics to streamline business operations and produce reproducible reports and dashboards.

---

Table of Contents
- [Why this project](#why-this-project)
- [Key features](#key-features)
- [Repository layout](#repository-layout)
- [Quick start](#quick-start)
- [Data format and expectations](#data-format-and-expectations)
- [Configuration](#configuration)
- [How to run](#how-to-run)
  - [Command-line scripts](#command-line-scripts)
  - [Programmatic usage (Python API)](#programmatic-usage-python-api)
  - [Notebooks & exploration](#notebooks--exploration)
- [Outputs](#outputs)
- [Testing & CI](#testing--ci)
- [Development notes & architecture](#development-notes--architecture)
- [Contributing](#contributing)
- [License & contact](#license--contact)
- [Troubleshooting](#troubleshooting)

Why this project
----------------
Store Sales Analysis provides a structured, reproducible pipeline for taking raw sales and inventory data and transforming it into:
- KPIs (revenue, gross profit, margin, units sold)
- Store- and product-level performance metrics
- Inventory turn analysis and restock recommendations
- Billing reconciliation and anomaly detection
- Visual reports and exportable CSV / Excel summaries

It is intended for small-to-medium retail operations, analysts, and data engineers who need a straightforward, customizable solution.

Key features
------------
- Modular design: billing, inventory, analytics modules separated for clarity
- Data validation and cleaning utilities
- Config-driven pipelines (YAML/.env)
- CLI scripts and Python API for automation
- Jupyter notebooks for EDA and reporting
- Unit tests and CI-friendly structure

Repository layout
-----------------
A recommended project layout (your actual repo may vary slightly):

- README.md
- LICENSE
- requirements.txt
- pyproject.toml (optional)
- config/
  - config.example.yaml
- data/
  - raw/              # place raw CSV/Parquet files here
  - processed/
  - sample_dataset.csv
- src/
  - store_sales_analysis/
    - __init__.py
    - cli.py
    - pipeline.py
    - billing/
      - __init__.py
      - reconcile.py
      - billing_utils.py
    - inventory/
      - __init__.py
      - stock.py
      - reorder.py
    - analytics/
      - __init__.py
      - kpis.py
      - cohort_analysis.py
    - io/
      - readers.py
      - writers.py
    - utils/
      - validation.py
      - logging.py
- notebooks/           # EDA and demo notebooks
- scripts/             # helper scripts (e.g. run_all.sh)
- tests/               # pytest tests
- docs/                # optional documentation

Quick start
-----------
Prerequisites:
- Python 3.8+
- Git

1. Clone the repo
   - git clone https://github.com/DishiGpt/store-sales-analysis.git
   - cd store-sales-analysis

2. Create and activate a virtual environment
   - python -m venv venv
   - source venv/bin/activate   # Linux / macOS
   - venv\Scripts\activate      # Windows

3. Install dependencies
   - pip install -r requirements.txt
   Or using poetry:
   - poetry install

4. Copy and edit configuration
   - cp config/config.example.yaml config/config.yaml
   - Edit paths / options to match your environment.

Data format and expectations
----------------------------
The pipeline expects tabular sales data (CSV, Parquet) with (at minimum) the following columns:

- date (YYYY-MM-DD or ISO datetime)
- store_id
- product_id
- quantity
- unit_price
- cost (optional but recommended)
- discount (optional)
- tax (optional)
- transaction_id (for billing/reconciliation)
- payment_type (optional)

Recommended sample header:
date,store_id,product_id,transaction_id,quantity,unit_price,cost,discount,tax,payment_type

If you have inventory snapshots, include:
- snapshot_date, store_id, product_id, stock_level

Configuration
-------------
Main configuration is stored in YAML (config/config.example.yaml). Example keys:
- data:
  - raw_dir: data/raw
  - processed_dir: data/processed
- reports:
  - output_dir: reports
- analytics:
  - kpi_window_days: 30
  - profit_margin_threshold: 0.1
- inventory:
  - reorder_point_days: 14
- logging:
  - level: INFO

How to run
----------

Command-line scripts
- Run full pipeline (example):
  - python -m store_sales_analysis.cli run --config config/config.yaml
- Run only analytics:
  - python -m store_sales_analysis.cli analytics --data data/processed/sales.parquet --out reports/kpis.csv
- Reconcile billing:
  - python -m store_sales_analysis.cli billing --transactions data/raw/transactions.csv --payments data/raw/payments.csv --out reports/reconciliation.xlsx

Programmatic usage (Python API)
- Import core functions from package:

```python
from store_sales_analysis.pipeline import run_full_analysis

run_full_analysis(
    raw_data_dir="data/raw",
    processed_dir="data/processed",
    reports_dir="reports",
    config_path="config/config.yaml"
)
```

- Compute KPIs for a DataFrame:

```python
from store_sales_analysis.analytics.kpis import compute_kpis
kpi_df = compute_kpis(sales_df, group_by=["store_id", "product_id"])
```

Notebooks & exploration
-----------------------
Notebooks in /notebooks are intended for EDA and interactive reporting. Launch with:

- jupyter lab
- or open specific notebook: notebooks/edA_sales_analysis.ipynb

Outputs
-------
Typical outputs the pipeline produces:
- reports/kpis_YYYYMMDD.csv
- reports/profit_summary.xlsx
- reports/inventory_reorder_list.csv
- visualizations: reports/figures/sales_by_store.png
- dashboards (if integrated): a generated HTML report or JSON used by a front-end

Testing & CI
------------
- Unit tests in /tests use pytest.
- Run tests locally:
  - pytest -q
- Suggested CI:
  - GitHub Actions workflow that runs linting, unit tests, and optionally builds docs.

Development notes & architecture
-------------------------------
- Modular design isolates billing, inventory, analytics responsibilities.
- Data ingestion -> validation -> transformation -> feature engineering -> reporting.
- Use vectorized pandas operations (or Dask for larger-than-memory).
- Logging and structured exceptions are centralized in src/store_sales_analysis/utils.

Example high-level architecture (ASCII):

Raw data -> Readers -> Cleaner/Validator -> Feature Engineering -> Analytics (KPIs, Cohorts) -> Reports / Dashboards
                         \-> Billing reconciliation -> Alerts

Contributing
------------
Contributions welcome — please follow these steps:
1. Fork the repository
2. Create a branch: git checkout -b feat/your-feature
3. Write tests for new functionality
4. Follow code style (black, flake8)
5. Open a pull request with a clear description of changes

Please include an issue for larger features before implementing.

License & contact
-----------------
This repository is provided under the MIT license (see LICENSE). If you want a different license, update LICENSE accordingly.

For questions or help, open an issue or contact maintainer: DishiGpt (GitHub: @DishiGpt).

Troubleshooting
---------------
- Common issues:
  - FileNotFoundError: check paths in config.yaml and ensure data files are in data/raw
  - Pandas parsing error: check delimiter and encoding of CSVs (utf-8 recommended)
  - Memory errors: downsample data or use chunked readers / Dask

- Debug tips:
  - Increase logging to DEBUG in config for detailed traces
  - Use smaller sample datasets in data/raw/sample_dataset.csv to iterate faster

Acknowledgements & next steps
----------------------------
- This project is a solid base for building reporting pipelines, retail dashboards, or automated restock systems.
- Next improvements to consider: real-time ingestion, database-backed storage (Postgres), or a web dashboard (Streamlit/Plotly Dash).

Thank you for using Store Sales Analysis — contributions, issues, and suggestions are encouraged!
