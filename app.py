from flask import *
import mlab
from mongoengine import *
from faker import Faker

app = Flask(__name__)

mlab.connect()

class Girl(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    rating = FloatField()




#Mongo
#1 Find record based on id
#mongoengine lazy loading
# girl=Girl.objects().with_id("59e32cc071c3060abca5dad6")
#
# #2 Delete
# if girl is None:
#     print("Not Found")
# else:
#     girl.delete()



@app.route("/")
def index():
    girl_list = Girl.objects()
    return render_template("girls.html", girls=girl_list)

@app.route("/List")
def list_item():
    return render_template("girl_list.html", names=["Minh", "Đán", "Tuấn Anh" , "Huy" , "Linh"], img = "https://rlv.zcache.com/big_smile_happy_face_drawer_knob_srf-r95f84f7818be4b3aa45a36488e23c00d_zp2d5_324.jpg?rlvnet=1")

@app.route("/Instruction")
def list_demo():
    d = {
        "name": "1 Ngày Đẹp Trời",
        "image": "http://static2.yan.vn/YanNews/2167221/201704/20170408-120355-hinh-anh-co-gai-mien-nui-tay-bac-xinh-dep-tuyet-voi-4_450x638.jpg"
        }
    return render_template("whatever.html", girl = d)

@app.route("/css-demo")
def css_demo():
    return render_template("css_demo.html")

@app.route("/admin")
def admin_page():
    girl_list = Girl.objects()
    return render_template("admin.html", girls=girl_list)


@app.route("/sign up")
def signup_page():
    return render_template("sign_up.html")

@app.route("/addon",methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add_girl.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        image = form["image"]
        description = form["description"]

        girl=Girl(name=name,description=description,image=image,rating=1.2)
        girl.save()

        return "Added"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/delete-girl/<girl_id>")
def delete_girl(girl_id):
    girl = Girl.objects().with_id(girl_id)
    if girl is None:
        return "Cannot found"
    else:
        return "Deleted" + girl_id

@app.route("/edit-girl/<girl_id>",methods = ["GET","POST"])
def edit_girl(girl_id):
    girl = Girl.objects().with_id(girl_id)
    if request.method == "GET":
        return render_template("edit.html",g=girl)
    elif request.method == "POST":
        formm = request.form
        name = form["name"]
        image = form["image"]
        description = form["description"]
        girl.update(set_name=name, set_iamge=image, set_description=description)
        return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)
