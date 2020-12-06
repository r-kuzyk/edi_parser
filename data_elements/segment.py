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

    def to_dict(self):
        return {'segment': self.id.content,
                'description': self.description,
                'data_elements': [element.content for element in self.data_elements]}
