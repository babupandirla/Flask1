from flask import Flask,render_template,jsonify
from app.primecheck import prime as pr
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/prime/<num>',methods=['GET'])
def prime(num):
    try:
        num=int(num)
    except:
        return jsonify({'Error':'Invalid input'})
    return jsonify({'result':pr(num)})