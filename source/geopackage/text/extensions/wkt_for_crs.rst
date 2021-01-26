`WKT for Coordinate Reference Systems <http://www.geopackage.org/spec120/#extension_crs_wkt>`_
______________________________________________________________________________________________


This extension allows the use of the "`Well-known text representation of coordinate reference systems <http://docs.opengeospatial.org/is/12-063r5/12-063r5.html>`_" format (OGC 12-063r5, also known as CRS WKT2) to describe SRSs.

gpkg_extensions
---------------

If using this extension, add a row to this table as described in Table 1.

.. list-table:: Table 1: ``gpkg_extensions``
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``table_name``
    - ``gpkg_spatial_ref_sys``
  * - ``column_name``
    - ``definition_12_063``
  * - ``extension_name``
    - ``gpkg_crs_wkt``
  * - ``definition``
    - http://www.geopackage.org/spec120/#extension_crs_wkt
  * - ``scope``
    - *read-write*

gpkg_spatial_ref_sys
--------------------

When this extension is in use, an additional column called ``definition_12_063`` is added to this table. If software is creating or updating a GeoPackage, it is expected to populate this column when it adds an SRS. For compatibility reasons, it should also populate the original (``definition``) column if possible (note that this is not possible for all SRSs). 

When reading a GeoPackage, client software is expected to prioritize ``definition_12_063`` column over ``definition``. If the software is unable to read ``definition_12_063`` (i.e., it does not recognize the extension) or that column is unpopulated, then it may fall back to using ``definition``.
