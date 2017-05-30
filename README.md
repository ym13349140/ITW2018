## 前期准备

首先需要拥有一台云主机的一个账户。若是新的主机，则需要按照[云主机配置文档](https://github.com/Zouzhp3/Learn/tree/master/Cloud)进行初始化部署。

> 若是云服务提供商提供的云主机，一般会已经安装好操作系统，因此可跳过以上文档中的“安装操作系统”章节。此外，若是阿里云的主机，则可能默认会配置好 IP 地址、yum 源、与关闭 firewalld 与 SELinux。

开放阿里云主机的某个对外端口需要在阿里云控制台进行设置。

记得配置新用户并对其授权 sudo，[教程：添加一个新用户并授权](http://www.cnblogs.com/woshimrf/p/5906084.html)。

## 部署

把项目文件上传到服务器上，并安装好数据库（目前没有用到数据库服务，因此没有安装）、虚拟环境 virtualenv 以及服务守护程序 supervisord。安装的具体细节参考我以前所写的 [Linux 服务器部署](https://github.com/Zouzhp3/Learn/blob/master/Flask/ch4%20Linux%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%83%A8%E7%BD%B2.md)。

本项目的路径是`/home/{{账户名}}/ITW2018`，虚拟环境目录在`/home/{{账户名}}/ITW2018/venv`中。当需要在服务器上用命令行运行服务时，需要先激活虚拟环境，然后再运行。

本项目所属的 supervisord 脚本的路径是`/etc/supervisord.d/ITW2018.ini`，内容如下：
```
[program:ITW2018] 
command=/home/{{账户名}}/ITW2018/venv/bin/python manage.py #runserver -h 0.0.0.0 -p 80
directory=/home/{{账户名}}/ITW2018
user=root
```

> 注意：当项目目录结构变更时，以上脚本也必须做相应的变更。且脚本中不能有注释。

## 项目更新后如何进行修改

登录云主机后，使用`ps aux | grep super`命令查找 supervisor 进程，kill 它，然后用`ps aux | grep python`命令查找本网站的 python 服务进程并 kill 它。

上传完最新版的项目文件后，使用`supervisord -c /etc/supervisord.conf`命令重新启动 supervisord，并可使用以下命令完成项目服务的重启。

```
supervisorctl status         # 显示监控状态
supervisorctl stop app       # 停止 app
supervisorctl start app      # 启动 app （往往需要先启动 virtualenv 虚拟环境）
supervisorctl restart app    # 重启 app
```

> 注意： 以上命令中的 app 都需要替换为 supervisord 脚本中所设置的项目名
