import psutil
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None

    if cpu_percent > 80 or mem_percent > 80:
        message = "High cpu or memory utilization!"

    return f"CPU Utilization: {cpu_percent}" \
           f" and Memory Utilization : {mem_percent}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')