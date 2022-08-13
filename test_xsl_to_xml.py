from xsl_to_xml import XslToXml


class TestXslToXml:
    def setup_method(self):
        self.xsl_to_xml_instance = XslToXml()
        print("Test Start")

    def teardown_method(self):
        print("Test End")

    def test_get_file_name_returns_only_the_name_of_the_file_when_path_is_provided(self):
        expected_response = "SampleXsl"
        actual_response = self.xsl_to_xml_instance.get_file_name("/Users/fictional-sniffle/SampleXsl.xsl")
        assert actual_response == expected_response

