import requests
from github import Github
from flask import Flask,jsonify

app = Flask(__name__)

username = "iamgr007"
client = Github('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')

repo = '{}/fota'.format(username)
repository = f"https://github.com/{repo}"

repo = client.get_repo("iamgr007/fota")



bms_files = []
iot_files = []
bms_latest = []
# BMS_versions_available = []
Latest_version = []

def getLatestBMS():
    global BMS_versions_available
    BMS_versions_available = []
    bms_contents = repo.get_contents("/bms")
    print(bms_contents)
    for b in bms_contents:
        file = b.path
        bms_files.append(file.split("/")[1])
        content = file.split("/")
        if content[-1].split(".")[1] == "BIN":
            # BMS_fileName = content[0].split("_")
            bmsversion = content[-1].split('.')[0]
            BMS_VersionNo = bmsversion.replace('V','')
            BMS_versions_available.append(int(BMS_VersionNo))
    print(max(BMS_versions_available))
    return(max(BMS_versions_available))

def getLatestIOT():
    global IOT_versions_available
    IOT_versions_available = []
    iot_contents = repo.get_contents("/iot")
    print(iot_contents)
    for t in iot_contents:
        file = t.path
        iot_files.append(file.split("/")[1])
        content = file.split("/")
        if content[-1].split(".")[1] == "BIN":
            # IOT_fileName = content[0].split("_")
            iotversion = content[-1].split('.')[0]
            IOT_VersionNo = iotversion.replace('V','')
            IOT_versions_available.append(int(IOT_VersionNo))
    print(max(IOT_versions_available))
    return(max(IOT_versions_available))
# print("bin file", bms_files)
# print("versions available", BMS_versions_available)



@app.route('/')
def index():
    return "iamgr007"
#Welcome messages

@app.route("/fota/bms/", methods=['GET'])
def getBmsFiles():
    return jsonify({'files':str(repo.get_contents("/bms"))})

@app.route("/fota/iot/", methods=['GET'])
def getIotFiles():
    return jsonify({'files':str(repo.get_contents("/iot"))})

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


@app.route("/fota/iot", methods=['GET'])
def get():
    return jsonify({'files':iot_files})
if __name__ == "__main__":
    app.run(debug=True)
