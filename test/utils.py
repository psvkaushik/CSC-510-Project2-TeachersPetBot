import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import asyncio
from time import sleep

load_dotenv()
DICORD_BOT_NAME = os.getenv('DICORD_BOT_NAME')


class EmailUtility:
    """
        Class provides methods handling mailing logic of attachments and remainders
    """
    def __init__(self):
        # Accepting username and password from env file.
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.from_address = 'no-reply@teacherspetbot.com'
        self.subject = 'TEACHERS PET BOT NOTIFICATION'
        self.output_message = ''

    def send_email(self, recipient: list, attachment=None, subject: str = '', body: str = '',
                   filename: str = ''):
        """
             Sends email to the specified recipients.

             Parameters:
                 recipient: user email address.
                 attachment: file attachments.
                 subject: subject of the email.
                 body: body of the email.
                 filename: specifies the file name it should use for attachment data.

             Returns:
                 returns either an error stating a reason for failure or returns a success message
                 indicating that the reminder has been added

         """
        # Recipient address are to be provided as list.
        to_address = recipient if isinstance(recipient, list) else [recipient]

        msg = MIMEMultipart()
        print(msg)
        msg['Subject'] = subject if subject else self.subject
        msg['From'] = self.from_address
        msg['To'] = ''.join(to_address)
        body = body if body else "This mail was sent from TeachersPetBot notification service," \
                                 " Please unsubscribe through bot to stop notifications."
        msg.attach(MIMEText(body, 'plain'))

        if attachment:
            # Attaching the attachment data only if it exists.
            part = MIMEBase('application', "octet-stream")
            part.set_payload(attachment)
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(part)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(list(self.from_address), to_address, msg.as_string())
            server.close()
            self.output_message = "successfully sent the mail to " + ''.join(recipient)
            print(self.output_message)
        except Exception as error:
            with open("err.log", "a", encoding='utf8') as f:
                f.write(f"Error while sending email : {str(error)}\n")
            raise error


async def wait_for_msg(testing_bot, channel, content):
    sleep(0.6)
    try:
        return await testing_bot.wait_for('message', timeout=2, check=lambda x: x.guild.id == channel.guild.id and x.author.name == DICORD_BOT_NAME and content in x.content)

    except asyncio.TimeoutError:
        #messages = await channel.history(limit=1).flatten()
        messages = [message async for message in channel.history(limit=1)]
        if not (len(messages) != 0 and content in messages[0].content):
            print(f'Message content {content} not found')
            raise Exception()
        return messages[0]


async def wait_for_channel_create(testing_bot, guild_id, name):
    try:
        return await testing_bot.wait_for('guild_channel_create', timeout=4, check=lambda x: x.guild.id == guild_id and x.name == name)
    except asyncio.TimeoutError:
        new_channel = next((ch for ch in testing_bot.get_guild(guild_id).text_channels if ch.name == name), None)
        if new_channel is None:
            print(f'Channel {name} not found')
            raise Exception()
        return new_channel
