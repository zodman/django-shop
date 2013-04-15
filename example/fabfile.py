

from fabric.api import local, settings, show,env, get, run, prompt, cd, lcd
env.hosts = ["depamap.com"]
env.user = "zodman"
PATH = "/home/zodman/disenomx/example"

def __remote_virtualenv(command):
    VIRTUAL_ENV = "/home/zodman/.virtualenvs/disenomx"
    source = '. %s/bin/activate && ' % VIRTUAL_ENV
    run(source + command)

def clear_memcached():
    run("""echo "flush_all" | nc -q 2 localhost 11211 """)


def deploy():
    with cd(PATH):
        run("git reset --hard HEAD")
        run("git pull")
        #__remote_virtualenv("pip install -r requires.txt")
        __remote_virtualenv("python manage.py migrate")
        #__remote_virtualenv("python manage.py syncdb")
        run("touch ../django.wsgi")
        clear_memcached()

