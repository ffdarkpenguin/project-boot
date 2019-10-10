# -*- coding: utf-8 -*-

import logging
import os

from flask import Flask, jsonify

be_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(be_dir)

log_level = logging.DEBUG
log_file = be_dir + "/logs/app.log"

logging.basicConfig(
    level=log_level,
    filename=log_file,
    format="%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger('app')
logger.info("Inicializando sistema...")

# Cria APP
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config["UPLOAD_FOLDER"] = project_dir + "/upload"
# app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route("/", methods=["GET"])
def config():
    return jsonify({"ok": True, "msg": "Sistema online"})


logger.info("Sistema pronto para receber requisições...")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
