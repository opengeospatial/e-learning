`RTree Spatial Indexes Extension <http://www.geopackage.org/spec130/#extension_rtree>`_
_______________________________________________________________________________________

This extension adds a new capability for spatially indexing geometry columns. This extension uses the rtree implementation provided by the `SQLite R-Tree Module extension <http://www.sqlite.org/rtree.html>`_.

gpkg_extensions
---------------

To use this extension, add a row to this table for each geometry column to be indexed as described in Table 1.

.. list-table:: Table 1: ``gpkg_extensions``
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``table_name``
    - *table containing geometry to index*
  * - ``column_name``
    - *column containing geometry to index*
  * - ``extension_name``
    - ``gpkg_rtree_index``
  * - ``definition``
    - http://www.geopackage.org/spec/#extension_rtree
  * - ``scope``
    - *read-write*

Virtual Tables and Triggers
---------------------------

The spatial index is established by creating a virtual table and a set of triggers.
These are detailed in `Appendix F.3 <http://www.geopackage.org/spec/#r77>`_.

