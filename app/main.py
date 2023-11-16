import uvicorn

from fastapi import FastAPI

from routes import api, desktop
from routes.devices import elio

app = FastAPI(
    title="GiraDesktp",
    description=(
        "A physical device to switch across your virtual desktops."
        " Project page: https://github.com/markoceri/giradesktop."
    ),
    version="1.0.0",
    docs_url="/",
    redoc_url="/docs"
)

# Include routers.
app.include_router(api.router, prefix="/api", tags=["api"])
app.include_router(desktop.router, prefix="/api", tags=["desktop"])
app.include_router(elio.router, prefix="/api", tags=["devices"])

if __name__ == "__main__":   
    uvicorn.run(app, host="0.0.0.0", port=8000)