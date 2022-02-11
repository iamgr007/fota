#Git application

import requests
# import base64
from github import Github


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
contents = repo.get_contents("")
print(contents)

# https://github.com/iamgr007/fota/blob/main/BMS_V0.BIN

for c in contents:
    file = c.path
    url = f"{repository}/{file}"
    print(url)
    r = requests.get(url, allow_redirects=True)
    content = file.split(".")
    if content[-1] == "BIN":
        download_link = f"{repository}/blob/main/{file}"
        open(c.path,'wb').write(r.content)
        fileName = content[0].split("_")
        version = fileName[-1].split()
        print("BMS software version = ", version)
        versionNo = version[0].replace('V', '')
        print("BMS Software Version Number is ",versionNo)
        #updated version logic

        #download that file

    # print(content)




# for x in content:
#     fileExt = content.split(".")
#     print(fileExt)
