from fastapi import FastAPI

from routes import routes

import uvicorn

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
app.include_router(routes, prefix="/api", tags=["api"])

if __name__ == "__main__":   
    uvicorn.run(app, host="127.0.0.1", port=8000)