Content Types
=============

What is in a GeoPackage
-----------------------

Like other relational databases, GeoPackages contain a number of tables. These tables fall into two categories, *metadata tables* and *user-defined data tables*.
GeoPackages contain two mandatory metadata tables, ``gpkg_contents`` and ``gpkg_spatial_ref_sys``. 
The presence of other metadata tables is dictated by the content being stored (see Content Types below). The name of the user-defined data table is the primary key for ``gpkg_contents`` and generally is a foreign key for content-specific metadata tables.

`gpkg_contents <http://www.geopackage.org/spec120/#_contents>`_
***************************************************************

The `gpkg_contents` table is the table of contents for a GeoPackage. 
The mandatory columns in this table are:

* ``table_name``: the actual name of the user-defined data table (this is also the primary key for this table)
* ``data_type``: the data type, e.g., "tiles", "features", "attributes" or some other type provided by an extension
* ``identifier`` and ``description``: human-readable text ("identifier" is analogous to "title")
* ``last_change``: the informational date of last change, in ISO 8601 format (for practical purposes, `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`_ applies)
* ``min_x``, ``min_y``, ``max_x``, and ``max_y``: the spatial extents of the content. (This is informational and often used by clients to provide a default view window.)
* ``srs_id``: spatial reference system (see next subsection)

`gpkg_spatial_ref_sys <http://www.geopackage.org/spec120/#spatial_ref_sys)>`_
*****************************************************************************

For content that has spatial reference (including but not limited to tiles and features), each row in contents must reference a coordinate reference system which is stored in the ``gpkg_spatial_ref_sys`` table. 
The mandatory columns in this table are:

* ``srs_name``, ``description``: a human readable name and description for the SRS 
* ``srs_id``: a unique identifier for the SRS; also the primary key for the table
* ``organization``: Case-insensitive name of the defining organization e.g., ``EPSG`` or ``epsg``
* ``organization_coordsys_id``: Numeric ID of the SRS assigned by the organization
* ``definition``: Well Known Text definition of the SRS.

At least three rows must be in this table. There must be one row for each of the following ``srs_id`` column values:

* *4326*: latitude and longitude coordinates on the WGS84 reference ellipsoid,
* *0*: undefined geographic coordinate reference systems, and
* *-1*: undefined Cartesian coordinate reference systems.

However, many more rows that reference other coordinate reference systems (CRSs) are possible. 
Using CRSs incorrectly is one of the most common ways to break GeoPackage interoperability. 
When in doubt, discuss CRSs with a geospatial expert to ensure that you are using an appropriate coordinate reference system for your situation.

`Features <http://www.geopackage.org/spec120/#features>`_
---------------------------------------------------------

Vector feature data are geographic entities including conceptual ones such as districts, real world objects such as roads and rivers, and observations. (An *observation* is an act that results in the estimation of the value of a feature property, and involves application of a specified procedure, such as a sensor, instrument, algorithm or process chain. A temperature at a given geographic location provided by a sensor is an example of an observation.) 
For vector feature data, there is one additional required table: ``gpkg_geometry_columns``. 
Features are stored in the user-defined data tables identified by the ``table_name`` values in ``gpkg_contents`` (one table per row).

.. figure:: http://www.geopackage.org/spec120/geopackage-features.png
    :width: 600px
Figure 1: UML Diagram of Features tables

`gpkg_geometry_columns <http://www.geopackage.org/spec120/#_geometry_columns>`_
*******************************************************************************

The ``gpkg_geometry_columns`` table describes the geometry for a particular Features table. 
Each feature table must have a corresponding row in this table. The required columns in this table are:

* ``table_name`` and ``column_name`` where the geometries are stored
* ``geometry_type_name`` `<http://www.geopackage.org/spec120/#geometry_types_core>`_
* ``srs_id`` the spatial reference system (see previous page)
* ``z`` and ``m`` are flags to indicate 3D/4D applications (Z values are for height/elevation/depth and M values are reserved for other types of domain-specific measurements)

`User-defined Data Tables <http://www.geopackage.org/spec120/#feature_user_tables)>`_
*************************************************************************************

Features are stored in user-defined data tables. Each features table has exactly one geometry column, a BLOB. 
(The structure of this BLOB is described `here <http://www.geopackage.org/spec120/#gpb_format>`_.) 
The `OGC Simple Features geometry types <http://www.geopackage.org/spec120/#geometry_types_core>`_ are the supported geometry types. 
Other than the geometry column and a primary key, the schema of a features table is up to the implementer. 
Properties (text, integer, or real) provide additional information about each feature. 
The GeoPackage standard has an `example schema <http://www.geopackage.org/spec120/#example_feature_table_cols>`_.

`Tiles <http://www.geopackage.org/spec120/#tiles>`_
---------------------------------------------------

The GeoPackage standard adopts a tile-based pyramid structure for storing imagery and raster maps at multiple resolutions.
An illustration of this structure is shown below.

.. figure:: ../img/pyramid2.png
   :height: 327
   :width: 560
Figure 2: A tile pyramid

The GeoPackage *tiles* option specifies a mechanism for storing raster data in tile pyramids. 

* "Tile pyramid" refers to the concept of pyramid structure of tiles of different spatial extent and resolution at different zoom levels, and the tile data itself. 
* "Tile" refers to an individual raster image such as a PNG or JPEG that covers a specific geographic area. 
* "Tile matrix" refers to rows and columns of tiles that all have the same spatial extent and resolution at a particular zoom level. 
* "Tile matrix set" refers to the definition of a tile pyramid’s tiling structure. 

This tile-based pyramid structure is particularly useful when handling a GeoPackage on small or constrained devices such as mobile phones, tablets or laptops because an appropriate resolution can be selected based on the zoom level and the device screen size.
This mechanism is based on the model for tile matrix sets described in Section 6 of the `WMTS Implementation Specification <http://www.opengeospatial.org/standards/wmts>`_.

If tiles are to be included in a GeoPackage, there are two additional required metadata tables, ``gpkg_tile_matrix_set`` and ``gpkg_tile_matrix``. 
In addition to these tables, each tile pyramid requires a user-defined table that contains the actual tiles.

.. figure:: http://www.geopackage.org/spec120/geopackage-tiles.png
    :width: 600px
Figure 3: UML Diagram of Tiles tables

`gpkg_tile_matrix_set <http://www.geopackage.org/spec120/#_tile_matrix_set>`_
*****************************************************************************

The ``gpkg_tile_matrix_set`` table describes names a tile matrix set (pyramid). The columns in this table are:

* ``table_name`` and ``srs_id`` match the entries in ``gpkg_contents``
* ``min_x``, ``min_y``, ``max_x``, and ``max_y``: the actual spatial extents of the tile pyramid. 

This is must be exact so that applications can use this information to geolocate tiles correctly. 
(This is in contrast with the extents in ``gpkg_contents`` which are informative and are expected to reflect the extents of *usable content*.)

`gpkg_tile_matrix <http://www.geopackage.org/spec120/#tile_matrix>`_
********************************************************************

Each tile matrix set is composed of one or more tile matrices, each identified by its zoom level. 
The required columns in this table are:

* ``table_name`` matches the entry in ``gpkg_contents`` and elsewhere
* ``zoom_level`` indicates the zoom levels present in the file.
* ``matrix_width`` and ``matrix_height`` describe the size of the tile matrix in tiles
* ``tile_width`` and ``tile_height`` describe the size of each tile in pixels
* ``pixel_x_size`` and ``pixel_y_size`` describe the size of each pixel 

By default, zoom levels are separated by powers of two, but if this is inappropriate for your scenario, other multiples are possible by using the `Zoom Other Levels <http://www.geopackage.org/spec120/#extension_zoom_other_intervals>`_ extension.

`User Data Tables <http://www.geopackage.org/spec120/#tiles_user_tables>`_
**************************************************************************

The physical tiles (data) are stored in user data tables with a specific schema. 
The required columns for these tables are:

* ``id`` is a primary key
* ``zoom_level`` indicates which tile matrix this tile is part of
* ``tile_column`` and ``tile_row`` are the zero-indexed tile number
* ``tile_data`` is the BLOB containing the tile image

Unless you use an extension, PNG and JPG are the two supported file types for the tiles. 
PNG is generally better for synthetic data (i.e., digital maps) because it is lossless and its compression codec compresses synthetic data fairly well. 
JPG is generally better for natural data (i.e., satellite or aerial imagery) due to its superior (though lossy) compression. 
However, since PNG supports alpha transparency and JPG does not, it is common to use PNG tiles around the boundary of a tile pyramid. 
This allows users to see the data underneath the tile boundaries. 
JPG files have an adjustable compression rating. 
We have found that a ratings in the range 50-75 (out of 100) work best for imagery. 
Ratings that are too high use too much space and ratings that are too low have too many visible artifacts. 
Within the 50-75 range it is a reasonable tradeoff between file size and image quality.

Tile pyramids may be sparsely populated. 
This is a good way to manage GeoPackage size. 
Applications should be aware of this possibility and if possible, drop to the next zoom level to render that part of the map. 

`Attributes <http://www.geopackage.org/spec120/#attributes>`_
-------------------------------------------------------------

Attributes are tables that only contain non-spatial data. 
The rules for attributes are similar to those for features, 
but attributes have no geometry column and the corresponding row in ``gpkg_contents`` has a ``data_type`` of "attributes".
This data is commonly joined with spatial data as required by an application. 

`Extensions <http://www.geopackage.org/spec120/#extension_mechanism>`_
----------------------------------------------------------------------

In addition to tiles, features, and attributes, GeoPackage has a well-defined extension mechanism to support use cases that are not part of the core standard. 
A GeoPackage extension is a set of one or more requirements clauses that either profiles / extends existing requirements clauses in the GeoPackage standard or adds new requirements clauses.
Existing requirement clause extension examples include additional geometry types, additional SQL geometry functions, and additional tile image formats. 
New requirement clause extension examples include spatial indexes, triggers, additional tables, other BLOB column encodings, and other SQL functions.

Files that use one or more extensions are by definition Extended GeoPackages.
There are two categories of extensions, *registered* and *community*.

`gpkg_extensions <http://www.geopackage.org/spec120/#extensions_table_definition>`_
***********************************************************************************

The extensions table describes the extensions that are in use in a GeoPackage.
The columns for this table are:

* ``table_name`` is the name of the SQLite table where the extension applies
* ``column_name`` is the name of the SQLite column (in the referenced ``table_name``) where the extension applies (in some situations this is *null*)
* ``extension_name`` is the case sensitive name of the extension that is required, in the form ``<author>_<extension_name>`` (the author name *gpkg* is reserved for OGC adopted extensions)
* ``definition`` is permalink, URI, or reference to a document that defines the extension
* ``scope`` is either *read-write* (for most extensions) or *write-only* (for extensions that can be used seamlessly by applications that are unaware of the extension as long as they operate in a read-only mode)

Registered Extensions
*********************

Registered extensions have been reviewed and adopted by OGC and are for all intents and purposes part of the standard. Most registered extensions are published as part of the `core standard <http://www.geopackage.org/spec120/#registered_extensions>`_ but they may be published independently as well.

The following extensions have been adopted by OGC:

* `Non-Linear Geometry Types <extensions/nonlinear_geometry_types.html>`_
* `RTree Spatial Indexes <extensions/rtree_spatial_indexes.html>`_
* `Zoom Other Intervals <extensions/zoom_other_intervals.html>`_
* `Tiles Encoding WebP <extensions/tiles_encoding_webp.html>`_
* `Metadata <extensions/metadata.html>`_
* `Schema <extensions/schema.html>`_
* `WKT for Coordinate Reference Systems <extensions/wkt_for_crs.html>`_
* `Tiled Gridded Coverage Data <extensions/tiled_gridded_coverage_data.html>`_
* `Related Tables <extensions/related_tables.html>`_

Follow the links for a description for each individual extension.

Community Extensions
********************

OGC acknowledges that there are use cases not covered by the GeoPackage standard. Implementers are welcome to use the extension mechanism defined here to develop community extensions. The extension mechanism provides advantages including discoverability (the extensions in use can be discovered by scanning a single table) and uniformity (declaring that an extension is in use indicates that a defined set of requirements are being met). However, this is a decision that should be made carefully as custom extensions do introduce interoperability risks.
OGC manages a registry of `community extensions <http://www.geopackage.org/extensions.html#_community_extensions>`_.

OGC is unable to endorse community extensions. Therefore an Extended GeoPackage containing community extensions will not pass conformance tests. However, a community of interest MAY waive that requirement in its own GeoPackage profile, with the caveat that it must bear the responsibility of endorsing the new extension(s).

Implementers that are interested in developing their own extensions are encouraged to contact OGC to ensure that the extensions are developed in accordance with OGC policies and in a way that minimizes risks to interoperability. OGC will consider adopting externally developed extensions that address a clear use case, have a sound technical approach, and have a commitment to implementation by multiple implementers.
