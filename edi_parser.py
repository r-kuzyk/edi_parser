import json

from data_elements.element import Element
from data_elements.segment import Segment
from edi_document import EdiDocument
from pathlib import Path
import time

from utils.config import DocumentSettings


class Parser:

    def __init__(self):
        """Initialize EDI document structure"""
        self.edi_document = EdiDocument()
        self.document = None

    def parse_document(self, document: str) -> EdiDocument:
        """Parse the text document into an object
        :param document:  file to be parsed.
        """
        self.document = document
        document_text = self._validate_document()
        self.parse_data(document_text)
        return self.edi_document

    def parse_data(self, data):
        for row in data:
            segment = Segment(content=row)
            self.parse_segment(segment)
            self._route_segment(segment)
        return self.edi_document

    def parse_segment(self, segment):
        content_as_list = segment.content.strip().strip(segment.segment_delimiter).split(segment.element_delimiter)
        segment.id = Element(content_as_list[0])
        segment.description = DocumentSettings.segment_description.get(segment.id.content, 'No decription')

        for element in content_as_list[1:]:
            data_element = Element(element)
            segment.data_elements.append(data_element)
        return segment

    def _route_segment(self, segment: Segment):
        """Determine what segment it is
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

    def _validate_document(self):
        """Check if document exists"""
        is_file = Path(self.document).is_file()

        if is_file:
            with open(self.document, "r") as f:
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

