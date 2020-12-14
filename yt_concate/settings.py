from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')

#環境變數存在檔案.env 使用時再讀取出來存回