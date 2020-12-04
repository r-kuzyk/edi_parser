

class Body:
    body_segments = []

    def add_segment(self, segment):
        self.body_segments.append(segment)

    def to_dict(self):
        segments_to_dict = {}
        for segment in self.body_segments:
            segments_to_dict.update(segment.to_dict())
        return segments_to_dict
