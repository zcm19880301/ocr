# ocr-client：箱号识别系统-客户端

## 功能列表
## 代码存放位置：

- 客户端-python代码：`/ocr/client/ocr-client-algorithm`
- 客户端-Java代码：`/ocr/client/ocr-client`
- 服务端-python代码：`/ocr/client/ocr-server-algorithm`
- 服务端-Java代码：`/ocr/client/ocr-server`
- 文档存放位置：`/ocr/doc`

## 基础架构搭建
- [ ] Springboot客户端搭建
- [ ] 系统框架搭建

### 客户端功能列表
- [ ] 提供http接口，上传文件和参数
- [ ] 存储上传的图片和参数
- [ ] 调用python提供的http接口，告知图片地址，告知参数让其解析；
- [ ] python解析完成，返回内容，存储，返回给使用者。
- [ ] 发起异步任务，让图片执行同步服务器操作
- [ ] 提供接口，让服务端定时通知这里，存储好数据给python用。

### 服务端功能列表
- [ ] 提供接口：同步图片服务；
- [ ] 提供接口，给python算法调用，将python的算法结果，推送到客户端中。