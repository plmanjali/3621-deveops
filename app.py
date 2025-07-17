from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['post'])
def submit():
    username = request.form['username']
    email = request.form['email']
    year = request.form['year']
    return render_template('res.html', name=username, email=email, year=year)

if __name__ == '__main__':
    app.run(debug=True)