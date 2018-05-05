# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"


class Card:
    def __init__(self, summary, indicator, source, detail=None):
        # TODO: add check that parameters are the proper class type
        self.summary = summary
        self.indicator = indicator
        self.source = source
        self.detail = detail
        self.links = []
        self.suggestions = []

    def get_card(self):
        output = dict(
            summary=self.summary,
            indicator=self.indicator,
            source=self.source.get_source()
        )
        if self.detail:
            output['detail'] = self.detail
        if len(self.links) > 0:
            output['links'] = list()
            for link in self.links:
                output['links'].append(link.get_link())
        if len(self.suggestions) > 0:
            output['suggestions'] = list()
            for suggestion in self.suggestions:
                output['suggestions'].append(suggestion.get_suggestion())
        return output

    def add_suggestion(self, suggestion):
        # TODO: add check that suggestion is the proper class type
        self.suggestions.append(suggestion)

    def add_link(self, link):
        # TODO: add check that link is the proper class type
        print(self.links)
        self.links.append(link)
