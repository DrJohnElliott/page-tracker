# src/page_tracker/app.py

import os
from functools import cache

from flask import Flask, render_template
from redis import Redis, RedisError

app = Flask(__name__)

from flask_autodoc import Autodoc

auto = Autodoc(app) 

@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{thinking face}", 500
    page_messages = f"This page has been seen {page_views} times."
    return render_template('index.html'), page_messages


@cache
def redis():
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
