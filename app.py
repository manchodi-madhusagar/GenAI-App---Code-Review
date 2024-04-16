from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Initialize OpenAI API
openai.api_key = os.getenv('sk-h4QcK58puqavFZa3q6vFT3BlbkFJD28NZ9asmGQxpM5EKy')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/review', methods=['POST'])
def review_code():
    code = request.form['code']

    # Call OpenAI API for code review
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=code,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0,
    )

    # Process API response
    # Here you would extract bugs, suggestions, and fixed code from the response
    bugs = []  # Placeholder for extracted bugs
    suggestions = []  # Placeholder for suggestions for improvement
    fixed_code = []  # Placeholder for fixed code snippets

    # Populate the results on the review page
    return render_template('review.html', bugs=bugs, suggestions=suggestions, fixed_code=fixed_code)

if __name__ == '__main__':
    app.run()



