`Tiles <http://www.geopackage.org/spec130/#tiles>`_
===================================================

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

.. figure:: http://www.geopackage.org/spec130/geopackage-tiles.png
    :width: 600px
Figure 3: UML Diagram of Tiles tables

`gpkg_tile_matrix_set <http://www.geopackage.org/spec130/#_tile_matrix_set>`_
-----------------------------------------------------------------------------

The ``gpkg_tile_matrix_set`` table describes names a tile matrix set (pyramid). The columns in this table are:

* ``table_name`` and ``srs_id`` match the entries in ``gpkg_contents``
* ``min_x``, ``min_y``, ``max_x``, and ``max_y``: the actual spatial extents of the tile pyramid. 

This is must be exact so that applications can use this information to geolocate tiles correctly. 
(This is in contrast with the extents in ``gpkg_contents`` which are informative and are expected to reflect the extents of *usable content*.)

`gpkg_tile_matrix <http://www.geopackage.org/spec130/#tile_matrix>`_
--------------------------------------------------------------------

Each tile matrix set is composed of one or more tile matrices, each identified by its zoom level. 
The required columns in this table are:

* ``table_name`` matches the entry in ``gpkg_contents`` and elsewhere
* ``zoom_level`` indicates the zoom levels present in the file.
* ``matrix_width`` and ``matrix_height`` describe the size of the tile matrix in tiles
* ``tile_width`` and ``tile_height`` describe the size of each tile in pixels
* ``pixel_x_size`` and ``pixel_y_size`` describe the size of each pixel 

By default, zoom levels are separated by powers of two, but if this is inappropriate for your scenario, other multiples are possible by using the `Zoom Other Levels <http://www.geopackage.org/spec130/#extension_zoom_other_intervals>`_ extension.

`User Data Tables <http://www.geopackage.org/spec130/#tiles_user_tables>`_
--------------------------------------------------------------------------

The physical tiles (data) are stored in user data tables with a specific schema. 
The required columns for these tables are:

* ``id`` is a primary key
* ``zoom_level`` indicates which tile matrix this tile is part of
* ``tile_column`` and ``tile_row`` are the zero-indexed tile number
* ``tile_data`` is the BLOB containing the tile image

PNG and JPG are the two tile file types supported by the core standard.

* PNG is generally better for synthetic data (i.e., digital maps) because it is lossless and its compression codec compresses synthetic data fairly well. 
* JPG is generally better for natural data (i.e., satellite or aerial imagery) due to its superior (though lossy) compression. 
* *The* `WebP Extension <extensions/tiles_encoding_webp.rst>`_ *allows for the use of* `WebP <https://developers.google.com/speed/webp/>`_ *files which feature both transparency and improved compression, but WebP support is not as ubiquitous.*

However, since PNG supports alpha transparency and JPG does not, it is common to use PNG tiles around the boundary of a tile pyramid. 
This allows users to see the data underneath the tile boundaries. 

.. note:: JPG files have an adjustable compression rating. 
   We have found that a ratings in the range 50-75 (out of 100) work best for imagery. 
   Ratings that are too high use too much space and ratings that are too low have too many visible artifacts. 
   Within the 50-75 range it is a reasonable tradeoff between file size and image quality.

By default, tiles pyramids are organized by powers of two.
There are two common strategies for maximizing the storage space efficiency for tiles.

1. Tile pyramids may be sparsely populated.
By leaving unnecessary tiles blank, clients can drop to the next zoom level to render that part of the map. 

2. To further optimize storage efficiency, consider using the `Zoom Other Intervals Extension <extensions/zoom_other_intervals.rst>`_ and refine zoom levels to match the data and its intended use.
