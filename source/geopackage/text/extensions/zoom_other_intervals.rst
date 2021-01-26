`Zoom Other Intervals <http://www.geopackage.org/spec120/#extension_zoom_other_intervals>`_
___________________________________________________________________________________________

This extension allows the use of tile pyramids with zoom levels that are separated by something other than a power of 2. This can be useful for certain types of raster data as described in this `blog post <http://geopackage.blogspot.com/2015/11/powers-of-two-scale-sets.html>`_.

gpkg_extensions
---------------

Add a row to this table for each tile pyramid that does not have tile matrices separated by powers of two as described in Table 1.

.. list-table:: Table 1: ``gpkg_extensions``
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``table_name``
    - *tile pyramid user data table name*
  * - ``column_name``
    - ``tile_data``
  * - ``extension_name``
    - ``gpkg_zoom_other``
  * - ``definition``
    - http://www.geopackage.org/spec120/#extension_zoom_other_intervals
  * - ``scope``
    - *read-write*

gpkg_tile_matrix
----------------

When using this extension, the ``pixel_x_size`` and ``pixel_y_size`` can differ by arbitrary amounts. One approach is to have the pixel sizes for the highest zoom level match the native resolution of the raster data as closely as possible and for the next highest zoom level to have significantly higher pixel sizes, perhaps matching the pixel size of a tile matrix from a more commonly used tile matrix set. This maximizes image quality and reduces wasted space.
