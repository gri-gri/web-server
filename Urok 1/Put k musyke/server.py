from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, Яндекс!"


@app.route('/yandex_music')
def music_ref():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h3>Смотрите, как классно. У меня всё правильно ведётся(см. код), вот только Яндекс.Музыка не разрешает размещать своё содержимое во фреймах. Браво!</h1>

                    <iframe src="https://music.yandex.ru/album/4480919/track/35798096" width="468" height="360" align="left">
                      Ваш браузер не поддерживает плавающие фреймы!
                    </iframe>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
