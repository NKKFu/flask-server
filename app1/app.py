from core.middlewares import PrefixMiddleware
from flask import Flask, request

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/app1')

@app.route('/')
def hello_world():
    cookie = request.cookies.get('sample_cookie')
    return f'Hello, world. Your cookie: {cookie}!'

@app.errorhandler(404)
def error404(e):
    print('404 error')
    return 'bad request!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
