from flask import Flask, render_template
from my_configure import my_configure

app = Flask(__name__)

 
@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', username=user)

 
if __name__ == '__main__':
    my_configure(app)
    app.run(port=8080, host='127.0.0.1')
