def link(label, url=None):
    result = {'label': label}
    if url:
        result['url'] = url

    return result
