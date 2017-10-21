from flask import Flask, render_template
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

# f = Faker()
#
# for _ in range (20):
#     g = Girl(name = f.name(),
#             image = "http://via.placeholder.com/500x300",
#             description = f.text(),
#             rating = 4.1)
#     g.save()

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

if __name__ == "__main__":
    app.run(debug=True)
