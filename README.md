# hallervote
a voting system built with python and twilio

## instructions

* spin up digital ocean box
* ssh to it

```
    wget https://github.com/sachee/hallervote/archive/master.tar.gz
    tar xzf master.tar.gz
    cd hallervote-master
```

Uncomment the last line of vote.py and delete the line above it.

```
    apt install python-pip util-linux
    pip install --upgrade pip
    pip install -r requirements.txt
    setsid python vote.py
```

* go to twilio, buy a phone number
* set it to use TwiML and paste in digital ocean ip
* test via text. rm votes.dat to reset
