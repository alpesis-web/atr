Nov 16 2014 | virtualenv, python | Kelly Chan
# Python with Virtualenv

### Virtualenv

    sudo apt-get install python-virtualenv
    virtualenv
    virtualenv env_name
    
    virtualenv --no-site-packages
    
    cd env_name
    source ./bin/activate
    
    deactivate
    
    pip install package_name
    
    # ~/.bashrc
    export PIP_REQUIRE_VIRTUALENV=true
    export PIP_RESPECT_VIRTUALENV=true


### Virtualenvwrapper

    sudo easy_install virtualenvwrapper  
    mkdir $HOME/.virtualenvs
    
    # ~/.bashrc
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    
    source ~/.bashrc
    
    workon
    lsvirtualenv
    
    mkvirtualenv env_name
    workon env_name
    rmvirtualenv env_name
    
    deactivate
    
    
