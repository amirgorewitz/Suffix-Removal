from flask import Flask, request, jsonify
import docx2txt
import re

app = Flask(__name__)

def find_simple_root(word):
    # Implement the logic to find and remove suffixes from the word
    # For example, using regular expressions.

    # Return the simple root form of the word.
    return word

@app.route('/process_document', methods=['POST'])
def process_document():
    word_doc = request.files['wordDoc']
    text = docx2txt.process(word_doc)

    # Find words with specific suffixes and get their simple root forms
    words = re.findall(r'\b\w+\b', text)
    simple_root_forms = [find_simple_root(word) for word in words]

    return jsonify({'words': simple_root_forms})

if __name__ == '__main__':
    app.run()
