from flask import Flask
from flask import request
import shlex
import subprocess

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args = request.args.getlist("arg")
    safe_args = [shlex.quote(arg) for arg in args]
    command = shlex.split(f"ps {' '.join(safe_args)}")

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return f"<pre>{result.stderr}</pre>", 400

    return f"<pre>{result.stdout}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
