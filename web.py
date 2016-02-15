"""Focused Redis Topics Course Website"""
__author__ = "Jeremy Nelson"

from flask import Flask, render_template, url_for

course = Flask(__name__)

@course.route("/Day <day>/<topic>")
def show_topic(day, topic):
    return render_template("{}/index.html".format(topic))


@course.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    course.run(host='0.0.0.0', port=20160, debug=True)
