from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def math_page():
    # Example expression
    expression = "e^{x} \\times \\cos(x - 1) - e^{x} \\times \\sin(x - 1)"
    return render_template('math.html', expression=expression)


if __name__ == '__main__':
    app.run(debug=True)
