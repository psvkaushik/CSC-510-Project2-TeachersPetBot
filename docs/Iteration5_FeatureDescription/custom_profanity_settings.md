# About !set_profanity_settings

This command lets instructors set custom profanity configurations.

# Location of Code

The code that implements the above mentioned functionality is located [here](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/profanity_custom.py)

# Code Description

## Functions

- set(ctx) <br>
  This function prompts the instructor to set the profanity settings.

- init(bot) <br>
  This function initializes this module, giving it access to discord bot. Also inits the clear spam function and puts default values in for the spam settings.

- profanity_penalize(author_id) <br>
  This function takes a message and determines whether the author who sent that message is spamming.

- handle_profanity(message, ctx, guild_id)
  This function handles the event of a profanity.

# How to run it? (Small Example)

Enter space-separated: "!set_profanity_settings"

Successful execution looks as below:  
<img width="822" alt="image" src="https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/144864099/7adec811-7169-406d-9643-b62f6b92d402">
