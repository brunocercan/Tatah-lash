from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="my-secret-pw",
        database="sys"
    )

@app.route("/consulta/data-agendamentos", methods=["GET"])
def consulta_agendamentos():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT NOME_CLIENTE, TELEFONE_CLIENTE, DATA_AGENDAMENTO FROM tata_lash
    """

    cursor.execute(query)
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)