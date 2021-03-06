import os

from flask import Flask, request, redirect, url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

b_host = os.environ.get("DB_HOST")


class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:a6569009@" + b_host + ":3306/donghaoran43"
    )
    SQLALCHEMY_ECHO = True


app = Flask(__name__)
app.secret_key = "dhr"
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


class cal_res(db.Model):
    # 定义表名
    __tablename__ = "cal_res"
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.String(45))
    calc = db.Column(db.String(45))
    # repr()方法显示一个可读字符串
    def __repr__(self):
        return "<Role: %s %s>" % (self.num, self.id)


a = ""


def process_input():
    global a

    msg = request.form.get("msg")
    msg = str(msg)
    a = msg + " = " + str(eval(msg))
    res = cal_res(num=str(eval(msg)), calc=msg)
    db.session.add(res)
    db.session.commit()


def process_output():
    return a


@app.route("/calc.php", methods=["POST", "GET"])
def user():
    process_input()
    output = process_output()
    nums = cal_res.query.all()
    return render_template("echo.jinja2", bean=output, nums=nums)


@app.route("/", methods=["POST", "GET"])
def index():
    return redirect(url_for("user"))


# Run
if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run()
