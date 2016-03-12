from fabric.api import *
env.use_ssh_config = True

env.hosts = ['dstarnotes']

def ping():
    run('uname --all')

def build():
    with lcd('docs'):
        local('sphinx-build -b html -d _build . ../htm')

def clean():
    local('rm -rf html')
    local('rm -rf docs/_build')

def push():
    local('git push origin master')

def pull():
    with cd('DstarNotes'):
        run('git pull')


