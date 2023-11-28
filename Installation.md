# Installation and Testing Guide

## Contents

- [ Running the bot locally ](#local)
  - [ Executing the bot script ](#run)
  - [ Run Tests ](#test)
- [ Running the bot on cloud ](#cloud)

<a name=local><a/>

### In order to run the bot locally Follow the instructions given below:

#### Create a Discord Bot

To create a Discord Bot, you must:

- have a [Discord Account](https://discord.com/login)
- have a Discord server for the bot
- create a Discord bot in the [Developer Portal](https://discord.com/developers/applications), but DO NOT ADD to your server yet ([Follow instructions here](https://realpython.com/how-to-make-a-discord-bot-python/))
- create a `.env` file with your Bot Token and add this to your .gitignore (Discord will automatically regenerate your token if you accidentally upload it to Github).<br/> NOTE: You dont need to include { } in the .env file.<br/>
  ```
  # .env
  DISCORD_TOKEN={your-bot-token}
  DICORD_BOT_NAME={your-bot-name}
  TEST_GUILD_ID={your-guild-id}
  TESTING_BOT_TOKEN={test-bot-token}
  TEST_BOT_NAME={test-bot-name}
  TEST_BOT_APP_ID={test-bot-application-id}
  BARD_API_KEY={your-bard-api-key}
  VERSION={custom bot version}
  ```

NOTE: Run the bot before inviting it to your server in order for auto-initiate commands to run

This includes the following:

- Creating Instructor Role
- Adding server owner to Instructor Role
- Creating Bot channels

<a name=run><a/>

### Run Teacher's Pet Bot

To run the Teacher's Pet Bot:

1. Ensure you have the following installed:
   - [Python 3](https://www.python.org/downloads/)
   - [pip](https://pip.pypa.io/en/stable/installation/)
2. Clone this repo onto your local machine
3. In the repository directory, run `pip install -r requirements.txt`
4. Run `python src/bot.py` to start the bot
5. Invite the bot to your server ([Follow instructions here](https://realpython.com/how-to-make-a-discord-bot-python/))
   - NOTE: When using the OAuth2 URL Generator, make sure you check the box which gives your bot Administrative permissions

<a name=test><a/>

### Run Tests

To run tests on the Teacher's Pet Bot:

1. Create a second bot for testing
2. Add the Test Bot's token to the `.env` file.<br/> NOTE: You dont need to include { } in the .env file.<br/>
   ```
   # .env
   DISCORD_TOKEN={your-bot-token}
   DICORD_BOT_NAME={your-bot-name}
   TEST_GUILD_ID={your-guild-id}
   TESTING_BOT_TOKEN={test-bot-token}
   TEST_BOT_NAME={test-bot-name}
   TEST_BOT_APP_ID={test-bot-application-id}
   BARD_API_KEY={your-bard-api-key}
   VERSION={custom bot version}
   ```
3. In `test/tests.py`, update the `TEST_GUILD_ID` to be the id of the server/guild you are testing in.
4. IMPORTANT(You will have two bots running at once for testing. One normal bot, one test bot): Start Teacher's Pet Bot by running one of the following commands in the root directory of the project:
   - Without Coverage: `pytest src/bot.py`
   - With Coverage: `coverage run --source=./src -m pytest src/bot.py`
5. Run the tests with `python test/tests.py` in the root directory of the project
6. If you collected coverage, run `coverage report` to see coverage details.

<a name=cloud><a/>

### In order to run the bot locally Follow the instructions given below:

# Hosting your discord.py bot on Heroku

### What are the prerequisites for this guide?

You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)] , and Heroku [[Link](https://signup.heroku.com/)].

### How to fork the repository and set it up to work with Heroku?

- Fork a copy of this repository by clicking the 'Fork' on the upper right-hand.
- Create an application for Heroku by clicking [here](https://dashboard.heroku.com/new-app).
- Under 'Deploy', do the following:
  - Deployment Method => Connect your GitHub
  - App connected to GitHub => Search for the forked repository
  - Automatic Deploy => Enable Automatic Deploy (to redeploy after every commit)
