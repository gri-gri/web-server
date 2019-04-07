from flask import Flask, render_template, redirect
from loginform import LoginForm
from my_configure import my_configure

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', username=user)


@app.route('/file_sample', methods=['GET', 'POST'])
def form():
    global pic
    form = LoginForm()
    if form.validate_on_submit():
        pic = form.file_load.data
        return redirect('/success')
    return render_template('login.html', title='Форма', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

 
if __name__ == '__main__':
    pic = None
    my_configure(app)
    app.run(port=8080, host='127.0.0.1')
    
