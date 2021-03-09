Attributes and Extensions
=========================

`Attributes <http://www.geopackage.org/spec130/#attributes>`_
-------------------------------------------------------------

Attributes are tables that only contain non-spatial data. 
The rules for attributes are similar to those for features, 
but attributes have no geometry column and the corresponding row in ``gpkg_contents`` has a ``data_type`` of "attributes".
This data is commonly joined with spatial data as required by an application. 

`Extensions <http://www.geopackage.org/spec130/#extension_mechanism>`_
----------------------------------------------------------------------

In addition to tiles, features, and attributes, GeoPackage has a well-defined extension mechanism to support use cases that are not part of the core standard. 
A GeoPackage extension is a set of one or more requirements clauses that either profiles / extends existing requirements clauses in the GeoPackage standard or adds new requirements clauses.
Existing requirement clause extension examples include additional geometry types, additional SQL geometry functions, and additional tile image formats. 
New requirement clause extension examples include spatial indexes, triggers, additional tables, other BLOB column encodings, and other SQL functions.

Files that use one or more extensions are by definition Extended GeoPackages.
There are two categories of extensions, *registered* and *community*.

`gpkg_extensions <http://www.geopackage.org/spec130/#extensions_table_definition>`_
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

Registered extensions have been reviewed and adopted by OGC and are for all intents and purposes part of the standard. Most registered extensions are published as part of the `core standard <http://www.geopackage.org/spec130/#registered_extensions>`_ but they may be published independently as well.

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
