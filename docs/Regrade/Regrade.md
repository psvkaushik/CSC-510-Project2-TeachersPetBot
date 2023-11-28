# Commands in Regrade Feature

!regrade-request

!update-request

!display-requests

!remove-request

# Location of Codehttps:

The code that implements the above commands is located [here](https://github.com/chandur626/TeachersPetBot/blob/main/src/regrade.py)

# About !regrade-request

This command lets a student add a regrade-request

# Code Description

## Functions

add_request(ctx, name: str, questions: str):

This function takes as arguments the values, context in which the command was called, name of the student, questions to be regraded.

# How to run it? (Small Example)

Run this command in regrade-requests channel

```
'!regrade-request '<Student Name> <questions>'
```

example : '!regrade-request "Student 1" "q1,q2,q3"'.

Successful execution of this command will display that the request was submitted.
If the command is executed in any other channel, a direct message from bot is sent asking to submit the request in regrade-requests channel.
If there are missing command line arguments, error message is shown along with syntax to enter the correct command.
if an existing regrade request is submitted again, duplicate request message is shown.

# About !update-request

This command lets a student update an existing regrade-request

# Code Description

## Functions

update_regrade_request(ctx, name: str, questions: str):

This function takes as arguments the values, context in which the command was called, name of the student, questions to be regraded.

# How to run it? (Small Example)

Run this command in regrade-requests channel

```
'!update-request '<Student Name> <questions>'
```

example : '!update-request "Student 1" "q3,q4,q8"'.

Successful execution of this command will display that the request was submitted.
If the command is executed in any other channel, a direct message from bot is sent asking to submit the request in regrade-requests channel.
If there are missing command line arguments, error message is shown along with syntax to enter the correct command.

# About !display-requests

This command lets a student display all the regrade requests

# Code Description

## Functions

display_requests(ctx):

This function takes as arguments the values, context in which the command was called. No other arguments are required.

# How to run it? (Small Example)

Run this command in regrade-requests channel channel

```
'display_requests'
```

example : 'display_requests'.

Successful execution of this command will display all the regrade requests.
If the command is executed in any other channel, a direct message from bot is sent asking to submit the request in regrade-requests channel.

# About !remove-request

This command removes an existing regrade request

# Code Description

## Functions

remove_regrade_request(ctx, name: str, questions: str):

This function takes as arguments the values, context in which the command was called, name of the student, questions to be regraded.

# How to run it? (Small Example)

Run this command in regrade-requests channel

```
'!remove-request '<Student Name> <questions>'
```

example : '!remove-request "Student 1" "q1,q2,q3"'.

Successful execution of this command will remove the request from the database.
If the command is executed in any other channel, a direct message from bot is sent asking to submit the request in regrade-requests channel.
If there are missing command line arguments, error message is shown along with syntax to enter the correct command.
