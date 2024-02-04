from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    print("Hello")
    return "Hello from the server!"

if __name__ == '__main__':
    app.run(debug=True)
