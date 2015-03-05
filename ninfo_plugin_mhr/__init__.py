from ninfo import PluginBase
import socket

ROOT = ".malware.hash.cymru.com"

class mhr_plug(PluginBase):
    """"""
    name          = 'mhr'
    title         = 'MHR'
    description   = 'CYMRU Malware Hash Registry'
    cache_timeout = 60*60
    types         = ['hash']

    def setup(self):
        pass

    def get_info(self, arg):
        host = arg + ROOT
        try:
            #The docs say it will only ever return 127.0.0.2, but it doesn't hurt to be explicit
            return socket.gethostbyname(host)=='127.0.0.2'
        except socket.gaierror:
            return False

    def render_template(self, output_type, arg, result):
        if not result:
            return ''
        return "Present"

plugin_class = mhr_plug
