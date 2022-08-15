from unittest.mock import patch, call

from xsl_to_xml import XslToXml


class TestXslToXml:
    CLEAN_STRING = """<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<test:module target="test"/>
	<xsl:template match="/">
	  <html>
	  <body>
		<h2>Dy CD Collection</h2>
		<table border="1">
		  <tr bgcolor="#9acd32">
			<th>Title</th>
			<th>Artist</th>
		  </tr>
		  <xsl:for-each select="catalog/cd">
		  <tr>
			<td><xsl:value-of select="title" /></td>
			<td><xsl:value-of select="artist" /></td>
		  </tr>
		  </xsl:for-each>
		</table>
	  </body>
	  </html>
	</xsl:template>
	<xsl:template name="sample_tdl1">
		<fo:block>
			TEXT1
			<test:tag id="10">TDL1</test:tag>
			<test:tag id="20">
				TDL2</test:tag>
			<test:tag id="30">
				TDL3
			</test:tag>
			TEXT2
			<test:tag id="40">TDL4
			</test:tag>
			<test:tag id="75"></test:tag>
			<test:tag id="50">
			
			TDL5
			
			</test:tag>
			<xsl:value-of select="concat('TEXT','3')"/>
			<test:tag id="60">T
			D
				L
				6</test:tag>
				T
				E
				X
				T
				4
			<test:tag id="70">
			T
			D
			L
			7
			</test:tag>
			<test:tag id="80">
			T
			D
			L
			8</test:tag>
			<test:tag id="90"><example_tag>T</example_tag>
			<xsl:value-of select="concat('D','L')"/>
			<example_tag>9</example_tag>
			</test:tag>
		</fo:block>
	</xsl:template>
	
	<xsl:template name="sample_tdl2">
		<fo:block><test:tag id="10">repeated ID</test:tag></fo:block>
		
	</xsl:template>
</xsl:stylesheet>"""

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

    @patch('xsl_to_xml.walk')
    @patch('builtins.open')
    def test_generate_xml_files(self, mock_open, mock_walk):
        mock_walk.return_value = [("/Users/fictional-sniffle/", ["dir"], ["SampleXsl.xsl"])]

        self.xsl_to_xml_instance.generate_xml_files()
        calls = [call("/Users/fictional-sniffle/SampleXsl.xsl"),
                 call("SampleXsl_lang.xml", "w")]

        mock_open.assert_has_calls(calls, any_order=True)

    @patch('xsl_to_xml.walk')
    def test_generates_list_of_directories_builds_path_from_tuple(self, mock_os):
        mock_os.return_value = [("/Users/ficional-sniffle/", ["dir"], ["SampleXsl.xsl"])]

        actual_response = self.xsl_to_xml_instance.get_list_of_directories()
        expected_response = ["/Users/fictional-sniffle/SampleXsl.xsl"]

        actual_response == expected_response

# Work in progress; gives a false positive
    @patch('os.write')
    def test_write_first_2_lines(self, mock_write):
        expected_output = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<test:module xmlns:test="http://www.test-page.com/tags" target="standard" suffix="lang">'''
        actual_output = self.xsl_to_xml_instance.write_first_2_lines(self.CLEAN_STRING, mock_write)

        actual_output == expected_output

    # def test_write_tags(self, mock):
    #     config_data = mock.mock_open(read_data='data')
    #     with mock.patch('xsl_to_xml.open', config_data) as mock_open:
    #         mock_open.write = mock()
    #         self.xsl_to_xml_instance.write_tags("lines", mock_open)

    #         mock_open.write.assert_called_with("lines")
