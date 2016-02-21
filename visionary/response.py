import json
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
BoundingPoly = namedtuple('BoundingPoly', ['vertices'])
BaseLogoAnnotation = namedtuple('LogoAnnotation', ['mid', 'description', 'score', 'boundingPoly'])
LabelAnnotation = namedtuple('LabelAnnotation', ['mid', 'description', 'score'])


# Fix default argument for namedtuple
def make_logo_annotation(mid, description, score, boundingPoly=None):
    return BaseLogoAnnotation(mid, description, score, boundingPoly)


class Response(object):
    def __init__(self, data):
        self.data = data

    @property
    def logo_annotations(self):
        responses = self.data.get('logoAnnotations', [])
        return [make_logo_annotation(**logo_annotation) for logo_annotation in responses]

    @property
    def label_annotations(self):
        responses = self.data.get('labelAnnotations', [])
        return [LabelAnnotation(**logo_annotation) for logo_annotation in responses]


class GoogleCloudVisionResponse(object):
    def __init__(self, content):
        self.content = content
        self.cache = None

    @property
    def error(self):
        return self.data.get('error')

    @property
    def ok(self):
        return self.data.get('error') is None

    @property
    def data(self):
        if self.cache is None:
            self.cache = json.loads(self.content)
        return self.cache

    @property
    def responses(self):
        responses = self.data.get('responses', [])
        return [Response(feature) for feature in responses]
