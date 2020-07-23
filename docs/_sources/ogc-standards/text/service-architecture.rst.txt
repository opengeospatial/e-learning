OGC Service Architecture
=============================

Overview
------------------------

The OGC Abstract Specification `Topic 12 - The OpenGIS Service Architecture <http://portal.opengeospatial.org/files/?artifact_id=1221>`_ provides a framework for developers to create software that enables users to access and process geospatial data from a variety of sources across generic computing interfaces within an open information technology environment.

* "a framework for developers" means that the OGC Standards are based on a comprehensive, common (i.e., formed by consensus for general use) plan for interoperable geoprocessing.
* "access and process" means that geodata users can query remote databases and control remote processing resources, for example in information systems using service oriented architecture.
* "from a variety of sources" means that users will have access to data acquired in a variety of ways and stored in a wide variety databases and knowledge bases.
* "across generic computing interfaces" means that OGC services enable reliable communication between otherwise disparate software resources that are equipped to use these interfaces.
* "within an open information technology environment" means that this OGC standard enables geoprocessing to take place outside of the closed environment of monolithic GIS, remote sensing, and automated systems that constrain access based on proprietary interfaces.


OWS Common
----------

The OGC Web Services Common `(OWS Common) <http://www.opengeospatial.org/standards/common>`_  provides guidance to OGC members who are developing OGC interface implementation standards. The purpose of OWS Common is to maintain consistency among OGC standards. OWS Common provides rules for specifying some of the parameters and data structures used in operation requests and responses. Each interface standard details additional aspects, including specifying all additional parameters and data structures needed in all operation requests and responses. The following is a list of some common aspects covered by OWS Common document:

* GetCapabilities operation (request, parameters, response)
* Exception reports
* Operations parameters
   * Bounding box
   * Coordinate reference systems
   * Format parameters
   * Data descriptions
   * Multilingual text encoding
* Operation request and response encoding (HTTP GET and HTTP POST)
* Guidance for OWS Implementation Specifications
