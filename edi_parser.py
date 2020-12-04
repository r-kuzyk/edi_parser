from data_elements.segment import Segment
from edi_document import EdiDocument, DocumentStructure
from pathlib import Path


class Parser:
    """Create a new Parser"""

    def __init__(self):
        self.edi_document = EdiDocument()

    def parse_document(self, document):
        document_text = self._validate_document(document)
        self.parse_data(document_text)
        return self.edi_document

    def parse_data(self, data):
        for row in data:
            segment = Segment(content=row)
            segment.parse_segment()
            headers_and_trailers = {**self.edi_document.headers, **self.edi_document.trailers}
            envelop_segment = headers_and_trailers.get(segment.id_element.content, None)
            if envelop_segment is not None:
                envelop_segment['segment'] = segment
            else:
                self.edi_document.body.add_segment(segment)
        return self.edi_document

    def _validate_document(self, document):
        is_file = Path(document).is_file()

        if is_file:
            with open(document, "r") as f:
                document = f.readlines()
        else:
            raise FileNotFoundError
        return document