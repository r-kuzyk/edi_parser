from data_elements.element import Element, SegmentIdElement
from edi_document import DocumentStructure
from utils.config import *


class Segment:

    def __init__(self, content):
        self.id_element = None
        self.data_elements = []
        self.content = content
        self.element_separator = DELIMITERS['element separator']
        self.segment_terminator = DELIMITERS['segment terminator']

    def parse_segment(self):
        content_as_list = self.content.strip().strip(self.segment_terminator).split(self.element_separator)
        segment_id = content_as_list[0]
        headers_and_trailers = {**DocumentStructure.headers, **DocumentStructure.trailers}
        segment = headers_and_trailers.get(segment_id, None)
        description = segment.get('description') if segment else None
        self.id_element = SegmentIdElement(segment_id, description=description)

        for element in content_as_list[1:]:
            data_element = Element(element)
            self.data_elements.append(data_element.content)

    def to_dict(self):
        return {'segment': self.id_element.content,
                'description': self.id_element.description,
                'data_elements': self.data_elements}
