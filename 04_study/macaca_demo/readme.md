##### 使用阿里巴巴的开源项目macaca进行web自动化测试实践


##### 安装
- Ubuntu离线安装：Nodejs: （Android user下完成 ）

    - 官网下载离线包：  https://nodejs.org/en/  
    node-v8.9.4-linux-x64.tar.xz

    - 将安装包拷贝到虚拟机，解压安装包：  
    tar -xJf node-v8.9.4-linux-x64.tar.xz

    - 移动解压出来的文件包到通用的软件安装目录 /opt/：  
    sudo mv node-v8.9.4-linux-x64 /opt/

    - 安装 npm 和 node 命令到系统命令：
      - sudo ln -s /opt/node-v8.9.4-linux-x64/bin/node /usr/local/bin/node
      - sudo ln -s /opt/node-v8.9.4-linux-x64/bin/npm /usr/local/bin/npm

    - 验证安装：   
        node -v
        npm -v

- 全局安装 macaca：

    - npm install -g macaca-cli macaca-electron macaca-android
    - MAC: (npm install -g macaca-cli macaca-electron macaca-ios macaca-android)  

- 安装浏览器驱动：

    - ChromeDriver ： npm i macaca-chromedriver --save-dev (GFW原因，可能会失败)
        - 可以使用：CHROMEDRIVER_CDNURL=http://npm.taobao.org/mirrors/chromedriver npm install chromedriver -g
        - 详情： https://github.com/macacajs/macaca-chromedriver/blob/master/README.md#default-version
    - 修改源：export CHROMEDRIVER_CDNURL=http://npm.taobao.org/mirrors/chromedriver/ （若安装失败）
    - 修改源：export ELECTRON_MIRROR=https://npm.taobao.org/mirrors/electron/ （若安装失败）
    - （其他如：iOS 环境、Android 环境，只有做手机端口测试时才需要安装）

    - 也可以用cnpm安装： https://www.cnblogs.com/fnng/p/5873878.html （速度很快）
——————————————————————————————————————————————————————————————————————

##### 运行
- 添加环境变量
- 切换root下，启动服务 macaca server --verbose
- Python执行脚本
    - cd work/Python_test/data_analysis/04_study/macaca_demo
    - python3 webtest_demo  (目前仅支持Electron，由于兼容性问题Chrome并不能使用)

——————————————————————————————————————————————————————————————————————

##### 总结

###### 巨多坑
###### https://testerhome.com/topics/7898
###### https://www.cnblogs.com/breakcircle/p/6378629.html
