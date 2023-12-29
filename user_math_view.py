from flask import Flask, render_template
import json

#  sorted_question_data.py takes in original _data.json and returns sorted_data.json
# user_math_view_v2 takes in sorted_data.json and makes them into latex and returns processed_data.json
# user_math_view.py loads processed_data.json into math.html and displays it


app = Flask(__name__)


@app.route('/')
def math_page():
    with open('processed_data.json', 'r') as file:
        data = json.load(file)
    return render_template('math.html', questions=data['questions'])


if __name__ == '__main__':
    app.run(debug=True)
