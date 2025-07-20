from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(
  title="App1 API",
  summary="App1 API documentation",
  description="This is the API for App1",
  version="1.0"
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
  """
  App1 main page.
  """
  return "<h1>Hello, App1</h1>"  #hello response

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)