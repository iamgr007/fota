import requests
from github import Github
from flask import Flask,jsonify

app = Flask(__name__)

username = "iamgr007"
client = Github('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')

repo = '{}/fota'.format(username)
repository = f"https://github.com/{repo}"

repo = client.get_repo("iamgr007/fota")

iot_contents = repo.get_contents("/iot")

bms_files = []
iot_files = []
bms_latest = []
BMS_versions_available = []
Latest_version = []

def getLatestBMS():
    global BMS_versions_available
    BMS_versions_available = []
    bms_contents = repo.get_contents("/bms")
    for b in bms_contents:
        file = b.path
        bms_files.append(file.split("/")[1])
        content = file.split(".")
        if content[-1] == "BIN":
            BMS_fileName = content[0].split("_")
            bmsversion = BMS_fileName[-1].split()
            BMS_VersionNo = bmsversion[0].replace('V','')
            BMS_versions_available.append(int(BMS_VersionNo))
    print(max(BMS_versions_available))
    return(max(BMS_versions_available))

def getLatestIOT():
    global IOT_versions_available
    IOT_versions_available = []
    iot_contents = repo.get_contents("/iot")
    for t in iot_contents:
        file = t.path
        iot_files.append(file.split("/")[1])
        content = file.split(".")
        if content[-1] == "BIN":
            IOT_fileName = content[0].split("_")
            iotversion = IOT_fileName[-1].split()
            IOT_VersionNo = iotversion[0].replace('V','')
            IOT_versions_available.append(int(IOT_VersionNo))
    print(max(IOT_versions_available))
    return(max(IOT_versions_available))
# print("bin file", bms_files)
# print("versions available", BMS_versions_available)








@app.route('/')
def index():
    return "iamgr007"
#Welcome messages

@app.route("/fota/bms/<ver>", methods=['GET'])
def getBMS(ver):
    print(ver)
    ver = int(ver)
    Lastest_version = getLatestBMS()
    if ver<Lastest_version:
        print("update available")
        return jsonify({'update':1, 'file':getLatestBMS()})
    else:
        print("device already up to date")
        return jsonify({'update':0})

@app.route("/fota/iot/<ver>", methods=['GET'])
def getIOT(ver):
    print(ver)
    ver = int(ver)
    Lastest_version = getLatestIOT()
    if ver<Lastest_version:
        print("update available")
        return jsonify({'update':1, 'file':getLatestIOT()})
    else:
        print("device already up to date")
        return jsonify({'update':0})

@app.route("/fota/iot", methods=['GET'])
def get():
    return jsonify({'files':iot_files})
if __name__ == "__main__":
    app.run(debug=True)
