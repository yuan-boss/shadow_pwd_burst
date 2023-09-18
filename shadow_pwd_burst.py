#!/usr/bin/python
# -*- coding: utf-8 -*-
import crypt
import time

from termcolor import colored, cprint
import sys
import threading,queue
import argparse
import imp
imp.reload(sys)

error_print = lambda x: cprint(x, "red")
success_print = lambda x: cprint(x, 'green', attrs=['underline'])
tip_print = lambda x: cprint(x, 'yellow')
banner_print = lambda x: cprint(x, 'magenta', attrs=['concealed'])

parser = argparse.ArgumentParser(usage='python shadow_pwd_burst.py -b shadow_pwd.txt -d pwd.txt', description="这是一个用于爆破linux/kali中/etc/shadow中的密文的工具", prog="shadow文件的密码爆破程序")
parser.add_argument('-b', dest='pwd_path', type=str, required=False, default='shadow_pwd.txt', help='需要爆破的密文的文件路径')
parser.add_argument('-d', dest='dict_path', type=str, required=False, default='pwd.txt', help='密码字典文件路径')

# 避免传入参数不正确，让报错变为友好提示
try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

def banner():
    banner_print(f'{35*"-"} linux/kali shadow文件密码爆破工具 {34*"-"}')
    banner_print(f'{15 * " "}version:0.1 | made by yuanboss | date:2023/09/18{15 * " "}')
    banner_print(f'{88*"*"}')
    banner_print(f'{40*"-"}yuanboss{40*"-"}')
    banner_print(""" 
                                                   .o8                                   
                                                  "888                                   
    oooo    ooo oooo  oooo   .oooo.   ooo. .oo.    888oooo.   .ooooo.   .oooo.o  .oooo.o 
     `88.  .8'  `888  `888  `P  )88b  `888P"Y88b   d88' `88b d88' `88b d88(  "8 d88(  "8 
      `88..8'    888   888   .oP"888   888   888   888   888 888   888 `"Y88b.  `"Y88b.  
       `888'     888   888  d8(  888   888   888   888   888 888   888 o.  )88b o.  )88b 
        .8'      `V88V"V8P' `Y888""8o o888o o888o  `Y8bod8P' `Y8bod8P' 8""888P' 8""888P' 
    .o..P'                                                                               
    `Y8P'                                                                                                                                                                    
        """)
    banner_print(f'{88*"*"}')
    banner_print(f'{40*"-"}yuanboss{40*"-"}')

# 提示
def tip():
    tip_print(f"""
    简介：该工具可以用于对linux/kali进行密码爆破
    注意：该工具必须在linux系统中执行
    使用帮助：
    可以通过-h参数查看具体的参数用法：python shadow_pwd_burst.py -h
    {100*'='}
    格式:python shadow_pwd_burst.py -b 要爆破的密文字典路径 -d 密码字典路径
    eg:python shadow_pwd_burst.py -b shadow_pwd.txt -d pwd.txt 
    {100*'='}\n
    """)


# 密码字典路径，密文路径
def shadow_pwd_burst(dic_pwd_path):
    thread_name = threading.current_thread().name
    tip_print(f'{50 * "-"}{thread_name}正在启动爆破{50 * "-"}')
    time.sleep(3)
    while not q.empty():
        shadow_pwd = q.get()
        # 去除空格换、行
        shadow_pwd = shadow_pwd.strip()
        if '$' in shadow_pwd:
            # 取出密文值
            salt = shadow_pwd[0:shadow_pwd.rindex('$')]
            try:
                for password in open(dic_pwd_path):
                    password = password.strip()
                    # 根据盐值，使用crypt函数对明文进行加密，形成密文
                    new_shadow_pwd = crypt.crypt(password, salt)
                    if shadow_pwd == new_shadow_pwd:
                        success_print(f'{thread_name}:密码爆破成功{(30 - len(password)) * "-"}>{password}')
                        break
                    else:
                        error_print(f'{thread_name}:密码错误{(30 - len(password)) * "-"}>{password}')
            except Exception as e:
                error_print(str(e))

def createQueue(shadow_pwd_path):
    shadow_pwd_list = []
    try:
        # 读取密文字典
        with open(shadow_pwd_path) as shadow_pwd_file:
            shadow_pwd_list = shadow_pwd_file.readlines()
    except Exception as e:
        print(f'文件读取除出错：{e}')
    for pwd in shadow_pwd_list:
        pwd = pwd.strip()
        q.put(pwd)

if __name__ == '__main__':
    threads = 5
    banner()
    tip()
    # 获得传入的参数值
    shadow_pwd_path = args.pwd_path
    dic_pwd_path = args.dict_path
    # 创建一个队列
    q = queue.Queue()
    # 将密文字典的密文放入队列
    createQueue(shadow_pwd_path)
    for thread in range(threads):
        t = threading.Thread(target=shadow_pwd_burst, args=(dic_pwd_path,), name=f'线程{thread}')
        t.start()
