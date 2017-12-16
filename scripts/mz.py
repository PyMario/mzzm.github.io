# coding: utf8

import base64
import requests


def mz(i):
    while True:
        if len(i) % 3 != 0:
            i = i + '='
        else:
            break
    lo = base64.b64decode(i)
    # print(lo)
    ve = requests.get(lo).text
    print(ve)


if __name__ == '__main__':
    mz('aHR0cHM6Ly9sbXptLmdpdGh1Yi5pby9teg')