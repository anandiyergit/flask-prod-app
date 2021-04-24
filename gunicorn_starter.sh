#!/bin/sh

# Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. 
# It's a pre-fork worker model. 
# The Gunicorn server is broadly compatible and simply implemented.
# Its light on server resources, and fairly speedy.

# Here we will be spinning up multiple threads with multiple worker processess(-w) and perform a binding.
gunicorn flaskAppServer:"create_app()" -w 2 --threads 2 -b 0.0.0.0:8003