Jan 01 2014 | virtualenv, python | Kelly Chan
# Installing VirtualBox on Ubuntu

open the file

    sudo nano /etc/apt/sources.list

add the source 

    deb http://download.virtualbox.org/virtualbox/debian saucy contrib
    deb http://download.virtualbox.org/virtualbox/debian raring contrib
    deb http://download.virtualbox.org/virtualbox/debian quantal contrib
    deb http://download.virtualbox.org/virtualbox/debian precise contrib
    deb http://download.virtualbox.org/virtualbox/debian lucid contrib non-free
    deb http://download.virtualbox.org/virtualbox/debian wheezy contrib
    deb http://download.virtualbox.org/virtualbox/debian squeeze contrib non-free

shell

    wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install virtualbox-4.3

