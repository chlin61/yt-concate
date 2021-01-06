from pytube import YouTube
from threading import Thread
from .step import Step
import os
from yt_concate.settings import VIDEOS_DIR


def DownloadVideo(inputs, logger):
    # ids = []
    # for s in inputs:
    url, video_dir, filename = inputs
    logger.info(url + ' Downloading ....')
    try:
        YouTube(url).streams.first().download(output_path=video_dir, filename=filename)
        logger.debug('Finish for download ' + url)

    except:
        logger.error('Error for download ' + url)
        logger.debug('Except :TimeError')


class DownloadVideos(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('Download Videos ...')
        source_data = len(data)
        # 用python內建的功能將重複性的影片路徑刪除
        yt_set = set([found.yt for found in data])
        logger.info('videos to download = ' + str(len(yt_set)))
        DWList = []
        for yt in yt_set:
            url = yt.url
            if utils.video_file_exist(yt):
                logger.debug(f'found existing video file for {url}, skipping..')
                continue
            DWList.append([url, VIDEOS_DIR, yt.id])
            # 將所有的需要下載的影片資訊 記錄在list
        threads = []
        for i in DWList:
            threads.append(Thread(target=DownloadVideo, args=(i, logger,)))
        count = 0
        a = []
        for i in threads:
            a.append(i)
            count += 1
            if count % 3 == 0 or count == len(threads):
                for c in a:
                    c.start()
                for c in a:
                    c.join()
                a = []

        return data
