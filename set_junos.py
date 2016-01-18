#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ncclient import manager

username = 'user1'
password = 'pass1'
ipv4 = '192.168.0.1'
port = 22

connection = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )


print '='*40
print 'Step 1. show running-config before commit'
print '='*40

request_config_interface = """
<configuration>
    <interfaces>
        <interface>
            <name>xe-0/0/0</name>
        </interface>
    </interfaces>
</configuration>"""

print connection.get_config(source='running', filter=('subtree', request_config_interface) )


print '='*40
print 'Step 2. set config on candidate-config'
print '='*40

request_set_config_interface = """
<config>
    <configuration>
         <interfaces>
            <interface>
                <name>xe-0/0/0</name>
                <enable/>
                <unit>
                    <name>0</name>
                    <family>
                        <inet>
                            <address>
                                <name>10.0.0.1/30</name>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
        </interfaces>
    </configuration>
</config>
"""

print connection.edit_config(target='candidate', config=request_set_config_interface)


print '='*40
print 'Step 3. validate candidate-config'
print '='*40

print connection.validate(source='candidate')


print '='*40
print 'Step 4. show config on candicate-config'
print '='*40

print connection.get_config(source='candidate', filter=('subtree', request_config_interface) )


print '='*40
print 'Step 5. commit'
print '='*40
print 'Do you commit? y/n'
choice = raw_input().lower()
if choice == 'y':
    connection.commit()
else:
    connection.discard_changes()


print '='*40
print 'Step 6. show running-config after commit'
print '='*40

print connection.get_config(source='running', filter=('subtree', request_config_interface) )


if connection:
    connection.close_session()
