from .Step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('postflight')