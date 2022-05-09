import requests
import hashlib
import datetime
import os

WEBSITE_URL=os.environ["CH_WEBSITE_URL"]
OUT_DIR=os.environ["CH_OUT_DIR"]

WEBSITE_URL="https://www.citruscircuits.org/uploads/6/9/3/4/6934550/2021-22_team_handbook__2_.pdf"
OUT_DIR="/home/cameron/website_monitoring/citrus/"

print("Time is: " + str(datetime.datetime.now()) + " checking website for changes")

r = requests.get(WEBSITE_URL)
if r.status_code != 200:
    print("Failed! " + r.text)
else:
    print("Success, saving..")

latest_md5 = hashlib.md5(r.content).digest()
with open(OUT_DIR + "latest_md5", "r") as f:
    md5 = f.readline()
    print(md5 + " compared to " + str(latest_md5))
    if (md5 == str(latest_md5)):
        print("Unchanged")
        exit()

with open(OUT_DIR + "latest_md5", "w+") as f:
    f.write(str(latest_md5))

with open(OUT_DIR + str(datetime.datetime.now()) + ".pdf", "w+b") as f:
    print("Writing out file")
    f.write(r.content)
    f.close()

