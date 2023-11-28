<h1> TeachersPetBot Previous Features </h1>

<h2> Iteration I </h2>

### Initialization

When Teacher's Pet has been added to a new server as a bot, it will do the following:

- Create a new role called Instructor with Administrative permissions if one does not already exist
- Add the owner of the guild to the Instructor role
- Create a #q-and-a channel if one doesn't already exist
- Create a #calendar channel if one doesn't already exist

In addition to this auto-set up, there is also a command which allows a user with the Instructor role to give the same role to another user. This command will only work for users with the Instructor role already (for example, the guild owner).

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/bot_join.png)

### Q&A

The Q&A functionality allow students to ask and answer questions anonymously. The questions are numbered and when answers are sent, they are combined with the question so they can be easily found. Answers are also marked with `Student Ans` and `Instructor Ans` to distinguish between the sources.  
To ask a question, type `!ask "Question"` in the #q-and-a channel. Example: `!ask "When is the midterm?"`.  
![image](https://user-images.githubusercontent.com/32313919/135383816-430792aa-b8c3-4d6b-8176-1621293d089e.png)  
To answer a question type `!answer <question_number> "Answer"` in the #q-and-a channel. Example: `!answer 1 "Oct 12"`.  
Student answer:  
![image](https://user-images.githubusercontent.com/32313919/135383913-4a7431c3-9e14-466b-9a07-683df39bc1bc.png)  
Instructor answer:  
![image](https://user-images.githubusercontent.com/32313919/135383932-551850ef-6f6c-4349-b3a4-d36ce583de14.png)

### Events/Calendar

Events are items relevant to a class that are time-sensitive. Currently, the types of events include office hours, exams, and assignments. Events in a class are kept track of, and assignments/exams are displayed in a calendar for students and instructors to see.

Events can be created by instructors. Creation of an event can be initiated in the private `instructor-commands` channel with the `!create` command. The bot will ask the instructor about various details for the event. Once the event is created, it should exist persistently within the system and will be added to the event list.

The calendar is updated at the creation of any new event that gets displayed on the calendar. Everything is ordered by date and sorted into two categories, past events and future events. Links attached to assignments are displayed in the calendar as well. The footer of the calendar is tagged with the last time it was updated.

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/calendar.png)

### Office Hours

The bot contains functionality for handling TA office hours. After a TA office hour event is added and it is time for a TA's office hour to open, the bot will automatically create office hour channels in the server, allowing students to enter the office hour queue and instructors to help students based on the queue. Once the closing time for the office hour is reached, the channels related to the TA's office hour are automatically deleted.

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_channels.png)

##### Entering an office hour (as a student)

Students may wish to receive individual help from a TA or they may want to join other students for help as a group (when they need help with a group project, etc); TeachersPetBot supports both of these use cases. A student may enter the queue as an individual using the `!oh enter` command within the text channel for an ongoing office hour. Upon doing so, a new group will be created and the student will become the sole member of that group. Student may enter existing groups by inputting `!oh enter <group_id>`, where `group_id` is the ID of the group the student wishes to join (group IDs will be displayed in the queue). Once it is an individual's (or group's) turn to be helped by the instructor, all members of the group will be invited into a voice channel where they will be able to talk with the TA.

Upon entering this command in an office hour channel:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_enter.png)

The queue will look like this:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_lone.png)

Upon entering an existing group, say group '000':

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_enter_grp.png)

The queue will look like this:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_group.png)

##### Exiting the office hour queue (as a student)

A student may wish to exit the office hour queue for whatever reason; they may do so by typing `!oh exit` in the channel they are in the queue for.

If a student exists in the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_lone.png)

And enters this command:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_exit.png)

The student will be wiped from the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_empty.png)

##### Traversing the queue (as an instructor)

Once the instructor is ready to help the next student in the queue, they may enter `!oh next` in the office hour text channel. Upon doing so, DMs will be sent to all group members next in the queue notifying them that it is their turn, and they will be able to enter the office hour voice channel.

If a student exists in the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_lone.png)

And an instructor wishes to help the next student in the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_next.png)

The student will be invited to the instructor's voice channel and the queue will be advanced:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_empty.png)

### Profanity Censoring

Using the Python package better-profanity, Teacher's Pet will catch profane words sent by members of the guild, delete the message, and re-send the exact message with the bad word(s) censored out. It will also catch profane words in messages which have been edited to incude bad words. This package supports censoring based off any non-alphabetical word dividers and swears with custom characters. NOTE: Currently the Bot does not censor swears which have had extra alphabetical characters added.

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/profanity_example.PNG)

<br>
<h2> Iteration II </h2>

### New Member joining channel

Upon a new member joining the channel the BOT send the member a welcome message to the member in a private chat:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/member_addition.jpeg)

### Instructor view/modification

The remove instructor command can only be used by an instructor in the instructor commands channel. I removes a existing instructor from the role of an instructor and revokes the members permission to access the instructor commands channel.

When the remove instructor command is used:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/remove_Instructor.png)

The getInstructor command can be used in any channel and list outs the members in the guild who have Instructor role.

When the get instructor command is used:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/get_Instructor.png)

### Attendance

This functionality can be used only by the instructor. instructor-commands is the channel used. The command checks the total students in the guild with the students currently available in the General voice channel. It then generates the number of attendees and absentees. Then the students list is pushed to the instructor-commands channel.

When the attendance is requested by the instructor in the correct channel:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/attendance.png)

When the attendance is requested by the instructor in the wrong channel:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/attendance_wrong_channel.png)

### Help

This is a custom help command which is describes the command and on demand of a specific command, it provides syntax of the command, permitted users and channels. This command can be executed in any channel and by anyone.

General Help:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/help.png)

Help for a specific command:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/help_command.png)

### Custom Profanity Censoring

Building upon the existing python package better-profanity, Teacher's pet, in addition to catching the existing profane words, will now give an option to declare custom words as profane. This adds them to the list of words to be filtered and any further use of said word would cause it to be censored.
NOTE: Currently the Bot does not censor swears which have had extra alphabetical characters added.
Working :
Use the below syntax to include the custom word to the profane list:
![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/custom_profanity1.png)

Whenever the above word is used the below flow is triggered :
![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/custom_profanity2.png)

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/custom_profanity3.png)

### Detecting Close Calls (Upcoming Assignments and Exams)

This task runs in the background, once a day it checks if there are any assignments and exams coming up and reminds students. It works as follows :

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/close_calls2.png)

Whenever there is nothing to remind :

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/close_calls1.png)

### Poll Command

This command allows the Instructors to create a custom poll for the class. The command takes the following as inputs - Duration of the poll, Topic on focus, Options . Once the poll duration is complete the the command ends and displays the result of the poll. Note: A student can only vote for single option.<br />
Example: `!poll 2 "Topic for Tmrw's class" Physics chemistry biology maths`

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/poll_command.png)

### Utility Commands

#### Ping Command

Since the bot is hosted on cloud ( In this case Heroku ). Its crucial to know the latency of the bot. This command `!ping` returns the ping and the corresponding response time.

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/ping_command.png)

#### Status Command

For the purpose of Debugging and maintaining the bot `!stats` command has been added to keep track of CPU usage, Bot up time, Bot version, No. of users and Memory usage.

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/stats_command.png)

<br>
<h2> Iteration III </h2>

<h4>Charts</h4>
Instructors (like TAs, and Professors) can quickly make graphcs and charts directly in discord to share with students/users. Instructors can use this feature to share grade distributions, lecture participation/attendance, or other course statistics. All charts are named and stored into a json file when they are created. Students have acess to a command that allows them to view previously presented charts.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/charts.gif"></p>

<!-- Need to update this -->
<h4>Email Configuration</h4>

This feature enables users to configure their email address in the system to receive important notifications, attachments from professors, assignment reminders. Users can also update, view and unconfigure a configured email address through the system.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/email-address.gif"></p>

<!-- Need to update this -->
<h4>Email Interaction</h4>

This feature notifies all students regarding the next assignment deadline which is due for a day through email.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/email-reminder.gif"></p>

<!-- Need to update this -->
<h4>Re-Grading</h4>

This feature provides a way for students to submit regrade requests and Instructors can collect information of the requests submitted. There are various commands included to add, update, display and remove regrade requests.
This usecase was based on regrade request submission for CSE 510 SE FALL21 mid examination.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/Regrade.gif"></p>

<!-- Need to update this -->
<h4>Link Saving</h4>

This feature is helpful to save all the messages which contain important URLs. we have built a user command "!send_links" This command lets users access all messages which contain URLs. The messages Containing URLs are automatically get appended in a file and the file is attached when the "!send_links" command is input.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/link-saving.gif"></p>

<!-- Need to update this -->
<h4>Project Event</h4>

This feature allows instructors or teaching assistants to create a project event by providing information such as description, link for project submission and deadline. The deadline reminder is taken care of Email Interaction feature.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/project-event.gif"></p>

<!-- Need to update this -->
<h4>Spam Detection</h4>
This feature is used to detect spam in message channels. When a user tries to send too many messages in the channel, it gives a warning. This is useful when multiple users are trying to send mutiple messages. The warning lets the student know that they have sent too many messages.

<p align="left"><img width=65% src="https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/Spam-Detection.gif"></p>

<hr />
  
<br>  
<h2> Iteration IV </h2>  
<h4>Bard AI</h4>
Experience the power of AI and engage in informative and creative conversations with Bard through our !Aichat feature. Ask questions, spark creativity, and enjoy intelligent interactions—all at your fingertips.
Google Bard can answer your questions, generate text, translate languages, and write different kinds of creative content.
To use this feature, simply type !Aichat in any channel. Bard will then start a chat session with you. You can type anything you want,
<p align="left"><img width=65% src="https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/assets/102000543/fe0a0388-e95e-4c42-9b8b-18d2b26ffb9c"></p>

With this feature

- we Provide users with a fun and engaging way to interact with the bot.
- Help them learn new things and get answers to their questions.
- Generate creative content.

<p align="left"><img width=65% src="https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/assets/102000543/65f3bf75-bdf8-4784-addd-5e0c9d0c603d"></p>
Tpye exit to exit from the AI chat mode.

<h4>Upgraded Spam Detection</h4>
This feature is used to detect spam in message channels. First instructors have the ability to fully customize their spam detection settings. 
<p align="left"><img width=65% src="docs/media/set_spam.gif"></p>
When a user tries to send too many messages to the channel, it gives a warning. When a warned user continues to spam after this, they will be temporarily put in timeout, effectively ending their spam. This is a good feature to help keep rogue students in check, while also stopping students from spamming for rank. 
<p align="left"><img width=65% src="docs/media/spam.gif"></p>
<hr />
<h4>User ranking on the server</h4>
This feature is added so that users can interact more on the server and the server becomes more engaging overall. The rank of the user describes how active they are on the server and the more the user messages on the server, it increases their XP which increases the level of the user. The highest level users have the best rank on the server. The spam detection feature plugged with this feature will ensure that the students are not sending rogue messages or spamming on the server just to level up.
<br/>
<p align="left"><img width=65% src="docs/media/rank.gif"></p>
When a user runs command !rank, it shows the user their own rank, XP and level on a card. Similarly, if the user runs the command !rank @username, it will display the rank, XP and level for that particular user if the user exists on the server. Otherwise, it will show that the user doesn't exist.
<p align="left"><img width=65% src="docs/media/rank2.gif"></p>
<p align="left"><img width=65% src="docs/media/rank3.gif"></p>
<hr />
<h4>Interactive Greetings: Elevating the Welcome Message with Important Links</h4>
This feature guarantees that whenever a new member joins, they are greeted with a warm and inclusive welcome message that not only extends a friendly reception but also provides them with all the necessary and significant links to get started and navigate the guild effectively. 
<p align="left"><img width=65% src="https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/assets/144291380/ddfeec14-211a-4a74-aed1-7f66f0d13d88"></p>
