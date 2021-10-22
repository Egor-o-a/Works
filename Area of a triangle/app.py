from flask import Flask, render_template, request
from math import sqrt
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        per = (float(num1) + float(num2) + float(num3))//2
        sum = sqrt(per*(per-float(num1))*(per-float(num2))*(per-float(num3)))
        return render_template('app.html', sum=sum)
    else:
        return render_template('app.html')
if __name__=='__main__':
    app.debug = True
    app.run()