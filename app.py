from flask import Flask, render_template, request, send_file
from ambient import generate_ambient_tone
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tone_path = None
    if request.method == "POST":
        mood = request.form.get("mood", "relax")
        tone_path = generate_ambient_tone(mood, filename="static/tones/preview.wav")
    return render_template("index.html", tone_path=tone_path)

@app.route("/download")
def download():
    return send_file("static/tones/preview.wav", as_attachment=True, download_name="your_tone.wav")

if __name__ == "__main__":
    os.makedirs("static/tones", exist_ok=True)
    app.run(debug=True)
