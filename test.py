import requests
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")


response = requests.get("https://jsonplaceholder.typicode.com/users?_limit=6")
posts_list = response.json()

@app.route("/")
def index():
    return render_template("index.html", users=posts_list)

@app.route("/remove/<int:user_id>", methods=["POST"])
def remove_user(user_id):
    
    requests.delete(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    
    global posts_list
    for user in posts_list:
        if user["id"] == user_id:
            posts_list.remove(user)
            break
            
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)