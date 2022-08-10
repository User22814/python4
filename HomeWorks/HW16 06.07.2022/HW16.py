import flask
from flask import Flask
import psycopg2
from flask import jsonify
from flask import request

# Model View Controller

# 127.0.0.1:5432 (localhost:5432) - текущая машина, откуда идёт запрос
# 192.168.1.121:5432 - локальный адрес текущей машины в этой подсети
# 89.218.132.130:80 - внешний "белый" ip-адрес от Казактелекома
# km.kz - домен первого уровня
# web.km.kz (89.218.132.130) - домен второго уровня

app = Flask(__name__)


@app.route("/")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def index():
    return "<h3>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
           "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and " \
           "scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap " \
           "into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the " \
           "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing " \
           "software like Aldus PageMaker including versions of Lorem Ipsum.</h3> "
