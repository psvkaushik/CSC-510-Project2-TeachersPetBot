"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
from better_profanity import profanity
import asyncio
from datetime import timedelta


profanity.load_censor_words()
custom_words = []
###########################
# Function: check_profanity
# Description: Uses better_profanity to check profanity in a message
# Inputs:
#      - msg: message from user
###########################
def check_profanity(msg):
    ''' check if message contains profanity through profanity module '''
    if msg in custom_words:
        return True

    return profanity.contains_profanity(msg)

###########################
# Function: censor_profanity
# Description: censor the message per better_profanity
# Inputs:
#      - msg: message from user
###########################
def censor_profanity(msg):
    ''' take action on the profanity by censoring it '''
    if msg in custom_words:
        msg = '****'
    return profanity.censor(msg)
