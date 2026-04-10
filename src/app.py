from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "unknown")
    environment = os.getenv("APP_ENV", "unknown")

    return f"""
    <h1>Artemis Simple App</h1>
    <p><b>Version:</b> {version}</p>
    <p><b>Environment:</b> {environment}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)