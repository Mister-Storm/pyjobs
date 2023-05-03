from fastapi import FastAPI

from pyjobs.web.api import router

server = FastAPI(debug=True)

server.include_router(router)
