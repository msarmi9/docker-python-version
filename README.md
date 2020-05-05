__What?__

This repo provides two Dockerfiles that provide examples of how to specify the python interpreter used to run a simple Flask app inside a container:

* `Dockerfile36` (runs the app with `python3.6.x`)
* `Dockerfile37` (runs the app with `python3.7.x`)

__Why?__

Docker can get tricky. This repo aims to help clarify the usage of a specific python version inside a running container. If you look closely, you'll notice that both `Dockerfiles` install `python3.7` along with `python3-pip`. However, `Dockerfile36` installs packages with `pip3`, which is associated with the `python3.6.x` version that comes bundled with it in `python3-pip`. On the other hand, `Dockerfile37` explicitly installs packages using the `pip` belonging to `python3.7`.  

When we launch our app with `flask run`, we're implicitly using the python version used to install that instance of `flask`. This means `Dockerfile36` will run the app with `python3.6.x` and `Dockerfile37` will run it with `python3.7.x`  

__How?__

The `flask` app just displays the python version used to invoke it on the homepage. To launch the app you can use:

* `docker-compose up web36`
* `docker-compose up web37`
