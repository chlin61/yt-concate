import sys
import getopt
import logging

from yt_concate.pipeline.Steps.preflight import Preflight
from yt_concate.pipeline.Steps.initializeyt import InitializeYT
from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.download_captions import DownloadCaptions
from yt_concate.pipeline.Steps.read_caption import ReadCaptions
from yt_concate.pipeline.Steps.search import Search
from yt_concate.pipeline.Steps.download_videos import DownloadVideos
from yt_concate.pipeline.Steps.edit_video import EditVideo
from yt_concate.pipeline.Steps.postflight import Postflight
from yt_concate.utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.Steps.step import StepException

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def printStage():
    print('main.py -c <channel_id> -s <search_word> -l <limit>')


def configLog():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s : %(message)s : %(asctime)s')
    fileHandler = logging.FileHandler('EvenLog.log')
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def main(argv):
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }
    short_opt = 'hc:s:l:'
    long_opt = 'channel_id search_word limit'.split()
    try:
        opts, args = getopt.getopt(argv, short_opt, long_opt)
    except getopt.GetoptError:
        printStage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py Option')
            print('Option:')
            print('{:<6}{:>15}{}'.format('-c', '--channel_id', 'input channel ID for youtube to download video.'))
            print('{:<6}{:>15}{}'.format('-s', '--search_word',
                                         'input Search Word to search caption from youtube video for Channel ID.'))

            sys.exit()
        elif opt in ('-c', '--channel_id'):
            inputs['channel_id'] = arg
        elif opt in ('-s', '--search_word'):
            inputs['search_word'] = arg
        elif opt in ('-l', '--limit'):
            inputs['limit'] = arg

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]
    logger = configLog()
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils, logger)


if __name__ == '__main__':  # 進入點
    main(sys.argv[1:])
