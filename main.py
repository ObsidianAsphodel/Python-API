from flask import *
import json, time

# creating the instance of the flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_page():
    data_set ={"Page" : "Home", "Message": "Successfully loaded the Home page", "Timestamp":time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route("/user/", methods=["GET"])
def request_page():
    user_query = str(request.args.get("user")) # /user/?user=Umbra

    data_set = {"Page" : "Request", "Message": f"Successfully loaded for {user_query}", "Timestamp": time.time()}

    # converts a subset of Python objects into a JSON string
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == "__main__":
    app.run(port=7777)