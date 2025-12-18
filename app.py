import os
import warnings
import pickle
import numpy as np
from flask import Flask, request, render_template
from feature import FeatureExtraction

warnings.filterwarnings("ignore")

# ---------------------------
# Load ML model (Render-safe)
# ---------------------------
MODEL_PATH = "pickle/model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Flask App
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        # Extract features
        extractor = FeatureExtraction(url)
        features = np.array(extractor.getFeaturesList()).reshape(1, -1)

        # Predict
        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0]

        prob_phishing = prob[0]         # Unsafe
        prob_legitimate = prob[1]       # Safe

        return render_template(
            "index.html",
            xx=round(prob_legitimate, 2),
            url=url
        )

    return render_template("index.html", xx=-1)

# ---------------------------
# Render Deployment Settings
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
