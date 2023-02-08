
import time

import logging

import smtplib

import requests

from decouple import config

from email.mime.text import MIMEText
 
class ServerMonitor:
    def __init__(self, url: str, email_recipient: str, max_retries: int = 3, retry_delay: int = 5):
        self.url = url
        self.email_recipient = email_recipient
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.logger = logging.getLogger(__name__)
    
    def check(self):
        for i in range(self.max_retries):
            try:
                response = requests.get(self.url)
                response.raise_for_status()
                if response.status_code >= 500 and response.status_code <= 599:
                    self.logger.error(f"Server is responding with error status code: {response.status_code}")
                    self.send_email("Server Error", f"The server is responding with error status code: {response.status_code}")
                    self.send_telegram_message(f"The server is responding with error status code: {response.status_code}")
                    break
                self.logger.info(f"Server is responding with status code: {response.status_code}")
                break
            except requests.exceptions.RequestException as error:
                self.logger.error(f"Server is not responding: {error}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
        else:
            self.logger.error(f"Server is not responding after {self.max_retries} attempts.")
            self.send_email("Server Not Responding", f"The server is not responding after {self.max_retries} attempts.")
            self.send_telegram_message(f"The server is not responding after {self.max_retries} attempts.")
        
    def send_email(self, subject: str, body: str):
        for i in range(self.max_retries):
            try:
                sender = config("EMAIL_FROM", default="ServerMonitor@example.com")
                msg = MIMEText(body)
                msg["Subject"] = subject
                msg["From"] = sender
                msg["To"] = self.email_recipient

                with smtplib.SMTP("smtp.example.com") as smtp:
                    smtp.send_message(msg)
                self.logger.info(f"Email sent successfully to {self.email_recipient}")
                break
            except smtplib.SMTPException as error:
                self.logger.error(f"Error sending email: {error}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
        else:
            self.logger.error(f"Failed to send email after {self.max_retries} attempts.")  

    def send_telegram_message(self, message: str):
        for i in range(self.max_retries):
            try:
                chat_id = config("TELEGRAM_CHAT_ID", default="")
                bot_token = config("TELEGRAM_BOT_TOKEN", default="")
                response = requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}")
                response.raise_for_status()
                self.logger.info(f"Telegram message sent successfully.")
                break
            except requests.exceptions.RequestException as error:
                self.logger.error(f"Error sending Telegram message: {error}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
        else:
            self.logger.error(f"Failed to send Telegram message after {self.max_retries} attempts.")


# Example usage
if __name__ == "__main__":
    monitor = ServerMonitor(
        "http://www.google.com", 
        "brahimbellahcen1996@gmail.com"
    )
    monitor.check()



