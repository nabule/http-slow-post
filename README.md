# About

This repository is a part of laboratory work and implementation of **slow POST** attack by breaking a **FLASK** application with multiple slow clients.

## Website Target

Target is a **flask** aplication hosted on a Linux server in a virtual machine with following parameters

* Virtual Machine
* Ubuntu Server x64
* 1024 MB RAM
* 1 Core
* Flask application with a POST request

### Dependencies

Application needs python and flask library for python. For ubuntu you can simply run followings:

```bash
apt-get install python2.7 python-pip
```

```bash
pip install flask
```

### Usage

```bash
python main.py
```

## Attacker

To simulate this DDOS, I have created a **GO** which opens multiple connections and sends content with a given interval, byte by byte.

### Dependencies

Application has dependency only on **GO** compiler. So, you need just to install it and that's all.

### Usage

```bash
go run attack.go <host> <port> <path> <contentSize> <interval> <clients>
```

# Simulation

In order to demonstrate how it works, we should configure our server 

## Server

```bash
$ python main.py 2> /dev/null & # start flask server and continue, don't block until end
$ htop # to monitor resources
```

## Client

Running following command we will
```bash
go run attack.go 192.168.100.6 5000 / 10000 100 50
```

attack target *192.168.100.6* on port *5000* by making POST on "/" resource.
Application will open 50 connections and will send 10k bytes of content with speed of 1byte/100ms.

## Results

Here is results I have obtained

| Bytes | Interval | Connections | CPU  | RAM    |
|-------|----------|-------------|------|--------|
| 10k   | 10ms     | 10          | 5%   | 76MB + |
| 10k   | 10ms     | 50          | 20%  | 80MB+  |
| 10k   | 10ms     | 200         | 84%  | 100MB+ |
| 10k   | 10ms     | 300         | 100% | 110MB+ |

**NOTE** : RAM is not increasing much as it grows with time, when all bytes are transferred. 

!(htop on last test)(/screenshots/htop-max.png)

## Conclusion

In this laboratory I had created a attacker tool which will open a conneciton with a server and send slowly POST data to server. By sending slow, we create a pool of connections and maintain it. In this conditions, server allocates resources and channels for receiving our data, which comes very slow. New connections are ignored, if we reach max connections limit set on the server. Otherwise, new connections are just very slow and annoying. On the last test, server was very slow, even `htop` had lags. Also, we should keep in considerations how many bytes we are allowed to send to attacked target.