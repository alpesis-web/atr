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


### References

1. [How to Install Node.js](http://howtonode.org/how-to-install-nodejs)
