from flask import Flask, render_template, request, jsonify
import wikipedia
app = Flask(__name__)

# wikipedia summary calling function
def check_wikipedia(query, session='general'):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return 'Sorry, I got no information about' + query

# Web API response using POST method
@app.route("/post", methods = ['POST'])
def lightning_response_post():
    userTextPost = request.json     # receive the json data from web app
    msg = userTextPost['freeText']
    res = check_wikipedia(msg)
    response = '.'.join(res.split('. ')[:10])
    reply = {"responseText": response}
    return jsonify(reply)       # return the response after making it a json object

# index page 
@app.route('/')
def index():
    return render_template("index.html")

# Running the app
if __name__ == "__main__":
    #ip = '127.0.0.1'
    #port_number = 5000
    app.run(threaded=True, port=5000)
