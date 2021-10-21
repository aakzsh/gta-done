from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    text = request.form.get("enter")
    i = 0
    flags = []
    for x in text:
        i += 1

        if x.islower():
            flags.append("static/" + x + ".png")
        elif x.isupper():
            flags.append("static/" + x + x.lower() + ".png")
        elif x == '?':
            flags.append("static/qmark.png")
        elif x == '/':
            flags.append("static/slash.png")
        elif x == ':':
            flags.append("static/colon.png")
        elif x == '.':
            flags.append("static/dot.png")
        elif x == '"' or x=="'":
            flags.append("static/_(1).png")
        elif x == ',':
            flags.append("static/,.png")
        elif x == ' ' or '':
            flags.append("static/space.png")
        elif x == ';':
            flags.append("static/semicolon.png")
        elif x=='\n':
            flags.append('end')
        elif x=='\r':#This line is very essential, its due to a new line character.
            flags.append("static/space.png")
        else:
            flags.append(f"static/{x}.png")

    return render_template("output.html", flags=flags, text=text)


if __name__ == "__main__":
    app.run(debug=True)