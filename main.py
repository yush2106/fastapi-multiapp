from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
#Import App1 and App2
from App1.app1 import app as app1
from App2.app2 import app as app2

main_app = FastAPI(
  title="Main API",
  summary="Main API documentation",
  description="This is the Main API",
  version="1.0"
)

main_app.mount("/app1", app1)  # Mount App1
main_app.mount("/app2", app2)  # Mount App2

@main_app.get("/", response_class=HTMLResponse)
async def read_root():
  """
  Main API page.
  """
  return "<h1>Hello, Main API</h1>"  #hello response

if __name__ == "__main__":
  uvicorn.run(main_app, host="0.0.0.0", port=8000)