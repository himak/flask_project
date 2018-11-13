# flask_project

## Config APP

Install virtual machine from vagrant config file:
```sh
$ vagrant up
```

SSH access to virtual machine for terminal (default username and password is "vagrant"):
```sh
$ vagrant ssh
```

Synchronized source files in host machine are located in virtual machine:
```sh
$ cd /vagrant/
```

Create VirtualEnv
```sh
$ virtualenv venv
$ . venv/bin/activate
```

Install Flask
```sh
$ pip install flask
```

## Start APP

View your IP address
```sh
$ ifconfig
```

Activate VirtualEnv
```sh
$ . venv/bin/activate
```

Run App
```sh
$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0
```

or

```sh
$ python run.py
```

Open your favorite browser in your host machine and open URL:
```sh
http://YOUR_IP_ADDRESS:5000
```
now you should see "Hello World"
