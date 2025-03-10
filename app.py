from flask import Flask

app = Flask(__name__)

@app.route('/<random_string>')
def returnRandomString(random_string):
    """Reverse the string and return provided URI"""
    return "".join(reversed(random_string))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)