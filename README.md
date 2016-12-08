# apache-flask-wsgi

## Description
Apache WSGI config to host multiple Flask sites
* Multithreaded
* Applications are in their own directories
* Each has their own virtualenv
* Apache listens on port 80 or port 443 and each site is a sub directory:
```
http://<IP>/app1
http://<IP>/app2
http://<IP>/app3
```

## Results
Example includes 3 Flask sites all with the same page:
```
app1/
  * result: Hello World from app1!
app2/
  * result: Hello World from app2!
app3/
  * result: Hello World from app3!
```
## Prerequisites
* yum install httpd mod_wsgi.x86_64

## Postrequisites
* create venv for each application and pip install flask
```
cd /var/www/wsgi/app1; virtualenv venv; source venv/bin/activate; pip install flask
```

For SSL, you can generate a private key and crt:
```
[root@dropbox flask-https]# openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
Generating a 2048 bit RSA private key
.....................................................................+++
...................................+++
writing new private key to 'server.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:US
State or Province Name (full name) []:VT
Locality Name (eg, city) [Default City]:Burlington
Organization Name (eg, company) [Default Company Ltd]:IPAs for Everyone
Organizational Unit Name (eg, section) []:
Common Name (eg, your name or your server's hostname) []:flask
Email Address []:
```

Then place server.key and server.crt in /etc/ssl/crt/ 


## Files
* wsgi.conf - put in /etc/httpd/conf.d/ for HTTP config
* wsgi-ssl.conf - put in /etc/httpd/conf.d/ for SSL config
* ssl.conf - example ssl.conf to put in /etc/httpd/conf.d/ for SSL config
* app(x)/app.wsgi - wsgi config for site app<x>
* app(x)/app.py - flask site for app<x>
