import socket
import sys
import platform
import os
from flask import Flask, jsonify
from flask import Blueprint

bp = Blueprint("root", __name__,  url_prefix="/")

@bp.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"}), 200


@bp.route("/info", methods=["GET"])
def info():
    return jsonify(
        {
            "hostname": socket.gethostname(),
            "kernel": platform.release(),
            "os": sys.platform,
            "python-version": sys.version,
        }
    ), 200
