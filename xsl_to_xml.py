import os

# # Getting the current work directory (cwd) :)
this_dir = os.getcwd()
# # Add the folder you want to run through
SUB_DIRECTORY_TO_CHECK = ""
OPENING_TAG = '<fo:block>'
CLOSING_TAG = "</fo:block>"
LANGUAGE = "_lang"


class XslToXml:
    def get_list_of_directories(self):
        LIST_OF_DIRS = []

        for root, directories, files in os.walk(this_dir + SUB_DIRECTORY_TO_CHECK):
            for file in files:
                if file.endswith(".xsl"):
                    LIST_OF_DIRS.append(os.path.join(root, file))

        return LIST_OF_DIRS

    def get_file_name(self, file_path: str):
        return file_path.split("/")[-1].replace(".xsl", LANGUAGE)

    def get_file_lines(self, file_path: str):
        file = open(file_path)
        # store all the lines in the file as a list
        lines = file.readlines()
        file.close()
        return lines

    def write_tags(self, lines, xml_file):
        xml_file.write(lines)

    def create_file(self, file_path: str):
        file_name = self.get_file_name(file_path)
        lines = self.get_file_lines(file_path)
        with open(f"{file_name}.xml", "w") as xml_file:
            self.write_tags(lines, xml_file)

    def generate_xml_files(self):
        for directory in self.get_list_of_directories():
            self.create_file(directory)
