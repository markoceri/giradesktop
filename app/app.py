from fastapi import FastAPI

from app.routes import router

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
app.include_router(router)