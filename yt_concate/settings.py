from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR ='DOWNLOADS'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTION_DIR = os.path.join(DOWNLOADS_DIR, 'caption')
OUTPUT_DIR = 'output'


# 環境變數存在檔案.env 使用時再讀取出來存回