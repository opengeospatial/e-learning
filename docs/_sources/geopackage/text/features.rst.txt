`Features <http://www.geopackage.org/spec130/#features>`_
=========================================================

Vector feature data are geographic entities including conceptual ones such as districts, real world objects such as roads and rivers, and observations. (An *observation* is an act that results in the estimation of the value of a feature property, and involves application of a specified procedure, such as a sensor, instrument, algorithm or process chain. A temperature at a given geographic location provided by a sensor is an example of an observation.) 
For vector feature data, there is one additional required table: ``gpkg_geometry_columns``. 
Features are stored in the user-defined data tables identified by the ``table_name`` values in ``gpkg_contents`` (one table per row).

.. figure:: http://www.geopackage.org/spec130/geopackage-features.png
    :width: 600px
Figure 1: UML Diagram of Features tables

`gpkg_geometry_columns <http://www.geopackage.org/spec130/#_geometry_columns>`_
-------------------------------------------------------------------------------

The ``gpkg_geometry_columns`` table describes the geometry for a particular Features table. 
Each feature table must have a corresponding row in this table. The required columns in this table are:

* ``table_name`` and ``column_name`` where the geometries are stored
* ``geometry_type_name`` `<http://www.geopackage.org/spec130/#geometry_types_core>`_
* ``srs_id`` the spatial reference system (see previous page)
* ``z`` and ``m`` are flags to indicate 3D/4D applications (Z values are for height/elevation/depth and M values are reserved for other types of domain-specific measurements)

`User-defined Data Tables <http://www.geopackage.org/spec130/#feature_user_tables>`_
------------------------------------------------------------------------------------

Features are stored in user-defined data tables. Each features table has exactly one geometry column, a BLOB. 
(The structure of this BLOB is described `here <http://www.geopackage.org/spec130/#gpb_format>`_.) 
The `OGC Simple Features geometry types <http://www.geopackage.org/spec130/#geometry_types_core>`_ are the supported geometry types. 
Other than the geometry column and a primary key, the schema of a features table is up to the implementer. 
Properties (text, integer, or real) provide additional information about each feature. 
The GeoPackage standard has an `example schema <http://www.geopackage.org/spec130/#example_feature_table_cols>`_.

The `Schema Extension <extensions/schema.html>`_ can be used to describe columns in more detail than just their name.
