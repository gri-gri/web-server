from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "Привет, Яндекс!"

@app.route('/image_sample')
def image():
    return '''<img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/Риана.jpg'))

@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                    <nav class="navbar navbar-light bg-light">
                      <span class="navbar-brand mb-0 h1">НУ, что сказать</span>
                    </nav>
                    <button type="button" class="btn btn-primary">Было сложно, но похоже, что я разобрался</button>
                    <h3>На самом деле, я так посмотрел, Bootstrap в каких-то аспектах здоровский</h3>
                    <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="{}" class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась - 2">
                        </div>
                        <div class="carousel-item">
                          <img src="{}" class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась - 3">
                        </div>
                        <div class="carousel-item">
                          <img src={} class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась - 4">
                        </div>
                      </div>
                    </div>
                  </body>
                </html>'''.format(url_for('static', filename='img/img1.jpg'), url_for('static', filename='img/img2.jpg'),
                                  'https://avatars.mds.yandex.net/get-pdb/966350/73f525c4-d3ca-4086-98e0-d8efb1016ac0/s1200?webp=false')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
