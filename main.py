from flask import Flask, render_template, request
app = Flask(__name__)
    
submitted = []

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        text = request.form["tTXT"]
        name = request.form["tNM"]
        submitted.append([[str(name)], [str(text)]])
        return render_template("index.html", submitted=submitted)
    else:
        return render_template("index.html", submitted=submitted)

if __name__ == '__main__':
    app.run(debug=True)