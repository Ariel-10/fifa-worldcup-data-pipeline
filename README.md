# ⚽ FIFA World Cup Data Pipeline

> An end-to-end data engineering project that ingests, processes and visualizes FIFA World Cup historical data (1930–2018).

![Pipeline](https://img.shields.io/badge/pipeline-end--to--end-blue)
![Docker](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3.14-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?logo=python&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-transform-FF694B?logo=dbt&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Problem Statement

Modern organizations receive data from multiple sources in different formats ut lack automated pipelines to reliably ingest, store, transform and visualize that data.

This project solves that problem by building a **complete data pipeline** that takes raw FIFA World Cup data and turns it into meaningful insights through an interactive dashboard — with full automation, reproducibility and clear documentation.

---

## 🎯 Objective

Build a production-ready, end-to-end data pipeline that:

- Ingests raw CSV data into a **Data Lake**
- Loads and structures data in a **Data Warehouse**
- Transforms data using **dbt**
- Visualizes insights in an interactive **Dashboard**
- Orchestrates all steps automatically with **Kestra**

---

## 🏗️ Architecture

```
Raw CSVs (Kaggle)
      ↓
  Python Script (ingestion)
      ↓
  MinIO — Data Lake (raw storage)
      ↓
  PostgreSQL — Data Warehouse (structured tables)
      ↓
  dbt — Transformations (clean models + metrics)
      ↓
  Streamlit — Dashboard (visualizations)
      ↑
  Kestra — Orchestration (automates all steps)
```

---

## 🛠️ Tech Stack

| Tool | Purpose | Why |
|---|---|---|
| **Python 3.14** | Data ingestion scripts | Flexible, industry standard |
| **uv** | Package & environment manager | Modern replacement for pip + venv |
| **Docker + Compose** | Containerization | Reproducible environment |
| **MinIO** | Data Lake (local GCS alternative) | S3-compatible, runs locally |
| **PostgreSQL 16** | Data Warehouse | Reliable, battle-tested |
| **dbt** | Data transformations | Industry standard for SQL transformations |
| **Kestra** | Pipeline orchestration | Modern, visual, 1000+ plugins |
| **Streamlit** | Dashboard | Fast to build, Python-native |
| **pgAdmin 4** | Database UI | Visual interface for PostgreSQL |

> 💡 This project is designed to be cloud-ready. MinIO → **Google Cloud Storage** and PostgreSQL → **BigQuery** with minimal configuration changes.

---

## 📊 Dataset

**Source:** [FIFA World Cup — Kaggle](https://www.kaggle.com/datasets/evangower/fifa-world-cup)

Two CSV files covering every World Cup from **Uruguay 1930** to **Russia 2018**:

| File | Rows | Description |
|---|---|---|
| `wcmatches.csv` | 900+ | Every match played — teams, scores, stages, dates, outcomes |
| `worldcups.csv` | 21 | Summary per tournament — winner, goals, attendance, teams |

> ⚠️ Data files are not included in this repository. Download them from Kaggle and place them in `data/raw/`.

---

## 📁 Project Structure

```
fifa-worldcup-data-pipeline/
│
├── data/
│   ├── raw/                 ← Downloaded CSVs go here (not tracked by git)
│   └── processed/           ← Transformed data
│
├── ingestion/
│   └── ingest.py            ← Uploads raw CSVs to MinIO Data Lake
├── warehouse/
│   └── load.py              ← Creates tables and loads data from MinIO into PostgreSQL
├── orchestration/           ← Kestra pipeline configuration
├── transform/               ← dbt models and transformations
├── dashboard/               ← Streamlit dashboard code
│
├── docker-compose.yaml      ← Spins up MinIO + PostgreSQL + Kestra + pgAdmin
├── pyproject.toml           ← Python dependencies managed with uv
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🚀 How to Run

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [Python 3.14+](https://www.python.org/downloads/) installed
- [uv](https://docs.astral.sh/uv/) installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Ariel-10/fifa-worldcup-data-pipeline.git
cd fifa-worldcup-data-pipeline

# 2. Install dependencies
uv sync

# 3. Download the dataset from Kaggle and place CSVs in data/raw/

# 4. Start all services
docker compose up

# 5. Run ingestion — uploads CSVs to MinIO Data Lake
uv run ingestion/ingest.py

# 6. Run warehouse load — creates tables and loads data into PostgreSQL
uv run warehouse/load.py
```

After running, verify the data at:
- **MinIO UI:** http://localhost:9001 — user: `root` / password: `rootroot`
- **Kestra UI:** http://localhost:8080
- **pgAdmin:** http://localhost:5050 — email: `admin@admin.com` / password: `root`

---

## 📈 Dashboard Previews

> Screenshots will be added once the dashboard is built.

---

## 🗺️ Roadmap

- [x] Project structure defined
- [x] Dataset selected
- [x] Docker Compose with MinIO + PostgreSQL + Kestra + pgAdmin
- [x] Python ingestion script — CSVs uploaded to MinIO
- [x] PostgreSQL warehouse tables — `raw_worldcups` and `raw_matches` loaded
- [ ] dbt transformation models
- [ ] Streamlit dashboard
- [ ] Full orchestration with Kestra
- [ ] README final documentation

---

## 👤 Author

**Ariel Ortega**
Data Engineering Zoomcamp 2026 — Personal Project

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
