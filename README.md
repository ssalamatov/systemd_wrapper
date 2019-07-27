Wrapper for systemd service and timer
Examples:

timer:
  in: info.py --timer apt-daily
  out: apt-daily.timer inactive, last started Mon 2019-07-01 11:23:24 MSK

service:
  in: info.py --service sshd
  out: sshd.service active, user None, group None, last started Fri 2019-04-12 19:14:06 MSK
