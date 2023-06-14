from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    output = subprocess.check_output(['python', 'script.py'])
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
