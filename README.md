说明

项目描述

未来课堂是一个基于Django开发的平台，平台的目标是致⼒于提升在线学习的完课率，目前在线教育领域都是在线看视频的方式，未来课堂开创最新“一对一”模式辅导，实现导师除了每天跟进并定期考核的制度外，还执行学、练、改、管、测五位一体的教学方法以及奖惩措施，以此促进学成率。 

功能介绍 

主要为vue提供接⼝功能，接口基于django rest framewok框架的基础搭建，利用其内置组件和⾃定义扩展实现用户认证和访问频率限制，依赖django-redis组件实现对缓存的操作，将用户访问记录放入redis实现认证操作。 

在线业务主线主要将课程分为“学位课”和“轻课”，基于django contenttype组件实现课程多价格策略，为了减轻数据库压力，提高结算的速度，将临时购买信息放入redis以便操作，购物支付包含贝里、优惠券、支付宝联合支付。

## 运行环境

| Project | Status | Description |
|---------|--------|-------------|
| python          | 3.6 | 在这个版本以及以上都可以 |
| Django               | 2.1.4 | 在这个版本以及以上都可以 |
| django-redis            | 4.10.0 | 在这个版本以及以上都可以 |
| djangorestframework                | 3.9.0 | 在这个版本以及以上都可以 |
| django-rest-framework | 0.1.0 | 在这个版本以及以上都可以 |
| certifi | 2018.11.29 | 在这个版本以及以上都可以 |
| chardet | 3.0.4 | 在这个版本以及以上都可以 |
| crypto | 1.4.1 | 在这个版本以及以上都可以 |
| idna | 2.8 | 在这个版本以及以上都可以 |
| Naked | 0.1.31 | 在这个版本以及以上都可以 |
| pytz | 2018.7 | 在这个版本以及以上都可以 |
| PyYAML | 3.13 | 在这个版本以及以上都可以 |
| redis | 3.0.1 | 在这个版本以及以上都可以 |
| requests | 2.21.0 | 在这个版本以及以上都可以 |
| shellescape | 3.4.1 | 在这个版本以及以上都可以 |
| urllib3 | 1.24.1 | 在这个版本以及以上都可以 |
| uWSGI | 2.0.17.1 | 在这个版本以及以上都可以 |

## 安装环境

##### 前端vue模块安装

进入vue源码目录

cd 07-luffy_project_01/

安装vue模块，默认去装package.json的模块内容，如果出现模块安装失败，手动再装

npm install 

##### 后端python模块安装

cd luffy_boy

pip3 install -r requirements.txt 



## API说明

| 路径 | 功能 |
|---------|--------|
| /course/category/ | 获取课程分类列表                                      |
| /courses/?category_id=1 | 获取category_id=1的所有课程                           |
| /coursedetail/1/        | 获取courseid=1的课程                                  |
| /login/                 | 登录认证,成功返回token                                |
| /reg/                   | 注册                                                  |
| /shoppingcar/           | 添加到购物车,支持增删改查,分别对应POST,DELETE,PUT,GET |
| /logout/                | 注销                                                  |
| /account/               | 结算,支持增改查,分别对应POST,PUT,GET                  |
| /payment/               | 生成订单将支付页面url传给前端                         |
| /myorder/               | 获取订单信息                                          |
| /get_pay_url/           | 获取订单付款链接                                      |
| /api/v1/trade/alipay/   | 用户付款后接受支付宝服务的请求修改订单和优惠券状态    |


## 运行方式
##### vue启动

cd 07-luffy_project_01/

npm run dev

##### django启动

请在luffy_boy/api/utils/keys中修改你的支付宝公钥和私钥否则无法调用支付接口

请务必启动Redis
Redis配置在settings.py中

使用Pycharm直接运行即可，
或者使用命令
`python3 manage.py runserver`

## 表关系
本项目涉及14个表，表关系包含一对一，一对多，多对多！
表关系图如下：

![表结构图.png](https://i.loli.net/2019/11/22/MUHSdLR261isIgh.png)

# 效果图

项目demo网址：[http://shop.yueqi.cf:8880/home](http://shop.yueqi.cf:8880/home)

## 登录

![登录页面.png](https://i.loli.net/2019/11/22/SgnvmUbKdcNW4Mq.png)



## 首页

![首页.png](https://i.loli.net/2019/11/22/QNmeDf9UckaYVpF.png)

## 免费课程

![免费课程.png](https://i.loli.net/2019/11/22/nMRI5wHb2SKG1Wk.png)

## 课程详情
#### 只能通过页面添加到购物车,必须要登录

![课程详情.png](https://i.loli.net/2019/11/22/foj7sxiV6PZ8zmk.png)



## 购物车

#### 选择价格策略,前端和后端redis数据会更改。可以删除课程！此操作必须要登录

![加入购物车.png](https://i.loli.net/2019/11/22/3zhvCI6jYTasOux.png)

## 结算

![结算页面.png](https://i.loli.net/2019/11/22/ujtmPUdAZqe5pHJ.png)

## 支付

![支付页面.png](https://i.loli.net/2019/11/22/XqStmslGOUriRxQ.png)

## 我的订单

![我的订单页面.png](https://i.loli.net/2019/11/22/Q21ArfkBLm59zyY.png)

Copyright (c) 2018-present, yue qi