# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_moves_get(self):
        """Test case for moves_get

        Gets information about one or more Pokemon attack moves!
        """
        query_string = [('name', 'name_example'),
                        ('power', 56),
                        ('accuracy', 56)]
        response = self.client.open(
            '/moves',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pokemon_all_get(self):
        """Test case for pokemon_all_get

        Gets information about all Pokemon.
        """
        response = self.client.open(
            '/pokemon/all',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pokemon_get(self):
        """Test case for pokemon_get

        Gets information about one or more Pokemon.
        """
        query_string = [('name', 'name_example'),
                        ('exact', true),
                        ('type', 'type_example')]
        response = self.client.open(
            '/pokemon',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
