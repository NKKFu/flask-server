from core.middlewares import PrefixMiddleware
from flask import Flask, make_response

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/app3')

@app.route('/<cookie>')
def hello_world(cookie: str):
    # Add sample cookie for the user
    defined_cookie = cookie or 'simple_cookie'
    response =  make_response(f'Cookie defined as: {defined_cookie}')
    response.set_cookie('sample_cookie', defined_cookie)
    return response

@app.errorhandler(404)
def error404(e):
    print('404 error')
    return 'bad request!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
