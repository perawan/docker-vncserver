#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import threading
import redis
from pymongo import MongoClient

# change folder
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

REDISBOT="redis://k:kopet1234@redis-16406.c1.us-east1-2.gce.cloud.redislabs.com:16406"
MONGO_BOTS="mongodb://root:kopet1234@ds147985.mlab.com:47985/kautsarbots"

r = redis.StrictRedis.from_url(REDISBOT)
pjm = MongoClient(MONGO_BOTS) #os.getenv('MONGO_PROJECTS')

def run0():
    print('booting..')
    while True:
        #print('running..')
        os.system('')
        gt = r.hgetall('deploy')
        if gt:

            for f in gt:
                dl = r.delete('deploy', f)
                if dl == 1:
                    fd = pjm['kautsarbots']['kautsarbot'].find_one({'_id': f.decode()})
                    if 'type' in fd and fd != None:
                        
                        print('deploy ' + str(fd['appname']))
                        typene = str(fd['type'])
                        num = str(fd['count'])
                        email = str(fd['email'])
                        apikey = str(fd['apikey'])
                        appname = str(fd['appname'])

                        #os.system('sh deploy.sh ' + email + ' ' + apikey + ' ' + typene + ' ' + appname + ' ' + num)
                        print('git add ning kopet')
                        branch = appname
                        git = 'https://ikamai:kopet1234@gitlab.com/ikamai-deployer/kautsarbot-deployer.git'

                        os.system('cp -r gitlabci.yml .gitlab-ci.yml')
                        os.system('git config --global user.email "you@example.com"')
                        os.system('git config --global user.name "Your Name"')
                        os.system('echo "sh deploy.sh ' + email + ' ' + apikey + ' ' + typene + ' ' + appname + ' ' + num + '" > run.txt')
                        os.system('rm -rf .git/; git init; git remote add origin '+git+'; git add .; git commit -m "init"; git branch '+str(branch)+'; git checkout '+str(branch)+'; git push -f origin '+str(branch)+';')

                        pjm['kautsarbots']['kautsarbot'].update_one({"_id": f.decode()}, {"$set": {"deploy": 1, "run": 1, "build": "build"}})

                #os.systemp
                time.sleep(1)
        time.sleep(1)
    return

if __name__ == '__main__':

    t = threading.Thread(target=run0)
    t.start()
