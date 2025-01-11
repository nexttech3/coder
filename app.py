from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="dashboard_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM data_table;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)