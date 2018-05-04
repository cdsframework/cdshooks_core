# -*- coding: utf-8 -*-

__author__ = "HLN Consulting, LLC"
__copyright__ = "Copyright 2018, HLN Consulting, LLC"

def link(label, url=None):
    result = {'label': label}
    if url:
        result['url'] = url

    return result
