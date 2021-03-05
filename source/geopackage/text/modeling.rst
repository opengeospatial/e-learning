Modeling Guidelines
===================

The GeoPackage encoding standard mandates in Requirements `22 <http://www.geopackage.org/spec/#r22>`_ and `30 <http://www.geopackage.org/spec/#r30>`_ that vector feature user tables shall only have a single geometry. This is advantageous for two reasons:

* It keeps the semantics of the data model concise: a feature has one shape. This is in line with other vector data formats with which GeoPackage is often compared, such as Shapefile or GeoJSON. By sharing this restriction, converting data from one format to another is more straightforward. This is particularly beneficial in enterprise workflows. For example, mobile components use a GeoPackage to view the business data, while the web-clients use a GeoJSON version of the same.
* Allowing multiple geometries per feature table would compromise GeoPackage's position in the GIS application ecosystem. Most ready-made GIS data viewers handle data formats in a uniform manner. Opening a file creates a layer on map and the layer shows the features contained in that file. There are usually some UI-capabilities to view properties of a feature or change the styling of a feature. If feature tables were to contain multiple geometries, the visualization of a GeoPackage in such a COTS-viewer would be much more complicated. What geometry should be shown on the map? All of them? Only the first? Editing tools would create a similar set of problems.

This restriction should not be seen as a limitation. Since a GeoPackage is a relational database, users can create rich data models to describe the required scenarios. Instead of adding more geometry columns to a single table, the general approach is to extract these geometries into a separate table, creating a one-to-many relationship between the geometries and the feature.

This document illustrates three different use-cases for associating multiple geometries with a single feature. For each, it:

* describes a common use-case
* presents a corresponding example of the database schema
* shows how these tables should be appropriately registered in the gpkg\_\* tables
* shows how views can be used to enhance the utility and usability of the resulting GeoPackage

Tracking previous geometries of a single feature
------------------------------------------------

Example use case
****************
You want to store the history of edits to the geometry of a pipe-feature. For each edit, you want to keep track of when that modification was made.

The last edit is the current geometry of the feature. This is the main pipe geometry that you want to present to your users by default.

Proposed Solution: Store the geometries of the feature in a table separate from the table that contains the pipe-metadata. These are the historical. Link these to the pipe-table.

Use a view to links a pipe to its most recent geometry. Add this view to the gpkg_contents table.

Table Design
************

.. image:: ../img/mgimage001.png

View Design
***********

::
  
  CREATE VIEW pipes_current AS 
  SELECT shape, max(date_created), type
  FROM pipe_history as A JOIN pipes as B 
  ON A.pipe_id=B.pipe_id 
  GROUP BY B.pipe_id;						

Table Entries
*************

.. list-table:: Table 1: ``gpkg_contents``
   :widths: 20 15 15 40 10
   :header-rows: 1
   
  * - ``table_name``
    - ``data_type``
    - ``identifier``
    - ``description``
    - ``srs_id``
  * - pipe_history
    - features
    - pipe_history
    - pipe edits
    - 4326
  * - pipes_current
    - features
    - pipes_current
    - current pipes
    - 4326

.. list-table:: Table 2: ``gpkg_geometry_columns``
   :widths: 20 20 15 15 15 15
   :header-rows: 1

  * - ``table_name``
    - ``column_name``
    - ``geometry_type_name``
    - ``srs_id``
    - ``z``
    - ``m``
  * - pipe_history
    - shape
    -	Geometry
    -	4326
    -	2
    -	2
  * - pipes_current	
    - shape	
    - Geometry	
    - 4326	
    - 2	
    - 2

Features consisting of multiple components
------------------------------------------

Example use case
****************
You need to model a feature that has multiple geometries. Associated with this main feature, are ancillary features, each which its own properties and shape. For example, the main feature is a park with a polygon boundary. Associated with this park are entrances, which are modeled as points.

Proposed Solution
*****************
Store the main features separately from the ancillary features. This allows you to associate different metadata with each feature/subfeature.

The park – boundary + entrances – can be tied together by using a view. This provides the “overview” picture, which remodels the park as a collection of geometries.

Table Design
************

.. image:: ../img/mgimage002.png

View Design
***********

*Note: This statement uses the ST_\* functions from the GPKG SQLite extension (cf. https://bitbucket.org/luciad/libgpkg)*

::

  CREATE VIEW park_complete AS 
  SELECT A.park_id, ST_GeomFromText('GEOMETRYCOLLECTION(' || ST_AsText(A.shape) || ',' || group_concat(ST_AsText(B.shape)) ||')')  as shape
  FROM park_json as A 
  JOIN park_entrances_json as B 
  ON A.park_id = B.park_id
  GROUP BY A.park_id;

Table Entries
*************

.. list-table:: Table 3: ``gpkg_contents``
   :widths: 20 15 15 40 10
   :header-rows: 1
   
  * - ``table_name``
    - ``data_type``
    - ``identifier``
    - ``description``
    - ``srs_id``
  * - park
    - features
    -	park
    -	Park boundaries
    -	4326
  * - park_entrances
    -	features
    -	park_entrances
    -	Park entrances
    -	4326
  * - park_complete
    -	features
    -	park_complete
    -	association of park boundary with entrances
    -	4326

.. list-table:: Table 4: ``gpkg_geometry_columns``
   :widths: 20 20 15 15 15 15
   :header-rows: 1

  * - ``table_name``
    - ``column_name``
    - ``geometry_type_name``
    - ``srs_id``
    - ``z``
    - ``m``
  * - park
    - shape
    -	Geometry
    -	4326
    -	2
    -	2
  * - park_entrance
    - shape
    -	Geometry
    -	4326
    -	2
    -	2
  * - park_complete
    -	shape
    -	Geometry
    -	4326
    -	2
    -	2

Features that have multi-resolution
-----------------------------------

Example use case
****************
For efficiency reasons, it is often desirable to have the same feature represented by different geometries of varying resolution. This is typically used for features with large extents, such as roads, rivers, municipal boundaries, etc …. The viewer application shows the coarser version of geometries at smaller scales (ie. zoomed out), while at larger scales (ie. zoomed in) it shows the most detailed version. In general, you would define a handful of scale-breaks upfront.

Proposed Solution
***************** 
Suppose we have multiple resolutions for roads in a road dataset:

* Store all geometries in a table, separate from the properties of the road. Associate with each geometry the scale-break for which it applies. In our example, we are using the [min|max]scale_denominator columns to store the scale-break values.

* A view joins together the properties with the geometries. This view will in effect contain many duplicates and should not be rendered as-is.

This solution requires the viewer-application to apply the correct filtering, relying on the min-max scale associated with the geometry. That is, the application only renders the geometries which are appropriate for each scale-break. This is an application-level requirement, unrelated to the GeoPackage format, and the implementation depends on the particular product you would be using. For products that support SLD, this scale-based filtering is fairly straightforward. In your FeatureTypeStyle, create multiple rules, one for each scale-break on the map. In each rule, filter all the geometries that do not correspond to the desired scalebreak.

For example, in SLD, a rule to only show the roads with a coarse resolution (zoomed out) would look something like this:

::

  <Rule>
    <Name>small scale</Name>
    <Description>
      <Title>small scaled roads</Title>
      <Abstract>shows only the low resolution roads</Abstract>
    </Description>
    <ogc:Filter>
      <ogc:PropertyIsGreaterThan>
        <ogc:PropertyName>min_scale_denominator</ogc:PropertyName>
        <ogc:Literal>2.0E8</ogc:Literal>
      </ogc:PropertyIsGreaterThan>
    </ogc:Filter>
    <MinScaleDenominator>2.0E8</MinScaleDenominator>
    <LineSymbolizer>
      <Stroke>
        <SvgParameter name="stroke">#0000ff</SvgParameter>
        <SvgParameter name="stroke-width">2</SvgParameter>
      </Stroke>
    </LineSymbolizer>
  </Rule>

Table Design
************

.. image:: ../img/mgimage003.png

View Design
***********

::
  
  CREATE VIEW  roads_all AS 
  SELECT  *
  FROM road as A 
  JOIN road_geometries as B 
  ON A.road_id = B.road_id						

Table Entries
*************

.. list-table:: Table 5: ``gpkg_contents``
   :widths: 20 15 15 40 10
   :header-rows: 1
   
  * - ``table_name``
    - ``data_type``
    - ``identifier``
    - ``description``
    - ``srs_id``
  * - road_geometries
    -	features
    - road_geometries
    -	Multiple resolution for road geometries
    -	4326
  * - roads_all
    -	features
    -	roads_all
    -	Multiple resolutions for road geometries, associated with properties of the roads	
    - 4326

.. list-table:: Table 6: ``gpkg_geometry_columns``
   :widths: 20 20 15 15 15 15
   :header-rows: 1

  * - ``table_name``
    - ``column_name``
    - ``geometry_type_name``
    - ``srs_id``
    - ``z``
    - ``m``
  * - road_geometries
    -	shape
    -	Geometry
    -	4326
    -	2
    -	2
  * - roads_all
    -	shape
    -	Geometry
    -	4326
    -	2
    -	2
