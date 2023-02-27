<?xml version="1.0" encoding="UTF-8"?>



<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">



    <xsl:output method="xml" />

    <xsl:strip-space elements="*" />



    <xsl:template match="/document">

    <dokument>

        <filename><xsl:value-of select="filename" /></filename>

        <basic_info>

            <invoice_number><xsl:value-of select="fields_compact/invoice_id" /></invoice_number>

            <date><xsl:value-of select="fields_compact/invoice_date" /></date>

        </basic_info>

        <amounts>

            <net_amount><xsl:value-of select="fields_compact/net_amount" /></net_amount>

            <total_amount><xsl:value-of select="fields_compact/total_amount" /></total_amount>

        </amounts>

    </dokument>




    </xsl:template>



</xsl:stylesheet>