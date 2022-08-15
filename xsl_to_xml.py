import os
import re

# # Getting the current work directory (cwd) :)
this_dir = os.getcwd()
# # Add the folder you want to run through
SUB_DIRECTORY_TO_CHECK = ''
OPENING_TAG = '<test:tag'
CLOSING_TAG = '</test:tag>'
XML_NAME_SUFFIX = 'lang'
XML_ENCODING = '<?xml version="1.0" encoding="UTF-8"?>\n'
TARGET = 'standard'
XML_OPENING_NODE = f'<test:module xmlns:test="http://www.test-page.com/tags" target="{TARGET}" suffix="{XML_NAME_SUFFIX}">\n'
XML_CLOSING_NODE = '</test:module>'
XML_ENCODING_REGEX = '<?xml version="1.0" encoding="(.+?)"?>'
XML_OP_NODE_REGEX = '<test:module target="(.+?)"/>'


class XslToXml:
    def get_list_of_directories(self):
        LIST_OF_DIRS = []

        for root, directories, files in os.walk(this_dir + SUB_DIRECTORY_TO_CHECK):
            for file in files:
                if file.endswith(".xsl"):
                    LIST_OF_DIRS.append(os.path.join(root, file))

        return LIST_OF_DIRS

    def get_file_name(self, file_path: str):
        return file_path.split("/")[-1].replace(".xsl", f'_{XML_NAME_SUFFIX}')

    def get_file_string(self, file_path: str):
        file = open(file_path)
        # store file as a string
        string = file.read()
        file.close()
        # remove comments from file
        clean_string = ''
        for item in string.split('<!--'):
            if '-->' in item:
                clean_string = clean_string + item [ item.find('-->')+len('-->') : ]
            else:
                clean_string = clean_string + item
        return clean_string

    def write_first_2_lines(self, string, xml_file):
        first_line = XML_ENCODING
        second_line = XML_OPENING_NODE
        if re.search(XML_ENCODING_REGEX, string) != None:
            first_line = '<?'+re.search(XML_ENCODING_REGEX, string).group()+'\n'
        if re.search(XML_OP_NODE_REGEX, string) != None:
            global TARGET
            TARGET = re.search(XML_OP_NODE_REGEX, string).group(1)
            second_line = XML_OPENING_NODE
        # take the encoding from the xsl
        xml_file.write(first_line)
        xml_file.write(second_line)

    def write_tags(self, string, xml_file):
        print(string)
        for item in string.split(CLOSING_TAG):
            if OPENING_TAG in item:
                print('\t'+item [ item.find(OPENING_TAG) : ]+CLOSING_TAG+'\n')
                xml_file.write('\t'+item [ item.find(OPENING_TAG) : ]+CLOSING_TAG+'\n')

    def write_last_line(self, xml_file):
        xml_file.write(XML_CLOSING_NODE)

    def create_file(self, file_path: str):
        file_name = self.get_file_name(file_path)
        string = self.get_file_string(file_path)

        with open(f"{file_name}.xml", "w") as xml_file:
            self.write_first_2_lines(string, xml_file)
            self.write_tags(string, xml_file)
            self.write_last_line(xml_file)

    def generate_xml_files(self):
        for directory in self.get_list_of_directories():
            self.create_file(directory)

instance = XslToXml()
instance.generate_xml_files()