NSG Profile of GeoPackage
=====================

Introduction
------------

The `National System for Geospatial-Intelligence (NSG) GeoPackage Profile <https://github.com/ngageoint/nsg_geopackage_2.1>`_ defines and tailors the implementable provisions prescribed for the NSG for a GeoPackage based on the OGC GeoPackage encoding standard. The profile provides detailed directions on how to use the clauses, options and parameters defined in the base GeoPackage standard. The goal is to ensure that NSG GeoPackages, GeoPackage SQLite Extensions, and supporting utilities and services fulfil their intended purposes and are fit for use.

The following is an overview of the NSG Profile.

File Names
----------

The NSG GeoPackage Profile provides guidance on how to name files so that ad-hoc naming conventions are avoided. The file naming scheme is `{Producer}_\{Data Product}_\{Geo Coverage Area}_\{Zoom Levels}_{Version}_{Date}`. The naming scheme makes it easier to organize related geopackages in a filesystem. For example, all geopackages produced by a specific organization for a particular geographic extent would be found in the same folder on a filesystem.

Tiles
------------------

The NSG GeoPackage Profile provides guidance on Tile Size, Zoom Levels, and Bounding Boxes. The profile mandates tiles of 256-pixel width by 256-pixel height for each tile in a tile pyramid of images. Further, the profile requires that pixel sizes vary by a factor of 2 between all adjacent zoom levels.

Guidance regarding bounding boxes is also provided. The bounding box presented by the `gpkg_tile_matrix_set` table is used to determine the geographic position of each tile in the tile pyramid, whereas the bounding box presented by the `gpkg_contents` is used to describe an informative bounding rectangle of all tiles in the tile pyramid data.

Features
------------------

The NSG GeoPackage Profile provides guidance on GeoPackage extensions for features. The guidance specifically focuses on the Geometry Types Extensions. In short, extension of geometry types is not currently allowed. Further guidance is provided regarding the GeoPackage RTree Spatial Indexes Extension that adds a capability for spatially indexing geometry columns.

Coordinate Reference Systems
----------------------------

The NSG GeoPackage Profile provides guidance on Coordinate Reference Systems (CRS) and their Well Known Text (WKT) definitions. WKT offers a compact machine- and human-readable representation of geometric objects or the critical elements of coordinate reference system (CRS) definitions. WKT was described in the Open Geospatial Consortium implementation specifications 99-036 through 06-103r4 and `ISO 19125-1:2004 <https://www.iso.org/obp/ui/#!iso:std:40114:en>`_ .

The profile mandates the use of the World Mercator projection for use cases that require precise locations and precise navigation (land, air, and sea). Further guidance is provided regarding CRSs used by raster tile pyramid and vector feature data tables in a GeoPackage.

Metadata
--------

The NSG GeoPackage Profile provides guidance on storage of NMIS v2.2 metadata as XML in GeoPackages that contain NSG data, and specifies use of particular metadata values in certain conditions per the National System for Geospatial Intelligence Metadata Foundation (NMF).


Data Validity Constraints
-------------------------

The NSG GeoPackage Profile specifies constraints on allowable data values in GeoPackage SQL tables to enable assessment and enforcement of data validity. The allowable data values serve as ranges or enumerations that specific attributes in geopackage tables may adopt.
