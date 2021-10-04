Data Encoding Standards
=======================

The datasets exchanged by geospatial software products have to be structured in a way that products by other vendors can read the data and interpret the information it contains. Without a well defined structure it would be almost impossible to enable an application to read and interpret data without losing or missing information. The need to define the structure and organisation of data formats and messaging protocols applies equally to binary formats such as GeoTIFF as it does to human-readable formats such as XML.

To support the ability of applications to exchange messaging and data that contains geospatial information, the OGC has developed a series of data model and encoding standards. These standards provide the rules for structuring and organising geospatial data for use in a given context. In some cases the standards present conceptual models, however in other cases the standards describe logical models that are intended to be implemented using one or more encoding formats. Many of the standards also provide rules on how to encode information according the logical models and in a particular format.

Let's take, for example, the Geography Markup Language (GML) standard. This standard describes a structure and rules for encoding geographic information in XML. The standard describes how instances of concepts such as features, geometry, coordinate reference systems, points, linestrings, polygons and several others should be written in XML. The rules are supported by an XML Schema Definition (XSD) file to allow validation of datasets.

In storage systems with limited capacity and networks with limited bandwidth, an alternative encoding standard such as OGC GeoPackage tends to be preferred. The GeoPackage standard describes how to structure and organise of geospatial data when storing it in an SQLite database. SQLite is a popular embedded database that is often found on devices with Size, Weight and Power (SWaP) constraints, such as tablets, smartphones and Internet-Of-Things (IoT) microcomputers.

By clearly and formally specifying encoding rules, the GML, GeoPackage and other OGC encoding standards make it possible to establish tests for validating whether a dataset complies to the requirements stated in the standards.

Contents:

.. toctree::
   :maxdepth: 1

   ../geopackage/text/basic-index.rst
   ../gml/text/index.rst
