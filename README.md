# fastapi-multiapp
When you want to mount multiple FastAPI apps simultaneously on a Linux Ubuntu, try this example approach.

In this resposity, use a main API to mount multi-apps from different paths.

## Deployment Path
| Project Path | File  | Description  |
|---|---|---|
| `Project/` | main.py    | Main API to mount apps |
| `Project/App1/`  | app1.py    | The app 1 |
| `Project/App2/`  | app2.py    | The app 2 |

## Installation

<pre lang="bash">
pip install fastapi  #install FastAPI
pip install uvicorn  #install Uvicorn
pip install gunicorn  #install Gunicorn
</pre>

## Usage
Gunicorn is a web server, use this commad to start the UvicornWorker to serve FastAPI.

<pre lang="bash">
gunicorn main:main_app -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000
</pre>

`-k` worker type

`-w` number of worker processes

`-b` bind address and port