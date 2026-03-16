import os
import psycopg2
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Obtener configuración de la base de datos desde variables de entorno
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'postgres')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

# Crear tabla si no existe
with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS notas (
                id SERIAL PRIMARY KEY,
                texto TEXT NOT NULL
            )
        ''')
    conn.commit()

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Mis Notas</title></head>
<body>
    <h1>Mis Notas</h1>
    <form method="POST">
        <input type="text" name="nota" placeholder="Escribe una nota" size="50">
        <button type="submit">Agregar</button>
    </form>
    <ul>
    {% for nota in notas %}
        <li>{{ nota }}</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nota = request.form['nota']
        if nota:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO notas (texto) VALUES (%s)', (nota,))
                conn.commit()
        return redirect('/')
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT texto FROM notas ORDER BY id DESC')
            notas = [row[0] for row in cur.fetchall()]
    return render_template_string(HTML_TEMPLATE, notas=notas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

