Flask-Aggregator
================

Batch the GET requests to your REST API into a single POST!


What does it do?
----------------

Flask-Aggregator adds an endpoint to your Flask application that handles
multiple GET requests in a single POST, and returns the reponse of each GET
request in a single JSON answer.


How to setup my application?
----------------------------

.. code-block:: python

   from flask import Flask
   from flask_aggregator import Aggregator

   app = Flask(__name__)
   Aggregator(app=app, endpoint="/batch")


How to aggregate?
-----------------------------------

.. code-block:: sh

   $ python example.py
   [go to another shell]
   $ curl -H "Content-type: application/json" -X POST 127.0.0.1:5000/batch \
                --data-raw '["/hello/world", "/hello/ramnes?question=Sup?"]'
   {
       "/hello/world": "Hello, world!",
       "/hello/ramnes?question=Sup?": "Hello, ramnes! Sup?"
   }


Is it ready for production yet?
-------------------------------

Well, read the source code and decide by yourself!

Chances are high that a lot of corner cases are not handled.
