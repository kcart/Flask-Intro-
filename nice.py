from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """Hi! This is the home page.
    <a href="/hello">Click this link to go to a greeting!</a>"""

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                
                <br><br>
                <label>Pick your adjective of choice (below). <br><br>

                <label><input type ="radio" name="compliment" value="awesome">awesome</label> <br>
                <label><input type ="radio" name="compliment" value="terrific">terrific</label><br>
                <label><input type ="radio" name="compliment" value="fantastic">fantastic</label><br>
                <label><input type ="radio" name="compliment" value="neato">neato</label><br>
                <label><input type ="radio" name="compliment" value="fantabulous">fantabulous</label><br>
                <label><input type ="radio" name="compliment" value="wowza">wowza</label><br>
                <label><input type ="radio" name="compliment" value="oh-so-not-meh">oh-so-not-meh</label><br>
                <label><input type ="radio" name="compliment" value="brilliant">brilliant</label><br>
                <label><input type ="radio" name="compliment" value="ducky">ducky</label><br>
                <label><input type ="radio" name="compliment" value="coolio">coolio</label><br>
                <label><input type ="radio" name="compliment" value="incredible">incredible</label><br>
                <label><input type ="radio" name="compliment" value="wonderful">wonderful</label><br>
                <label><input type ="radio" name="compliment" value="smashing">smashing</label><br>
                <label><input type ="radio" name="compliment" value="lovely">lovely</label><br>

                <br><br>
                <input type="submit">
                
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    compliment_greeting = request.args.get("compliments")

    #AWESOMENESS = [
     #   'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
      #  'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    #compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s, I think you're %s!
        </body>
    </html>""" % (player, compliment_greeting)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
