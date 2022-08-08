<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
	  <html>
	  <body>
		<h2>My CD Collection</h2>
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
	<xsl:template name="sample_kml1">
		<fo:block>
			TESTO1
			<multi:lingua id="10">KML1</multi:lingua>
			<multi:lingua id="20">
				KML2</multi:lingua>
			<multi:lingua id="30">
				KML3
			</multi:lingua>
			TESTO2
			<multi:lingua id="40">KML4
			</multi:lingua>
			<multi:lingua id="75"></multi:lingua>
			<multi:lingua id="50">
			
			KML5
			
			</multi:lingua>
			<xsl:value-of select="concat('TESTO','3')"/>
			<multi:lingua id="60">K
			M
				L
				6</multi:lingua>
				T
				E
				S
				T
				O
				4
			<multi:lingua id="70">
			K
			M
			L
			7
			</multi:lingua>
			<multi:lingua id="80">
			K
			M
			L
			8</multi:lingua>
			<multi:lingua id="90"><bold>K</bold>
			<xsl:value-of select="concat('M','L')"/>
			<italic>9</italic>
			</multi:lingua>
		</fo:block>
	</xsl:template>
</xsl:stylesheet>