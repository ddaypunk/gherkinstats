__author__ = 'andydelso'


class Gherkin:
    def __init__(self, tags, feature_name, scenarios, background=None):
        self.tags = tags
        self.feature_name = feature_name
        self.scenarios = scenarios
        self.background = background