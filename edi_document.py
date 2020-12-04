from data_elements.body import Body
from data_elements.envelop import Interchange, FunctionalGroup, TransactionSet


class DocumentStructure:

    headers = {'ISA': {'segment': None,
                       'description': 'Interchange Control Header'},
               'GS': {'segment': None,
                      'description': 'Functional Group Header'},
               'ST': {'segment': None,
                      'description': 'Transaction Set Header'}}

    data = {'BODY': {'segment': None,
                     'description': 'Body Content'}}

    trailers = {'SE': {'segment': None,
                       'description': 'Transaction Set Trailer'},
                'GE': {'segment': None,
                       'description': 'Functional Group Trailer'},
                'IEA': {'segment': None,
                        'description': ' Interchange Control Trailer '}}

# class DocumentHeaders:
#     def __init__(self):
#         self.interchange_header = Interchange().header
#         self.functional_group_header = FunctionalGroup().header
#         self.transaction_set_header = TransactionSet().header
#         self.headers_structure = DocumentStructure.headers
#
#     def build_headers(self):
#         self.headers_structure['ISA']['segment'] = self.interchange_header
#         self.headers_structure['GS']['segment'] = self.functional_group_header
#         self.headers_structure['ST']['segment'] = self.transaction_set_header
#
#     def to_dict(self):
#         return {self.interchange_header.to_dict}


class EdiDocument(DocumentStructure):
    """
    An EDI X12 Document
    """

    def __init__(self):
        self.interchange = Interchange()
        self.functional_group = FunctionalGroup()
        self.transaction_set = TransactionSet()
        self.body = Body()
        self._build_document_structure()

    def _build_document_structure(self):
        # TODO refactor it
        self.headers['ISA']['segment'] = self.interchange.header
        self.headers['GS']['segment'] = self.functional_group.header
        self.headers['ST']['segment'] = self.transaction_set.header
        self.data['BODY']['segment'] = self.body
        self.trailers['SE']['segment'] = self.transaction_set.trailer
        self.trailers['GE']['segment'] = self.functional_group.trailer
        self.trailers['IEA']['segment'] = self.interchange.trailer

    def to_dict(self):
        return {'Parsed':
                [self.headers['ISA']['segment'].to_dict(),
                self.headers['GS']['segment'].to_dict(),
                self.headers['ST']['segment'].to_dict(),
                self.data['BODY']['segment'].to_dict(),
                self.trailers['SE']['segment'].to_dict(),
                self.trailers['GE']['segment'].to_dict(),
                self.trailers['IEA']['segment'].to_dict()]}

