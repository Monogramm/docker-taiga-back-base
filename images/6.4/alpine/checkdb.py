import os, sys, psycopg2

DB_NAME = os.getenv('TAIGA_DB_NAME', os.getenv('POSTGRES_DB'))
DB_HOST = os.getenv('TAIGA_DB_HOST', os.getenv('POSTGRES_HOST'))
DB_PORT = os.getenv('TAIGA_DB_PORT', os.getenv('POSTGRES_PORT','5432'))
DB_USER = os.getenv('TAIGA_DB_USER', os.getenv('POSTGRES_USER'))
DB_PASS = os.getenv('TAIGA_DB_PASSWORD', os.getenv('POSTGRES_PASSWORD'))

safe_conn_string = (
    "dbname='" + DB_NAME +
    "' user='" + DB_USER +
    "' host='" + DB_HOST +
    "' port='" + DB_PORT +
    "' password='******'")

conn_string = (
    "dbname='" + DB_NAME +
    "' user='" + DB_USER +
    "' host='" + DB_HOST +
    "' port='" + DB_PORT +
    "' password='" + DB_PASS + "'")
print("Connecting to database:\n" + safe_conn_string)
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

cur.execute("select * from information_schema.tables where table_name=%s", ('django_migrations',))
exists = bool(cur.rowcount)

if exists is False:
    print("Database does not appear to be setup.")
    sys.exit(2)
