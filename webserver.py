from flask import Flask,jsonify
from src.jsoner import show_the_write


app=Flask(__name__)

@app.route('/api/printHello')
def hello():
    data={'value':'Hello World'}
    return jsonify(data)


@app.route('/api/modifyRecepie')
def modrec():
    data=show_the_write()
    return jsonify(data)


if __name__=='__main__':
    app.run(debug=True,port=80)