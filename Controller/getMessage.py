from flask import Flask, request, jsonify, render_template
import json


app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):

    user_data = {
        "userID": user_id,
        "message": testDict[user_id]
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    
    return render_template("meme_index.html", user_id = user_id, message=testDict[user_id])
    #return jsonify(user_data), 200

@app.route("/get-user/all/")
def get_all_users():

    for user_id in testDict:
        user_data = {
            "userID": user_id,
            "message": testDict[user_id]
        }

        extra = request.args.get("extra")
        if extra:
            user_data["extra"] = extra

        
        return render_template("meme_index.html", user_id = user_id, message=testDict[user_id])
        #return jsonify(user_data), 200

@app.route("/create-message/<userid>", methods=['POST'])
def create_message(userid):
    if(userid in testDict):
        testDict[userid] = "This is a new message"
    else:
        testDict[userid] = "This is a new user too!"
    data = "success!"
    return jsonify(testDict), 201

if __name__ == "__main__":
    global testDict
    testDict = {"1": "lol", "2": "sol", "3": "rotfl"}
    app.run(debug=True)