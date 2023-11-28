# cron_job to email reminders

This cron job is responsible to email users regarding the reminders due for that specific day.

# Location of Code

The implementation for this command is available in [src/event_creation.py](https://github.com/chandur626/TeachersPetBot/blob/8813e476d85caaffe034434daecf6461f353a792/src/event_creation.py#L279)

# Code Description

## Functions

1. def check_reminders_due_today(): <br>
   This function is executed every 24 hours. This function retrieves all the assignments and projects which are due today and sends an emil to the users regarding the reminder.

# How to run it? (Small Example)

Let's say that you join the server that has the TeachersPetBot active and online. All you have to do is configure an email and
create an assignment due for next day and check for an email.
Successful execution of this will send an email to all the users who have their email configured.
![email_reminder](https://github.com/chandur626/TeachersPetBot/blob/main/data/media/email_reminder.gif)
