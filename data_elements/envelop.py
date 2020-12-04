
class Envelope:
    def __init__(self, header, trailer):
        self.header = header
        self.trailer = trailer


class Interchange(Envelope):
    def __init__(self, header=None, trailer=None):
        Envelope.__init__(self, header, trailer)


class FunctionalGroup(Envelope):
    def __init__(self, header=None, trailer=None):
        Envelope.__init__(self, header, trailer)


class TransactionSet(Envelope):
    def __init__(self, header=None, trailer=None):
        Envelope.__init__(self, header, trailer)