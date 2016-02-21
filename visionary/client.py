# coding=utf-8
import json
import base64
import requests
from .exceptions import GoogleCloudVisionException
from .response import GoogleCloudVisionResponse


class GoogleCloudVision(object):
    API_URL_PATTERN = "https://vision.googleapis.com/v1/images:annotate?key=%s"
    HEADERS = {"Content-Type": "application/json"}

    def __init__(self, api_key):
        self.api_url = self.API_URL_PATTERN % api_key

    def make_request(self, image, *features):
        """
        Makes single image request
        :param image: One of file object, path, or URL
        :param features: Recognition features
        :return:
        """
        return {
            "image": {
                "content": self.image_to_base64(image)
            },
            "features": [{
                             "type": feature.type_,
                             "maxResults": feature.max_results
                         } for feature in features]
        }

    def image_to_base64(self, image):
        """
        :param image: One of file object, path, or URL
        :return: Base64 of image
        """
        if isinstance(image, file):
            return base64.b64encode(image.read())
        elif isinstance(image, str):
            if image.startswith("http"):
                # it's URL
                return base64.b64encode(requests.get(image).content)
            # it's path
            with open(image) as f:
                return base64.b64encode(f.read())

        raise ValueError("Unrecognizable image param: it must one of"
                         " file object, path or URL, not %s" % type(image))

    def make_body(self, image, *features):
        if isinstance(image, (list, tuple)) and len(image) > 1:
            requests_ = []
            for item in image:
                image_, features_ = item[0], item[1:]
                requests_.append(self.make_request(image_, *features_))
        else:
            requests_ = [self.make_request(image, *features)]
        return {'requests': requests_}

    def annotate(self, image, *features):
        """
        :param image: One of file object, path, or URL
        :param features: list of Vision Features
        :return: GoogleCloudVisionResponse
        """
        body = self.make_body(image, *features)
        try:
            response = requests.post(self.api_url, json.dumps(body), headers=self.HEADERS)
        except requests.RequestException as exc:
            raise GoogleCloudVisionException(exc)
        else:
            return GoogleCloudVisionResponse(response.content)
