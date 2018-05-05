# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"


class Source:
    def __init__(self, label, url=None, icon=None):
        # TODO: add check that parameters are the proper class type
        self.label = label
        self.url = url
        self.icon = icon

    def get_source(self):
        output = dict(
            label=self.label
        )
        if self.url:
            output['url'] = self.url
        if self.icon:
            output['icon'] = self.icon
        return output
