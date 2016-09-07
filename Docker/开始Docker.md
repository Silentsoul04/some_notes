接下来需要:

* 安装docker软件
* 在容器中运行一个软件镜像
* 在Docker Hub中查找镜像
* 创建一个自己的docker镜像
* 创建Docker Hub账户并建立镜像仓库
* 创建一个自己的镜像
* 将你的镜像push到你的Docker Hub


`docker run hello-world`详解:

![](_images/container_explainer.png)

当你运行`docker run hello-world`时,docker引擎会:

* 检查你是否有hello-world函数镜像
* 从docker hub下载镜像
* 在容器中加载镜像并运行它

Docker镜像可以像启动数据库一样复杂的启动软件,等你或其他人输入数据,存储数据。
