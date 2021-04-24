from flask import Blueprint
import logging

bp = Blueprint('query',__name__,url_prefix='/query')

@bp.route('/greeting')
def greeting():
    logging.info('GET /query/greeting')
    return 'Hello this message is coming from query Blueprint.'