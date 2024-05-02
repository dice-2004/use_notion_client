from flask import Flask,session,redirect,url_for,render_template
import sqlite3
from my_package import func,notion,write_log
import os
from notion_client import Client
import configparser


app = Flask(__name__)

################################### 定数設定　###################################################
DATABASE = "DB.db"
TXT_LOG = "history.log"

config = configparser.ConfigParser()#IDを取得（config.iniから
config.read('./config.ini')
DB_ID_notion = config['DB_ID']['DataBase_id']


################################### 定数設定　###################################################


def login_required(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for("login"))
        else:
            return func(*args, **kwargs)
    return wrapper




@app.route("/")
def home():
    return redirect(url_for("top"))

@app.route("/top")
def top():
    contents=notion.get_page_content("101bb3fdc8704344bc5a4c46482b0427")
    print(contents)
    write_log.WriteLog("w","w","w")
    return render_template("home.html",contents=contents)

@app.route("/test")
def test():
    contents,n=notion.get_filtered_pages(DB_ID_notion)#第二引数に,"q"で特定のカテゴリ
    write_log.WriteLog("w","w","w")
    return contents





if __name__ == "__main__":  # Flask起動
    app.run(port=int("5000"), debug=True, host="localhost")
    # 開発時 -> port=int("5000"),debug=True,host='localhost'
    # 実装時 -> port=int("5000"),debug=True,host='localhost'
