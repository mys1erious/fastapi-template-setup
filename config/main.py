import hupper
from fastapi import FastAPI

from config.runner import run
from src.core.routes import router as core_router


app = FastAPI()


app.include_router(core_router)


if __name__ == "__main__":
    reloader = hupper.start_reloader('runner.run')
    run()
