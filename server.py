from flask import Flask, render_template  
app = Flask(__name__)


@app.route('/play')
def play():
    x=3
    return render_template('index.html', x=x)  

@app.route('/play/<int:x>')
def play_box(x):
    return render_template('index.html', x=x)

@app.route('/play/<int:x>/<color>')
def play_boxes(x, color):
    return render_template('index.html', x=x, color=color)  



if __name__=="__main__":  
    # app.run(debug=True)
    app.run(debug=True, host="localhost", port=8000)