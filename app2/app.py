from core.middlewares import PrefixMiddleware
from flask import Flask, make_response, request

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/app2')

@app.route('/')
def hello_world():
    response =  make_response('Cookie deleted')
    response.delete_cookie('sample_cookie')
    return response

@app.errorhandler(404)
def error404(e):
    print('404 error')
    return 'bad request!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
