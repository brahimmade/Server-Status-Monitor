# Server Monitor Script #

    The Server Monitor script is a Python script that monitors the status of a given server and sends notifications if the server is not responding or if it returns an error status code (5xx).

Requirements

    Python 3.x
    requests library
    python-decouple library
    logging library

Features

    Monitoring of server status
    Automatic retry mechanism in case of failed checks
    Configurable maximum number of retries and retry delay
    Notifications via email and Telegram
    Logging of all events to a file for easy debugging

Usage

    1 - Clone or download the script to your local machine or server.
    
    2 - Install the required libraries by running the following command in your terminal or command prompt:
        pip install requests python-decouple
    
    3 - Set the following environment variables in a .env file in the same directory as the script:
        URL=<server url>
        MAX_RETRIES=<maximum number of retries>
        RETRY_DELAY=<delay in seconds between retries>
        EMAIL_SUBJECT=<email subject>
        EMAIL_FROM=<sender email address>
        EMAIL_TO=<recipient email address>
        SMTP_SERVER=<SMTP server address>
        SMTP_PORT=<SMTP server port>
        SMTP_USER=<SMTP server username>
        SMTP_PASS=<SMTP server password>
        TELEGRAM_TOKEN=<Telegram Bot API token>
        TELEGRAM_CHAT_ID=<Telegram chat id>

    4 - Replace the placeholders in the .env file with the actual values for your server and notification preferences.

    5 - Run the script by typing python server_monitor.py in your terminal or command prompt.

    6 - Optionally, you can use a task scheduler like cron or the Task Scheduler on Windows to run the script at regular intervals.

Class Structure
    The script includes the following class:

    ServerMonitor
        check method: checks the status of the server and sends notifications if necessary.
        send_email method: sends an email notification.
        send_telegram_message method: sends a Telegram message notification.
        logger attribute: a logger instance that logs messages to the console and a file.
        
Configuration
    The script can be configured by modifying the environment variables in the .env file and by adjusting the logging configuration in the script.

Contributing
    Feel free to submit pull requests or suggest improvements to the script.