from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Count characters in a string, probably not the fastest way
    """
    counter = dict()
    if request.method == 'POST':
        data = request.form['content']
        for letter in data:
            counter.setdefault(letter, 0)
            counter[letter] += 1

    return render_template('index.html', counter=counter)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
