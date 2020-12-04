class Element:
    """Base element"""

    def __init__(self, content):
        self.content = content

    @property
    def to_dict(self):
        return {'element': self.content}


class SegmentIdElement(Element):

    def __init__(self, content, **kwargs):
        super().__init__(content)
        self.description = kwargs.get('description', None)

    @property
    def to_dict(self):
        if self.description is not None:
            # TODO check it
            return super().to_dict
        else:
            return {
                'segment_id': self.content,
                'description': self.description
            }
