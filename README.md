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

Create Virtualenv
```sh
$ virtualenv venv
```

Install Flask
```sh
$ pip install flask
```

## Start APP

Start Vagrant box
```sh
$ vagrant up
$ vagrant ssh
```

View your IP address
```sh
$ ifconfig
```

Activate VirtualEnv
```sh
$ cd /vagrant/
$ . venv/bin/activate
```

Run App
```sh
<<<<<<< HEAD
$ python run.py
=======
$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0
>>>>>>> 40e9d354849a5701fbaf55651fd03648b478f234
```

or

```sh
$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0
```

Open your favorite browser in your host machine and open URL:
```sh
http://YOUR_IP_ADDRESS:5000
```
now you should see "Hello World"
