<p align="center"><img src="https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/teacherspet.png" alt="alt text" width=200 height=200>
  
  <h1 align="center"> Teacher's Pet </h1>
  
<h2 align="center"> Streamline Your Class Discord</h2>

![Python](https://img.shields.io/badge/python-v3.7+-brightgreen.svg)
![GitHub](https://img.shields.io/github/license/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
![GitHub issues](https://img.shields.io/github/issues/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
![GitHub closed issues](https://img.shields.io/github/issues-closed/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
![Lines of code](https://tokei.rs/b1/github/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
[![codecov](https://codecov.io/gh/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/branch/main/graph/badge.svg?token=QTKU51PZSO)](https://codecov.io/gh/tanmaypardeshi/CSC-510-Project2-TeachersPetBot)
[![GitHub Workflow Status](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/actions/workflows/test.yml/badge.svg)](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/actions/workflows/test.yml)

[![codecov](https://codecov.io/gh/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/graph/badge.svg?token=3QCL57IUZF)](https://codecov.io/gh/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
![GitHub](https://img.shields.io/github/license/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
[![DOI](https://zenodo.org/badge/718312021.svg)](https://zenodo.org/doi/10.5281/zenodo.10211826)
[![](https://tokei.rs/b1/github/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0).
![Github pull requests](https://img.shields.io/github/issues-pr/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
[![GitHub stars](https://badgen.net/github/stars/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)](https://badgen.net/github/stars/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
![Respost - Write comment to new Issue event](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/Respost.yml/badge.svg)
![version](https://img.shields.io/badge/version-4.1-blue)
![Greetings](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/Greetings.yml/badge.svg)
![Close as a feature](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/close_as_a_feature.yml/badge.svg)
![GitHub contributors](https://img.shields.io/github/contributors/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0)
[![Style Checker and Prettify Code](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/Style_Checker_and_Prettify_Code.yml/badge.svg)](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/Style_Checker_and_Prettify_Code.yml)
[![Running Code Coverage](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/codecov.yml/badge.svg)](https://github.com/psvkaushik/CSC-510-Project2-TeachersPetBotv2.0/actions/workflows/codecov.yml)

<!-- I am not sure about this parameter yet. Any idea what to do about this? -->
<!-- ![GitHub deployments](https://img.shields.io/github/deployments/Ashwinshankar98/TeachersPetBot/discord-bot-phase2)<br/> -->

## Contents

1. [ Description ](#desc)
2. [ Bot Features](#features)
3. [ Installation and Running ](#instrun)
4. [ Testing ](#testing)
5. [ Bot Commands ](#commands)
6. [ Future Scope ](#fscope)
7. [ Want to contribute? ](#contribute)
8. [ License ](#license)

<a name="desc"></a>
Click Below to Watch The Video!

https://youtu.be/wzObedlYgho

<h2>Software Engineering Project for CSC 510 : Phase V</h2>

Teacher's Pet is a Discord Bot for class instructors to streamline their Discord servers. Discord is a great tool for communication and its functionalities can be enhanced by bots and integrations.

For 5.0, we created new tools for instructors and students to use to improve course communication. After version 4.0's success, we decided we wanted to improve upon some of its features including spam, profanity settings, penalty, awarding-penalize XP, QNA channel etc. Our main objective for 5.0 was to make using Discord a more controlled and enjoyable experience.

<hr />

<a name="features"></a>

<h2>Bot Features</h2>

[Click here to see the features of iterations I, II, III and IV.](docs/feature-history.md)

1. **Custom profanity settings**  
   Users entering NSFW messages can be warned, timed-out, or banned based on instructor-defined or default settings—warning, timeout, followed by server ban
2. **Persistent Block from server**  
   Banned users remain blocked; when the bot restarts, attempting reentry leads to an automatic kick if the bot is offline. Online attempts are barred
3. **Instructor Channel**  
   Tagging instructors results in questions being posted in the instructor QNA channel; replies posted back to the main channel, ensuring no question goes unnoticed
4. **DB initialization**
   Proper integration with databases ensures new user entry upon bot restart; detects and creates missing user database entries on server join
5. **Spam Violation penalty**
   Users receive 10XP penalty for spamming, enhancing the XP-based ranking system and receiving timeouts for improper behavior
6. **NSFW violation penalty**
   Custom XP penalties set by instructors for users posting NSFW messages in chat channels
7. **!Award XP**  
   Instructors award XP to users in the instructor channel for encouraging positive behaviors
8. **!Penalize XP**  
   Instructors can reduce XP for reasons like invalid input or irrelevant discussions
9. **!Leaderboard**  
   Users access top 10 rankers' leaderboard based on their ranks and XP
10. **!unblock_user**  
    Instructors gain authority to unblock users by usernames, allowing banned individuals to rejoin

<a name="instrun"></a>

<h2> Installation and Running </h2>

#### Tools and Libraries Used

In addition to the packages from [requirements.txt](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/requirements.txt) which need to be installed, please have the following installed on your machine:

- [Python 3.9.7](https://www.python.org/downloads/)
- [Sqlite](https://www.sqlite.org/download.html)

To install and run Teacher's Pet, follow the instructions in the [Installation and Testing Guide](Installation.md).

<a name="testing"></a>

<h2>Testing </h2>

To run tests on the Teacher's Pet, follow instructions in the [Installation and Testing Guide](Installation.md).

<hr />

<a name="commands"></a>

<h2> Bot Commands </h2>

<h3> Bot commands from iteration V </h3>   
  
`!Leaderboard` any user can run to see the leaderboard of top 10 rankers

`!penalize <@member> <xp_points_penalized>` can use this new command to reduce XP (Instructor command)

`!award <@member> <xp_points_awarded>` can use this in the instructor channel to award XP to users (Instructor command)

`!unblock_user` Allows instructors to have the power to unblock users (Instructor command)
<br>

<h3> Bot commands from iteration I, II, III, IV </h3>    
  
`set_spam_settings command` Set the spam_settings (Instructor command)

`!setInstructor <@member>` Set a server member to be an instructor (Instructor command)

`!removeInstructor <@member>` Remove a server member from the instructor role (Instructor command)

`!getInstructor` Get the current instructors in the server

`!attendance` Find attendance from voice channel (Instructor command)

`!ask "<question>"` Ask a question

`!answer <question_number> "<answer>"` Answer a question

`!poll <command>` Run a poll for students (Instructor command)

`!create` Start creating an event (Instructor command)

`!oh enter` Enter an office hour queue as an individual student

`!oh enter <group_id>` Enter an office hour queue with a group of students

`!oh exit` Exit the office hour queue

`!oh next` Go to next student in queue as an instructor (Instructor command)

`!help` Gets the descriptions for all commands

`!help <command>` Describes a command in detail

`!ping` Find the latency of network

`!stats` Gets the statistics of system and softwares used

`!regrade-request` This command lets a student add a regrade-request

`!update-request` This command lets a student update an existing regrade-request

`!remove-request` This command removes a regrade request

`!display_requests` This command lets a student display all regrade requests

`!chart` This command lets admins make a custom chart of any type with any size of dataset

`!check_chart` This command lets students/users check any chart if previously created

`!create_email` This command enables users to configure their email address to receive important reminder notifications and attachments

`!view_email` This command enables users to view their configured email address

`!update_email` This command enables users to update their configured email address

`!remove_email` This command enables users to delete their configured email address

`!create -> press project button` This command enables users to create a project

<hr />

<a name="fscope"></a>

<h2> Future Scope </h2>

This bot has endless possibilities for functionality. Features which we are interested in adding but did not have time for include but are not limited to:

- Adding detailed error display integration to the bot
- Add Tutor role
- Add ways for users to lose exp in the rank feature(spamming etc)
- Add commands so an instructor can customize how rank exp is awarded(what for and how much etc)
- Refactor code to use cogs
- Add a gibberish detector that deletes comments that are irrelevant to the class
- Funnel the AI chat responses to a limited set(so AI only answers questions an instructor wants them to answer)
- Upgrade to a better chatbot API that is free

<hr />

<a name="contribute"></a>

<h2>How to Contribute? </h2>

Check out our [CONTRIBUTING.md](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/CONTRIBUTING.md) for instructions on contributing to this repo and helping enhance this Discord Bot, as well as our [Code of Conduct](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/CODE_OF_CONDUCT.md) guidelines.

<a name="license"></a>

<h2> License </h2>

The project is licensed under the [MIT License](https://github.com/tanmaypardeshi/CSC-510-Project2-TeachersPetBot/blob/main/LICENSE).

<hr />

<h3> Team Members </h3>

- :octocat: [Ayush Agarwal](https://github.com/ayush-ai8)
- :octocat: [Kaushik Pillalamarri](https://github.com/psvkaushik)
- :octocat: [Surya Upadyayula](https://github.com/SuryaUpadyayula)
- :octocat: [Vaishnavi Naik](https://github.com/VaishnaviNaik96)

<h3> Previous Authors </h3>

#### Sam Kwiatkowski-Martin

#### Abhinav Sinha

#### Chandana Ray

#### Tanmay Pardeshi

#### Sandesh Aladhalli Shivarudre Gowda

#### Chandatahas Reddy Mandapati

#### Sri Pallavi Damuluri

#### Niraj Lavani

#### Harini Bharata

#### Ashwin Shankar Umasankar

#### Itha Aswin

#### Kailash Singaravelu

#### Saikaushik Kalyanaraman

#### Shakthi Nandana Govindan

# Contact us

For any questions and contribution please contact: ncsuse23@gmail.com

Made with ❤️ on GitHub.
