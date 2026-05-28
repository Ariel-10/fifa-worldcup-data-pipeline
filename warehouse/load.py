import io
import pandas as pd
import psycopg2
from minio import Minio

# Connection to MinIO and PostgreSQL
client = Minio(
    "localhost:9000",
    access_key="root",
    secret_key="rootroot",
    secure=False,
)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="fifa_dw",
    user="root",
    password="root",
)
cur = conn.cursor()

# Create tables if they don't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_worldcups (
        year         INTEGER PRIMARY KEY,  -- Tournament year (unique identifier)
        host         TEXT,                 -- Host country
        winner       TEXT,                 -- Champion team
        second       TEXT,                 -- Runner-up
        third        TEXT,                 -- Third place
        fourth       TEXT,                 -- Fourth place
        goals_scored INTEGER,              -- Total goals in the tournament
        teams        INTEGER,              -- Number of qualified teams
        games        INTEGER,              -- Total matches played
        attendance   INTEGER               -- Total attendance across all matches
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_matches (
        year           INTEGER,  -- Tournament year (foreign key to raw_worldcups)
        country        TEXT,     -- Host country of the match
        city           TEXT,     -- City where the match was played
        stage          TEXT,     -- Tournament stage (Group, QF, SF, Final, etc.)
        home_team      TEXT,     -- Home team name
        away_team      TEXT,     -- Away team name
        home_score     INTEGER,  -- Goals scored by home team
        away_score     INTEGER,  -- Goals scored by away team
        outcome        TEXT,     -- Match result (H = home win, A = away win, D = draw)
        win_conditions TEXT,     -- Extra info if decided by AET or penalties
        winning_team   TEXT,     -- Name of the winning team (null if draw)
        losing_team    TEXT,     -- Name of the losing team (null if draw)
        date           TEXT,     -- Match date
        month          TEXT,     -- Month of the match
        dayofweek      TEXT      -- Day of the week
    );
""")

conn.commit()

# Download CSV from MinIO and load in PostgreSQL
def load_csv_from_minio(bucket, object_name):
    response = client.get_object(bucket, object_name)
    return pd.read_csv(io.BytesIO(response.read()))

# Load worldcups data
df_wc = load_csv_from_minio("fifa-worldcup", "raw/worldcups.csv")
for _, row in df_wc.iterrows():
    cur.execute("""
        INSERT INTO raw_worldcups VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (year) DO NOTHING;  -- Skip if tournament year already exists
    """, tuple(row))

# Load matches data
df_m = load_csv_from_minio("fifa-worldcup", "raw/wcmatches.csv")
for _, row in df_m.iterrows():
    cur.execute("""
        INSERT INTO raw_matches VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """, tuple(row))

conn.commit()
cur.close()
conn.close()
print("Data successfully loaded in PostgreSQL")