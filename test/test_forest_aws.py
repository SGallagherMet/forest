"""Amazon web services infrastructure"""
import unittest
import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(script_dir, "../bokeh_apps",
                                "plot_sea_two_model_comparison"))
import main


class TestS3Bucket(unittest.TestCase):
    def setUp(self):
        self.server_address = "https://s3.eu-west-2.amazonaws.com"
        self.bucket = main.S3Bucket()

    def test_server_address(self):
        self.assertEqual(self.bucket.server_address, self.server_address)
