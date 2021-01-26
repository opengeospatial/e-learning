`Related Tables Extension <http://docs.opengeospatial.org/is/18-000/18-000.html>`_
__________________________________________________________________________________


This extension allows a GeoPackage to contain additional data that is related to geospatial (e.g., features) or attributes data.
As an example, this can be used to establish a many-to-many relationship between features (e.g., points, lines, or areas) and multimedia files. 
By definition, the "left" side of the relationship is the "base" data and the "right" side of the relationship is the "related" data.

`gpkg_extensions <http://docs.opengeospatial.org/is/17-066r1/17-066r1.html#gpkg_extensions>`_
---------------------------------------------------------------------------------------------

To use this extension, add rows to this table as described in Table 1.

.. list-table:: Table 1: ``gpkg_extensions``
   :widths: 20 15 15 40 10
   :header-rows: 1
   
  * - ``table_name``
    - ``column_name``
    - ``extension_name``
    - ``definition``
    - ``scope``
  * - ``gpkgext_relations``
    - *NULL*
    - ``gpkg_related_tables``
    - http://docs.opengeospatial.org/is/18-000/18-000.html
    - *read-write*
  * - *name of actual User Defined Mapping Table*
    - *NULL*
    - ``gpkg_related_tables``
    - http://docs.opengeospatial.org/is/18-000/18-000.html
    - *read-write*

`gpkgext_relations <http://docs.opengeospatial.org/is/18-000/18-000.html#_gpkgext_relations>`_
----------------------------------------------------------------------------------------------

This table describes extended relationships.
To define a relationship, add a row to this table with columns as described in Table 2.

.. list-table:: Table 2: ``gpkg_metadata``
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``id``
    - *primary key*
  * - ``base_table_name``
    - Name of the table containing the base data (e.g., features) to relate
  * - ``base_primary_column``
    - Name of the primary key column in ``base_table_name``
  * - ``related_table_name``
    - Name of the table containing the related content
  * - ``related_primary_column``
    - Name of the primary key column in ``related_table_name``
  * - ``relation_name``
    - Name (profile) of the relationship
  * - ``mapping_table_name``
    - Name of a [user-defined mapping table](#user-defined-mapping-table)

.. hint::
    To further define the semantics for a relationship, consider using the `Schema Extension <schema.rst>`_ on the ``mapping_table_name`` column.

User-defined Mapping Table
--------------------------

A user-defined mapping table describes the many-to-many relationships between base data and related data.
A user-defined mapping table requires at least the columns defined in Table 3.

.. list-table:: Table 3: User-defined Mapping Table
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``base_id``
    - The primary key value of the base data table
  * - ``related_id``
    - The primary key value of the related data table

Add a row to this table for each related pair.

Using Profiles
--------------

This extension offers a number of profiles. Each profile adds some specialized rules to make relationships more meaningful.

Media
*****

When the ``relation_name`` of a relationship is "*media*", the related table must be an `attributes <http://www.geopackage.org/guidance/getting-started.html#attributes>`_ table with at least the columns defined in Table 4:


.. list-table:: Table 4: Media Attributes Table
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - *any*
    - Primary Key
  * - ``data``
    - BLOB containing multimedia content
  * ``content_type``
    - MIME type of data

.. hint::
    If you want to avoid data duplication, add a column to the user-defined mapping table containing a hash of the data. That way you can check to see whether a piece of media already exists in the table before adding it.

Simple Attibutes
****************

When the ``relation_name`` of a relationship is "*simple_attributes*", the related table must be an `attributes <http://www.geopackage.org/guidance/getting-started.html#attributes>`_ table and that table must have TEXT, INTEGER, or REAL columns (no BLOB or NULL).

Related Features
----------------

When the ``relation_name`` of a relationship is "*features*", the related table must be a `features <http://www.geopackage.org/guidance/getting-started.html#features>`_ table.
