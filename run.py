from app import app
import os

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8000, debug=app.config['DEBUG'])