from flask import Flask, render_template, request, url_for, redirect
from flask_login.utils import login_required, login_user
from flask_wtf.csrf import CSRFProtect

from users import login_manager, users, User

app = Flask(__name__)
app.secret_key = 'This is totally s3cr3t key!'

login_manager.init_app(app)
CSRFProtect(app)

results = []


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    if request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for('student'))

    return 'Bad login'


@app.route('/')
@login_required
def student():
    return render_template('poll_secure.html')


@app.route('/results', methods=['POST', 'GET'])
@login_required
def result():
    if request.method == 'POST':
        result = request.form
        results.append(result)
        with open('database.txt', 'a') as f:
            f.write('Name: {}\nChemistry: {}\nPhysics: {}\nMaths: {}\n***\n'
                    .format(result['Name'], result['Chemistry'], result['Physics'], result['Mathematics']))
        return render_template("results.html", result=result)
    else:
        return render_template('all_results.html', results=results)


if __name__ == '__main__':
    app.run()
