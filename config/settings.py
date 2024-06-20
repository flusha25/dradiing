import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('cUMbCnCfEvQ2OjaDkteXNVrJXHcn0l7CLAosFWrBUfGPaCTsnLxnf6v7CQzZElFl')
SECRET = os.getenv('nU77jI83WgIQDTa5OhoJEDaJpsuqXbzo1vIM8g5TMYEUgKTrgb4LRnnPED4WTzvw')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

quote_currency = 'USDT'
initial_investment = 1.0  # investment amount 
rsi_period = 6  # ფასის მოძრაობის სიჩქარე
commission_rate = 0.001  #  
stop_loss_percentage = 0.015  # 10% stop loss ex: 0.015
take_profit_percentage = 0.05  # 20% take profit ex: 0.05.23