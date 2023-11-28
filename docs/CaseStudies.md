## Case Study

We have implemented following functionalites across multiple platforms and tested. Following are the case studies:

1. Custom profanity settings
   Whenever a user enters an nsfw message, the user can be warned, timed-out and even blocked from the server as per the settings of the instructor or the default
   settings which is warning, followed by timeout followed by ban from server

2. Persistent Block from server
   If a user is banned and kicked out from the server they remain blocked, if they try to join the server when the bot is not running, it will kick them out when
   the bot starts up. If they try to join again when the bot is running, it will not let them join the server

3. Instructor Mentions Channel  
   If any user tags any instructor or refer instructors, the Question will pop up in the instructor QNA channel and once they reply to the message in that  
   channel it will be posted back to the main channel. It will help ensure that no question goes unnoticed as all the questions are available to see at one glance  
   with no clutter in a separate channel

4. DB initialization
   Proper integration with databases ensures new user entry upon bot restart; detects and creates missing user database entries on server join.

5. Spam Violation penalty
   Users receive a 10XP penalty for spamming, enhancing the XP-based ranking system, and receiving timeouts for improper behavior.

   ![spam_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/0912b6ce-50ce-45e8-9180-02ad3be6ec8d)

6. NSFW violation penalty
   Custom XP penalties set by instructors for users posting NSFW messages in chat channels.

   ![nsfw_profanity_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/0a1a5f82-0da4-4b3f-a1d6-db4694e4791f)

7. !Award XP
   Instructors award XP to users in the instructor channel for encouraging positive behaviors.

   ![award_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/c0ac2d86-96ae-46f9-add3-d3d3fa593733

8. !Penalize XP
   Instructors can reduce XP for reasons like invalid input or irrelevant discussions.

   ![penalize_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/c26fa9ed-2d64-4be3-9ae0-1064079d618b)

9. !Leaderboard
   Users access the top 10 rankers' leaderboard based on their ranks and XP.

   ![leaderboard_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/730895ed-c163-4496-9dd9-defb8d442b82)

10. !unblock_user
    Instructors gain authority to unblock users by usernames, allowing banned individuals to rejoin.

![unblock_user_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/996ac853-8eb4-45aa-a3a9-f46b39cdd7ab)
