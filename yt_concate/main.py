from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.Step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.Steps.download_captions import DownloadCaptions
from yt_concate.utils import Utils
from yt_concate.pipeline.Steps.preflight import Preflight
from yt_concate.pipeline.Steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        # Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':  # 進入點
    main()
