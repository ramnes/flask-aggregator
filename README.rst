Flask-Aggregator
================

.. image:: https://img.shields.io/pypi/v/flask-aggregator.svg

Batch the GET requests to your API into a single POST. Save requests latency and
reduce REST chatiness.

I was inspired by `this article
<http://tech.3scale.net/2013/04/18/accelerate-your-mobile-api-with-nginx-and-lua/>`_
from 3scale, and by `their NGINX aggregator
<https://github.com/solso/api-aggregator>`_ - but I wanted something simpler.


What does it do?
----------------

Flask-Aggregator adds an endpoint to your Flask application that handles
multiple GET requests in a single POST, and returns the response of each GET
request in a JSON stream.


What does that mean?
--------------------

It means that instead of sending multiple GET requests:

.. code-block:: sh

   -> GET /route1
   <- answer1
   -> GET /route2
   <- answer2
   -> GET /route3
   <- answer3


You can now just send a single POST that aggregates them all:

.. code-block:: sh

  -> POST /aggregate ["/route1", "/route2", "/route3"]
  <- {
         "/route1": answer1,
  <-     "/route2": answer2,
  <-     "/route3": answer3
     }


Why?
----

Mobile networks.


How to install?
---------------

.. code-block:: sh

    $ pip install flask-aggregator


How to setup my application?
----------------------------

.. code-block:: python

   from flask import Flask
   from flask_aggregator import Aggregator

   app = Flask(__name__)
   Aggregator(app=app, endpoint="/batch")


How to aggregate?
-----------------

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

Not really.

As of today, Flask-Aggregator executes the aggregated requests in a
synchronous manner, which makes it only useful if latency is a real issue and
response time is not, and that more than N requests are sent at the same time,
where N is maximum number of concurrent requests on user's client.

Also, it has limitations such has:

* no automatic caching mechanism browser-side, since it uses a POST request
* no header support at all for now, which means no cookie, etag, or whatever
* no other HTTP verb than GET is supported for now

Last but not least, chances are high that a lot of corner cases are not handled.


License
-------

MIT
