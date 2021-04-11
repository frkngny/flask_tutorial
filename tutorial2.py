from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template('2_index.html', x=name, mylist=['a', 'b', 'c'])


if __name__ == "__main__":
    app.run()