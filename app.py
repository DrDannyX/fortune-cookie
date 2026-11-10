import random
from flask import Flask, render_template, request

app = Flask(__name__)

MODES = {
    "engineering": "engineering-fortunes.txt",
    "general":     "general-fortunes.txt",
    "lawyer":      "lawyer-fortunes.txt",
}

def load_fortunes(mode):
    with open(MODES[mode], "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    if mode == "general":
        # Strip leading "N→" number prefix
        lines = [line.split("→", 1)[-1].strip() if "→" in line else line for line in lines]
    return lines

@app.route("/")
def index():
    mode = request.args.get("mode", "engineering")
    if mode not in MODES:
        mode = "engineering"
    fortunes = load_fortunes(mode)
    fortune = random.choice(fortunes)
    return render_template("index.html", fortune=fortune, mode=mode)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
