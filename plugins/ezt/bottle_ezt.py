'''
### docco

'''

__author__ = 'Greg Stein'
__version__ = '0.1'
__license__ = 'MIT'

### CUT HERE (see setup.py)

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

import ezt
import bottle


class EZTPlugin(bottle.BaseTemplatePlugin):
    ''' ### docco '''

    name = 'ezt'

    def __init__(self, lookup=['.'], options={}, default_vars={},
                 compress_whitespace=True, base_format=ezt.FORMAT_HTML):
        bottle.BaseTemplatePlugin.__init__(self, lookup, options, default_vars)
        self.compress_whitespace = compress_whitespace
        self.base_format = base_format

    def prepare(self, source=None, filepath=None,
                compress_whitespace=None, base_format=None, **options):
        if compress_whitespace is None:
            compress_whitespace = self.compress_whitespace
        if base_format is None:
            base_format = self.base_format
        template = ezt.Template(compress_whitespace=compress_whitespace)
        if source:
            template.parse(source, base_format)
        else:
            template.parse_file(filepath, base_format)
        return template

    def render(self, template, data):
        buffer = StringIO.StringIO()
        template.generate(buffer, data)
        return buffer.getvalue()


Plugin = EZTPlugin
