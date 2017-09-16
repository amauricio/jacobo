class Headers():
    
    lst = {}
    
    def __init__(self):
        pass
    @staticmethod
    def push(key , value):
        if key not in Headers.lst:
            Headers.lst[key] = value
    
    @staticmethod
    def get(key):
        try:
            return Headers.lst[key]
        except IndexError:
            return None
    @staticmethod
    def set(key, new_value):
        if key in Headers.lst:
            Headers.lst[key] = new_value
        else:
            raise IndexError('Not found ' + key)
    
    @staticmethod
    def push_from_response(lines):
        ##separate by breaklines
        by_line = str(lines).split('\n')
        for line in by_line:
            ##separate by two points
            line = str.replace(line, '\n', '')
            line = str.replace(line, '\r', '')
            line = str.replace(line, '\t', '')
            tokenizr = line.split(':')
            if len(tokenizr) > 1:
                Headers.push( tokenizr[0].strip(), tokenizr[1].strip()  )