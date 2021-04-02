from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    text = request.form.get("enter")
    data = text
    return render_template('output.html', data=text)


if __name__ == "__main__":
    app.run(debug=True)