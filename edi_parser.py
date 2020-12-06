import json

from data_elements.segment import Segment
from edi_document import EdiDocument
from pathlib import Path
import time


class Parser:

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
            self._route_segment(segment)
        return self.edi_document

    def _route_segment(self, segment):
        """Determine what segment it is
        :param segment:
        """
        if segment.id.content == 'ISA':
            self.edi_document.interchange.header = segment
        elif segment.id.content == 'GS':
            self.edi_document.functional_group.header = segment
        elif segment.id.content == 'ST':
            self.edi_document.transaction_set.header = segment
        elif segment.id.content == 'SE':
            self.edi_document.transaction_set.trailer = segment
        elif segment.id.content == 'GE':
            self.edi_document.functional_group.trailer = segment
        elif segment.id.content == 'IEA':
            self.edi_document.interchange.trailer = segment
        else:
            self.edi_document.body.add_segment(segment)

    def _validate_document(self, document):
        is_file = Path(document).is_file()

        if is_file:
            with open(document, "r") as f:
                document = f.readlines()
        else:
            raise FileNotFoundError
        return document

    def save_to_json(self, file_name=None):
        if file_name is None:
            timestr = time.strftime("%Y%m%d-%H%M%S")
            file_name = f'parsed_{timestr}.json'

        with open(file_name, 'w') as outfile:
            json.dump(self.edi_document.to_dict(), outfile, indent=4)
        return file_name

