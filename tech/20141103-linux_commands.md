Nov 03 2014 | linux | Kelly Chan
# Linux Commands

### nano

- `nano file_name`: open/create a file
- `nano -w /etc/fstab`: no auto switch lines
- `ctrl+O`: save
- `ctrl+C`: cancel
- `ctrl+X`: exit

### chmod

    chmod [who] [opt] [mode] file_name
    
    who:
    - u: author
    - g: group users
    - o: others
    - a: all users
    
    
    opt: operations
    

用法1：其语法格式为：chmod [who] [opt] [mode] 文件/目录名       
其中who表示对象，是以下字母中的一个或组合：
u：表示文件所有者
g：表示同组用户
o：表示其它用户
a：表示所有用户
opt则是代表操作，可以为：
+：添加某个权限
-：取消某个权限
=：赋予给定的权限，并取消原有的权限
mode则代表权限：
r：可读
w：可写
x：可执行
为同组用户增加对文件a.txt的读写权限： chmod g+rw a.txt
