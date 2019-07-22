from flask import Flask

app = Flask('__name__')

@app.route('/')
def index():
    return '<h1>hello</h1>'


@app.route('/test/<a>:<b>:<c>')
def greet(a,b,c):
    return '<h1>{}.{}.{}</h1>'.format(a,b,c)


app.run()