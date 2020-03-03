from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        form = request.form
        a = float(form["A"])
        n = float(form["n"])
        i = float(form["i"])
        df = (((1+i)**n)-1)/(i*(i+1)**n)
        p = round(a/df,2)
        result=f'The monthly payment is ${p}.'
        return render_template('index.html', display=result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
