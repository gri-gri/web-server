from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/image_sample')
def image():
    print('Ok')
    return '<h1>Привет, Яндекс! Я - {ВАШЕ ИМЯ}</h1><br>'+\
    '''<img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/Риана-other.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
