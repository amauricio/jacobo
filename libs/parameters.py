from optparse import OptionParser


class MyParser(OptionParser):
    def format_epilog(self, formatter):
        return formatter.format_epilog(self.epilog)
    def format_help(self, formatter=None):
        if formatter is None:
            formatter = self.formatter
        result = []
        if self.usage:
            result.append(self.get_usage())
        if self.description:
            result.append(self.format_description(formatter))
            
        result.append(self.format_option_help(formatter))
        result.append("\n")
        result.append(self.format_epilog(formatter))
        result.append("\n")
        return "".join(result)

class Parameters():
    
    help_text = """
    Jacobo is a tiny webcrawler, easy to use.

    (e.g) python jacobo.py -u http://mysite.com -d 2 --random-agent -v 3

    """
    parser = MyParser(usage=help_text)
    options = None
    args = None

    def __init__(self):
         #define attributes for app

        self.set_options()

    
    def set_options(self):
        # -- Options --##

        
        self.parser.add_option("-u","--url", dest="url",
                        help='Target URL (e.g. "http://www.site.com/)')
        self.parser.add_option("-o", dest="out",  help=("Define out file"), metavar="OUT")

        self.parser.add_option("-d", dest="depth",
                        help="Define depth level [1,2,3]", metavar="DEPTH")

        self.parser.add_option("--user-agent", dest="agent",
                            help="User-Agent", metavar="AGENT")

        self.parser.add_option("--random-agent", action='store_true', default=False, help="Set a random User-Agent" )

        self.parser.add_option("-v", dest="verbose",  help=("Define verbose level"), metavar="VERBOSE")
        

        (self.options, self.args) = self.parser.parse_args()
                    
    