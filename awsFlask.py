from flask import Flask, request, send_from_directory
import os
print(os.getcwd())
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/static/fota/bms/')
def send_bms():
    dir_list = os.listdir('static/fota/bms/')
    print(dir_list)
    return send_from_directory('static', "abc.txt")

if __name__ == "__main__":
    app.run()
