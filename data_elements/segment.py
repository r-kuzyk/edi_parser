from data_elements.element import Element
from utils.config import *


class Segment:

    def __init__(self, content):
        self.id = None
        self.data_elements = []
        self.content = content
        self.description = ''
        self.element_delimiter = DocumentSettings.element_delimiter
        self.segment_delimiter = DocumentSettings.segment_delimiter

    def parse_segment(self):
        content_as_list = self.content.strip().strip(self.segment_delimiter).split(self.element_delimiter)
        self.id = Element(content_as_list[0])
        self.description = DocumentSettings.segment_description.get(self.id.content, 'No decription')

        for element in content_as_list[1:]:
            data_element = Element(element)
            self.data_elements.append(data_element)

    def to_dict(self):
        return {'segment': self.id.content,
                'description': self.description,
                'data_elements': [element.content for element in self.data_elements]}
