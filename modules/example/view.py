from flask import Blueprint
from models import Msg

example = Blueprint('example',
                    __name__,
                    url_prefix='/',
                    template_folder='templates',
                    static_folder='static')


@example.route("/")
def example_app():
    """Simple function to test example"""
    a = Msg.query.all()
    msg = ''
    for i in a:
        msg += i.name

    return f"Hello World: {msg}"
