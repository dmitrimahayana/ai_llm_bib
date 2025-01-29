from security.authentication import *
import time


@app.post("/")
async def root_endpoint():
    message = "connected"
    return {"message": message}


@app.post("/health_check")
def health_check():
    message = "Fastapi is working... Git last push at 2025-01-29 20:23"
    start_time = time.time()
    elapsed_time = round(time.time() - start_time, 2)
    return {
        "message": message,
        "response_time": elapsed_time
    }