from flask import Flask
from rx import Observable, Observer

app = Flask(__name__)


@app.route('/')
def get_strings(observer):
    observer.on_next("Antony")
    observer.on_next("Nduhiu")
    observer.on_next("Mundia")
    observer.on_completed()


class ShowReactive(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Finished")

    def on_error(self, error):
        print("Error: {0}".format(error))


source = Observable.create(get_strings)
source.subscribe(ShowReactive())

if __name__ == '__main__':
    app.run(debug=True)
