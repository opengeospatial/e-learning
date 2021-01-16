WMS - Introduction
==================

Introduction
------------
The OGC Web Map Service Interface Standard (WMS) defines a set of interfaces for requesting map images over the Internet. WMS makes it easy for a client to request images on demand changing parameters such as size and coordinate reference systems. A WMS server (i.e. a service that implements the WMS standard) provides information about what maps the service provides, and it produces a map and answers queries about content the content of a map.


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

This `OGC WMS Demo server <https://ows.terrestris.de/osm/service?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3>`_ publishes maps created by Terrestris from OpenStreetMap data.

The ``GetMap`` request queries the server with a set of parameters describing the map image. The values of the parameters are taken from the Capabilities document. A correctly formulated ``GetMap`` request will create the image shown below.

.. image:: ../img/getmap-demo.png
      :width: 70%



The URL of this link is composed of the following parameters and values:


.. code-block:: properties

      https://ows.terrestris.de/osm/service?
      REQUEST=GetMap&
      SERVICE=WMS&
      VERSION=1.3.0&
      LAYERS=OSM-WMS&
      STYLES=&
      CRS=EPSG:4326&
      BBOX=51.49451,-0.11377,51.53267,-0.06971&
      WIDTH=400&
      HEIGHT=300&
      FORMAT=image/png&
      TRANSPARENT=TRUE

`Link to the GetMap request <https://ows.terrestris.de/osm/service?REQUEST=GetMap&SERVICE=WMS&VERSION=1.3.0&LAYERS=OSM-WMS&STYLES=&CRS=EPSG:4326&BBOX=51.49451,-0.11377,51.53267,-0.06971&WIDTH=400&HEIGHT=300&FORMAT=image/png&TRANSPARENT=TRUE>`_


Client Usage
------------

A client needs to know the location of the WMS service to be able to interact with the server. The location is usually called the 'end point' of the service. The end point is the URI for the GetCapabilities request. For example:


The URL of this link is composed of the following parameters and values:

.. code-block:: properties

  https://ows.terrestris.de/osm/service?
  REQUEST=GetCapabilities&
  SERVICE=WMS&
  VERSION=1.3

`Link to the GetCapabilities request <https://ows.terrestris.de/osm/service?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3>`_


References
----------

`Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
