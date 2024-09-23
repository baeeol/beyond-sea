from flask import Flask
from routes import router

app = Flask(__name__)

app.register_blueprint(router.router_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
