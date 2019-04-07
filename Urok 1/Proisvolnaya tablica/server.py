from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, Яндекс!"


@app.route('/table/<int:n>/<int:m>')
def table(n, m):
    stable = '''<!doctype html>
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
                    <table class="table">
                      <tbody>
                        {}
                      </tbody>
                    </table>
                  </body>
                </html>'''
    add_str = ''
    for row_num in range(1, n+1):
        add_str += '<tr>'
        for col_num in range(1, m+1):
            add_str += '  <td>Номер строки: {}, номер столбца: {}</td>\n'.format(row_num, col_num)
        add_str = add_str.strip()
        add_str += '</tr>'
    return stable.format(add_str)

    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
