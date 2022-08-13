from unittest.mock import patch, call

from xsl_to_xml import XslToXml


class TestXslToXml:
    def setup_method(self):
        self.xsl_to_xml_instance = XslToXml()
        print("Test Start")

    def teardown_method(self):
        print("Test End")

    def test_get_file_name_returns_only_the_name_of_the_file_when_path_is_provided(self):
        expected_response = "SampleXsl_lang"
        actual_response = self.xsl_to_xml_instance.get_file_name("/Users/zfictional-sniffle/SampleXsl.xsl")
        assert actual_response == expected_response

    # Investigate mocks/spies/stubs

    @patch('os.walk')
    @patch('builtins.open')
    def test_generate_xml_files(self, mock_open, mock_walk):
        mock_walk.return_value = [("/Users/fictional-sniffle/", ["dir"], ["SampleXsl.xsl"])]

        self.xsl_to_xml_instance.generate_xml_files()

        mock_open.called_with("/Users/fictional-sniffle/SampleXsl.xsl")
        mock_open.called_with("SampleXsl_lang.xml", "w")
