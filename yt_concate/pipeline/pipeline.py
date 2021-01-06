from .Steps.step import StepException
from yt_concate.utils import Utils


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils, logger):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils, logger)
            except StepException as e:
                print('Exception happened:', e)
                break
