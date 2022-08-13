import os

# # Getting the current work directory (cwd)
this_dir = os.getcwd()
# # Add the folder you want to run through
SUB_DIRECTORY_TO_CHECK = ""
OPENING_TAG = '<fo:block>'
CLOSING_TAG = "</fo:block>"


class XslToXml:
    def get_list_of_directories(self):
        LIST_OF_DIRS = []

        for root, directories, files in os.walk(this_dir + SUB_DIRECTORY_TO_CHECK):
            for file in files:
                if file.endswith(".xsl"):
                    LIST_OF_DIRS.append(os.path.join(root, file))

        return LIST_OF_DIRS

    def get_file_name(self, file_path: str):
        return file_path.split("/")[-1].replace(".xsl", "")

    def get_file_lines(self, file_path: str):
        file = open(file_path)
        # store all the lines in the file as a list
        lines = file.readlines()
        file.close()
        return lines

    def copy_last_line(self, lines, xml_file):
        xml_file.write(lines[-1])

    def copy_first_2_lines(self, lines, xml_file):
        xml_file.write(lines[0])
        xml_file.write(lines[1])

    def get_indexes(self, lines):
        start_index = 0
        end_index = 0
        for line in lines:
            if OPENING_TAG in line:
                start_index = lines.index(line) + 1
            if CLOSING_TAG in line:
                end_index = lines.index(line)
        return start_index, end_index

    def write_tags(self,end_index, lines, xml_file, star_index):
        while star_index < end_index:
            xml_file.write(lines[star_index])
            star_index = star_index + 1

    def create_file(self, file_path: str):
        file_name = self.get_file_name(file_path)
        lines = self.get_file_lines(file_path)

        with open(f"{file_name}.xml", "w") as xml_file:
            self.copy_first_2_lines(lines, xml_file)
            star_index, end_index = self.get_indexes(lines)
            self.write_tags(end_index, lines, xml_file, star_index)
            self.copy_last_line(lines, xml_file)

    def generate_xml_files(self):
        for directory in self.get_list_of_directories():
            self.create_file(directory)
