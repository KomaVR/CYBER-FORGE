---
title: "Flask-SocketIO documentation"
description: "
Start the app
$ python3 thephish_app.py

The server that will be used to run the application is the WSGI server provided by eventlet, since it is listed in the requirements. It is needed for the WebSocket protocol to work and avoid falling back to HTTP long polling. Without eventlet, the default Flask WSGI server (Werkzeug) will be used.
If you wish to use another WSGI server (e.g. Gunicorn) or use a reverse proxy (e.g. NGINX), the  explains how to do that.
Now the application should be reachable at http://localhost:8080.
⚠️ Warning: If you are using Mozilla Firefox to use ThePhish and for some reason an error message appears during the analysis, the solution may be found here.
"
url: "https://flask-socketio.readthedocs.io/en/latest/deployment.html"
category: "Web Exploitation"
---
