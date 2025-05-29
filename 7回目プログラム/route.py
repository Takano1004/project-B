from flask import request, render_template
import controller

def create_route(app):  

    @app.route("/")
    def index():
        return controller.top()

    @app.route("/json", methods=["GET", "POST"])
    def json():
        if "data" in request.args:
            d = request.args.get("data")
            if d in ["user", "item", "category", "dept"]:
                return controller.json(d)
        return "GETパラメータを指定してください"
    @app.route("/lost-user")
    def lost_user():
   　　 return "ルート！"
