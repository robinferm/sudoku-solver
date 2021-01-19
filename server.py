from flask import Flask, render_template, request, make_response, jsonify
from sudoku import solve
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def solve_sudoku():
    #inputWord = request.get_json()
    result = solve()
    res = make_response(jsonify(result), 200)

    return res

if __name__ == '__main__':
    app.run(debug=True)
