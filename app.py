from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
    code = request.form["code"]
    try:
        result = subprocess.run(["python3", "-c", code], capture_output=True, text=True, timeout=5)
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
elif __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Use port 10000

