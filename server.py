# -*- Coding: utf-8 -*-
from typing import Any

from flask import Flask
from flask import jsonify
from services.api_shodan import ShodanAPI

app = Flask(__name__)


@app.route(r'/api/')
@app.route(r'/api/<keyword>/')
@app.route(r'/api/<keyword>/<int:count>')
def api_hosts(keyword: str = None, count: int = 10) -> Any:
    if not keyword:
        return "You must specify a keyword to search for any host.", 200

    hosts = ShodanAPI().get_results(keyword)
    hosts['matches'] = hosts['matches'][:count]
    hosts['total'] = len(hosts['matches'])

    return jsonify({'data': hosts}), 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)
