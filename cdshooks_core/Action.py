# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"


class Action:
    def __init__(self, action_type, description, resource=None):
        # TODO: add check that parameters are the proper class type
        self.action_type = action_type
        self.description = description
        self.resource = resource

    def get_action(self):
        output = dict(
            type=self.action_type,
            description=self.description
        )
        if self.resource:
            output['resource'] = self.resource
        return output
