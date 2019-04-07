from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, Яндекс!"


@app.route('/youtube/<int:number>')
def youtube(number):
    stable = '''<!doctype html>
                  <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
		    {}
                  </body>
                </html>'''
    if 1 <= number <= 5:
        add_str = '''<iframe src='https://www.youtube.com/watch?v=aUixTgX8dxU' width="468" height="400" align="left">
                       Ваш браузер не поддерживает плавающие фреймы!
                     </iframe>''' * number
    else:
        add_str = '<h1>Вы ввели неподходящее число!</h1>'
    return stable.format(add_str)

    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
