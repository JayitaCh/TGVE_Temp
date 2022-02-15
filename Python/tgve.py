import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    print(path)
    print(app.static_folder)
    print(os.path.exists(app.static_folder))
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        print("Path branch")
        return send_from_directory(app.static_folder, path)
    else:
        print("index.html branch")
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
