_This File describes each source file and details of all classes, methods and functions in each file_

### <u> [bot.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/bot.py) </u>

Iteration 5

1. **_Function_**: display_leaderboard

   **_Description_**: Command used to get the top 10 rankers based on their ranks and XP in the group.

2. **_Function_**: set_spam_settings

   **_Description_**: Command available to instructors to set spam settings.

3. **_Function_**: set_profanity_settings
   
   **_Description_**: Command available to instructors to set profanity settings.
   
4. **_Function_**: award

    **_Description_**: Command available to instructors to award xp to students.
   
6. **_Function_**: penalize

  **_Description_**: Command available to instructors to penalize students by reducing xp.
  
7. **_Function_**: unblockUser

  **_Description_**: Command available to instructors to unblock blocked students.

### <u> [db.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/db.py) </u>

1. **_Function_**: connect

   **_Description_**: Called during startup of the bot. Connect program to database file db.sqlite

2. **_Function_**: select_query

   **_Description_**: Called from bot.py to send SQL to the database and get the response

3. **_Function_**: mutation_query

   **_Description_**: Called from bot.py for mutation on the database

### <u> [profanity_help.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/profanity_help.py) </u>

1. **_Function_**: check_profanity

   **_Description_**: checks if message contains profanity through profanity module

2. **_Function_**: censor_profanity

   **_Description_**: takes action on the profanity by censoring it

### <u> [spam.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/spam.py) </u>

1. **_Function_**: set

   **_Description_**: This is used to set the custom settings for each action related to spam, available only to instructors.

2. **_Function_**: clear_spam

   **_Description_**: This function runs in loop every x seconds to clear the message enteries by each user.

3. **_Function_**: init

   **_Description_**: It starts the db setup for the bot regarding the SPAM settings.

4. **_Function_**: handle_spam

   **_Description_**: This function handles spam based on the metrics stored in the DB during init, It will also award the penalty based on the setup by the instructor and give the warnings and timeouts accordingly.

---

**Description**: What this does

1. **_Function_**: on_ready

   **_Description_**: run on bot start-up

2. **_Function_**: on_guild_join

   **_Description_**: run when a user joins a guild with the bot present

   **_Inputs_**:

   - _guild_: the guild the user joined from

3. **_Function_**: on_member_join

   Description: run when member joins a guild in which bot is alreay present

   **_Inputs_**:

   - member: the user details

4. \***_Function_**: on_member_remove

   **_Description_**: run when member leaves a guild in which bot is alreay present

   **_Inputs_**:

   - guild: the guild the user joined from

5. **_Function_**: on_message

   **\*\***Description**\*\***: run when a message is sent to a discord the bot occupies

   **_Inputs_**:

   - _message_: the message the user sent to a channel

6. **_Function_**: on_message_edit

   **_Description_**: run when a user edits a message

   **_Inputs_**:

   - before: the old message
   - after: the new message

7. **_Function_**: test

   **_Description_**: Simple test command that shows commands are working.

   **_Inputs_**:

   - ctx: context of the command

   **_Outputs_**:

   - Sends test successful message back to channel that called test

8. **_Function_**: get_instructor

   **_Description_**: Command used to give Instructor role out by instructors

   **_Inputs_**:

   - ctx: context of the command
   - member: user to give role

   **_Outputs_**:

   - Sends confirmation back to channel

9. **_Function_**: set_instructor

   **_Description_**: Command used to give Instructor role out by instructors

   **_Inputs_**:

   - ctx: context of the command
   - member: user to give role

   **_Outputs_**:

   - Sends confirmation back to channel

10. **_Function_**: remove_instructor

    **_Description_**: Command used to remove a user from Instructor role by instructors

    **_Inputs_**:

    - ctx: context of the command
    - member: user to remove role

    **_Outputs_**:

    - Sends confirmation back to channel

11. **_Function_**: create_event

    **_Description_**: command to create event and send to event_creation module

    Ensures command author is Instructor

    **_Inputs_**:

    - ctx: context of the command

    **_Outputs_**:

    - Options to create event

12. **_Function_**: oh

    **_Description_**: command related office hour and send to office_hours module

    **_Inputs_**:

    - ctx: context of the command
    - command: specific command to run
    - args: arguments for command

    **_Outputs_**:

    - Office hour details and options

13. **_Function_**: ask

    **_Description_**: command to ask question and sends to qna module

    **_Inputs_**:

    - ctx: context of the command
    - question: question text

      **_Outputs_**:

    - User question in new post

14. **_Function_**: answer

    **_Description_**: command to answer question and sends to qna module

    **_Inputs_**:

    - ctx: context of the command
    - q_num: question number to answer
    - answer: answer text

    **_Outputs_**:

    - User answer in question post

15. **_Function_**: ping

    **_Description_**: Shows latency for debugging

16. **_Function_**: stats

    **_Description_**: Shows stats like

17. **_Function_**: poll

    **_Description_**: Poll functionality for administrators

    **_Inputs_**:

    - ctx: context of the command
    - minutes: minutes in integer
    - question: Enter the topic on which the poll is created
    - options: options for poll
      **_Outputs_**:
    - Poll in discord channel. results after the specified time.

18. **_Function_**: custom-profanity

    **_Description_**: Define a word to be added to the profanity filter

    **_Inputs_**:

    - ctx: context of the command

19. **_Function_**: attendance

    **_Description_**: Gets the attendance when requested by the instructor for audio channel

    **_Inputs_**:

    - ctx: context of the command

20. **_Function_**: begin_tests

    **_Description_**: Start the automated testing

    **_Inputs_**:

    - ctx: context of the command

21. **_Function_**: end_tests

    **_Description_**: Finalize automated testing

    **_Inputs_**:

    - ctx: context of the command

22. **_Function_**: test_dummy

    **_Description_**: Run the bot

### <u> [cal.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/cal.py) </u>

**\***Description**\*:** What this does

1. **_Function_**: display_events

   **_Description_**: Sends or updates the embed for the calendar

   **_Inputs_**:

   - ctx: context of function activation

1. **_Function_**: update_calendar

   **_Description_**: Builds the calendar embed

1. **_Function_**: init

   **_Description_**: Initializes the calendar, creating channel and embed call

   **_Inputs_**:

   - b: bot

1. **_Function_**: closecalls

   **_Description_**: checks if any deadlines are coming up within a day .

   This code runs in the background periodically

   **_Inputs_**:

   - channel : the channel 'course-calendar'

### <u> [event_creation.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/event_creation.py) </u>

**\***Description**\*:** Functionality for creating new events

1. **_Function_**: create_event

   **_Description_**: creates an event by the specifications of the instructor creating the event

   **_Inputs_**:

   - ctx: context of this discord message

   - testing_mode: flag indicating whether this event is being created during a system test

   **_Outputs_**: new event created in database

1. **_Function_**: init

   **_Description_**: initializes this module, giving it access to discord bot

   **_Inputs_**:

   - b: discord bot

   **_Outputs_**: None

### <u> [office_hours.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/office_hours.py) </u>

**_Description_**: functionality related to administering office hours

1. Class: Group

   **_Description_**: contains information about an office hour group

1. Class: OfficeHourQueue

   **_Description_**: contains information about an office hour queue

1. Method: enqueue

   **_Description_**: adds a student to the office hour queue

   **_Inputs_**:

   - student: student to add to the office hour queue

   **_Outputs_**: None

1. Method: display_queue

   **_Description_**: displays the office hour queue in the office hour channel

   **_Outputs_**: office hour queue as a message in the office hour channel

1. **_Function_**: office_hour_command

   **_Description_**: handles a command given in an office hour channel

   **_Inputs_**:

   - ctx: context of this discord message
   - command: office hour command given
   - args: extra arguments given to command

1. **_Function_**: open_oh

   **_Description_**: opens an office hour for students to get help from

   **_Inputs_**:

   - guild: discord guild this office hour is relevant for
   - ta: name of TA who is holding this office hour

   **_Outputs_**:

   - creation of channels relevant to office hour

1. **_Function_**: close_oh

   **_Description_**: closes an office hour session

   **_Inputs_**:

   - guild: discord guild this office hour is relevant for
   - ta: name of TA who is holding this office hour

   **_Outputs_**:

   - deletion of channels relevant to office hour

1. Class: TaOfficeHour

   **_Description_**: contains information about when an office hour is held

1. **_Function_**: check_office_hour_loop

   **_Description_**: runs intermittently to open or close office hours based on the current time

1. **_Function_**: add_office_hour

   **_Description_**: adds a new TA office hour to the guild

   **_Inputs_**:

   - guild: discord guild this office hour is relevant for
   - ta_office_hour: TA office hour information

   **_Outputs_**:

   - adds a new TA office hour to the system

1. **_Function_**: init

   **_Description_**: initializes office hours module

   **_Inputs_**:

   - b: discord bot

### <u> [profanity_help.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/profanity_help.py) </u>

**\***Description**\*:** What this does

1. **_Function_**: check_profanity

   **_Description_**: Uses better_profanity to check profanity in a message

   **_Inputs_**:

   - msg: message from user

2. **_Function_**: censor_profanity

   **_Description_**: censor the message per better_profanity

   **_Inputs_**:

   - msg: message from user

### <u> [qna.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/qna.py) </u>

**\***Description**\*:** Implements Q and A functionality

1. Class: QuestionsAnswers

   **_Description_**: object with question details

   **_Inputs_**:

   - q: question text
   - number: question number
   - message: id of the message associated with question
   - ans: answers to the question

   **_Outputs_**: None

2. **_Function_**: question

   **_Description_**: takes question from user and reposts anonymously and numbered

   **_Inputs_**:

   - ctx: context of the command
   - q: question text

   **_Outputs_**:

   - User question in new post

3. **_Function_**: answer

   **_Description_**: adds user answer to specific question and post anonymously

   **_Inputs_**:

   - ctx: context of the command
   - num: question number being answered
   - ans: answer text to question specified in num
     **_Outputs_**:
   - User answer added to question post

### <u> [attendance.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/attendance.py) </u>

**\***Description**\*:** Attendance functionality

1. **_Function_**: compute

   **_Description_**: Finds attendees and absentees of class

   **_Inputs_**:

   - bot: bot that sends commands to test TeachersPetBot
   - ctx: Context of the function activation

   **_Outputs_**: None

### <u> [help_command.py](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/blob/main/src/help_command.py) </u>

**\***Description**\*:** help command functionality

1. **_Function_**: helper

   **_Description_**: Directs the help functions when called and is executes !help command

   **_Inputs_**:

   - ctx: Context of the function activation

   **_Outputs_**: Result of !help
