from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("../models/2")
CLASS_NAMES = ["glioma tumor", "meningioma tumor", "no tumor", "pituitary tumor"]


def read_file_as_img(data) -> np.ndarray:
    img = Image.open(BytesIO(data))
    img = img.resize((512, 512))
    return np.array(img).astype(np.float32)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_img(await file.read())
    img_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(img_batch)
    pred_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": pred_class, "confidence": float(confidence)}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
