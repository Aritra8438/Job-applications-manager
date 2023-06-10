import os
import requests
import telebot
import uuid
import validators
import magic
from pyresparser import ResumeParser
import warnings

warnings.filterwarnings("ignore")

API_KEY = '6204403979:AAEHWICGbr7vWYZX6Ga570dc6soU9HxDf4U'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    username = message.from_user.username
    if username is None:
        username = "A Random User"
    print(username + " has triggered the bot")
    bot.send_message(message.chat.id, "Welcome " + username + " ( in a 🤖 voice), How Can I help you?")
    help_text = "You can provide me with your resume (preferably in PDF/DOCX format). \n" \
                "Or, you can provide me with the file url (preferably in PDF/DOCX format and not in g-drive docs " \
                "format). \n" \
                "I will recommend available jobs for you 🪄. Thank You."
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['greet'])
def greet(message):
    try:
        username = message.from_user.username
        if username is None:
            username = "A Random User"
        print(username + " is greeted by the bot")
        bot.reply_to(message, "HEY " + username + ", Nice To Meet You")
    except Exception as e:
        bot.send_message(message.chat.id, "Can you try again?")


@bot.message_handler(commands=['github'])
def github(message):
    try:
        username = message.from_user.username
        if username is None:
            username = "A Random User"
        print(username + " asked for the repo link")
        repo_text = 'Hey , [here](https://github.com/Aritra8438/Job-applications-manager) you ' \
                    'will ' \
                    'find the source code of this bot.'
        bot.send_message(message.chat.id, repo_text, parse_mode='Markdown')
    except Exception as e:
        bot.send_message(message.chat.id, "Can you try again?")


@bot.message_handler(content_types=['document'])
def handle_document(message):
    username = message.from_user.username
    if username is None:
        username = "A Random User"
    print(username + " has requested this service")
    try:
        bot.send_message(message.chat.id, "Hi " + username + ", We are currently parsing your resume")
        _, file_ext = os.path.splitext(message.document.file_name)
        url = "https://api.telegram.org/bot" + API_KEY + "/getFile"
        payload = {"file_id": message.document.file_id}
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        url = "https://api.telegram.org/file/bot" + API_KEY + "/" + response.json()["result"]["file_path"]
        file_name = uuid.uuid4()
        path_to_download = 'Resumes/' + str(file_name) + file_ext
        response = requests.get(url)
        if response.status_code == 200:
            with open(path_to_download, "wb") as file:
                file.write(response.content)
        else:
            print("Failed to download the file. Status code:", response.status_code)
        data = ResumeParser(path_to_download).get_extracted_data()
        linked_in_url = "https://www.linkedin.com/jobs/search/?"
        skills = data["skills"]
        exp = "f_E=1"
        if data["total_experience"] <= 1:
            exp = "f_E=1%2C2"
        elif data["total_experience"] <= 3:
            exp = "f_E=2%2C3"
        elif data["total_experience"] <= 6:
            exp = "f_E=3%2C4"
        elif data["total_experience"] <= 8:
            exp = "f_E=4%2C5"
        elif data["total_experience"] <= 11:
            exp = "f_E=5%2C6"
        else:
            exp = "f_E=6"
        linked_in_url += exp
        bot.send_message(message.chat.id,
                         "Hi " + data["name"] + ", Please verify your email address and mobile number \nemail "
                                                "address: " + data['email'] + "\nmobile_no: " + data["mobile_number"])
        bot.send_message(message.chat.id, "If those information are correct, you might want to apply for this jobs")
        jobs = "Based on your resume, you can apply for these jobs, All the best 🌟 \n"
        for skill in skills:
            jobs += "[" + skill + "](" + linked_in_url + "&keywords=" + skill + ")\n"
        bot.send_message(message.chat.id, jobs, parse_mode='Markdown')
    except Exception as e:
        bot.send_message(message.chat.id, "Hey, there were some problems while parsing your resume, make sure you "
                                          "have submitted a resume and try again")
        bot.send_message(message.chat.id, str(e))


@bot.message_handler(content_types=['text'])
def handle_document(message):
    try:
        username = message.from_user.username
        if username is None:
            username = "A Random User"
        print(username + " has requested this service")
        file_url = message.text
        if not validators.url(file_url):
            bot.send_message(message.chat.id, "This url is malformed")
            return
        file_id = file_url.split('/')[-2]
        url = f"https://drive.google.com/uc?id={file_id}"
        response = requests.get(url)
        file_ext = magic.from_buffer(response.content, mime=True).split('/')[-1]
        if file_ext != 'pdf':
            file_ext = 'docx'
        file_name = uuid.uuid4()
        path_to_download = 'Resumes/' + str(file_name) + "." + file_ext
        if response.status_code == 200:
            with open(path_to_download, "wb") as file:
                file.write(response.content)
        else:
            print("Failed to download the file. Status code:", response.status_code)
        data = ResumeParser(path_to_download).get_extracted_data()
        linked_in_url = "https://www.linkedin.com/jobs/search/?"
        skills = data["skills"]
        exp = "f_E=1"
        if data["total_experience"] <= 1:
            exp = "f_E=1%2C2"
        elif data["total_experience"] <= 3:
            exp = "f_E=2%2C3"
        elif data["total_experience"] <= 6:
            exp = "f_E=3%2C4"
        elif data["total_experience"] <= 8:
            exp = "f_E=4%2C5"
        elif data["total_experience"] <= 11:
            exp = "f_E=5%2C6"
        else:
            exp = "f_E=6"
        linked_in_url += exp
        bot.send_message(message.chat.id,
                         "Hi " + data["name"] + ", Please verify your email address and mobile number \nemail "
                                                "address: " + data['email'] + "\nmobile_no: " + data["mobile_number"])
        bot.send_message(message.chat.id, "If those information are correct, you might want to apply for this jobs")
        jobs = "Based on your resume, you can apply for these jobs, All the best 🌟 \n"
        for skill in skills:
            jobs += "[" + skill + "](" + linked_in_url + "&keywords=" + skill + ")\n"
        bot.send_message(message.chat.id, jobs, parse_mode='Markdown')
    except Exception as e:
        bot.send_message(message.chat.id, "Hey, there were some problems while parsing your resume, make sure you "
                                          "have shared public link and it links to a resume and try again")
        bot.send_message(message.chat.id, str(e))


bot.polling()
