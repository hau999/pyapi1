from flask import Flask, jsonify
import utils
app = Flask(__name__)
@app.route("/news/<int:news_id>",methods = ["GET"])
def get_new_by_id(news_id):
    return jsonify({"Ket qua binh phuong": utils.get_news_by_id(news_id)})

if __name__ == "__main__":
    app.run()