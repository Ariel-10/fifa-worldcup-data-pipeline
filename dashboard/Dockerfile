# base image — lightweight
FROM python:3.12-slim

# working directory
WORKDIR /app

# install deps — no cache = smaller image
RUN pip install --no-cache-dir \
    streamlit==1.45.1 \
    plotly==6.1.2 \
    pandas==2.2.3 \
    sqlalchemy==2.0.41 \
    psycopg2-binary==2.9.10

# copy source
COPY . .

# expose port
EXPOSE 8501

# startup command
CMD ["streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true"]