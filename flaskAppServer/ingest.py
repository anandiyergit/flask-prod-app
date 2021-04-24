from flask import Blueprint
import logging

bp = Blueprint('ingest',__name__,url_prefix='/ingest')

@bp.route('/greeting')
def greeting():
    logging.info('GET /ingest/greeting')
    return 'Hello this message is coming from ingest Blueprint.'