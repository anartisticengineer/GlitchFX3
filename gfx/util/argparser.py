class ArgParser:
    _ARGS = {}

    @property
    def args(self):
        return self._ARGS

    def __init__(self):
        pass

    def parse(self, *params):
        self._ARGS.clear()
        for param in params:
            try:
                (p_key, p_val) = param.split(' ')
            except (AttributeError, UnboundLocalError, ValueError):
                print('An error occurred with the parameter')
            p_val = p_val if p_val.isalpha() else float(p_val)
            self._ARGS[p_key] = p_val

