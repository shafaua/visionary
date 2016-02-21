import os
import unittest
from visionary import GoogleCloudVision, LabelDetection, LogoDetection
from visionary.compat import bytes, str
from visionary.response import GoogleCloudVisionResponse, Response, BaseLogoAnnotation, \
    LabelAnnotation

API_KEY = '<dummy>'
IMAGE_URL = 'https://upload.wikimedia.org/wikipedia/commons/c/ce/Transparent.gif'
IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', '1px.gif'))

TEST_JSON_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'data.json'))
ONE_PIXEL_BASE64 = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"


class GcvTestCase(unittest.TestCase):
    def setUp(self):
        self.client = GoogleCloudVision(API_KEY)

    def test_one_image_from_file(self):
        with open(IMAGE_PATH) as f:
            req = self.client.make_body(f)

            expected = {
                'requests': [{'features': [], 'image': {'content': ONE_PIXEL_BASE64}}]}
            self.assertEqual(req, expected)

    def test_one_image_from_url(self):
        req = self.client.make_body(IMAGE_URL)
        expected = {
            'requests': [{'features': [], 'image': {'content': ONE_PIXEL_BASE64}}]}
        self.assertEqual(req, expected)

    def test_one_image_path(self):
        req = self.client.make_body(IMAGE_PATH)
        expected = {
            'requests': [{'features': [], 'image': {'content': ONE_PIXEL_BASE64}}]}
        self.assertEqual(req, expected)

    def test_multiple_images(self):
        with open(IMAGE_PATH) as f:
            req = self.client.make_body([
                (IMAGE_PATH, LogoDetection(), LabelDetection()),
                (IMAGE_URL, LogoDetection(), LabelDetection()),
                (f, LogoDetection(), LabelDetection()),
            ])

            expected = {'requests': [{'image': {'content': ONE_PIXEL_BASE64},
                                      'features': [{'type': 'LOGO_DETECTION', 'maxResults': 10},
                                                   {'type': 'LABEL_DETECTION', 'maxResults': 10}]}, {'image': {
                'content': ONE_PIXEL_BASE64}, 'features': [
                {'type': 'LOGO_DETECTION', 'maxResults': 10}, {'type': 'LABEL_DETECTION', 'maxResults': 10}]},
                                     {'image': {'content': ONE_PIXEL_BASE64},
                                      'features': [{'type': 'LOGO_DETECTION', 'maxResults': 10},
                                                   {'type': 'LABEL_DETECTION', 'maxResults': 10}]}]}
            self.assertEqual(req, expected)

    def test_logo_annotation(self):
        with open(TEST_JSON_FILE) as f:
            content = f.read()
            response = GoogleCloudVisionResponse(content)

            self.assertTrue(response.ok)
            self.assertEqual(len(response.responses), 1)
            resp = response.responses[0]
            self.assertIsInstance(resp, Response)
            self.assertEqual(len(resp.logo_annotations), 2)

            ann = resp.logo_annotations[0]
            self.assertIsInstance(ann, BaseLogoAnnotation)
            self.assertEqual(ann.description, "Visa")
            self.assertIsInstance(ann.boundingPoly, dict)

    def test_label_annotation(self):
        with open(TEST_JSON_FILE) as f:
            content = f.read()
            response = GoogleCloudVisionResponse(content)
            resp = response.responses[0]
            self.assertEqual(len(resp.label_annotations), 3)
            ann = resp.label_annotations.pop()
            self.assertIsInstance(ann, LabelAnnotation)


unittest.main()
