from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python meh!'
  
@app.route('/hola/<name>')
def hola(name):
    return 'Web App with Python meh! ' + name + name
  
if __name__ == '__main__':
    app.run()
