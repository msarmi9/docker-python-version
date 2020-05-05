This repo provides two Dockerfiles that provide examples of how to specify the python interpreter used to run a simple Flask app inside a container:

* `Dockerfile36` runs the app with `python3.6.x`
* `Dockerfile37` runs the app with `python3.7.x`


The `flask` app just displays the python version used to invoke it on the homepage. To launch the app you can use:

* `docker-compose up web36`
* `docker-compose up web37`

