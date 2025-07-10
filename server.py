from flask import Flask

MESSAGE = "shhh, this is secrect"

app = Flask(__name__)

@app.route('/')
def get_secrect_message():
    return MESSAGE + "\n"

if __name__ == '__main__':
    app.run(port=5684)
