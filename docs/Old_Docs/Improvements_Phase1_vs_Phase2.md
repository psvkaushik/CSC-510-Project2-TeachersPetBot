**This File briefly ecompares and explains the improvements along with the new additons done to this application in the Phase II Development**

|  Improvements | Phase I   | Phase II  |
| ------------ | ------------ | ------------ |
| Test case error handling | Test cases had many local hard coded variables and was falining when running in a local windows system. Also some existing test cases were failing. | Fixed all the issues with test files and added support for running in windows. Made sure the hard coded values are made as variables in the .env file to be uploaded as input. |
| Handling all use cases (Test) | Test cases did not cover many existing use cases (Eg. Profanity) | Covered all the use cases from Phase I and wrote cases to handle newly added features. |
| Restricting access (Feature) | Instructor channel visible and accesible to all members. | Restricted instructor channel access to only instructors and when a instructor is remove and re-added made sure the chats inthe period he wans't available is not accessible to him. |
| Hosted in Heroku (Deployment) | Had to run the bot locally | Hosted in heroku for better convenience and higher consistency. |
| QnA handling (Database) | Did not store questions and answers in a database | created database to store QnAs. |
| Read me and feature docs (Documentation) | Had phase 1 details in Read me but no separate file explaining functions | The new docs have updated feature descriptions and function descriptions in isolation |
| Office Hour run | Office hour run in the very first time after BOT is added/re-added to the server raises a Key error even if database has values. | Fixed the same, by making sure the check is run only after the database populates the BOT's local variables |
| Create events and office hours | The bot always threw an error when trying to create a new event/ office hour as the BOT waiting time for a response was very less. | Modified the code to wait for longer duration to recieve user input before throwing error. |
| Instructor check before adding | Previous blindly tried to add instructor. Shows a success message even if the member already had a instructor role. | Modified code to check if the person was already an instructor and outputs information accordingly. |
| Text channels recreating | If the bot is added to a server it recreated some default channels each time again and again. | Code changes to check for the existence of the channel before adding it. |
| Help | Used inbuild discord help | Added custom help command to better suite the usage. |
