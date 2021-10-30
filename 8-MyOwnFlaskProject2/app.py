from flask import Flask

### Create an instance of the Flask class. This functions as our WSGI (Web Server Gateway Interface) application
### https://www.fullstackpython.com/wsgi-servers.html
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
