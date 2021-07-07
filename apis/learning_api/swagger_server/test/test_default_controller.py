# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_random_get(self):
        """Test case for random_get

        Get information about a random user.
        """
        response = self.client.open(
            '/random',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_get(self):
        """Test case for user_get

        Get information about specific users.
        """
        query_string = [('firstname', 'firstname_example'),
                        ('lastname', 'lastname_example'),
                        ('gender', 'gender_example'),
                        ('page', 1)]
        response = self.client.open(
            '/user',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
