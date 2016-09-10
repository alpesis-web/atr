########################################
edX Platform: Installation
########################################


******************
devstack
******************




option 1: installing the devstack with official version.

::

    $ mkdir devstack
    $ cd devstack
    $ curl -L https://raw.githubusercontent.com/edx/configuration/master/vagrant/release/devstack/Vagrantfile > Vagrantfile
    $ vagrant plugin install vagrant-vbguest
    $ vagrant up


option 2: installing the devstack with pre-downloaded files.

NOTE: Since devstack contains a box with 3GB around and edx-platform is extremely big (around 800MB), we recommend to download the box and edx-platform repo at the first step.


::

    

