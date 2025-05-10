from flask import Blueprint, Response, abort, current_app, request
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    generate_latest,
    multiprocess,
)

metrics_bp = Blueprint("metrics", __name__, url_prefix="/metrics")


@metrics_bp.before_request
def restrict_metrics_access():
    """Restrict /metrics access to authorized IPs only."""
    authorized_ips = current_app.config["AUTHORIZED_METRICS_IPS"]
    if request.remote_addr not in authorized_ips:
        abort(403)


@metrics_bp.route("/")
def prometheus_metrics():
    """Give access to prometheus metrics."""
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)
