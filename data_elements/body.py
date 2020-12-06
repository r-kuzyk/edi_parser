class Body:

    def __init__(self):
        self.body_segments = []

    def add_segment(self, segment):
        self.body_segments.append(segment)

    def to_dict(self):
        segments_to_dict = []
        for segment in self.body_segments:
            segments_to_dict.append(segment.to_dict())
        return {'Body segments': segments_to_dict}

    def segments(self):
        return self.body_segments
