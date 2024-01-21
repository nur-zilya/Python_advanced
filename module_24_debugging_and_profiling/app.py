from typing import List, Optional
import datetime
import sentry_sdk
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

sentry_sdk.init(
    dsn="https://dca573015b21f462057ab9d2625112f6@o4506609570152448.ingest.sentry.io/4506609573625856",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
@metrics.counter('requests', 'Number of requests')
def hello_world():
    1/0 # raises an error
    return "<p>Hello, World!</p>"


@app.route("/hello", methods=["GET"])
def hello():
    return f"Welcome"


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, threaded=True)