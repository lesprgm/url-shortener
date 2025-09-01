from flask import Flask, request, render_template, redirect, url_for, flash
import json, os, re, string, random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages
DATA_FILE = "storage.json"

# Load data
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Generate unique short ID
def generate_id(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Validate URL
def valid_url(url):
    pattern = re.compile(
        r'^(http|https)://'  # must start with http:// or https://
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # domain
    )
    return re.match(pattern, url)

@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()
    count = len(data)

    if request.method == "POST":
        full_url = request.form["url"]

        if not valid_url(full_url):
            flash("Invalid URL. Please enter a valid one starting with http:// or https://")
            return redirect(url_for("index"))

        # Check if already exists
        for short_id, stored_url in data.items():
            if stored_url == full_url:
                flash(f"URL already shortened: {request.host_url}{short_id}")
                return redirect(url_for("index"))

        # Generate a unique short ID
        short_id = generate_id()
        while short_id in data:
            short_id = generate_id()

        data[short_id] = full_url
        save_data(data)

        flash(f"Shortened URL: {request.host_url}{short_id}")
        return redirect(url_for("index"))

    return render_template("index.html", count=count)

@app.route("/<short_id>")
def redirect_url(short_id):
    data = load_data()
    if short_id in data:
        return redirect(data[short_id])
    else:
        flash("Invalid shortened URL!")
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
