from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    nya = "にゃ"
    return render_template('index.html', post=nya)

if __name__ == "__main__":
    app.run(debug=True)
