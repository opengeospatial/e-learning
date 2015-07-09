WEB Map Service (WMS)
=====================

This tutorial provides a practical introduction to OGC Web Map Service (WMS) Interface standard.

Goals
-----
- Understand what WMS can be used for
- Understand WMS requests and best practices

Web Map Service (WMS)
---------------------
The latest version of WMS is 1.3.0 [#ogc-06-042].

A WMS Server:

- Provides information about what maps a service can produce
- Produces a Map
- Answers queries about content of a Map


WMS Operations
--------------
- **GetCapabilities**
- **GetMap**
- **GetFeatureInfo** (Optional) - gets underlying data (vector) and attributes for a given pixel 
- **DescribeLayer** (Optional) - gets corresponding WFS to retrieve additional information about the layer
- **GetLegendGraphic** (Optional) - gets the legend for a map

WMS Exceptions
--------------

What if something goes wrong?

How will the service let me know?

WMS Exceptions
--------------

XML
    EXCEPTIONS=application/vnd.ogc.se_xml
PNG
    EXCEPTIONS=application/vnd.ogc.se_inimage
Blank
    EXCEPTIONS=application/vnd.ogc.se_blank
JSON
    EXCEPTIONS=application/json
    

WMS Examples
------------
The examples are based on a local installation of GeoServer http://geoserver.org/

Instructions `here <http://live.osgeo.org/en/quickstart/geoserver_quickstart.html>`_

`WMS support in GeoServer <http://docs.geoserver.org/stable/en/user/services/wms/reference.html>`_

WMS GetCapabilities
-------------------
Request example:

.. code-block:: properties

   http://localhost:8080/geoserver/topp/wms?
   service=WMS&
   version=1.3.0&
   request=GetCapabilities


`Link <http://localhost:8080/geoserver/topp/wms?service=WMS&version=1.3.0&request=GetCapabilities>`_

 
WMS GetCapabilities Response
----------------------------
Provides information about:
 
-  How to invoke GetMap 
-  Types of exceptions
-  List of layers

WMS GetMap Parameters
---------------------
service
    *WMS*
version
    *1.0.0, 1.1.0, 1.1.1, 1.3.*
request 
    *getMap*
layers
    comma separated list of layers map    
styles
    comma separated list of styles for each layer     
    
    
WMS GetMap Parameters
---------------------
srs or crs
    Value is in form EPSG:nnn. crs is the parameter key used in WMS 1.3.0.
bbox
    Bounding box for map extent. Value is minx,miny,maxx,maxy in units of the SRS.
width
    Width of map output, in pixels.
height
    Height of map output, in pixels.            

WMS GetMap Parameters
---------------------
format
    Format for the map output. 
    
      Examples:

      - format=image/png
      - format=image/png8
      - format=image/png8
      - format=application/pdf  
      - format=kmz

Optional WMS GetMap Parameters
------------------------------
transparent
    true or false
bgcolor
    Background color for the map image in RRGGBB (e.g. FFFFFF)
exceptions
    For example: EXCEPTIONS=application/vnd.ogc.se_xml
time
    time in ISO8601. For example: TIME=2001-12-12T18:00:00.0Z
sld
    A URL referencing a Styled Layer Descriptor XML file for map styling.



WMS GetMap
----------


`Request example: <http://localhost:8080/geoserver/wms?bbox=-130,24,-66,50&styles=population&Format=image/png&request=GetMap&layers=topp:states&width=550&height=250&srs=EPSG:4326>`_


.. code-block:: properties
	
   http://localhost:8080/geoserver/wms?
      bbox=-130,24,-66,50&
      styles=population&
      Format=image/png&
      request=GetMap&
      layers=topp:states&
      width=550&height=250&
      srs=EPSG:4326




WMS GetFeatureInfo
------------------

`Request example: <http://localhost:8080/geoserver/wms?bbox=-130,24,-66,50&styles=population&format=jpeg&info_format=text/plain&request=GetFeatureInfo&layers=topp:states&query_layers=topp:states&width=550&height=250&x=170&y=160>`_

.. code-block:: properties


   http://localhost:8080/geoserver/wms?
   bbox=-130,24,-66,50&
   styles=population&
   format=jpeg&
   info_format=text/plain&
   request=GetFeatureInfo&
   layers=topp:states&
   query_layers=topp:states&
   width=550&
   height=250&
   x=170&
   y=160




 
WMS GetLegendGraphic
--------------------
Optional request, provided by WMSs that support SLD

`Request example: <http://localhost:8080/geoserver/topp/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=states>`_

.. code-block:: properties

   http://localhost:8080/geoserver/topp/ows?
   service=WMS&
   request=GetLegendGraphic&
   format=image%2Fpng&
   width=20&
   height=20&
   layer=states




