import requests
import hashlib
import datetime
import os
import time

DELAY=60*120
WEBSITE_URL=os.environ["CH_WEBSITE_URL"]
OUT_DIR=os.environ["CH_OUT_DIR"]

print("Script startup :)")

while True:
    time.sleep(DELAY)
    print("Time is: " + str(datetime.datetime.now()) + " checking website for changes")
    r = requests.get(WEBSITE_URL)
    if r.status_code != 200:
        print("Failed! " + r.text)
    else:
        print("Success, saving..")
    
    latest_md5 = hashlib.md5(r.content).digest()
    with open(OUT_DIR + "/latest_md5", "r") as f:
        md5 = f.readline()
        print(md5 + " compared to " + str(latest_md5))
        if (md5 == str(latest_md5)):
            print("Unchanged")
            continue
    
    with open(OUT_DIR + "/latest_md5", "w+") as f:
        f.write(str(latest_md5))
    
    with open(OUT_DIR + str(datetime.datetime.now()) + ".pdf", "w+b") as f:
        print("Writing out file")
        f.write(r.content)
        f.close()
