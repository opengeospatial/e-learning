`Nonlinear Geometry Types Extension <http://www.geopackage.org/spec130/#extension_geometry_types>`_
___________________________________________________________________________________________________

This extension allows the use of `extended geometry types <http://www.geopackage.org/spec130/#geometry_types_extension>`_. 

gpkg_extensions
---------------

Add a row to this table for each geometry type in use as described in Table 1.

.. list-table:: Table 1: ``gpkg_extensions``
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``table_name``
    - *table containing extended geometry*
  * - ``column_name``
    - *column containing extended geometry*
  * - ``extension_name``
    - ``gpkg_geom_<gname>`` where ``<gname>`` is the uppercase name of the extended geometry type
  * - ``definition``
    - http://www.geopackage.org/spec130/#extension_geometry_types
  * - ``scope``
    - *read-write*

Features Tables
---------------

When using this extension, use the appropriate type code in the geometry type byte of the geometry.
The ``X`` bit is *0*.
(An ``X`` bit of *1* only applies when using the now-deprecated `User Defined Geometry Types Extension of GeoPackageBinary Geometry Encoding <http://www.geopackage.org/spec110/#extension_geometry_encoding>`_).
