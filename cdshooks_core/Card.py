# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"

def card(summary, indicator, source):
    return {
        'summary': summary, 'detail': '', 'indicator': indicator,
        'source': source, 'links': []
    }
