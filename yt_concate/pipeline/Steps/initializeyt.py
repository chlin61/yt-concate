# 把video list建立出實例來
from .step import Step
from yt_concate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils, logger):
        return [YT(url) for url in data]
#  把video link 轉成物件

