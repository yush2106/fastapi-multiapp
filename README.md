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

<pre lang="python">
pip install fastapi  #install FastAPI
pip install uvicorn  #install Uvicorn
pip install gunicorn  #install Gunicorn
</pre>

## Usage
`-k` worker type

`-w` number of worker processes

`-b` bind address and port

<pre lang="python">
gunicorn main:main_app -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000
</pre>