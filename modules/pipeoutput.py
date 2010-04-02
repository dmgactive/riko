# pipeoutput.py
#

def pipe_output(_INPUT, conf=None, verbose=False, **kwargs):
    """This operator outputs the input source, i.e. does nothing.

    Keyword arguments:
    _INPUT -- source generator
    
    Yields (_OUTPUT):
    source items
    """   
    for item in _INPUT:
        #todo convert back to XML or JSON
        yield item

# Example use
if __name__ == '__main__':
    items = pipe_output([{"title":"one"}, {"title":"two"}, {"title":"three"}])
    for item in items:
        print item
