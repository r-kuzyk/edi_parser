from data_elements.segment import Segment


class Envelope:
    def __init__(self):
        self.header = Segment(None)
        self.trailer = Segment(None)


class Interchange(Envelope):
    def __init__(self):
        Envelope.__init__(self)


class FunctionalGroup(Envelope):
    def __init__(self):
        Envelope.__init__(self)


class TransactionSet(Envelope):
    def __init__(self):
        Envelope.__init__(self)