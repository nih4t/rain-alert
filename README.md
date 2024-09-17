# Never Forget Your Umbrella Again ☂️

If you’re the kind of person who sometimes forgets an umbrella on rainy days, this script is here to save the day! It checks the weather forecast and sends you a friendly reminder via Telegram if it’s going to rain **today**.

## What Does This Script Do?

- **Checks today’s weather** using OpenWeatherMap for your location.
- **Sends a Telegram message** if rain is expected so you won’t forget your umbrella.

## What You Need to Get Started

Here’s what you’ll need to set this up:
1. **An OpenWeatherMap API Key**: You can grab one for free by signing up at [OpenWeatherMap](https://openweathermap.org/appid).
2. **A Telegram Bot**: You’ll need to create your own Telegram bot and get a bot token and your chat ID. If you’re not familiar with how to do that, follow [this guide](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e).
3. **Python Libraries**: This script uses the `requests` library to talk to the APIs. It’s easy to install!

## Setup Instructions

### Step 1: Install Python Libraries
Before running the script, make sure you have the required libraries installed. Open your terminal or command line and run:

```bash
pip install requests
```

### Step 2: Add Your API Key and Telegram Bot Info
Open the script and replace the following placeholders with your actual details:

- **API_KEY**: Your OpenWeatherMap API key.
- **bot_token**: Your Telegram bot’s token.
- **bot_chatID**: Your chat ID where you want to receive the message.

Here’s the section of the code you’ll need to update:

```python
API_KEY = "your_openweathermap_api_key"
bot_token = "your_telegram_bot_token"
bot_chatID = "your_telegram_chat_id"
```

### Step 3: Customize Your Location
Change the latitude (`LAT`) and longitude (`LON`) in the script to the coordinates of your city or wherever you want the forecast:

```python
LAT = 6.268720  # Example latitude
LON = 100.439522  # Example longitude
CNT = 4  # Number of forecast periods to check (all today)
```

The `CNT` value checks today’s forecast by looking at the next four periods (morning, afternoon, evening, night).

### How It Works

Once you’ve set it up:
1. The script sends a request to OpenWeatherMap to check the weather for your location.
2. It checks whether rain is forecasted today.
3. If rain is expected, the script sends you a message on Telegram that says:

   ```
   Bring umbrella, It's raining today ☂️⚡
   ```

And that’s it! You’ll get an alert when rain is expected so you can prepare.

## Automate the Script

Want to run this script automatically every morning? You can set it up to run daily using services like [PythonAnywhere](https://www.pythonanywhere.com/) or schedule it on your local machine using a task scheduler (e.g., Windows Task Scheduler or a cron job on Linux/Mac).

By scheduling it, you’ll get the weather alert automatically at the time you want!

Now you're ready to say goodbye to rainy day surprises and always stay dry with your trusty umbrella!
