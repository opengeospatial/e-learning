.. include:: ../cover.rst 

Coordinates in WMS
------------------
- BBOX specifies minx,miny,maxx,maxy 
- **x** and **y** are the axes based of the CRS
- What x and y are depends on the CRS
- X is usually Axis 1 or Mayor Axis
- Y is usually Axis 2 or Minor Axis


Where to get Axes information
-----------------------------

- `EPSG <http://www.epsg-registry.org>`_
- `WMS 1.3 Standard (OGC 06-042) Annex B <http://portal.opengeospatial.org/files/?artifact_id=14416>`_

EPSG:4326 Report
----------------
.. image:: ../img/epsg4326-report.jpg
      :width: 50%
  
`Link to EPSG Report <http://www.epsg-registry.org/report.htm?type=selection&entity=urn:ogc:def:crs:EPSG::4326&reportDetail=long&style=urn:uuid:report-style:default-with-code&style_name=OGP%20Default%20With%20Code&title=>`_

EPSG:4326 - Axes Order
----------------------
The report specifies the order of the Axes

.. image:: ../img/epsg4326-axes-order.jpg
      :width: 70%
      
So:

- X is Latitude
- Y is Longitude      
      
CRS:84- Axes Order
------------------

.. image:: ../img/crs84-axes-order.jpg
      :width: 60%

CRS:84- Axes Order
------------------
   
.. image:: ../img/crs84-axes-order2.jpg
      :width: 90%
    
So:

- X is Longitude
- Y is Latitude   


Request WMS 1.3 BBOX
--------------------

- The Axes order in WMS are minx,miny,maxx,maxy. 
- US Bounds are:

   - Longitude -178 to -66
   - Latitude 18 to 71


Using EPSG:4326 

.. code-block:: properties

      CRS=EPSG:4326&BBOX=18,-178,71,-66
      
Using CRS:84  
   
.. code-block:: properties

      CRS=CRS:84&BBOX=-178,18,-66,71 








       


  
  
      

