from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    text = request.form.get("enter")
    length = len(text)
    news = []
    i = 0
    line = 0
    flags = []
    for x in text:
        i += 1

        if x == 'A':
            flags.append("static/Aa.png")
        elif x == 'B':
            flags.append("static/Bb.png")
        elif x == 'C':
            flags.append("static/Cc.png")
        elif x == 'D':
            flags.append("static/Dd.png")
        elif x == 'E':
            flags.append("static/Ee.png")
        elif x == 'F':
            flags.append("static/Ff.png")
        elif x == 'G':
            flags.append("static/Gg.png")
        elif x == 'H':
            flags.append("static/Hh.png")
        elif x == 'I':
            flags.append("static/Ii.png")
        elif x == 'J':
            flags.append("static/Jj.png")
        elif x == 'K':
            flags.append("static/Kk.png")
        elif x == 'L':
            flags.append("static/Ll.png")
        elif x == 'M':
            flags.append("static/Mm.png")
        elif x == 'N':
            flags.append("static/Nn.png")
        elif x == 'O':
            flags.append("static/Oo.png")
        elif x == 'P':
            flags.append("static/Pp.png")
        elif x == 'Q':
            flags.append("static/Qq.png")
        elif x == 'R':
            flags.append("static/Rr.png")
        elif x == 'S':
            flags.append("static/Ss.png")
        elif x == 'T':
            flags.append("static/Tt.png")
        elif x == 'U':
            flags.append("static/Uu.png")
        elif x == 'V':
            flags.append("static/Vv.png")
        elif x == 'W':
            flags.append("static/Ww.png")
        elif x == 'X':
            flags.append("static/Xx.png")
        elif x == 'Y':
            flags.append("static/Yy.png")
        elif x == 'Z':
            flags.append("static/Zz.png")
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
        elif x == ' ':
            line = line + 1
            flags.append("static/space.png")
        elif x == ';':
            flags.append("static/semicolon.png")
        else:
            flags.append("static/" + x + ".png")

    return render_template("output.html", flags=flags, text=text)


if __name__ == "__main__":
    app.run(debug=True)