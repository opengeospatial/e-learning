`Schema <http://www.geopackage.org/spec130/#extension_schema>`_
_______________________________________________________________

This extension provides a means to describe the columns of tables in a GeoPackage with more detail than can be captured by the SQL table definition directly. The information provided by this extension can be used by applications to, for instance, present data contained in a GeoPackage in a more user-friendly fashion or implement data validation logic. The extension was originally designed to describe the schema of *features* but it could apply to any user-defined table with user-defined columns. 

gpkg_extensions
---------------

To use this extension, add the following rows to this table as described in Table 1.

.. list-table:: Table 1: ``gpkg_extensions``
   :widths: 20 15 15 40 10
   :header-rows: 1
   
  * - ``table_name``
    - ``column_name``
    - ``extension_name``
    - ``definition``
    - ``scope``
  * - ``gpkg_data_columns``
    - *NULL*
    - ``gpkg_schema``
    - http://www.geopackage.org/spec130/#extension_schema
    - *read-write*
  * - ``gpkg_data_column_constraints``
    - *NULL*
    - ``gpkg_schema``
    - http://www.geopackage.org/spec130/#extension_schema
    - *read-write*

gpkg_data_columns
-----------------

Add a row to this table for each column that needs to be further described as described in Table 2.

.. list-table:: Table 2: ``gpkg_data_columns``
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``table_name``
    - *user-defined table name*
  * - ``column_name``
    - *user-defined column name*
  * - ``name``
    - A human-readable identifier (e.g. short name) for the column_name content
  * - ``title``
    - A human-readable formal title for the column_name content
  * - ``description``
    - A human-readable description for the column_name content
  * - ``mime_type``
    - MIME type of column_name if BLOB type, or NULL for other types
  * - ``constraint_name``
    - Column value constraint name (lowercase) specified by reference to gpkg_data_column_constraints.constraint name (see below)

Using This Extension
--------------------

Defining an Enumeration
***********************

To define an enumeration for a column, add one row to ``gpkg_data_column_constraints`` for each enumerated value as described in Table 3. (Other values can be *NULL* and are to be ignored.) 

.. list-table:: Table 3: ``gpkg_data_column_constraints`` for an enumeration
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``constraint_name``
    - Name of constraint (lowercase)
  * - ``constraint_type``
    - ``enum``
  * - ``value``
    - Specified case sensitive value
  * - ``description``
    - Description of the enum value

Defining a Range
****************

To define a numeric range for an column, add one row to ``gpkg_data_column_constraints`` as described in Table 4. (Other values can be *NULL* and are to be ignored.)

.. list-table:: Table 4: ``gpkg_data_column_constraints`` for a range
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``constraint_name``
    - Name of constraint (lowercase)
  * - ``constraint_type``
    - ``range``
  * - ``min``
    - Minimum value
  * - ``min_is_inclusive``
    - *0* (false) if min value is exclusive, or *1* (true) if min value is inclusive
  * - ``max`
    - Maximum value
  * - ``max_is_inclusive``
    - *0* (false) if max value is exclusive, or *1* (true) if min value is inclusive
  * ``description``
    - Description of the constraint

Defining a GLOB
***************

A `GLOB <https://www.sqlite.org/lang_expr.html#glob>`_ is a pattern-matching expression. You can add a GLOB constraint for a column to constrain values to those that match the specified pattern. To do this, add one row to `gpkg_data_column_constraints` as as described in Table 5.

.. list-table:: Table 5: ``gpkg_data_column_constraints`` for a range
   :widths: 20 80
   :header-rows: 1
   
  * - Column
    - Value
  * - ``constraint_name``
    - Name of constraint (lowercase)
  * - ``constraint_type``
    - ``glob``
  * - ``value``
    - actual GLOB expression
  * - ``description``
    - Description of the constraint

Defining a MIME Type for a BLOB
*******************************
To constraint a BLOB column to a specific MIME type, set the ``mime_type`` column for that row in ``gpkg_data_columns``. (The ``constraint_name`` column of ``gpkg_data_columns`` can be *NULL* and the ``gpkg_data_column_constraints`` table does not apply.) 

.. note::
    This constraint must be controlled through software – it is not possible for SQLite to control this directly.

