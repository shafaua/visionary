# coding=utf-8
class GoogleCloudVisionException(Exception):
    def __init__(self, text):
        self.text = text

    def __unicode__(self):
        return "There was a problem with request: %s" % self.text
