from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(
  title="App2 API",
  summary="App2 API documentation",
  description="This is the API for App2",
  version="1.0"
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
  """
  App2 main page.
  """
  return "<h1>Hello, App2</h1>"  #hello response

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)