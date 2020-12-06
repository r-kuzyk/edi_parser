from data_elements.body import Body
from data_elements.envelop import Interchange, FunctionalGroup, TransactionSet


class EdiDocument:
    """
    An EDI X12 Document
    """
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

