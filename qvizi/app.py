from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/todo')
def todo():
    tasks = ['პითონი', 'დალაგება', 'მეცადინეობა']
    return render_template("index.html", tasks=tasks)


# @app.route("/<sub>/todo/")
# def add_task():
#     return


if __name__ == '__main__':
    app.run(debug=True)