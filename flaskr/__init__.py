import os
from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

if __name__ == "__main__":
    app.run(debug=True)
    
import flaskr.views # import views.py for page endpoints 