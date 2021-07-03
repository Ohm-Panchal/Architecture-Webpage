from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('HomePage.html')

@app.route('/Projects')
def Projects():
    return render_template('Projects.html')

if __name__ == "__main__":
    app.run()