#!/usr/bin/env python3


import sys
import os
import random
from twython import Twython

sys.path.insert(0, 'credentials/') ##add the credentials folder
import credentials

## Credential appraisal - hail to the lord
CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_SECRET

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
# print(twitter.verify_credentials()) ##debug


twitter.update_status(status='Von guten Mächten treu und still umgeben behütet, \
so will ich mit euch leben und mit euch gehen in ein neues Jahr. @ungarjo @sektionschef')
