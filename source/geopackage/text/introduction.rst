GeoPackage - Introduction
=========================

Introduction
------------

The GeoPackage Encoding Standard describes a set of rules and conventions for storing vector features, imagery tile matrix sets, raster map tile matrix sets and non-spatial tabular data in an `SQLite <https://sqlite.org>`_ database. The standard also describes rules for extending the capabilities of a GeoPackage.

History
  GeoPackage 1.0 was approved as a standard in January 2014.
  GeoPackage 1.1 was approved as a standard in August 2015.
  GeoPackage 1.2 was approved as a standard in August 2017.
  GeoPackage 1.3 was approved as a standard in November 2020.
Versions
  1.3 is the current latest version
Test Suite
  A test suite exists in the `OGC repository. <https://github.com/opengeospatial/ets-gpkg12>`_


Usage
-----

GeoPackage is used for storing and accessing:

* Vector feature data
* Imagery tile matrix sets
* Raster map tile matrix sets
* Non-spatial tabular data
* Metadata that describes other stored data

Implementation Summary
----------------------

- Implemented in an SQLite database
- Feature geometry is encoded in Well-Known Binary (WKB) based on the OGC standard ”Simple Feature Access” (`Part 1: Common architecture (OGC 06-103r4) <http://portal.opengeospatial.org/files/?artifact_id=25355>`_, `Part 2: SQL option (OGC 06-104r4) <http://portal.opengeospatial.org/files/?artifact_id=25354>`_)
- Supports both vector feature data and tile matrix sets of imagery and maps
- Ideal format for encoding geospatial data where Size, Weight and Power (SWaP) are limited

Relation to other OGC Standards
-------------------------------

Due to its XML serialization, `Geography Markup Language (GML) <https://www.ogc.org/standards/gml>`_ is well suited to geospatial data exchange across networks.
In contrast, GeoPackage is better suited to storage and random access of geospatial data on a file system.
GeoPackage implements the OGC standard ”Simple Feature Access” (see above) which provides a common way for applications to store and access feature data in relational or object-relational databases.

External links
--------------

The GeoPackage.org information `website <http://www.geopackage.org>`_ contains additional information.
