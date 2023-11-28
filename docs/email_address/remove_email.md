# !remove_email

This command enables users to delete their configured email address.

# Location of Code

The implementation for this command is available in [src/email_address.py](https://github.com/chandur626/TeachersPetBot/blob/8813e476d85caaffe034434daecf6461f353a792/src/email_address.py#L80)

# Code Description

## Functions

1. def remove_email(ctx): <br>
   This function is invoked when !remove_email command is entered in the bot. Returns error if there is no active email configured against the user, deletes the email address otherwise.

# How to run it? (Small Example)

Let's say that you join the server that has the TeachersPetBot active and online. All you have to do is
enter the command '$remove_email'.

```
!remove_email
```

Successful execution of this command will deletes your email address and reverts with the success message through the bot.

![!remove_email](https://github.com/chandur626/TeachersPetBot/blob/main/data/media/email_address.gif)
