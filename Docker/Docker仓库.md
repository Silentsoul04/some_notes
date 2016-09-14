#####仓库(Repository)

>仓库(Repository)是集中存放镜像的地方。

>一个容易混淆的概念是注册服务器（Registry）。实际上注册服务器是管理仓库的具体服务器，每个服务器上可以有多个仓库，而每个仓库下面有多个镜像。从这方面来说，仓库可以被认为是一个具体的项目或目录。例如对于仓库地址 docker.docker.com/ubuntu 来说，hub.docker.com 是注册服务器地址，ubuntu 是仓库名。

>大部分时候，并不需要严格区分这两者的概念。

#####Docker Hub
[Docker Hub](https://hub.docker.com/)是Docker官方维护的一个注册服务器。其中包括了超过15000镜像，大部分需求，都可以通过Docker Hub中直接下载镜像来实现

* 登录
    - 使用 `docker login`输入用户名,密码邮箱完成注册登录。注册成功后，本地用户目录的`.dockercfg `中将保存用户的认证信息。
* 基本操作
    - `docker search` 搜索
    - `docker pull` 下载到本地
    - `docker push` 推送到 docker hub

#####自动创建

>自动创建(Automated Build)功能对于需要经常升级镜像内程序来说，十分方便。有时候，用户创建了镜像，安装了某个软件，如果软件发布新版本则需要手动更新镜像

而自动创建允许用户通过Docker Hub指定跟踪一个目标网站(支持Github或BitBucket)上的项目，一旦项目发生新的提交，则自动执行 创建。

要配置自动创建,步骤如下:

* 创建并登陆 Docker Hub,以及目标网站
* 在目标网站中创建连接账号到Docker Hub
* 在Docker Hub 中 [配置一个自动创建](https://registry.hub.docker.com/builds/add/)
* 选取一个目标网站中的项目(需要包含 Dockerfile)和分支
* 指定 Dockerfile位置，并提交创建
之后,可以在Docker Hub的 [自动创建页面](https://registry.hub.docker.com/builds/) 跟踪每次创建的状态

####私有仓库

>有时候使用 Docker Hub这样的公共仓库可能不方便，用户可以创建一个本地仓库供私人使用。

>docker-registry 是官方提供的工具，可以用于构建私有的镜像仓库。

#####仓库配置文件

>Docker 的 Registry 利用配置文件提供了一些仓库的模板（flavor），用户可以直接使用它们来进行开发或生产部署。

**模板**

在 config_sample.yml 文件中，可以看到一些现成的模板段：

* common：基础配置
* local：存储数据到本地文件系统
* s3：存储数据到 AWS S3 中
* dev：使用 local 模板的基本配置
* test：单元测试使用
* prod：生产环境配置（基本上跟s3配置类似）
* gcs：存储数据到 Google 的云存储
* swift：存储数据到 OpenStack Swift 服务
* glance：存储数据到 OpenStack Glance 服务，本地文件系统为后备
* glance-swift：存储数据到 OpenStack Glance 服务，Swift 为后备
* elliptics：存储数据到 Elliptics key/value 存储
示例:
```
common:
    loglevel: info
    search_backend: "_env:SEARCH_BACKEND:"
    sqlalchemy_index_database:
        "_env:SQLALCHEMY_INDEX_DATABASE:sqlite:////tmp/docker-registry.db"

prod:
    loglevel: warn
    storage: s3
    s3_access_key: _env:AWS_S3_ACCESS_KEY
    s3_secret_key: _env:AWS_S3_SECRET_KEY
    s3_bucket: _env:AWS_S3_BUCKET
    boto_bucket: _env:AWS_S3_BUCKET
    storage_path: /srv/docker
    smtp_host: localhost
    from_addr: docker@myself.com
    to_addr: my@myself.com

dev:
    loglevel: debug
    storage: local
    storage_path: /home/myself/docker

test:
    storage: local
    storage_path: /tmp/tmpdockertmp
```
