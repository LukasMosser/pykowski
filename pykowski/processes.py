from os import chdir
from shlex import split
from subprocess import Popen


def run_karambola(name, home):
    chdir(home)
    chdir("computation/"+name)
    cmd_line = "../../../../karambola "+name+".poly --nolabels --force w000 --force w100 --force w200 --force w300 --force w010 --force w110 --force w210 --force w310 --force w020 --force w102 --force w120 --force w202 --force w220 --force w320 -o results"
    args = split(cmd_line)
    p = Popen(args)
    p.communicate()
    chdir(home)
    return True
