from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Incrementar a contagem de acessos
    try:
        with open('acessos.txt', 'r') as arquivo:
            contador = int(arquivo.read())
    except (ValueError, FileNotFoundError):
        # Caso o arquivo esteja vazio ou não seja encontrado,
        # inicialize o contador com zero
        contador = 0
    
    contador += 1
    
    with open('acessos.txt', 'w') as arquivo:
        arquivo.write(str(contador))

    # Renderizar o template com o currículo e a quantidade de acessos
    return render_template('index.html', contador=contador)

if __name__ == '__main__':
    app.run()
