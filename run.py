from flask import Flask, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key="afdoijaw23409aoj()_)(&%#$%)"
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=90)