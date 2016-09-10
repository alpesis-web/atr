###############################
Installation
###############################

********************
Prequisition
********************

- `Virtualbox 5.0`_
- `Ubuntu 14.04.3 (Trusty64)`_
- `openstack-dev/devstack`_

.. _`Virtualbox 5.0`: https://www.virtualbox.org
.. _`Ubuntu 14.04.3 (Trusty64)`: http://www.ubuntu.com/download/server
.. _`openstack-dev/devstack`: https://github.com/openstack-dev/devstack


********************
Virtualbox
********************

- create a vm
- network settings: bridge, allow all


********************
Ubuntu 14.04.3
********************

- install the server (with MAAS)

********************
Openstack
********************

::

    $ cd /
    $ sudo mkdir openstack
    $ cd openstack
    $ sudo chown -R stack:stack /openstack 
    $ git clone https://github.com/openstack-dev/devstack
    $ cd devstack
    $ git checkout stable/juno
    $ ./stack.sh

Once done, open the dashboard: http://ip/, login with admin/password
