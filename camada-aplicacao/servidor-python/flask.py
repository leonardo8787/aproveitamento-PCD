from flask import Flask, send_from_directory, abort

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('servidor-python')
def serve_file(filename):
    try:
        return send_from_directory('.', filename)
    except Exception as e:
        abort(404, description="Arquivo não encontrado")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
