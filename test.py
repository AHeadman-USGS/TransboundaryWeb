from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    test = 1+2
    return render_template('index.html', point=test)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

