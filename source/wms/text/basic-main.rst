WMS - Introduction
==================

Introduction
------------
The OGC Web Map Service Interface Standard (WMS) defines a set of interfaces for requesting map images over the Internet. WMS makes it easy for a client to request images on demand changing parameters such as size and coordinate reference systems. A WMS server (i.e. a service that implements the WMS standard) provides information about what maps the service provides, and it produces a map and answers queries about content the content of a map.


History
  WMS version 1.0.0 in April 2000, followed by version 1.1.0 in June 2001,and version 1.1.1 in January 2002. The OGC released WMS version 1.3.0 in January 2004.
Versions
  1.3 is the current latest version 
Test Suite
  Test suites are available for: 
      - `WMS 1.1.1 <http://cite.opengeospatial.org/teamengine/>`_ 
      - `WMS 1.3.0 <http://cite.opengeospatial.org/teamengine/>`_
Implementations
   Implementations can be found at the OGC database. `here <http://www.opengeospatial.org/resource/products/byspec>`_

Usage
-----
Through a highly configurable interface the WMS standard makes map images (but not source data) available in standard image formats. Government agencies publish all kinds of official map cartography using this standard. Other large organizations use this standard to enable independent departments to interact more easily internally. Anybody using this standard can use it to overlay map images from many different sources regardless of the underlying software.

WMS provides a standard interface for requesting a geospatial map image.  The benefit of this is that WMS clients can request images from multiple WMS servers, and then combine them into a single view for the user.  The standard guarantees that these images can all be overlaid on one another using a common geospatial coordinate reference system.  Numerous servers and clients support WMS.


Relation to other OGC Standards
-------------------------------

- OGC Web Map Tile Service Interface Standard (WMTS): The WMTS standard is a better fit For highly scalable systems (many simultaneous requests) that only need static maps. It complements the WMS standard with cachable static map tiles. WMS servers can be used as data sources or rendering engines for WMTS services.
- OGC Web Feature Service (WFS): The WFS standard is a better fit for extended query functionality of spatial data. It provides programmatic access to the geographic feature data. WMS and WFS often go together. An organization publishing both WMS and WFS often use the same data source.
- OGC Styled Layer Descriptor Interface Standard (SLD): The SLD standard allows the user to modify the cartographic appearance of a map image. It is an optional feature of the OGC WMS standard.
- OGC Symbology Encoding (SE): The SE standard describes how to define map symbology. It is used to modify the cartographic appearance of map images. It is an optional feature of the OGC WMS and SLD standards.


Overview of WMS Operations
----------------------------

WMS specifies a number of different request types, two of which are required by any WMS server:

GetCapabilities
   Returns metadata about a WMS server, including how to generate WMS requests and what parameters can be used. The metadata includes supported image formats and the availability of layers. Metadata for each layer include: bounding box, coordinate reference system, URI of the data and whether the layer is mostly opaque or not.
GetMap
   Returns a map image. Parameters specified in the GetMap request include: width and height of the map, coordinate reference system, rendering style and image format.

Optional WMS operations include:

GetFeatureInfo
   Returns information (e.g. data) associated to a coordinate of the map image. The layer supporting this operation is marked as 'queryable'.
DescribeLayer
   Returns additional information about the requested layer.
GetLegendGraphic
   Returns a legend, as an image, for the map image, providing a visual guide to the map elements.
   
   

Example
-------

This `OGC WMS Demo server <http://metaspatial.net/cgi-bin/ogc-wms.xml?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3>`_ publishes data from Great Britain provided by the Ordnance Survey.

The ``GetMap`` request queries the server with a set of parameters describing the map image. The values of the parameters are taken from the Capabilities document. A correctly formulated ``GetMap`` request will create the image shown below. 

.. image:: ../img/getmap-demo.png
      :width: 70%


The URL of this link has been truncated for better readability.
  

.. code-block:: properties

      http://metaspatial.net/cgi-bin/ogc-wms.xml?
      VERSION=1.3.0& 
      REQUEST=GetMap& 
      SERVICE=WMS& 
      LAYERS=DTM,Overview,Raster_250K,Topography,nationalparks,Infrastructure,Places& 
      STYLES=,,,,,,& 
      CRS=EPSG:27700& 
      BBOX=424735.97883597884,96026.98412698413,467064.02116402116,127773.01587301587& 
      WIDTH=400& 
      HEIGHT=300& 
      FORMAT=image/png&
      BGCOLOR=0xffffff& 
      TRANSPARENT=TRUE
  

`Get Map Link <ttp://metaspatial.net/cgi-bin/ogc-wms.xml?VERSION=1.3.0&REQUEST=GetMap& SERVICE=WMS& LAYERS=DTM,Overview,Raster_250K,Topography,nationalparks,Infrastructure,Places& STYLES=,,,,,,& CRS=EPSG:27700&BBOX=424735.97883597884,96026.98412698413,467064.02116402116,127773.01587301587& WIDTH=400& HEIGHT=300&FORMAT=image/png& BGCOLOR=0xffffff& TRANSPARENT=TRUE>`_



Client Usage
------------

A client needs to know the location of the WMS service to be able to interact with the server. The location is usually called the 'end point' of the service. The end point is the URI for the GetCapabilities request. For example: 

.. code-block:: properties
  
  http://metaspatial.net/cgi-bin/ogc-wms.xml?
  REQUEST=GetCapabilities&
  SERVICE=WMS&
  VERSION=1.3

`Link <http://metaspatial.net/cgi-bin/ogc-wms.xml?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3>`_  


References
----------

`GeoServer  WMS reference <http://docs.geoserver.org/stable/en/user/services/wms/reference.html>`_ - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_



