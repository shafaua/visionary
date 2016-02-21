# coding=utf-8
class BaseFeature(object):
    def __init__(self, max_results=10):
        self.max_results = max_results


class LogoDetection(BaseFeature):
    type_ = "LOGO_DETECTION"


class LabelDetection(BaseFeature):
    type_ = "LABEL_DETECTION"


class UnspecifiedDetection(BaseFeature):
    type_ = "TYPE_UNSPECIFIED"


class FaceDetection(BaseFeature):
    type_ = "FACE_DETECTION"


class LandmarkDetection(BaseFeature):
    type_ = "LANDMARK_DETECTION"


class TextDetection(BaseFeature):
    type_ = "TEXT_DETECTION"


class SafeSearchDetection(BaseFeature):
    type_ = "SAFE_SEARCH_DETECTION"


class ImagePropertiesDetection(BaseFeature):
    type_ = "IMAGE_PROPERTIES"
