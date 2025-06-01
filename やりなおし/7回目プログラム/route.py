from flask import request, redirect, send_from_directory, render_template
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

    @app.route("/lost/user")
    def lost_user():
        return controller.lost_user()

    @app.route("/lost/register")
    def lost_register():
        return controller.lost_register()

    @app.route("/form/download")
    def form_download():
        return controller.form_download

   
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            new_user = ユーザ(
            氏名=request.form['氏名'],
            所属ID=request.form['所属ID'],
            電話番号=request.form['電話番号'],
            メールアドレス=request.form['メールアドレス'],
            住所=request.form['住所']
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template('register_complete.html')
        else:
            return render_template('lost_user.html')  # フォームを表示するテンプレートを返す
            @app.route("/lost/request", methods=["GET", "POST"])
            def lost_request():
                if request.method == "POST":
                    学籍番号 = request.form.get("学籍番号")
                    氏名 = request.form.get("氏名")
                    学年 = request.form.get("学年")
                    学部学科 = request.form.get("学部学科")
                    特徴 = request.form.get("特徴")
                    落とした場所 = request.form.get("落とした場所")
                    落とした日時 = request.form.get("落とした日時")
                    # 処理例（ログ表示など）
            print("遺失物依頼:", 学籍番号, 氏名, 学年, 学部学科, 特徴, 落とした場所, 落とした日時)

            # 後でDB保存・メール通知・照合など処理を追加できる
        return render_template("lost_request_complete.html")
        return render_template("lost_request.html")


