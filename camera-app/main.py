import io
import time
from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse
from picamera2 import Picamera2

app = FastAPI()
picam2 = None

@app.on_event("startup")
def startup_event():
    global picam2
    picam2 = Picamera2()
    config = picam2.create_video_configuration(main={"size": (1280, 720)})
    picam2.configure(config)
    picam2.start()

@app.on_event("shutdown")
def shutdown_event():
    picam2.stop()
    picam2.close()

@app.get("/image")
def get_image():
    data = io.BytesIO()
    picam2.capture_file(data, format="jpeg")
    return Response(content=data.getvalue(), media_type="image/jpeg")

def mjpeg_generator():
    while True:
        # Capture JPEG into memory
        frame = io.BytesIO()
        picam2.capture_file(frame, format="jpeg")

        # Yield MJPEG frame
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" +
            frame.getvalue() +
            b"\r\n"
        )

        time.sleep(0.05)  # ~20 FPS (adjust as needed)

@app.get("/stream")
def stream():
    return StreamingResponse(
        mjpeg_generator(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
