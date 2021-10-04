Exercise WMS - UK Metaspatial Server
========================================

GetMap - Exercise (5 points)
---------------------------
1. Name 5 layers available in the UK WMS Server example 
2. Name the style for the **National Parks** layer 
3. What is the coordinate system the client is using to do the request?
4. Change the request and perform a query using `WGS84 <http://spatialreference.org/ref/epsg/wgs-84/>`_ and getting the image as GIF.

..
   http://metaspatial.net/cgi-bin/ogc-
   wms.xml?VERSION=1.3.0&REQUEST=GetMap&SERVICE=WMS&LAYERS=DTM,Overvie
   w,Raster_250K,Topography,Infrastructure,Places&STYLES=,,,,,,&
   CRS=EPSG:4326&BBOX=50.76,-1.65,51.045,-
   1.045&WIDTH=400&HEIGHT=300&FORMAT=image/png&BGCOLOR=0xffffff&TRANSP
   ARENT=TRUE

GetFeatureInfo - Exercise (5 points)
-----------------------------------
1. Do a getFeatureInfo to get more details about a park from the **National Parks** layer 
2. What is the name of the point located in the pixel where: X=231 and Y=290?

..
   Clay Hill Cattle Grid
   bus stop



   