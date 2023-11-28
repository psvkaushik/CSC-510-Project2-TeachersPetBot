## Create a Discord Bot

To create a Discord Bot, you must:

- have a [Discord Account](https://discord.com/login)
- have a Discord server for the bot
- create a Discord bot using [link](https://realpython.com/how-to-make-a-discord-bot-python/))
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
