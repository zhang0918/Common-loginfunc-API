# coding=utf-8
import os
import sys
import subprocess

modulename = sys.argv[1]


def getAllModule():
    modulelist = os.popen('pip list').read()
    strmodule = ''.join(map(str, modulelist))
    print strmodule
    if modulename not in strmodule:
        try:
            cmd = 'pip install ' + modulename
            data = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while data.poll() is None:
                line = data.stdout.readline()
                line = line.strip()
                if line:
                    print('{}'.format(line))
        except Exception as e:
            print e
    else:
        print modulename + ' exist!'


if __name__ == "__main__":
    getAllModule()