Basic GeoPackage Concepts
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

Running the Executable Test Suite
---------------------------------

The `GeoPackage Executable Test Suite <https://cite.opengeospatial.org/teamengine/>`_ (ETS) is a conformance test suite that verifies the structure and content of a GeoPackage data container.
To run the ETS, do the following:

1. Open the site (linked above).
2. Create an account using the link provided.
3. Log in.
4. Create a new session.
5. Choose the GeoPackage 1.2 specification (or later if available).
6. Provide a file using either the URL box or a file upload.
7. Select the "Start" button.

The ETS is open source software hosted in a `GitHub Repository <https://github.com/opengeospatial/ets-gpkg12>`_.
