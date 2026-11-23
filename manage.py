# -*- coding: utf-8 -*-

from application import create_app
from application.extensions import db

app = create_app('default')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(host='0.0.0.0', port=7345, debug=True)