

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label> Rotate by:
            <input type="text" name="rot" value=0 />
            </label>
            <textarea name="text"> {0} </textarea>
            <input type="submit" value="Submit Query" />
        </form>    
    </body>
</html>   

"""

@app.route("/", methods=["POST"])
def encrypt(): 
#store the values of request parameters in local variables
    rot = request.form["rot"]
    text = request.form["text"]

#convert data types as necessary
    rot_int = int(rot)

    new_string = rotate_string(text, rot_int)

    return form.format(new_string)


#encrypt value of text parameter using rotate_string
#return encrypted string wrapped in <h1> tages


@app.route("/")
def index():

    return form.format("")

app.run()

