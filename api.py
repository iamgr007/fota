from flask import Flask,jsonify

app = Flask(__name__)

files = [{'name':"BMS_V0.BIN",
        'version':"0",
        'Description':"This is the first version of the BMS",
        'filename':"BMS_V0"},
        {'name':"BMS_V1.BIN",
        'version':"1",
        'Description':"This is the second version of the BMS",
        'filename':"BMS_V1"}]

@app.route('/')
def index():
    return "iamgr007"
#Welcome messages

@app.route("/files", methods=['GET'])
def get():
    return jsonify({'files':files})
# http://127.0.0.1:5000/files gives the version details of all files

@app.route('/files/<int:version>',methods=['GET'])
def get_course(version):
    return jsonify({'version': files[version]})
# http://127.0.0.1:5000/files/0 gives the version details of file[0]

@app.route('/files', methods=['POST'])
def create():
    file = {'name':"BMS_V2.BIN",
            'version':"2",
            'Description':"This is the third version of the BMS",
            'filename':"BMS_V2"}
    files.append(file)
    return jsonify({'uploaded': file})
# doing 'curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/files'
#updates/posts new file in files

@app.route('/files/<int:version>', methods=['PUT'])
def update_version(version):
    files[version]['Description'] = "just messing with it"
    return jsonify({'file':files[version]})
# doing 'curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/files/0'
#updates the description of file[version]

@app.route('/files/<int:version>', methods=['DELETE'])
def delete(version):
    files.remove(files[version])
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run(debug=True)

ota/bms/V185
#if file exists
{
  "update": 1,
  "filename": "V187"
}

#if file edoesnt xist
{
  "update": 0
}
