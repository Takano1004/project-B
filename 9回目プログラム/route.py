from flask import request, redirect, send_from_directory
import controller

def create_route(app):

    @app.route("/")
    def index():
        return controller.top()
    
    @app.route("/json", methods=["GET","POST"])
    def json():
        if "data" in request.args:
            d = request.args.get("data")
            if d in ["user","item","category","dept"]:
                return controller.json(d)
        return("GETパラメータを指定してください")
    
    @app.route("/item_list", methods=["GET","POST"])
    def item_list():
        k = request.form.get("key") if "key" in request.form else ""
        return controller.f_item(k)

    @app.route("/item_detail", methods=["GET","POST"])
    def item_detail():
        if request.method == "POST":
            id = request.form.get("id")
            d = {
                "拾得物ID":id, 
                "変更内容":request.form.get("act"), 
                "ユーザID":request.form.get("user"), 
            }
            controller.act_reg(d)
            return redirect(f"/item_detail?id={id}")
        if "id" in request.args:
            id = request.args.get("id")
            return controller.d_item(id)
        return("GETパラメータを指定してください")
    
    @app.route("/reg_user", methods=["GET","POST"])
    def reg_user():
        if request.method == "POST":
            d = {
                "氏名":request.form.get("name"), 
                "所属ID":request.form.get("dept"), 
                "電話番号":request.form.get("phone"), 
                "メールアドレス":request.form.get("mail"), 
            }
            controller.user_reg(d)
            return redirect("/reg_user")
        return controller.user_form()
    
    @app.route("/reg_item", methods=["GET","POST"])
    def reg_item():
        if request.method == "POST":
            file = request.files["img"]
            d= {
                "拾得物分類ID":request.form.get("category"),
                "拾得場所":request.form.get("place"),
                "色":request.form.get("color"),
                "特徴":request.form.get("spec"),
                "ユーザID":request.form.get("user"),
            }
            controller.item_reg(d, file)
            return redirect("/reg_item")
        return controller.item_form()

    @app.route("/req_item")
    def req_item():
        return controller.req_item()

    @app.route("/req_list")
    def req_list():
        return controller.req_list()

    @app.route("/dl")
    def dl():
        return controller.dl()
    
    @app.route("/dlp")
    def dlp():
        controller.dl_data()
        return send_from_directory(".", "out.xlsx", mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
