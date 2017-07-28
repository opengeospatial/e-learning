
WMTS - Introduction
======================

Introduction
------------
The OGC `07-057r7 OpenGIS Web Map Tile Service Implementation Standard (WMTS) <http://www.opengeospatial.org/standards/wmts>`_ defines a set of interfaces for making web-based requests of map tiles of spatially referenced data using tile images with predefined content, extent, and resolution.

WMTS complements the OGC Web Map Service interface standard (WMS) for the web based distribution of cartographic maps. While WMS focuses on rendering custom maps and is an ideal solution for dynamic data or custom styled maps, particularly when combined with the OGC Style Layer Descriptor (SLD) standard, WMTS trades the flexibility of custom map rendering for the scalability made possible by serving static data (base maps) where the bounding box and scales have been constrained to discrete tiles. The fixed set of tiles allows for the implementation of a WMTS service using a web server that simply returns existing files. The fixed set of tiles also enables the use of standard network mechanisms for scalability such as distributed cache systems.


History and Versions
--------------------

WMTS built on earlier efforts to develop scalable, high performance services for web based distribution of cartographic maps. WMTS was inspired by the `OSGeo Tile Map Service Specification <http://wiki.osgeo.org/index.php/Tile_Map_Service_Specification>`_. Similar initiatives such as Google maps and NASA OnEarth were also considered. The standard included both a resource (RESTful approach) and procedure oriented architectural styles (KVP and SOAP encoding) in an effort to harmonize this interface standard with the OSGeo specification.

While developing a profile of WMS was initially considered, limiting a WMS in the ways important to allow efficient access to cacheable tiles proved awkward while forcing implementors to read both a standard and a profile seemed less efficient than developing a standalone specification.

WMTS version 1.0.0 was released in 2007, and the Web Map Tile Service Simple Profile was released in 2013.


Test Suite
----------

A beta version of the `OGC Web Map Tile Service 1.0.0 - Executable Test Suite <http://cite.opengeospatial.org/te2/about/wmts/1.0.0/site>`_ was available as of July 2017. Updates can be found at the `OGC Compliance Program Available Tests and Roadmap <http://cite.opengeospatial.org/roadmap>`_.


Implementations
---------------

Information regarding WMTS implementations can be found under `OGC Implementation Statistics <http://www.opengeospatial.org/resource/products/byspec>`_.


Usage
-----

WMTS provides a standards-based solution to serve digital maps using predefined image tiles. The service advertises the tiles it has available through a standardized declaration in the ServiceMetadata document common to all OGC web services. This declaration defines the tiles available in each layer (i.e. each type of content), in each graphical representation style, in each format, in each coordinate reference system, at each scale, and over each geographic fragment of the total covered area. The ServiceMetadata document also declares the communication protocols and encodings through which clients can interact with the server. Clients can interpret the ServiceMetadata document to request specific tiles.

The WMTS standard complements the existing Web Map Service standard of the OGC. The WMS standard focuses on flexibility in the client request enabling clients to obtain exactly the final image they want. A WMS client can request that the server creates a map by overlaying an arbitrary number of the map layers offered by the server, over an arbitrary geographic bound, with an arbitrary background color at an arbitrary scale, in any supported coordinate reference system. The client may also request that the map layers be rendered using a specific server advertised style or even use a style provided by the client when the WMS server implements the OGC Styled Layers Descriptor (SLD) standard. However, all this flexibility comes at a price: server image processing must scale with the number of connected clients and there is only limited potential to cache images between the server and client since most images are different.

As web service clients have become more powerful, it has become possible to consider an alternative strategy by which a client requests pre-defined map image tiles. Though these tiles might not be exactly at the desired positions, the client and can perform image overlays themselves, clipping and mosaicking the provided tiles into a final image. This approach enables servers to scale based on communication processing abilities rather than image processing abilities because servers can pre-render some or all of their images and utilize image caching strategies. The fixed set of images also enables network providers to cache images between the client and the server, reducing latency and bandwidth use.

Prior to WMTS, some WMS server providers had developed their own tiling structures built by constraining WMS GetMap requests to a fixed set and then advertising those constraints in their service metadata. Although this mechanism enabled those servers to scale as just described, the tiling structure and the advertising and discovery mechanisms were not standardized, forcing a specialized client interface for each service.

WMTS offers a standardized approach to declaring the images which a client can request from a server, enabling a single type of client to be developed for all servers.


Relationship to Other OGC Standards
-----------------------------------

- The `OGC Web Map Service Interface Standard (WMS) <http://www.opengeospatial.org/standards/wms>`_ is a better fit for rendering custom maps and provides an ideal solution for dynamic data or custom styled maps, particularly when combined with the OGC Style Layer Descriptor (SLD) standard. WMS servers can be used as data sources or rendering engines for WMTS services.

- The `OGC Web Feature Service Interface Standard (WFS) <http://www.opengeospatial.org/standards/wfs>`_ is a better fit for extended query functionality of spatial data. It provides programmatic access to the geographic feature data. An organization publishing both WMS and WFS often use the same data source.


Overview of WMTS Resources and Operations
-----------------------------------------

A WMTS abstract specification describes the semantics of the resources offered by the servers and requested by the client. It specifies the semantics of the ServiceMetadata document, of the Tile images or representations, and of the optional FeatureInfo documents providing descriptions of the maps at specific locations.

Client-server exchange mechanisms are specified under two distinct architectural styles. Under the first "procedural-oriented" style, the GetCapabilities, GetTile and optional GetFeatureInfo operations use the encodings of Key-Value Pairs (KVP), "plain-old XML" (POX) messages, or XML messages embedded in SOAP envelopes. Under the second "resource-oriented" style, request mechanisms and an endpoint publishing strategy are specified to enable an style more closely resembling that of `REpresentational State Transfer (REST) <http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_, particularly `Richardson Maturity Model Level 1 <http://docs.opengeospatial.org/guides/16-057r1.html#_rest_and_open_geospatial_resources>`_. This approach is based on web URL endpoints that enable clients to simply request the ServiceMetadata, Tile, and FeatureInfo resources as documents.

It should be noted that while KVP, POX, and SOAP are more commonly found under the procedural-oriented style, they `could theoretically also be utilized in resource-oriented approach <https://www.innoq.com/blog/st/2006/11/soap-vs.-pox-vs.-rest/>`_.

Under a resource-oriented pattern, a scalable WMTS service could be created using no image processing logic at all by pre-rendering images and relying only on an ordinary web server to return the static ServiceMetadata XML document and provide the image tile files. The images are considered by the HTTP protocol to be standard web resources, and providers could leverage their existing technologies to improve the flow of those resources to requesting clients.

Whichever style is used, WMTS-enabled services can generally offer advantages in performance and scalability by dividing maps into individual tiles that can be returned quickly. Performance can be enhanced by utilizing locally stored, pre-rendered tiles that will not require any image manipulation or geoprocessing. With tile-based mapping it is important that servers be able to handle asynchronous access to tiles, as most clients will simultaneously request multiple tiles to fill a single view.

The WMTS interface allows a client to retrieve three general types of resources:

ServiceMetadata resource
   A ServiceMetadata resource (in response to a GetCapabilities operation under the procedural-oriented architectural style) is required in compliant implementations. It describes the abilities and information holdings of the specific server implementation. This operation also supports negotiation of the standard version being used for client-server interactions.

Tile resource
   A Tile resource (in response to a GetTile operation under the procedural-oriented architectural style) is required in compliant implementations. It shows a fragment of a map representation of a layer.

FeatureInfo resource
   A FeatureInfo resource (in response to a GetFeatureInfo operation under the procedural-oriented architectural style) is optional. It provides information about the features located at a particular pixel of a tile map, in a similar way to the WMS GetFeatureInfo operation, by providing, for example, the thematic attribute name and value pairs in textual form.

The WMTS serves a single tile of a single layer of a map. As illustrated in the following figure, tiles are related in a hierarchy called a "Tile Matrix Set" in which coarser-resolution tiles are nearer the top and finer resolution tiles nearer the bottom.

.. image:: ../img/Tiles.png
      :width: 70%

Unlike WMS, there is no specified way to request a server to combine and return a map tile with information coming from more than one layer in a single fetching process. WMTS clients that want to show a combination of layers must make independent requests for the layer tiles and then combine or overlay the responses. Also bounding boxes and scales of these WMTS tiles are constrained to a discrete set of values.

A full explanation of the geometry of the tiled space can be found in Clause 6.1 of `07-057r7 OpenGIS Web Map Tile Service Implementation Standard <http://www.opengeospatial.org/standards/wmts>`_


Specific WMTS Resources and Operations
--------------------------------------

WMTS specifies several resource and request operation types, two of which are required in a compliant implementation (GetCapabilities and GetTile) and another which is optional (GetFeatureInfo).

GetCapabilities
   The GetCapabilities response is characterized in a "ServiceMetadata" document, which describes how to identify WMTS resources or generate WMTS request operations. The primary content of the metadata is TileMatrixSet summary information and detailed content such as bounding box, supported coordinate reference system (CRS), whether as well-known scale set is available, and TileMatrix data about any of a number of levels. An optional "Themes" section, when present, obviates the need to specify any inheritance rules for layer properties. Under the resource-oriented style, an appropriate resource name such as "WMTSGetCapabilities.xml" would be chosen.

GetTile
   The GetTile operation in procedural-oriented style allows WMTS clients to take the information from the GetCapabilities response and request a particular Tile of a particular TileMatrixSet in a predefined format. Under the resource-oriented style, the client merely requests the representation of any offered Tile resource by performing a request to the address following the standard semantics of the transport protocol.

(Optional) GetFeatureInfo
   GetFeatureInfo requests may be made about the features at or near a particular pixel location. Requests must specify the tile along with a pixel location on that tile, and the WMTS server may choose which information to provide about nearby features. `WMTS Clause 7.3.1 <http://www.opengeospatial.org/standards/wmts>`_ recommends Level 0 of the `Geography Markup Language (GML) Simple Features Profile <http://portal.opengeospatial.org/files/?artifact_id=42729>`_ as a supported document format for FeatureInfo resources.



- - -

GetCapabilities

   NSG Requirement 2: An NSG WMTS server shall declare its support for GetCapabilities operations using KVP with HTTP GET

   NSG Requirement 3: An NSG WMTS server shall generate a ServiceMetadata document in response to a SOAP encoded GetCapabilities request

   NSG Requirement 4: An NSG WMTS server shall generate a ServiceMetadata document in response to a GetResourceRepresentation request in REST architecture


GetTile Requests

   NSG Requirement 5: An NSG WMTS server shall respond to a GetTile operation request with a tile map that complies with the requested parameters

   NSG Requirement 6: An NSG WMTS server shall respond to a SOAP encoded GetTile operation request with an image in the MIME type specified by the Format parameter of the request

   NSG Requirement 7: An NSG WMTS server shall provide standard endpoints from which a representation of each Tile resource can be obtained


GetFeatureInfo Requests

   NSG Requirement 8: An NSG WMTS server shall implement HTTP GET transfer of the GetFeatureInfo operation request using KVP encoding

   KVP encoding of the GetFeatureInfo operation request shall follow the requirement for operation parameters specified in Table 7 below and that follows the abstract description specified in Normative Reference 1, Table 25

   NSG Requirement 9: An NSG WMTS server shall implement SOAP encoding using HTTP POST transfer of the GetFeatureInfo operation request, using SOAP version 1.2 encoding

   NSG Requirement 10: An NSG WMTS server shall provide standard endpoints from which representation of the FeatureInfo resources can be obtained



- - -

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

`Ref name <ref_link>`_ - `license name <license_Link>`_
`GeoServer  WMS reference <http://docs.geoserver.org/stable/en/user/services/wms/reference.html>`_ - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
