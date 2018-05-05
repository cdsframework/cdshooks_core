# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"


class Suggestion:
    def __init__(self, label, uuid=None):
        # TODO: add check that parameters are the proper class type
        self.label = label
        self.uuid = uuid
        self.actions = []

    def get_suggestion(self):
        output = dict(
            label=self.label
        )
        if self.uuid:
            output['uuid'] = self.uuid
        if len(self.actions) > 0:
            output['actions'] = list()
            for action in self.actions:
                output['actions'].append(action.get_action())
        return output

    def add_action(self, action):
        # TODO: add check that action is the proper class type
        self.actions.append(action)
