import os
from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTION_DIR

class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTION_DIR):
            captions = {}
            with open(os.path.join(CAPTION_DIR, caption_file), 'r') as f:
                count = 0
                time = None
                for line in f:
                    if count % 4 == 1:
                        time = line.strip()
                    if count % 4 == 2:
                        cap = line.strip()
                        captions[cap] = time
                    count += 1
            data[caption_file[:-4]] = captions
        pprint(data)
        return data
