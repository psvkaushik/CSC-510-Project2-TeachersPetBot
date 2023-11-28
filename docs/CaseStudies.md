## Case Study

We have implemented following functionalites across multiple platforms and tested. Following are the case studies:

1. Custom profanity settings
   Users entering NSFW messages can be warned, timed out, or banned based on instructor-defined or default settings—warning, timeout, followed by server ban.

   ![set_profanity_settings_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/2fcb7cf5-98c1-46d9-9581-3037cfda9950)

2. Persistent Block from server
   Banned users remain blocked; when the bot restarts, attempting reentry leads to an automatic kick if the bot is offline. Online attempts are barred.

   ![blocked_user_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/b9860091-fafd-4515-958c-835582126bdd)

3. Instructor Mentions Channel  
   Tagging instructors results in questions being posted in the instructor QNA channel; replies are posted back to the main channel, ensuring no mention goes
   unnoticed.

   ![instructor_mention_gif](https://github.com/psvkaushik/CSC-510-Project3-TeachersPetBotv2.0/assets/22112102/e54c2fc2-67e2-4d81-83f3-7061e5d0120a)

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
