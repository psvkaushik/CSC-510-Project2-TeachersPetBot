# About !set_spam_settings

This command lets instructors set their own customized spam settings

# Location of Code

The code that implements the above mentioned gits functionality is located [here](../../src/spam.py).

# Code Description

## Functions

- async def set(ctx): <br>
  This function prompts the instructor (only inside the instructor commands channel) for what settings they would like to apply the spam detector. For example, instructors are allowed to set how many messages per unit of time a student is allowed to send before they are warned of spamming, and when they are timed out. Also they are allowed to set how long the timeout will last. Then the function takes all the input prompts and places them into the database so the spam detector knows how to do its job correctly.

# How to run it? (Small Example)

Enter: "!set_spam_settings"

This will be followed by the prompt: How many messages should a user be able to send before they are put in timeout?

Enter how many messages a user should be able to send before warned of spam: "3"

This will be followed by the prompt: How many messages should a user be able to send before they are put in timeout?

Enter how many meesages a user should be able to send before they are put in timeout: "4"

This will be followed by the prompt: How much time should users have to send 3 messages before they will be warned and then eventually put in timeout?

Enter the unit of time (in seconds) over which students are allowed to send 3 and 4 messages without being warned of spam and timed out respectively (In other words what you enter in how much are users allowed to send x messages. If the user sends x+1 messages in this amount of time, then they will be accused of spamming): "10"

This will be followed by the prompt: How long should a user be placed in timeout when caught spamming? Format: min,hours,days Example: 5,0,0 is 5 minutes

Enter the amount of time a user should be placed in timeout in the format outlined above: 10,0,0

Below is an example of using the !set_spam_settings command:

<p align="center"><img width=85% src="../media/set_spam.gif"></p>

Successful execution will result in a spam detector similar to below.

<p align="center"><img width=85% src="../media/spam.gif"></p>

# Use Case Example

Let's say you are an English professor and you have a class discord that you use for your live classes. Let's say you often ask multiple questions at once to your students. For example your class just read a book and you send out 10 questions for them to respond to on the chat. Some students may answer all 10 questions very quickly, so quickly in fact they could be banned by the default spam settings since if they send more than 5 messages in 15 seconds they will be banned for spamming. Luckily, our teacher's pet bot offers the !set_spam_settings command such that you can change the number of messages to 15 for days where you will be asking multiple questions at once. Then when students answer your question very quickly, they won't be accused of spamming. But even still, if a mean student set a spam bot loose on the discord it would be banned for spam if it broke your new set threshold. So with our highly customizable spam command, you can set your spam settings to meet whatever needs you require.
