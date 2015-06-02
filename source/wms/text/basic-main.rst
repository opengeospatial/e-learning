WMS - Introduction
==================

Introduction
------------
The OGC Web Map Server (WMS) defines a set of interfaces for requesting map images over Internet. 
WMS makes it easy for a client to request images on demand changing parameters such as size and
coordinate reference systems. A WMS Server provides information about what maps can the service
provides, produces a map and answers queries about content of a Map.


History
  WMS version 1.0.0 in April 2000, followed by version 1.1.0 in June 2001,and version 1.1.1 in January 2002. The OGC released WMS version 1.3.0 in January 2004.
Versions
  1.3 is the current latest version 
Test Suite
  Test suites exist for: 
      - `WMS 1.1.1 <http://cite.opengeospatial.org/teamengine/>`_ 
      - `WMS 1.3.0 <http://cite.opengeospatial.org/teamengine/>`_
Implementations
   Implementations can be found at the OGC database. `here <http://www.opengeospatial.org/resource/products/byspec>`_

Usage
-----
The standard makes map images available and accessible through a highly configurable interface 
in standard image formats. Government agencies publish all kinds of official map cartography 
using this standard. Other large organizations use this standard to enable independent departments 
to interact more easily internally. Anybody using this standard can use it to overlay map data 
from many different sources regardless of the underlying software.


Relation to other OGC Standards
-------------------------------

- Web Map Tile Server (WMTS): For highly scalable systems which only need static maps the WMTS standard is a better fit. It complements the WMS standard with cachable static map tiles. WMS server can be used as data sources / rendering engines for WMTS.
- Web Feature Service (WFS): For extended query functionality of map content the WFS standard is a better fit. It complements the WMS by giving access to geographic features of the same map. WMS and WFS often go together. Having two separate endpoints allows to easily separate map and feature access to different user groups.
- Styled Layer Descriptor: This standard allows the user to modify the cartographic appearance of a map image. It is an optional feature of the OGC WMS standard.
- Symbology Encoding: This standard describes hwo to define map symbology and is used modify the cartographic appearance of map images. It is an optional feature of the OGC WMS and SLD standards.


WMS Operations
--------------

WMS specifies a number of different request types, two of which are required by any WMS server:

GetCapabilities
   returns metadata about the WMS request and parameters (such as map image format and WMS version compatibility) and the available layers (map bounding box, coordinate reference systems, URI of the data and whether the layer is mostly opaque or not)
GetMap
   returns a map image. Parameters include: width and height of the map, coordinate reference system, rendering style, image format

Request types that WMS providers may optionally support include:

GetFeatureInfo
   if a layer is marked as 'queryable' then you can request data about a coordinate of the map image.
DescribeLayer
   gets corresponding WFS to retrieve additional information about the layer
GetLegendGraphic
   return an image of the map's legend image, giving a visual guide to map elements
   
   

Example
-------

This `OGC WMS Demo server <http://metaspatial.net/cgi-bin/ogc-wms.xml?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3>`_ provides data from Great Britain and provide by the Ordnance Survey.

The ``GetMap`` request queries the server with a set of parameters describing the map image. The values of the parameters are taken from the Capabilities document. A correctly formulated ``GetMap`` request will create the image shown below. 

.. image:: ../img/getmap-demo.png
      :width: 70%


*The URL of this link has been truncated for better readability.*::

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
  TRANSPARENT=TRUE&

Use the link: `GetMap <http://metaspatial.net/cgi-bin/ogc-wms.xml?VERSION=1.3.0&REQUEST=GetMap&SERVICE=WMS&LAYERS=DTM,Overview,Raster_250K,Topography,nationalparks,Infrastructure,Places&STYLES=,,,,,,&CRS=EPSG:27700&BBOX=424735.97883597884,96026.98412698413,467064.02116402116,127773.01587301587&WIDTH=400&HEIGHT=300&FORMAT=image/png&BGCOLOR=0xffffff&TRANSPARENT=TRUE&EXCEPTIONS=XML>`_ to retrieve the map image form the Demo Server. It will be rendered dynamically each time you request the image (given that no proxy interferes and delivers an earlier graphic rendition of the map data).



Client Usage
------------

To use a WMS service in a client you need the end point of the service. For example this GetCapabilities request: http://metaspatial.net/cgi-bin/ogc-wms.xml?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3
