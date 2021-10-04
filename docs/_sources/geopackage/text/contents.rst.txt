Content Types
=============

What is in a GeoPackage
-----------------------

Like other relational databases, GeoPackages contain a number of tables. 
The following figure shows the mandatory and optional tables of a GeoPackage.

.. figure:: ../img/geopackage-overview.png
   :width: 560
Figure 1: UML diagram of mandatory and optional GeoPackage tables

GeoPackage tables fall into two categories, *metadata tables* and *user-defined data tables*.
GeoPackages contain two mandatory metadata tables, ``gpkg_contents`` and ``gpkg_spatial_ref_sys``. 
The presence of other metadata tables is dictated by the content being stored (see next pages). The name of the user-defined data table is the primary key for ``gpkg_contents`` and generally is a foreign key for content-specific metadata tables.

`gpkg_contents <http://www.geopackage.org/spec130/#_contents>`_
***************************************************************

The `gpkg_contents` table is the table of contents for a GeoPackage. 
The mandatory columns in this table are:

* ``table_name``: the actual name of the user-defined data table (this is also the primary key for this table)
* ``data_type``: the data type, e.g., "tiles", "features", "attributes" or some other type provided by an extension
* ``identifier`` and ``description``: human-readable text ("identifier" is analogous to "title")
* ``last_change``: the informational date of last change, in ISO 8601 format (for practical purposes, `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`_ applies)
* ``min_x``, ``min_y``, ``max_x``, and ``max_y``: the spatial extents of the content. (This is informational and often used by clients to provide a default view window.)
* ``srs_id``: spatial reference system (see next subsection)

`gpkg_spatial_ref_sys <http://www.geopackage.org/spec130/#spatial_ref_sys)>`_
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

However, many other coordinate reference systems (CRSs) are possible. 
Using CRSs incorrectly is one of the most common ways to break GeoPackage interoperability. 
When in doubt, discuss CRSs with a geospatial expert to ensure that you are using an appropriate CRS for your situation.

.. hint::
    Use the `WKT for Coordinate Reference Systems Extension <extensions/wkt_for_crs.html>`_ to express atypical CRSs.
