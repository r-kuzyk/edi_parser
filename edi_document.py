from data_elements.envelop import Interchange, FunctionalGroup, TransactionSet

class Body:

    def __init__(self):
        self.body_segments = []

    def add_segment(self, segment):
        self.body_segments.append(segment)

    def to_dict(self):
        segments_to_dict = []
        for segment in self.body_segments:
            segments_to_dict.append(segment.to_dict())
        return {'Body segments': segments_to_dict}

    def segments(self):
        return self.body_segments


class EdiDocument:
    def __init__(self):
        self.interchange = Interchange()
        self.functional_group = FunctionalGroup()
        self.transaction_set = TransactionSet()

        self.body = Body()

    def to_dict(self):
        return {'Parsed data': [self.interchange.header.to_dict(),
                                self.functional_group.header.to_dict(),
                                self.transaction_set.header.to_dict(),
                                self.body.to_dict(),
                                self.transaction_set.trailer.to_dict(),
                                self.functional_group.trailer.to_dict(),
                                self.interchange.trailer.to_dict()]}

