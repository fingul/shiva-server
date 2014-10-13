# -*- coding: utf-8 -*-
from flask.ext.restful import Resource, Response
import msgpack

from shiva.auth import Roles, ACLMixin
# from shiva.sync.decorators import binary


def binary(func):
    def wrapped(*args, **kwargs):
        response = func(*args, **kwargs)

        return BinaryResponse(response)

    return wrapped


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

    @binary
    def get(self):
        return {}
