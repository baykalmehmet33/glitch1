from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask! Baykal'
  
@app.route('/hola/<name>')
def hola(name):
    return 'Web App with Python Flask! ' + name + name
  
if __name__ == '__main__':
    app.run()
