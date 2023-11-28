# !create

This command enables users to create several events. This documentation is concerned only with creating project event.

# Location of Code

The implementation for this command is available in [src/event_creation.py](https://github.com/chandur626/TeachersPetBot/blob/8813e476d85caaffe034434daecf6461f353a792/src/event_creation.py#L88)

# Code Description

## Functions

1. def create_event(ctx, testing_mode): <br>
   This function is invoked when !create command is entered in the bot. Displays several events when this command is invoked and users are expected to select the type of event. Once the user selects project event, bot asks user to enter the due date, submission link and description of the project in a specific format. Returns an error if the data is not entered in the expected format.

# How to run it? (Small Example)

Let's say that you join the server that has the TeachersPetBot active and online. All you have to do is
enter the command '$create'.

```
!create
```

Successful execution of this command will list type of events to be configured including project and reverts with the success message through the bot once the project creation is successful.

![!project_event](https://github.com/chandur626/TeachersPetBot/blob/main/data/media/project_event.gif)
