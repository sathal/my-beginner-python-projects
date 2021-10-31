### Steps to run the application in the browser on port 5000 from terminal - by following these steps you are launching a very simple builtin server
# 1) In the terminal navigate to the directory containing the .py file there the Flask class is instantiated
# 2) Start the virtual environment by using the following command: $ . venv/bin/activate
# 3) Tell flask where to find your application by adding it to the FLASK_APP environment variable using the following command: $ export FLASK_APP=yourAppName
# 4) Enable all development feature by running the following: $ export FLASK_ENV=development
# 5) Start your application with the following command: $ flask run

from flask import Flask

app = Flask(__name__) # Create an instance of the Flask class. This functions as our WSGI (Web Server Gateway Interface) application

@app.route("/") # Tells Flask what URL should trigger the following method
def hello_world():
    return "<p>Hello, World!!!</p>" # The method returns what we want displayed in the user's browser
