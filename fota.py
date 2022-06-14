import requests
from flask import Flask,jsonify,request, send_from_directory
import os
import logging
import ast

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')

BMS_versions_available = []
IOT_versions_available = []

def getLatestBMS():
    global BMS_versions_available
    BMS_versions_available = []
    bms_contents = os.listdir('static/fota/bms/')
    print(bms_contents)
    for b in bms_contents:
        bmsversion = b.split('.')[0]
        print(bmsversion)
        BMS_Version = bmsversion.replace('V','')
        print(BMS_Version)
        temp = BMS_Version.replace('B','')
        BMS_VersionNo_HEX = '0x'+str(temp)
        print(BMS_VersionNo_HEX)
        BMS_VersionNo_INT = ast.literal_eval(BMS_VersionNo_HEX)
        print(BMS_VersionNo_INT)
        BMS_versions_available.append(int(BMS_VersionNo_INT))
    print(max(BMS_versions_available))
    return(max(BMS_versions_available))

def getLatestIOT():
    global IOT_versions_available
    IOT_versions_available = []
    iot_contents = os.listdir('static/fota/iot/')
    print(iot_contents)
    for t in iot_contents:
        iotversion = t.split('.')[0]
        IOT_VersionNo = iotversion.replace('V','')
        IOT_versions_available.append(int(IOT_VersionNo))
    print(max(IOT_versions_available))
    return(max(IOT_versions_available))

@app.route('/')
def default_route():
    """Default route"""
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')
    return jsonify('iamgr007')


@app.route("/fota/bms/", methods=['GET'])
def getBmsFiles():
    return jsonify({'files':str(os.listdir('static/fota/bms/'))})

@app.route("/fota/iot/", methods=['GET'])
def getIotFiles():
    return jsonify({'files':str(os.listdir('static/fota/iot/'))})

@app.route("/fota/bms/<ver>", methods=['GET'])
def getBMS(ver):
    print(ver)
    try:
        tmp = '0x'+str(ver)
        verINT = ast.literal_eval(tmp)
        print(verINT)
        Lastest_version = getLatestBMS()
        if verINT<Lastest_version:
            print("update available")
            return jsonify({'update':1, 'file':getLatestBMS()})
        else:
            print("device already up to date")
            return jsonify({'update':0})
    except:
        print("invalid request")
        return jsonify({'update':0})

@app.route("/fota/iot/<ver>", methods=['GET'])
def getIOT(ver):
    print(ver)
    try:
        ver = int(ver)
        Lastest_version = getLatestIOT()
        if ver<Lastest_version:
            print("update available")
            return jsonify({'update':1, 'file':getLatestIOT()})
        else:
            print("device already up to date")
            return jsonify({'update':0})
    except:
        print("invalid request")
        return jsonify({'update':0})


@app.route("/fota/iot/dwn/<path:path>", methods=['GET'])
def downloadIOT(path):
    return send_from_directory('static/fota/iot', path)

@app.route("/fota/bms/dwn/<path:path>", methods=['GET'])
def downloadBMS(path):
    return send_from_directory('static/fota/bms', path)

if __name__ == "__main__":
    logHandler = logging.FileHandler('fota.log')
    logHandler.setLevel(logging.INFO)
    app.logger.addHandler(logHandler)
    app.logger.setLevel(logging.INFO)
    app.run(debug=True,port=8080)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
