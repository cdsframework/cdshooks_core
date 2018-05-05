# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"


class Link:
    def __init__(self, label, url, link_type, app_context=None):
        # TODO: add check that parameters are the proper class type
        self.label = label
        self.url = url
        self.link_type = link_type
        self.app_context = app_context

    def get_link(self):
        output = dict(
            label=self.label,
            url=self.url,
            type=self.link_type
        )
        if self.app_context:
            output['appContext'] = self.app_context
        return output
