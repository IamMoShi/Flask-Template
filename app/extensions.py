from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
metrics = PrometheusMetrics(
    None,
    group_by="endpoint",
    defaults_prefix="flask",
    path=None,
    defaults={"histogram": True},
)
