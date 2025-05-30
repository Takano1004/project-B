from flask import request, redirect, send_from_directory
import controller

def create_route(app):

    @app.route("/")
    def index():
        return controller.top() #"/"にアクセスしたときに、controller.topを実行。トップページを返す処理を行う
    
    @app.route("/json", methods=["GET","POST"])
    def json():
        if "data" in request.args:
            d = request.args.get("data")
            if d in ["user","item","category","dept"]:
                return controller.json(d)
        return("GETパラメータを指定してください")
    
