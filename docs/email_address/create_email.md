# !create_email

This command enables users to configure their email address to receive important reminder notifications and attachments.

# Location of Code

The implementation for this command is available in [src/email_address.py](https://github.com/chandur626/TeachersPetBot/blob/8813e476d85caaffe034434daecf6461f353a792/src/email_address.py#L7)

# Code Description

## Functions

1. def create_email(ctx, email_address): <br>
   This function is invoked when !create_email command is entered in the bot. This function expects user to enter an email address to be configured. Returns error if there is already an active email configured against the user, configures the email address otherwise.

# How to run it? (Small Example)

Let's say that you join the server that has the TeachersPetBot active and online. All you have to do is
enter the command '$create_email' and the email address you want to configure.

```
!create_email your_email_address
!create_email no-reply-test@teacherspetbot.com
```

Successful execution of this command will configure your email address and reverts with the success message through the bot.

![!create_email](https://github.com/chandur626/TeachersPetBot/blob/main/data/media/email_address.gif)
