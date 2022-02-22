import requests
from flask import Flask,jsonify,request, send_from_directory
import os
app = Flask(__name__)

BMS_versions_available = []
IOT_versions_available = []

def getLatestBMS():
    global BMS_versions_available
    BMS_versions_available = []
    bms_contents = os.listdir('static/fota/bms/')
    print(bms_contents)
    for b in bms_contents:
        bmsversion = b.split('.')[0]
        BMS_VersionNo = bmsversion.replace('V','')
        BMS_versions_available.append(int(BMS_VersionNo))
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
def index():
    return "iamgr007"
#Welcome messages

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
        ver = int(ver)
        Lastest_version = getLatestBMS()
        if ver<Lastest_version:
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
    app.run(debug=True,port=8080)
