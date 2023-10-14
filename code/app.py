from flask import Flask, render_template
from controllers.animals_controller import animals_blueprint
import os

app = Flask(__name__)

app.register_blueprint(animals_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4999))
    app.run(host='0.0.0.0', port=port)

