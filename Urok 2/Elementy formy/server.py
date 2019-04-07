from flask import Flask, render_template, redirect, request
from loginform import LoginForm
from my_configure import my_configure

app = Flask(__name__)
my_configure(app)
 
@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', username=user)


@app.route('/form_sample', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        print(request.form['username_first'])
        print(request.form['real_name'])
        print(request.form['password'])
        print(request.form['sex'])
        print(request.form['commentary'])
        print(request.form['language'])
        print(request.form['remember_me'])
        return redirect('/success')
    return render_template('login.html', title='Форма', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

 
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
