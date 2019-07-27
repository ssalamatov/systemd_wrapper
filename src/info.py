# -*- coding: utf-8 -*-

import re
import argparse
import subprocess


def get_last_running(unit):
    p = subprocess.Popen('systemctl status' + ' ' + unit, stdout=subprocess.PIPE, shell=True)
    (data, _) = p.communicate()
    m = re.search(r'Active: .* since (.*);(.*)',
                  data.decode())

    if m:
        return m.group(1)


def get_info(unit):
    p = subprocess.Popen('systemctl show' + ' ' + unit + ' --all', stdout=subprocess.PIPE, shell=True)
    (data, _) = p.communicate()

    buf = {}
    data = data.decode().strip()
    if data != '':
        for line in data.split('\n'):
            key, value = line.split('=', maxsplit=1)
            value = value or None
            buf[key] = value
    buf.update(last=get_last_running(unit))
    return buf


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--service')
    parser.add_argument('--timer')
    args = parser.parse_args()

    service = args.service
    timer = args.timer

    if timer:
        buf = get_info(timer + '.timer')

        if buf:
            print('{Id} {ActiveState}, last started {last}'.format(**buf))

    if service:
        buf = get_info(service + '.service')
        if buf:
            print('{Id} {ActiveState}, user {User}, group {Group}, '
                  'last started {last}'.format(**buf))


if __name__ == '__main__':
    main()
