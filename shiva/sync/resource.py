# -*- coding: utf-8 -*-
from flask.ext.restful import Resource, Response

from shiva.auth import Roles, ACLMixin


class BinaryResponse(Response):

    def __init__(self, *args, **kwargs):
        params = {
            'mimetype': 'application/octet-stream',
        }

        return super(BinaryResponse, self).__init__(**params)


class SyncResource(Resource, ACLMixin):
    """
    Endpoint responsible for all the shiva2shiva communication.
    """
    allow = [Roles.SHIVA]

    def get(self):
        return {}
