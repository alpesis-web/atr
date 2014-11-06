Nov 06 2014 | linux, ubuntu | Kelly Chan
# Installing Node.js on Ubuntu

1. installing dependencies


- `sudo apt-get install g++ curl libssl-dev apache2-utils`
- `sudo apt-get install git-core`


2. running the commands


- `git clone git://github.com/ry/node.git`
- `cd node`
- `./configure`
- `make`
- `sudo make install`

### open admin auth on win7

- `net user administrator /active:yes`

### installing bower

error:

    bower command not found
    
solution:

    npm config set prefix /usr/local
    npm install -g bower
    
    which bower

### installing python packages

    sudo apt-get install python-setuptools
    sudo apt-get install python-pip


### References

1. [How to Install Node.js](http://howtonode.org/how-to-install-nodejs)
2. [操作权限不够?教你开启Win7管理员帐户](http://soft.zol.com.cn/271/2718681.html)
