# app.py
import joblib
import numpy as np
from flask import Flask, request, render_template_string
from PIL import Image

app = Flask(__name__)

# Load model (savedmodel.pth must be present in the same folder)
data = joblib.load("savedmodel.pth")
model = data["model"]

HTML_PAGE = """
<!doctype html>
<title>Olivetti Face Classifier</title>
<h2>Upload an image (it will be converted to 64x64 grayscale)</h2>
<form method=post enctype=multipart/form-data action="/predict">
  <input type=file name=image>
  <input type=submit value="Upload & Predict">
</form>
{% if pred is not none %}
  <h3>Predicted class: {{ pred }}</h3>
{% endif %}
"""

def preprocess_image(file_stream):
    img = Image.open(file_stream).convert("L").resize((64, 64))
    arr = np.array(img, dtype=np.float32).reshape(1, -1) / 255.0
    return arr

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_PAGE, pred=None)

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return "No file uploaded", 400
    f = request.files["image"]
    X = preprocess_image(f.stream)
    pred = int(model.predict(X)[0])
    return render_template_string(HTML_PAGE, pred=pred)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
