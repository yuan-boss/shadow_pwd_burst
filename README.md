# shadow_pwd_burst



## 声明

> 本工具仅供用于学习爆破，严禁用于非授权爆破



## 工具简介

该工具可以多线程爆破linux/kali密码
注意：该工具必须在linux系统中执行

可以使用-b参数表示需要爆破的密文文件，使用-d参数表示密码字典



## 下载须知

pwd.txt是测试密码字典

shadow_pwd.txt是测试的密文字典

与shadow_pwd_burst.py文件存放于同一目录才可正常使用





## 使用帮助

```
可以通过-h参数查看具体的参数用法：python shadow_pwd_burst.py -h
格式:python shadow_pwd_burst.py -b 要爆破的密文字典路径 -d 密码字典路径
例如:python shadow_pwd_burst.py -b shadow_pwd.txt -d pwd.txt 
```





## 演示

```cmd
python shadow_pwd_burst.py
```



![image-20230918164422436](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230918164422436.png)



![image-20230918164434467](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230918164434467.png)

![image-20230918164729096](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230918164729096.png)





```cmd
 python shadow_pwd_burst.py -b shadow_pwd.txt1 -d pwd.txt
```

![image-20230918164624054](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230918164624054.png)



![image-20230918164711237](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230918164711237.png)





![image-20230918164729096](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230918164729096.png)