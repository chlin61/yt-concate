from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        source_data = len(data)
        yt_set = set([found.yt for found in data])  # 用python內建的功能將重複性的影片路徑刪除
        print('videos to download = ', len(yt_set))
        for yt in yt_set:
            url = yt.url
            if utils.video_file_exist(yt):
                print(f'found existing video file for {url}, skipping..')
                continue
            print(url + ' downloading ....')
            try:
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

            except:
                #  太多Timeout
                print('Except :TimeError')
                for found in data:
                    if yt == found.yt:
                        data.remove(found)
        print('原來found caption :', source_data)
        print('download video for found caption:', len(data))
        return data
