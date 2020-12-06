
class DocumentSettings:
    """Current Settings"""

    element_delimiter = "*"
    segment_delimiter = "~"
    sub_element_delimiter = ":"

    segment_description = {'ISA': 'Interchange Control Header',
                           'GS': 'Functional Group Header',
                           'ST': 'Transaction Set Header',
                           'SE': 'Transaction Set Trailer',
                           'GE': 'Functional Group Trailer',
                           'IEA': 'Interchange Control Trailer '}
