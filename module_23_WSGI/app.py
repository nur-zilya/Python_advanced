import json

class App:
    def __init__(self):
        self.routes = {}


    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator


    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        func = self.routes.get(path)

        if func is None:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return ['Page not found']

        args = path.split('/')[2:]
        start_response('200 OK', [('Content-Type', 'application/json')])
        return func(environ, start_response, *args)


app = App()

@app.route('/hello')
def say_hello(environ, start_response):
   start_response('200 OK', [('Content-Type','application/json')])
   return [json.dumps({"response": "Hello, world!"}, indent=4)]


@app.route('hello/<name>')
def say_hello_with_name(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [json.dumps({"response": f"Hello {name}!"}, indent=4)]


