Using the QGIS Application
==========================

There are several different ways to create and read a GeoPackage. Most of the implementing software products have their own unique way of supporting the handling of a GeoPackage. In this chapter we will show how a GeoPackage can be read using the free and open source QGIS application that can be found at https://www.qgis.org/en/site/. 

In QGIS, open the states10.gpkg file, through the vector file loader button.

.. image:: ../img/open_states10.png
   :height: 327
   :width: 560

Once QGIS has loaded the GeoPackage, it will display US state boundaries. As a GeoPackage reader, QGIS is able to read the geometries, spatial reference system and other geospatial content.

.. image:: ../img/view_states10.png
   :height: 327
   :width: 560

Now we will have a look at the feature properties. Right click on the layer name (which is displayed as statesQGIS) and select Open Attribute Table from the pop-up menu.

.. image:: ../img/open_attribute_table.png
   :height: 327
   :width: 560

The properties of all features in the statesGIS dataset are displayed in an attribute table. The data can now be queried and modified like any other feature dataset in a desktop GIS.

.. image:: ../img/view_attribute_table.png
   :height: 327
   :width: 560
