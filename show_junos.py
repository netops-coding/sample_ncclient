#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ncclient import manager

username = 'user1'
password = 'pass1'
ipv4 = '192.168.0.1'
port = 22

connection = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )

print connection.get_config(source='running')
