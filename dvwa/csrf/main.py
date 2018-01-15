from flask import Flask, render_template, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def redirect():
    return render_template('index.html')

@app.route('/easy')
def easy():
    with open('templates/attacks/easy.html') as attack_file:
        form = attack_file.read()
    return render_template(
        'form-easy.html',
        contents=escape(form)
    )

@app.route('/medium')
def medium():
        with open('templates/attacks/medium.html') as attack_file:
            form = attack_file.read()
        return render_template(
            'form-medium.html',
            contents=escape(form)
        )

@app.route('/hard')
def hard():
    return render_template('form-hard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
