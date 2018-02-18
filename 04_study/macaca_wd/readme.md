##### WD.py is a Python WebDriver client

###### 仅仅安装macaca-cli是不够的，若想要驱动浏览器还需要macaca-electron和macaca-chromedriver，顾名思义这两个包，分别用来驱动electron和chrome，但由于高版本Chrome不兼容，个人建议使用electron，至于macaca-android，取决于是否需要做移动端测试。

###### 除了工具支持外，想要通过Python执行测试，还需要pip install wd，虽然脚本中不要求引用这个包，但是不安装的话，脚本跑不起来。

###### 今天最大的收获就是，确定macaca中支持Python部分的代码，虽然抽离出来放到macaca目录，但是如何调用运行还没搞清楚，目前还不能做2次开发，依然需要先启动服务：macaca server --verbose，然后再运行python xxx.py。（很不爽）

###### 看了一下macaca支持python的源码，只是对如何写脚本，或如何找到自己需要的特性，更加了解。 （待后续再研究，现在不钻牛角尖，day5开始写爬虫）

###### https://macacajs.github.io/wd.py/
