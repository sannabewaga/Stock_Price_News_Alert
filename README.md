# Stock_Price_News_Alert

**Overview**


Stock News Alert is a Python script that monitors the daily percentage change in the stock price of a specified company (e.g., Tesla Inc.) and sends an email alert if the percentage change exceeds a certain threshold. The script also retrieves the latest news headlines related to the company from the News API and includes them in the email alert.

**Features**

Monitors the daily percentage change in the stock price of a specified company.
Retrieves the latest news headlines related to the company from the News API.
Sends an email alert if the percentage change in the stock price exceeds a certain threshold.
Includes the latest news headlines in the email alert.

**How It Works**

Fetching Stock Data: The script uses the Alpha Vantage API to fetch daily stock price data for the specified company (e.g., Tesla Inc.).
Calculating Percentage Change: It calculates the percentage change in the stock price between the current day and the previous day.
Fetching News Data: The script retrieves the latest news headlines related to the specified company from the News API.
Sending Email Alert: If the percentage change in the stock price exceeds a certain threshold (e.g., 1%), the script sends an email alert to notify the user. The email includes the percentage change and the latest news headlines related to the company.

**Configuration:**

Open the main.py file and update the following variables with your own values:
STOCK: The stock symbol of the company you want to monitor (e.g., "TSLA" for Tesla Inc.).
COMPANY_NAME: The name of the company you want to monitor (e.g., "Tesla Inc").
API_KEY: Your API key for the Alpha Vantage API.
NEWS_API: Your API key for the News API.
SENDER_EMAIL: Your email address for sending the email alerts.
SENDER_PASSWORD: Your email password for authentication.
RECIPIENT_EMAIL: The email address where you want to receive the email alerts.


![image](https://github.com/sannabewaga/Stock_Price_News_Alert/assets/113686593/25d7b337-1a3d-49ba-bf3f-c025201c7206)
![image](https://github.com/sannabewaga/Stock_Price_News_Alert/assets/113686593/b83953da-e8b2-4034-b269-011868a1c520)

