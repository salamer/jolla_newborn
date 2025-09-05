from jolla import server,render,render_json

def index(request):
    return render('index.html')

def data(request):
    data = {'data': request['id']}
    return render_json(data)

class app(server.WebApp):
    urls = [
        (r'/', index),
        (r'/data/<id>', data),
    ]

if __name__ == '__main__':
    server = server.jolla_server(app)
    server.run_server()
