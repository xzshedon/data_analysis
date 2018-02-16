# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from requests import post
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])    # 默认只支持GET，需要指定支持POST
def index():
    if request.method == "GET":     # request.method获得前端请求方式
        return render_template('index.html')    # render_template渲染前端内容
    elif request.method == "POST":
        fontcolor = request.form.get('fontcolor')   # request.form获取前端表单，属于dir的子类
        fonts = request.form.get('fonts')   # 通过dir的get方式获取需要的值
        sizes = request.form.get('sizes')
        word = request.form.get('name')

        data = {           # 构建post的data
            'fontcolor': fontcolor,
            'fonts': fonts,
            'sizes': sizes,
            'word': word,
        }

        html = post('http://www.uustv.com/', data=data).text    # 获取POST得到的URL，并以text形式赋值
        dom = BeautifulSoup(html, "html.parser")    # html.parser是解析器，一定要加，用于解析html
        img_url = dom.find_all('div','tu')[0].img['src']    # 获取签名图片虚拟地址，通过第一个div名字叫tu中，img标签的src
        apaths = 'http://www.uustv.com/' + img_url  # 组合签名图片的物理路径
        return render_template('index.html', apath=apaths)  # 结合端参数，给apath赋值，实现更新签名

if __name__ == '__main__':
    app.run(debug=True,)
