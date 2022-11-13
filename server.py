from flask import Flask, request, jsonify, send_from_directory, abort, send_file
from flask_cors import CORS, cross_origin
from sentiment_analysis import SentimentAnalysis
import json
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import numpy as np
import io
# import cv2
from uuid import uuid4

MIN_CHARACTER_LENGTH = 100
MAX_CHARACTER_LENGTH = 50000

DEFINED_ERROR_TEXT_NOT_FOUND = "e-f055"
DEFINED_ERROR_TEXT_SHORTER_MIN = "e-1f80"
DEFINED_ERROR_TEXT_EXCEED_MAX = "e-c570"

app = Flask(__name__)
CORS(app, support_credentials=True)

SentiA = SentimentAnalysis()

def validate_input_field(request):
    if "text" in request.form.keys():
        data = request.form["text"]
    elif "file" in request.files.keys():
        f = request.files["file"]
        data = f.stream.read().decode("utf-8")
    else:
        return (
            jsonify(
                {
                    "code": DEFINED_ERROR_TEXT_NOT_FOUND,
                    "message": f"input text field not found",
                }
            ),
            400,
        )

    if len(data) < MIN_CHARACTER_LENGTH:
        return (
            jsonify(
                {
                    "code": DEFINED_ERROR_TEXT_SHORTER_MIN,
                    "message": f"input text field does not have enough {MIN_CHARACTER_LENGTH} characters",
                }
            ),
            400,
        )
    elif len(data) > MAX_CHARACTER_LENGTH:
        return (
            jsonify(
                {
                    "code": DEFINED_ERROR_TEXT_EXCEED_MAX,
                    "message": f"input text field exceeds {MAX_CHARACTER_LENGTH} characters",
                }
            ),
            400,
        )
    return data

@app.route("/sentiment-analysis", methods=["POST"])
@cross_origin(supports_credentials=True)
def sentiment_analysis_route():
    data = validate_input_field(request=request)
    if data != "":
        out = SentiA.inference(data)
        # print("data = ", data)

        print("OUT = ", out )
    if isinstance(data, tuple):
        import ipdb; ipdb.set_trace()
        return out
    else:
        # return {"sentiment": -0.286}
        out = json.dumps(out)
        return out


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8001)