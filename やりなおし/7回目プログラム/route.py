from flask import request, redirect, send_from_directory, render_template #修正前from flask import request, redirect, send_from_directory
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
    @app.route("/item/search")
    def item_search():
        return render_template("item_search.html")

    @app.route("/item/request")
    def item_request():
        return render_template("item_request.html")

    @app.route("/item/list")
    def item_list():
        return render_template("item_list.html")
    
