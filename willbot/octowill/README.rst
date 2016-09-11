###########################
Octowill
###########################


*************************
Installation
*************************

Ubuntu 14.04

::

    $ sudo apt-get install python-virtualenv redis-server
    or
    $ bash requirements/ubuntu.sh

Octowill

::

    $ cd /path/to/project/
    $ sudo mkdir octowill
    $ sudo chown -R user:group /path/to/octowill/
    $ sudo su user

    $ cd octowill
    $ mkdir venvs
    $ virtualenv venvs/octowill
    $ source venvs/octowill/bin/activate

    $ git clone https://github.com/KellyChan/octowill.git

install packages

::

    $ cd octowill
    $ pip install -r requirements.txt


**********************
Configuration
**********************

config.py

::

    $ cd octowill
    $ cp config.py.sample config.py
    $ vim config.py                   # update USERNAME, PASSWORD, V2_TOKENS


run 

::

    $ ./start_dev/will.py
