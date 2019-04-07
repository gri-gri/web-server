from flask import Flask, render_template, redirect, request
from loginform import LoginForm
from my_configure import my_configure

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', username=user)


@app.route('/odd_even', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    try:
        if form.validate_on_submit() or request.form['inputt'] == '0':
            return render_template('success.html', number=int(request.form['inputt']), form=form)
        return render_template('login.html', title='Форма', form=form)
    except KeyError:
        return render_template('login.html', title='Форма', form=form)

 
if __name__ == '__main__':
    my_configure(app)
    app.run(port=8080, host='127.0.0.1')
    
