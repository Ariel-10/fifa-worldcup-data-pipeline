# ⚽ FIFA World Cup Data Pipeline

> An end-to-end data engineering project that ingests, processes and visualizes FIFA World Cup historical data (1930–2018).

![Pipeline](https://img.shields.io/badge/pipeline-end--to--end-blue)
![Docker](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3.11-3776AB?logo=python&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-transform-FF694B?logo=dbt&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Problem Statement

Modern organizations receive data from multiple sources in different formats, but lack automated pipelines to reliably ingest, store, transform and visualize that data.

This project solves that problem by building a **complete data pipeline** that takes raw FIFA World Cup data and turns it into meaningful insights through an interactive dashboard with full automation, reproducibility and clear documentation.

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
| **Python** | Data ingestion scripts | Flexible, industry standard |
| **Docker + Compose** | Containerization | Reproducible environment |
| **MinIO** | Data Lake (local GCS alternative) | S3-compatible, runs locally |
| **PostgreSQL** | Data Warehouse | Reliable |
| **dbt** | Data transformations | Industry standard for SQL transformations |
| **Kestra** | Pipeline orchestration | Modern, simple, visual |
| **Streamlit** | Dashboard | Fast to build, Python-native |

> 💡 This project is designed to be cloud-ready. MinIO can be replaced with **Google Cloud Storage** and PostgreSQL with **BigQuery** with minimal configuration changes.

---

## 📊 Dataset

**Source:** [FIFA World Cup — Kaggle](https://www.kaggle.com/datasets/evangower/fifa-world-cup)

Two CSV files covering every World Cup from **Uruguay 1930** to **Russia 2018**:

| File | Description |
|---|---|
| `wcmatches.csv` | Every match played — teams, scores, stages, dates, outcomes |
| `worldcups.csv` | Summary per tournament — winner, goals, attendance, teams |

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
├── ingestion/               ← Python scripts to load data into MinIO
├── orchestration/           ← Kestra pipeline configuration
├── warehouse/               ← SQL scripts to create PostgreSQL tables
├── transform/               ← dbt models and transformations
├── dashboard/               ← Streamlit dashboard code
│
├── docker-compose.yaml      ← Spins up all services
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🚀 How to Run

> Instructions will be added as each module is built.

### Prerequisites
- Docker Desktop installed
- Python 3.11+
- dbt Core installed

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/Ariel-10/fifa-worldcup-data-pipeline.git
cd fifa-worldcup-data-pipeline

# 2. Download the dataset from Kaggle and place CSVs in data/raw/

# 3. Start all services
docker compose up

# 4. Run ingestion
# (instructions coming soon)
```

---

## 📈 Dashboard Previews

> Screenshots will be added once the dashboard is built.

---

## 🗺️ Roadmap

- [x] Project structure defined
- [x] Dataset selected
- [x] Docker Compose with MinIO + PostgreSQL + Kestra
- [ ] Python ingestion script
- [ ] PostgreSQL warehouse tables
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
