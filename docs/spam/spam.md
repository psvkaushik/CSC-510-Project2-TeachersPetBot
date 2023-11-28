# Location of Codehttps:

The code that implements the above commands is located [here](../../src/spam.py)

# Code Description

This code implements a spam detector that issues warnings to students who send too many messages based on a message threshold and a time-allowed threshold. If a user sends more messages than allowed in a certain amount of time, then that user will be put in time-out after a warning.

## Functions

def init(bot):

This function takes a bot as an argument and uses that bot to set the bot for the spam.py file. Additionally, this function creates a task to be constantly running called clear_spam(), which essentially determines the amount of time a user is allowed to send x amount of messages before being detected as spam. Init also inserts default spam setting values into the database if the bot is new to the guild.

        warning_num = 4  # number of messages before warning of spam
        timeout_num = 5  # number of messages before timeout
        timeout_min = 5  # number of minutes in timeout
        timeout_hour = 0  # hours in timeout
        timeout_day = 0  # days in timeout
        time_between_clears = 15  # time threshold mentioned above

These values are then inserted into the database if values weren't already there.

async def clear_spam():

This function constantly runs every x amount of seconds, where x is time_between_clears aka the time threshold in the bot's database. This function deletes everything in the spam.txt file such that every x seconds the spam detector can start from 0 when counting someone's messages for spam. For example, if a user sends 30 messages in 5 seconds that is spam, but if a user sends 30 messages in 1 hour that should not be spam. So the clear_spam function clears the spam.txt file every x seconds to make sure users are fairly evaluated on whether they are spamming or not.

async def handle_spam(message, ctx, guild_id)

This function is called from bot.py on every message that is sent by non-instructors in the guild. This function opens up spam.txt to count how many times the particular author of the last message sent has sent messages in the guild in the past x amount of seconds, where x is the value set in the database 'time_between_clears'. Then the function looks to see if that count exceeds the warning threshold setting and the timeout threshold setting which are also in the database. If the user sends more messages than the warning threshold then this function sends a message warning that the user is spamming too much. If the user sends more messages than the timeout threshold, then the user is put into timeout. The function then queries the database to decide how long to put the user in timeout, based on what the instructor set in the database, or what was there by default.

# How to run it? (Small Example)

This code runs everytime a message is sent in the channel.

## An example

### Send the following messages in the channel(must do this faster than in 15 seconds):

Message: h
Message: h
Message: h
Message: h
Message: h
By the default settings, the channel will now give a warning saying too many messages.

### Send on more message immediately following:

#### halkneoihan

By the default settings, as long as you are not the instructor or an admin, you will be placed in timeout for 5 minutes.

# Use Case Example

The main use case of this feature is that if you are an instructor running an online class you wouldn't want students to just spam your chat with constant gibberish. For example, let's say you are the chem professor with the chem discord and you are running office hours over discord. Suddenly one of the students in the office hour accidently spills something on their keyboard causing it to spam the text 'a' over and over again. Suddenly it would be impossible to read questions from your other students. However, if you are using our teacher's pet bot, it will automatically handle the situation by temporarily putting the student in timeout such that they won't be spamming the chat anymore.

Below is what the feature looks like in action:

<p align="center"><img width=85% src="../media/spam.gif"></p>
