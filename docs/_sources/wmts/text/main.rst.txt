WMTS - Introduction
===================

Introduction
------------
The OGC `Web Map Tile Service Implementation Standard (WMTS) <http://www.opengeospatial.org/standards/wmts>`_ defines a set of interfaces for making web-based requests of map tiles of spatially referenced data using tile images with predefined content, extent, and resolution. The standard includes the WMTS Specification ("WMTS Spec") `07-057r7 OpenGIS Web Map Tile Service Implementation Standard <http://www.opengeospatial.org/standards/wmts>`_ along with collateral documentation such as profiles and XML documents.

WMTS complements the OGC `Web Map Service interface standard (WMS) <http://www.opengeospatial.org/standards/wms>`_ for the web based distribution of cartographic maps. WMS focuses on flexibility in the client request enabling clients to obtain exactly the final image they want. While WMS focuses on rendering custom maps and is well-suited for dynamic data or custom styled maps, WMTS trades the flexibility of custom map rendering for the scalability made possible by serving static data (base maps) where the bounding box and scales have been constrained to discrete tiles. The fixed set of tiles allows for the implementation of a WMTS service using a web server that simply returns existing files. The fixed set of tiles also enables the use of standard network mechanisms for scalability such as distributed cache systems.

WMS servers can also be used as data sources or rendering engines for WMTS services. Similarly, the `OGC Web Feature Service Interface Standard (WFS) <http://www.opengeospatial.org/standards/wfs>`_ is a better fit for extended query functionality of spatial data. It provides programmatic access to the geographic feature data. An organization publishing both WMS and WFS often use the same data source.

Overview of WMTS Operations
---------------------------

WMTS specifies several operation types, two of which are required in a compliant WMTS implementation, and another which is optional.

GetCapabilities
   The GetCapabilities response is characterized in a "ServiceMetadata" document, which describes how to identify WMTS resources or generate WMTS request operations. The primary content of the metadata is TileMatrixSet summary information and detailed content such as bounding box, supported coordinate reference system (CRS), whether a well-known scale set is available, and TileMatrix data about any of a number of levels. An optional "Themes" section, when present, obviates the need to specify any inheritance rules for layer properties. Under a resource-oriented architectural style, an appropriate resource name such as "WMTSCapabilities.xml" would be chosen.

GetTile
   The GetTile operation under a procedural-oriented architectural style allows WMTS clients to take the information from the GetCapabilities response to request a particular Tile of a particular TileMatrixSet in a predefined format. Under the resource-oriented style, the client merely requests the representation of any offered Tile resource by performing a request to the address following the standard semantics of the transport protocol.

(Optional) GetFeatureInfo
   GetFeatureInfo requests may be made about the features at or near a particular pixel location. Requests must specify the tile along with a pixel location on that tile, and the WMTS server may choose which information to provide about nearby features. `WMTS Clause 7.3.1 <http://www.opengeospatial.org/standards/wmts>`_ recommends Level 0 of the `Geography Markup Language (GML) Simple Features Profile <http://portal.opengeospatial.org/files/?artifact_id=42729>`_ as the supported document format for FeatureInfo resources.


Example GetTile Request
-----------------------

The ``GetTile`` request queries the server with a set of parameters describing the map tile image. The values of these parameters are taken from a WMTS Capabilities document. A correctly formulated ``GetTile`` request will create the image shown below.

.. image:: ../img/wmts100.png
      :width: 30%

The URL of this link is composed of the following parameters and values:

.. code-block:: properties

  http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?
  SERVICE=WMTS&
  REQUEST=GetTile&
  VERSION=1.0.0&
  LAYER=cite&
  STYLE=default&
  FORMAT=image/png&
  TILEMATRIXSET=InspireCrs84Quad&
  TILEMATRIX=11&
  TILEROW=431&
  TILECOL=2107

`Link to the corresponding GetTile request <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cite&STYLE=default&FORMAT=image/png&TILEMATRIXSET=InspireCrs84Quad&TILEMATRIX=11&TILEROW=431&TILECOL=2107>`_.

Client Usage
------------

A client needs to know the web location of the WMTS service, typically called the service 'endpoint'. The endpoint is the URL for the GetCapabilities request. For example, a typical URL might be composed of the following parameters and values:

.. code-block:: properties

  http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?
  service=WMTS&
  request=GetCapabilities

`Link to the corresponding GetCapabilities request <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?service=WMTS&request=GetCapabilities>`_.


References
----------

`Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
