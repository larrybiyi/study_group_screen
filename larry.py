
#!usr/bin/env python

import getpass
import telnetlib

HOST = "10.10.10.116"
user = input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"term length 0\n")
tn.write(b"show version\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii"))
