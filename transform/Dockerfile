# dbt requires python <=3.12
FROM python:3.12-slim

# git required by dbt internals
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# local: dbt-postgres / GCP equivalent: dbt-bigquery
RUN pip install dbt-core dbt-postgres -q

WORKDIR /usr/app/dbt