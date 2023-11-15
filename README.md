# page-tracker


##### A project using Docker create a robust continious integration pipeline for a Flask web application. The web app is a simple page for tracking views stored persistently in a Redis data store.



#### Project Architecture 
The application consists of two Docker containers, The first container will run a Flask application on top of Gunicorn, responding to HTTP requests and updating the number of page views. The second container will run a Redis instance for storing page view data persistently in a local volume on the host machine.

* Project developed by Bartosz Zaczyński and is located at https://realpython.com/docker-continuous-integration/