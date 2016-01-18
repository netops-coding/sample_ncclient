# sample_ncclient
It's sample code for NETCONF using [ncclient](https://github.com/ncclient/ncclient).
It was posted blog for [Advent Calender of NetOpsCoding](http://qiita.com/advent-calendar/2015/netopscoding)(in Japanese).
http://qiita.com/taijijiji/items/394d6af5a71834c4e48a

# Install
```
sudo pip install ncclient
```

```
git clone git@github.com:netops-coding/sample_ncclient.git
```

# show_junos.py
It's code runs 'show configuration' command to JUNOS router.

How to run.

```
python show_junos.py
```

Output

```
<rpc-reply message-id="urn:uuid:xxxxxx-xxxxxx">
  <data>
    <configuration changed-seconds="1450593048" changed-localtime="2015-12-20 15:30:48 JST">
      <version>xx.xx.xx</version>
      <system>
        <host-name>router</host-name>
        <time-zone>Asia/Tokyo</time-zone>

       (snippet)
```

# set_junos.py
It's code runs to edit following configuration command to JUNOS router.

```
delete interfaces xe-0/0/0 disable
set interfaces xe-0/0/0 unit 0 family inet address 10.0.0.1/30
```

How to use

```
python set_junos.py
```

Output

```
========================================
Step 1. show running-config before commit
========================================
<rpc-reply message-id="urn:uuid:xxxxxx-xxxxxx">
  <data>
    <configuration commit-seconds="1450688416" commit-localtime="2015-12-21 18:00:16 JST" commit-user="user1">
      <interfaces>
        <interface>
          <name>xe-0/0/0</name>
          <disable/>
        </interface>
      </interfaces>
    </configuration>
  </data>
</rpc-reply>

========================================
Step 2. set config on candidate-config
========================================
<rpc-reply message-id="urn:uuid:xxxxxx-xxxxxx">
  <ok/>
</rpc-reply>

========================================
Step 3. validate candidate-config
========================================
<rpc-reply message-id="urn:uuid:xxxxxx-xxxxxx">
  <commit-results>
</commit-results>
  <ok/>
</rpc-reply>

========================================
Step 4. show config on candicate-config
========================================
<rpc-reply message-id="urn:uuid:xxxxxx-xxxxxx">
  <data>
    <configuration changed-seconds="1450688512" changed-localtime="2015-12-21 18:01:52 JST">
      <interfaces>
        <interface>
          <name>xe-0/0/0</name>
          <undocumented>
            <enable/>
          </undocumented>
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
  </data>
</rpc-reply>

========================================
Step 5. commit
========================================
Do you commit? y/n
y
========================================
Step 6. show running-config after commit
========================================
<rpc-reply message-id="urn:uuid:xxxxxx-xxxxxx">
  <data>
    <configuration commit-seconds="1450688535" commit-localtime="2015-12-21 18:02:15 JST" commit-user="user1">
      <interfaces>
        <interface>
          <name>xe-0/0/0</name>
          <undocumented>
            <enable/>
          </undocumented>
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
  </data>
</rpc-reply>
```
