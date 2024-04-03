import logging
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

flaskapp = Flask(__name__)
metrics = PrometheusMetrics(flaskapp)
metrics.info("app_info", "flaskapp Info", version="1.0.0")

@flaskapp.route("/")
def index():
    return 'Flask x Prometheus x Grafana !'
