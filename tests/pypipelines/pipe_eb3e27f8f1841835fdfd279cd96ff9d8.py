# Pipe pipe_eb3e27f8f1841835fdfd279cd96ff9d8 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipeurlinput import pipe_urlinput
from pipe2py.modules.pipefetchdata import pipe_fetchdata
from pipe2py.modules.pipetextinput import pipe_textinput
from pipe2py.modules.pipefilter import pipe_filter
from pipe2py.modules.piperename import pipe_rename
from pipe2py.modules.piperegex import pipe_regex
from pipe2py.modules.pipeoutput import pipe_output


def pipe_eb3e27f8f1841835fdfd279cd96ff9d8(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return [(u'', u'q', u'Caption search term', u'text', u'maverick'), (u'', u'url', u'Caption URL', u'url', u'file://data/rsc-ne-scotland.org.uk_mashe_ititle_xml_jisc10bean.xml')]

    if context and context.describe_dependencies:
        return [u'pipefetchdata', u'pipefilter', u'pipeoutput', u'piperegex', u'piperename', u'pipetextinput', u'pipeurlinput']

    forever = pipe_forever()

    sw_521 = pipe_urlinput(
        context, forever, conf={'debug': {'type': 'url', 'value': ''}, 'default': {'type': 'url', 'value': 'file://data/rsc-ne-scotland.org.uk_mashe_ititle_xml_jisc10bean.xml'}, 'prompt': {'type': 'text', 'value': 'Caption URL'}, 'name': {'type': 'text', 'value': 'url'}, 'position': {'type': 'number', 'value': ''}})

    sw_572 = pipe_fetchdata(
        context, forever, URL=sw_521, conf={'URL': {'terminal': 'URL', 'type': 'url'}, 'path': {'type': 'text', 'value': 'body.div.p'}})

    sw_621 = pipe_textinput(
        context, forever, conf={'debug': {'type': 'text', 'value': ''}, 'default': {'type': 'text', 'value': 'maverick'}, 'prompt': {'type': 'text', 'value': 'Caption search term'}, 'name': {'type': 'text', 'value': 'q'}, 'position': {'type': 'number', 'value': ''}})

    sw_584 = pipe_filter(
        context, sw_572, RULE_1_value=sw_621, conf={'COMBINE': {'type': 'text', 'value': 'and'}, 'MODE': {'type': 'text', 'value': 'permit'}, 'RULE': [{'field': {'type': 'text', 'value': 'content'}, 'value': {'terminal': 'RULE_1_value', 'type': 'text'}, 'op': {'type': 'text', 'value': 'contains'}}]})

    sw_595 = pipe_rename(
        context, sw_584, conf={'RULE': [{'field': {'type': 'text', 'value': 'begin'}, 'op': {'type': 'text', 'value': 'copy'}, 'newval': {'type': 'text', 'value': 'ctime'}}, {'field': {'type': 'text', 'value': 'content'}, 'op': {'type': 'text', 'value': 'copy'}, 'newval': {'type': 'text', 'value': 'title'}}]})

    sw_606 = pipe_regex(
        context, sw_595, conf={'RULE': [{'field': {'type': 'text', 'value': 'ctime'}, 'match': {'type': 'text', 'value': '(.*)'}, 'replace': {'type': 'text', 'value': '&time=$1'}}]})

    _OUTPUT = pipe_output(
        context, sw_606, conf={})

    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_eb3e27f8f1841835fdfd279cd96ff9d8(Context())

    for i in pipeline:
        print i
