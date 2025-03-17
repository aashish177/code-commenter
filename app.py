from flask import Flask, render_template, request, jsonify
from commenter.parser import insert_docstrings_in_code

app = Flask(__name__) # Initialize Flask app

@app.route('/')
def index():
    # Render the homepage.
    return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process_code():
#     # Process Python code and return updated code with AI-generated docstrings
#     try:
#         code = request.form['code'] # Get code from the HTML form
#         updated_code = insert_docstrings_in_code(code)
#         return jsonify({"updated_code": updated_code})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file uploads and process Python code with AI-generated docstrings
    if 'file' not in request.files:
        return jsonify({"error": "No selected file"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.endswith('.py'):
        return jsonify({"error": "Only .py files are allowed"}), 400
    
    # Read file content
    code = file.read().decode("utf-8")

    # Process with AI
    updated_code = insert_docstrings_in_code(code)

    return jsonify({"updated_code": updated_code})

if __name__ == '__main__':
    app.run(debug=True)
