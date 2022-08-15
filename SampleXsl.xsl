<?xml version="1.0" encoding="ISO-8859-1"?>
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
		<!-- <fo:block><test:tag id="20">repeated ID 2</test:tag></fo:block> -->
	</xsl:template>
</xsl:stylesheet>