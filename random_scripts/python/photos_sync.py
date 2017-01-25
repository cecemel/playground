import os, time

while True:
    outcome = os.system("rsync -avz --partial  ~/Documents/d90 -e ssh cecemel-cup:~/d90/")
    if outcome == 0:
        break
    print("Failed, trying again")
    time.sleep(10)

