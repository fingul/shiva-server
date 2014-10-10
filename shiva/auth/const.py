# -*- coding: utf-8 -*-


class Roles:
    USER = '1'
    ADMIN = '2'
    SHIVA = '3'

    @classmethod
    def _as_tuple(cls):
        return (cls.USER, cls.ADMIN, cls.SHIVA)

    @classmethod
    def _as_dict(cls):
        return {
            'USER': cls.USER,
            'ADMIN': cls.ADMIN,
            'SHIVA': cls.SHIVA,
        }
