Advanced GeoPackage Concepts
============================

Identifying a GeoPackage
------------------------

A `GeoPackage <http://geopackage.org>`_ is an `SQLite Database <http://sqlite.org/index.html>`_ file with a `.gpkg extension <http://www.geopackage.org/spec120/#r3>`_. 
If you are unsure whether a file is an SQLite database, you can use a binary or text editor to view the starting bytes of the file and see if they state `"SQLite format 3" <http://www.geopackage.org/spec120/#r1>`_.

Opening a GeoPackage
--------------------

There are a number of ways to open a GeoPackage. 

* For using a command-line SQL interface, consider the "sqlite" command.
* For using a graphical SQL interface, consider `DB Browser for SQLite <http://sqlitebrowser.org/>`_.
* For using a web application, consider using `NGA's application <http://ngageoint.github.io/geopackage-js/>`_ as long as the GeoPackage file isn't too big.
* For using a desktop application, there are a number of options. We recommend choosing the GeoPackage implementation that is best suited for your operational environment. 

The GeoPackage community tries to maintain a list of operational GeoPackage implementations and this list can be found on the `implementations page <http://www.geopackage.org/implementations.html>`_. Additional information on specific products and versions of products that implement GeoPackage can also be found at http://www.opengeospatial.org/resource/products. You can search by specific versions of the GeoPackage standard. Note: Search for all implementing products.

Creating a GeoPackage
---------------------

Similarly, if you wish to create a new GeoPackage from scratch or from an existing source file such as a ShapeFile or .csv, below are some suggestions:

* For using direct SQL access, start with the `empty geopackage template <http://www.geopackage.org/data/empty.gpkg>`_
* For using a desktop application, refer to the implementations list above
* For using a command line program, consider the `GDAL <http://www.gdal.org>`_ vector and raster utilities 
* This `blog post <http://www.fulcrumapp.com/blog/working-with-geodata/>`_ (The section titled "Creating a GeoPackage with Reference Data") provides an example that describes steps for creating a GeoPackage using ogr2ogr. The post also provides information on how to add the `SpatiaLite <https://www.gaia-gis.it/fossil/libspatialite/index>`_ extension to enable further spatial analysis in SQLite.


    Note: For maximum interoperability, start your database identifiers (table names, column names, etc.) with a lowercase character and only use lowercase characters, numbers 0-9, and underscores (`_`).

Checking a GeoPackage Version
-----------------------------

Using a direct SQL interface such as DB Browser is the easiest way to check a GeoPackage version. SQLite uses `"pragma" statements<https://www.sqlite.org/pragma.html>`_ to implement non-standard SQL functions. 
These statements can be executed just like any other SQL statement and where relevant, they return a result set. The two pragmas you need to know are:

* `PRAGMA application_id`
   * 1196444487 (the 32-bit integer value of 0x47504B47 or `GPKG` in ASCII) for GPKG 1.2 and greater 
   * 1196437808 (the 32-bit integer value of 0x47503130 or `GP10` in ASCII) for GPKG 1.0 or 1.1
* `PRAGMA user_version`
   * For versions 1.2 and later, this returns an integer representing the version number in the form MMmmPP (MM = major version, mm = minor version, PP = patch). Therefore 1.2 is 10200.
   
What is in a GeoPackage
-----------------------

Like other relational databases, GeoPackages contain a number of tables. These tables fall into two categories, user-defined data tables and metadata tables. GeoPackages contain two mandatory metadata tables, ``gpkg_contents`` and ``gpkg_spatial_ref_sys``. 
The presence of other metadata tables is dictated by the content being stored (see Content Types below). The name of the user-defined data table is the primary key for ``gpkg_contents`` and generally is a foreign key for content-specific metadata tables.

`gpkg_contents <http://www.geopackage.org/spec120/#_contents>`_
***************************************************************

The `gpkg_contents` table is the table of contents for a GeoPackage. 
The mandatory columns in this table are:

* ``table_name``: the actual name of the user-defined data table (this is also the primary key for this table);
* ``data_type``: the data type, e.g., "tiles", "features", "attributes" or some other type provided by an extension;
* ``identifier`` and ``description``: human-readable text ("identifier" is analogous to "title");
* ``last_change``: the informational date of last change, in ISO 8601 format (for practical purposes, `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`_ applies);
* ``min_x``, ``min_y``, ``max_x``, and ``max_y``: the spatial extents of the content. (This is informational and often used by clients to provide a default view window.);
* ``srs_id``: spatial reference system (see next subsection).

`gpkg_spatial_ref_sys <http://www.geopackage.org/spec120/#spatial_ref_sys)>`_
*****************************************************************************

For content that has spatial reference (including but not limited to tiles and features), each row in contents must reference a coordinate reference system which is stored in the ``gpkg_spatial_ref_sys`` table. 
The mandatory columns in this table are:

* ``srs_name``, ``description``: a human readable name and description for the SRS; 
* ``srs_id``: a unique identifier for the SRS; also the primary key for the table;
* ``organization``: Case-insensitive name of the defining organization e.g., ``EPSG`` or ``epsg``;
* ``organization_coordsys_id``: Numeric ID of the SRS assigned by the organization;
* ``definition``: Well Known Text definition of the SRS.

At least three rows must be in this table. There must be one row for each of the following ``srs_id`` column values:

* *4326*: latitude and longitude coordinates on the WGS84 reference ellipsoid,
* *0*: undefined geographic coordinate reference systems, and
* *-1*: undefined Cartesian coordinate reference systems.

However, many more rows that reference other coordinate reference systems (CRSs) are possible. 
Using CRSs incorrectly is one of the most common ways to break GeoPackage interoperability. 
When in doubt, discuss CRSs with a geospatial expert to ensure that you are using an appropriate coordinate reference system for your situation.
