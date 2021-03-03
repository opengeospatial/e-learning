GeoPackage - Introduction
=========================

Introduction
------------

The GeoPackage Encoding Standard describes a set of rules and conventions for storing vector features, imagery tile matrix sets, raster map tile matrix sets and non-spatial tabular data in an SQLite database. The standard also describes rules for extending the capabilities of a GeoPackage.

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
- Feature geometry is encoded in Well Known Text (WKT) based on the OGC OpenGIS® Simple Features Interface Standard (SFS)
- Supports both vector feature data and tile matrix sets of imagery and maps
- Ideal format for encoding geospatial data where Size, Weight and Power (SWaP) are limited

Tables
------

The following figure shows the mandatory and optional tables of a GeoPackage.

.. image:: ../img/geopackage-overview.png
   :height: 327
   :width: 560


Relation to other OGC Standards
-------------------------------

Due to its XML serialization, GML is well suited to geospatial data exchange across networks.
In contrast, GeoPackage is better suited to storage and random access of geospatial data on a file system.
GeoPackage implements the OGC OpenGIS® Simple Features Interface Standard (SFS) which provides a common way for applications to store and access feature data in relational or object-relational databases.

Applications
------------

The following are some applications and APIs that can be used with GeoPackage:

* `SQLite <apps/sqlite.html>`_
* `GDAL / OGR <apps/gdal-ogr.html>`_
* `QGIS <apps/qgis.html>`_
* `The GeoPackage-Java library <apps/geopackage-java.html>`_

External links
--------------

The GeoPackage.org information `website <http://www.geopackage.org>`_ contains additional information.
