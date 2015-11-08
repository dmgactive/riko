# Pipe pipe_06c4c44316efb0f5f16e4e7fa4589ba2 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipesort import pipe_sort
from pipe2py.modules.pipenumberinput import pipe_numberinput
from pipe2py.modules.pipetail import pipe_tail
from pipe2py.modules.pipeoutput import pipe_output


def pipe_06c4c44316efb0f5f16e4e7fa4589ba2(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return [(u'', u'numberinput1', u'How many items do you want in the feed?', u'number', u'5')]

    if context and context.describe_dependencies:
        return [u'pipefetch', u'pipenumberinput', u'pipeoutput', u'pipesort', u'pipetail']

    forever = pipe_forever()

    sw_123 = pipe_fetch(
        context, forever, conf={'URL': {'type': 'url', 'value': 'file://data/news.yahoo.com_rss_topstories.xml'}})

    sw_135 = pipe_sort(
        context, sw_123, conf={'KEY': [{'field': {'type': 'text', 'value': 'title'}, 'dir': {'type': 'text', 'value': 'DESC'}}]})

    sw_131 = pipe_numberinput(
        context, forever, conf={'debug': {'type': 'number', 'value': ''}, 'default': {'type': 'number', 'value': '5'}, 'prompt': {'type': 'text', 'value': 'How many items do you want in the feed?'}, 'name': {'type': 'text', 'value': 'numberinput1'}, 'position': {'type': 'number', 'value': ''}})

    sw_106 = pipe_tail(
        context, sw_135, count=sw_131, conf={'count': {'terminal': 'count', 'type': 'number'}})

    _OUTPUT = pipe_output(
        context, sw_106, conf={})

    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_06c4c44316efb0f5f16e4e7fa4589ba2(Context())

    for i in pipeline:
        print i
