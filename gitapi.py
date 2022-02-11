#Git application

import requests
# import base64
from github import Github

BMS_Version_IN = "BMS_V186"
IOT_Version_IN = "IOT_V186"
Input = ["BMS_V186", "IOT_V186"]
ProcessedInput = []
username = "iamgr007"
client = Github('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')
# url = f"https://api.github.com/users/{username}"
# user_data = requests.get(url).json()
# pprint(user_data)
# g=Github()
# user=client.get_user(username)
# repos = user.get_repos()
# repoName = client.get_repo("iamgr007/fota")
# # print("repo:", repo)
repo = '{}/fota'.format(username)
# # print("{}/fota".format(url))
# # repoName = "fota"
repository = f"https://github.com/{repo}"
# print(repository)

repo = client.get_repo("iamgr007/fota")
bms_contents = repo.get_contents("/bms")
iot_contents = repo.get_contents("/iot")
# print(contents)
# https://github.com/iamgr007/fota/blob/main/BMS_V0.BIN
# https://github.com/iamgr007/fota/raw/main/bms/BMS_V186.BIN

# BMS_IN = BMS_Version_IN.split("_")
# BMS_VersionNo_IN = BMS_IN[-1].replace('V','')
# print("Exisiting BMS Version : ", BMS_VersionNo_IN)
# IOT_IN = IOT_Version_IN.split("_")
# IOT_VersionNo_IN = IOT_IN[-1].replace('V','')
# print("Exisiting IOT Version : ", IOT_VersionNo_IN)

for i in range(len(Input)):
    tmp = Input[i].split("_")
    ProcessedInput.append(tmp)
# BMS_IN = ProcessedInput
# print(ProcessedInput)
BMS_versions_available = []
IOT_versions_available = []

for p in ProcessedInput:
    if p[0] == "BMS":
        BMS_IN = p
        print("BMS split:",BMS_IN)
        BMS_IN_No = BMS_IN[1].replace('V','')
        for b in bms_contents:
            file = b.path
            content = file.split(".")
            if content[-1] == "BIN":
                BMS_fileName = content[0].split("_")
                bmsversion = BMS_fileName[-1].split()
                BMS_VersionNo = bmsversion[0].replace('V','')
                BMS_versions_available.append(int(BMS_VersionNo))
                for v in BMS_versions_available:
                    if v > int(BMS_IN_No):
                        print("BMS current software version :", BMS_IN_No, "BMS available update : ", v)
                        download_link = f"{repository}/raw/main/{file}"
                        print("download the BMS update from:",download_link)
                    else:
                        print("software is up to date")
    elif p[0] == "IOT":
        IOT_IN = p
        print("IOT split:",IOT_IN)
        IOT_IN_No = IOT_IN[1].replace('V','')
        for b in iot_contents:
            file = b.path
            content = file.split(".")
            if content[-1] == "BIN":
                IOT_fileName = content[0].split("_")
                iotversion = IOT_fileName[-1].split()
                IOT_VersionNo = iotversion[0].replace('V','')
                IOT_versions_available.append(int(IOT_VersionNo))
                for v in IOT_versions_available:
                    if v > int(IOT_IN_No):
                        print("IOT current software version :", IOT_IN_No, "IOT available update : ", v)
                        download_link = f"{repository}/raw/main/{file}"
                        print("download the IOT update from:",download_link)
                    else:
                        print("software is up to date")

# print("BMS versions available : ",BMS_versions_available)

# versions_available = []
# for c in contents:
#     file = c.path
#     url = f"{repository}/{file}"
#     print(url)
#     r = requests.get(url, allow_redirects=True)
#     content = file.split(".")
#     if content[-1] == "BIN":
#         download_link = f"{repository}/blob/main/{file}"
#         open(c.path,'wb').write(r.content)
#         fileName = content[0].split("_")
#         version = fileName[-1].split()
#         print("BMS software version = ", version)
#         versionNo = version[0].replace('V', '')
#         versions_available.append(int(version))
#         print("BMS Software Version Number is ",versionNo)
# print(versions_available)
# for i in versions_available:
#     if int(versionNo_IN) < i:
#         download_link = f"{repository}/blob/main/{file}"
#     else:
#         print("you are upto date!")


        #updated version logic

        #download that file

    # print(content)




# for x in content:
#     fileExt = content.split(".")
#     print(fileExt)
