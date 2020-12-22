import os
from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTION_DIR




class Utils:

    def __init__(self):
        pass

    def create_dir(self):
        # if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        # if not os.path.exists(CAPTION_DIR):
        os.makedirs(CAPTION_DIR, exist_ok=True)
        # if not os.path.exists(VIDEOS_DIR):
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id_from_url(url) + '.txt')

    def cation_file_exist(self, url):
        path = self.get_caption_filepath(url)
        # 確認檔案是否存在且檔案大小大於0
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        # 確認檔案是否存在且檔案大小大於0
        return os.path.exists(path) and os.path.getsize(path) > 0



