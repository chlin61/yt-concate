from yt_concate.pipeline.Steps.preflight import Preflight
from yt_concate.pipeline.Steps.initializeyt import InitializeYT
from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.download_captions import DownloadCaptions
from yt_concate.pipeline.Steps.read_caption import ReadCaptions
from yt_concate.pipeline.Steps.search import Search
from yt_concate.pipeline.Steps.download_videos import DownloadVideos
from yt_concate.pipeline.Steps.postflight import Postflight
from yt_concate.utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.Steps.step import StepException


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        # Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':  # 進入點
    main()
