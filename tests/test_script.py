import json
import os
import unittest
from edi_parser import Parser
from pathlib import Path


class TestParser(unittest.TestCase):

    base_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    file_input = base_dir / 'edi_test.txt'
    file_output = base_dir / 'data.json'
    parser = Parser()

    def test_convert_edi_format_to_dict(self):
        document = self.parser.parse_document(self.file_input)
        edi_to_dict = document.to_dict()
        self.assertTrue(type(edi_to_dict) is dict)

    def test_save_document_in_json_format_with_name(self):
        self.parser.parse_document(self.file_input)
        self.parser.save_to_json(self.file_output)
        self.assertTrue(Path(self.file_output).exists())

    def test_save_document_in_json_format_with_default_name(self):
        self.parser.parse_document(self.file_input)
        file_name = self.parser.save_to_json()
        self.assertTrue(Path(file_name).exists())

