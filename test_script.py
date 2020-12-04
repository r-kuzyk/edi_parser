import json

from edi_parser import Parser

file_input = 'C:\edi_parser\\tests\edi_test.txt'
file_output = 'C:\edi_parser\\tests\data.json'
parser = Parser()


if __name__ == '__main__':

    document = parser.parse_document(file_input)
    edi_to_dict = document.to_dict()

    with open(file_output, 'w') as outfile:
        json.dump(edi_to_dict, outfile)
