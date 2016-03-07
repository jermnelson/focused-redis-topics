"""Focused Redis Topics Course Website"""
__author__ = "Jeremy Nelson"

from flask import Flask, render_template, url_for

course = Flask(__name__)

@course.route("/help-downloads")
def help_and_downloads():
    return render_template("help-and-downloads.html")

@course.route("/open-badge")
def badge():
    return render_template("open-badge.html")

@course.route("/<day>/")
@course.route("/<day>/<topic>")
def show_topic(day, topic=None):
    if topic is None:
        return render_template("{}.html".format(day))
    return render_template("{}/index.html".format(topic))


@course.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    course.run(host='0.0.0.0', port=5001, debug=True)
