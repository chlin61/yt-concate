from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils, logger):
        search_word = inputs['search_word']
        found = []  # 找到的list
        for yt in data:
            captions = yt.captions
            if not captions:  # 如有不存在的字幕檔  則略過~
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        # print(found)
        return found
