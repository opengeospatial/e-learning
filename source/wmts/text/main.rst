
WMTS - Introduction
======================

Introduction
------------
The OGC `Web Map Tile Service Implementation Standard (WMTS) <http://www.opengeospatial.org/standards/wmts>`_ defines a set of interfaces for making web-based requests of map tiles of spatially referenced data using tile images with predefined content, extent, and resolution.

WMTS complements the OGC `Web Map Service interface standard (WMS) http://www.opengeospatial.org/standards/wms>`_ for the web based distribution of cartographic maps. While WMS focuses on rendering custom maps and is an ideal solution for dynamic data or custom styled maps, particularly when combined with the OGC `Styled Layer Descriptor (SLD) standard <http://www.opengeospatial.org/standards/sld>`_, WMTS trades the flexibility of custom map rendering for the scalability made possible by serving static data (base maps) where the bounding box and scales have been constrained to discrete tiles. The fixed set of tiles allows for the implementation of a WMTS service using a web server that simply returns existing files. The fixed set of tiles also enables the use of standard network mechanisms for scalability such as distributed cache systems.


History and Versions
--------------------

WMTS built on earlier efforts to develop scalable, high performance services for web based distribution of cartographic maps. WMTS was inspired by the `OSGeo Tile Map Service Specification <http://wiki.osgeo.org/index.php/Tile_Map_Service_Specification>`_. Similar initiatives such as Google maps and NASA OnEarth were also considered. The standard included both a resource (RESTful approach) and procedure oriented architectural styles (KVP and SOAP encoding) in an effort to harmonize this interface standard with the OSGeo specification.

While developing a profile of WMS was initially considered, limiting a WMS in the ways important to allow efficient access to cacheable tiles proved awkward while forcing implementors to read both a standard and a profile seemed less efficient than developing a standalone specification.

WMTS version 1.0.0 (Document reference number OGC 07-057r7) was released in 2007, and the Web Map Tile Service Simple Profile was released in 2013.


Test Suite
----------

A beta version of the `OGC Web Map Tile Service 1.0.0 - Executable Test Suite <http://cite.opengeospatial.org/te2/about/wmts/1.0.0/site>`_ was available as of July 2017. Updates can be found at the `OGC Compliance Program Available Tests and Roadmap <http://cite.opengeospatial.org/roadmap>`_.


Implementations
---------------

Information regarding WMTS implementations can be found under `OGC Implementation Statistics <http://www.opengeospatial.org/resource/products/byspec>`_.


Usage
-----

WMTS provides a standards-based solution to serve digital maps using predefined image tiles. The service advertises the tiles it has available through a standardized declaration in the ServiceMetadata document common to all OGC web services. This declaration defines the tiles available in each layer (i.e., each type of content), in each graphical representation style, in each format, in each coordinate reference system, at each scale, and over each geographic fragment of the total covered area. The ServiceMetadata document also declares the communication protocols and encodings through which clients can interact with the server. Clients can interpret the ServiceMetadata document to request specific tiles.

The WMTS standard complements the existing Web Map Service standard of the OGC. The WMS standard focuses on flexibility in the client request enabling clients to obtain exactly the final image they want. A WMS client can request that a server create a map by overlaying an arbitrary number of map layers offered by the server, over an arbitrary geographic bound, with an arbitrary background color at an arbitrary scale, in any supported coordinate reference system. The client may also request that the map layers be rendered using a specific server advertised style, or even use a style provided by the client when the WMS server implements the OGC Styled Layers Descriptor (SLD) standard. However, all this flexibility comes at a price: server image processing must scale with the number of connected clients and there is only limited potential to cache images between the server and client since most images are different.

As web service clients have become more powerful, it has become possible to consider an alternative strategy by which a client requests predefined map image tiles. Though these tiles might not be exactly at the desired positions, the client and can perform image overlays themselves, clipping and mosaicking the provided tiles into a final image. This approach enables servers to scale based on communication processing abilities rather than image processing abilities because servers can pre-render some or all of their images and utilize image caching strategies. The fixed set of images also enables network providers to cache images between the client and the server, reducing latency and bandwidth use.

Prior to WMTS, some WMS server providers had developed their own tiling structures built by constraining WMS GetMap requests to a fixed set and then advertising those constraints in their service metadata. Although this mechanism enabled those servers to scale as just described, the tiling structure and the advertising and discovery mechanisms were not standardized, forcing a specialized client interface for each service.

WMTS offers a standardized approach to declaring the images that can be requested from a server, enabling a single client type to be developed for all servers.


Relationship to Other OGC Standards
-----------------------------------

- The `OGC Web Map Service Interface Standard (WMS) <http://www.opengeospatial.org/standards/wms>`_ is a better fit for rendering custom maps and provides an ideal solution for dynamic data or custom styled maps, particularly when combined with the OGC Style Layer Descriptor (SLD) standard. WMS servers can be used as data sources or rendering engines for WMTS services.

- The `OGC Web Feature Service Interface Standard (WFS) <http://www.opengeospatial.org/standards/wfs>`_ is a better fit for extended query functionality of spatial data. It provides programmatic access to the geographic feature data. An organization publishing both WMS and WFS often use the same data source.


Overview of WMTS Resources and Operations
-----------------------------------------

A WMTS abstract specification describes the semantics of the resources offered by the servers and requested by the client. It specifies the semantics of the ServiceMetadata document, of the Tile images or representations, and of the optional FeatureInfo documents providing descriptions of the maps at specific locations.

Client-server exchange mechanisms are specified under two distinct architectural styles. Under the first "procedural-oriented" style, the requests and responses for GetCapabilities, GetTile and (optional) GetFeatureInfo operations use the encodings of Key-Value Pairs (KVP), "plain-old XML" (POX) messages, or XML messages embedded in SOAP envelopes. Under the second "resource-oriented" style, request mechanisms and an endpoint publishing strategy are specified to enable an approach more closely resembling that of `REpresentational State Transfer (REST) <http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_, particularly `Richardson Maturity Model Level 1 <http://docs.opengeospatial.org/guides/16-057r1.html#_rest_and_open_geospatial_resources>`_. This approach is based on web URL endpoints that enable clients to directly access the ServiceMetadata, Tile, and FeatureInfo resources as documents (i.e., the request is implicit in the URL itself).

Under a resource-oriented pattern, a scalable WMTS service could be created using no image processing logic at all by pre-rendering images and relying only on an ordinary web server to return the static ServiceMetadata XML document and provide the image tile files. The images are considered by the HTTP protocol to be standard web resources, and providers could leverage their existing technologies to improve the flow of those resources to requesting clients.

Whichever style is used, WMTS-enabled services can generally offer advantages in performance and scalability by dividing maps into individual tiles that can be returned quickly. Performance can be enhanced by utilizing locally stored, pre-rendered tiles that will not require any image manipulation or geoprocessing. With tile-based mapping, it is important that servers be able to handle asynchronous access to tiles, as most clients will simultaneously request multiple tiles to fill a single view.

The WMTS interface allows a client to retrieve three general types of resources:

ServiceMetadata resource
   A ServiceMetadata resource (accessed directly under the resource-oriented style or in response to a GetCapabilities operation under the procedural-oriented style) is required in compliant implementations. It describes the abilities and information holdings of the specific server implementation. This operation also supports negotiation of the standard version being used for client-server interactions.

Tile resource
   A Tile resource (accessed directly under the resource-oriented style or in response to a GetTile operation under the procedural-oriented style) is required in compliant implementations. It shows a fragment of a map representation of a layer.

FeatureInfo resource
   A FeatureInfo resource (accessed directly under the resource-oriented style or in response to a GetFeatureInfo operation under the procedural-oriented style) is optional. It provides information about the features located at a particular pixel of a tile map. It does this in a manner similar to the WMS GetFeatureInfo operation by providing, for example, thematic attribute name and value pairs in textual form.

The WMTS serves a single tile of a single layer of a map. As illustrated in the following figure, tiles are related in a hierarchy called a "Tile Matrix Set" in which coarse-resolution tiles are near the top and finer resolution tiles nearer the bottom.

.. image:: ../img/Tiles.png
      :width: 70%

Unlike WMS, there is no specified way to request a server to combine and return a map tile with information coming from more than one layer in a single fetching process. WMTS clients that want to show a combination of layers must make independent requests for the layer tiles and then combine or overlay the responses. Also, bounding boxes and scales of these WMTS tiles are constrained to a discrete set of values.

A full explanation of the geometry of the tiled space can be found in Clause 6.1 of the WMTS Specification `07-057r7 OpenGIS Web Map Tile Service Implementation Standard <http://www.opengeospatial.org/standards/wmts>`_.


Specific WMTS Resources and Operations
--------------------------------------

WMTS specifies several resource / request operation types, two of which are required in a compliant implementation (GetCapabilities and GetTile) and another which is optional (GetFeatureInfo).

GetCapabilities
   The GetCapabilities response is characterized in a "ServiceMetadata" document, which describes how to identify WMTS resources or generate WMTS request operations. The primary content of the metadata is TileMatrixSet summary information and detailed content such as bounding box, supported coordinate reference system (CRS), whether a well-known scale set is available, and TileMatrix data about any of a number of levels. An optional "Themes" section, when present, obviates the need to specify any inheritance rules for layer properties. Under the resource-oriented style, an appropriate resource name such as "WMTSGetCapabilities.xml" would be chosen.

GetTile
   The GetTile operation in procedural-oriented style allows WMTS clients to take the information from the GetCapabilities response and request a particular Tile of a particular TileMatrixSet in a predefined format. Under the resource-oriented style, the client merely requests the representation of any offered Tile resource by performing a request to the address following the standard semantics of the transport protocol.

(Optional) GetFeatureInfo
   GetFeatureInfo requests may be made about the features at or near a particular pixel location. Requests must specify the tile along with a pixel location on that tile, and the WMTS server may choose which information to provide about nearby features. `WMTS Clause 7.3.1 <http://www.opengeospatial.org/standards/wmts>`_ recommends Level 0 of the `Geography Markup Language (GML) Simple Features Profile <http://portal.opengeospatial.org/files/?artifact_id=42729>`_ as a supported document format for FeatureInfo resources.


Example GetCapabilities Requests
--------------------------------

Under the procedural-oriented style, a WMTS client can request a ServiceMetadata document using KVP with HTTP GET in the following manner. This example was adapted from the WMTS 1.0.0 Reference Implementation at the OGC `Compliance Testing GitHub Wiki <https://github.com/opengeospatial/cite/wiki/Reference-Implementations>`. The URL was wrapped to improve readability.

.. code-block:: properties

      http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?
      service=WMTS&
      request=GetCapabilities

The same request submitted using XML with HTTP POST would have the following form:

.. code-block:: properties

      <?xml version="1.0" encoding="UTF-8"?>
      <ows:GetCapabilities
      xmlns:ows="http://www.opengis.net/ows/1.1"
      xmlns:wps="http://www.opengis.net/wps/1.0.0"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.opengis.net/ows/1.1 ..\wpsGetCapabilities_request.xsd"
      language="en-CA" service="WPS">
      <ows:AcceptVersions>
            <ows:Version>1.0.0</ows:Version>
      </ows:AcceptVersions>
      </ows:GetCapabilities>


Under the resource-oriented style, the WMTS Specification contains no normative requirements to constrain the "request" for the GetCapabilities resource. But a representative example can be adapted from the `OSGeo WMTS Guide <https://svn.osgeo.org/tilecache/branches/wmts/docs/WMTSGuide.txt>`_:

.. code-block:: properties

      http://your.domain.com/tilecache.py/1.0.0/WMTSCapabilities.xml


Example GetCapabilities Response: POX
-------------------------------------

An example of a compliant WMTS service's POX response to a procedural-oriented GetCapabilities request operation is presented below.

The following figure provides a summary-level depiction of the major content blocks:

.. image:: ../img/GetCapabilities-POX.png
      :width: 70%

This response declares the service's support for GetCapabilities operations using KVP with HTTP GET. The corresponding XML schema can be found in the normative `WMTS Schemas <http://schemas.opengis.net/wmts/>`_ (narrative description in Clause 7.1.1.2 of the WMTS Specification). This example was adapted from the WMTS 1.0.0 Reference Implementation at the OGC `Compliance Testing GitHub Wiki <https://github.com/opengeospatial/cite/wiki/Reference-Implementations>`.

.. code-block:: properties

      <?xml version='1.0' encoding='UTF-8'?>
      <Capabilities xmlns="http://www.opengis.net/wmts/1.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_response.xsd">
        <ows:ServiceIdentification>
          <ows:Title>deegree 3 CITE Demonstration Suite</ows:Title>
          <ows:Abstract>deegree CITE Demonstration Suite</ows:Abstract>
          <ows:ServiceType>WMTS</ows:ServiceType>
          <ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
        </ows:ServiceIdentification>
        <ows:ServiceProvider>
          <ows:ProviderName>lat/lon GmbH</ows:ProviderName>
          <ows:ProviderSite xlink:href="http://www.lat-lon.de"/>
          <ows:ServiceContact>
            <ows:IndividualName>Dirk Stenger</ows:IndividualName>
            <ows:PositionName>Software developer</ows:PositionName>
            <ows:ContactInfo>
              <ows:Phone>
                <ows:Voice>0228/18496-0</ows:Voice>
                <ows:Facsimile>0228/18496-29</ows:Facsimile>
              </ows:Phone>
              <ows:Address>
                <ows:DeliveryPoint>Aennchenstr. 19</ows:DeliveryPoint>
                <ows:City>Bonn</ows:City>
                <ows:AdministrativeArea>NRW</ows:AdministrativeArea>
                <ows:PostalCode>53177</ows:PostalCode>
                <ows:Country>Germany</ows:Country>
                <ows:ElectronicMailAddress>info@lat-lon.de</ows:ElectronicMailAddress>
              </ows:Address>
              <ows:OnlineResource xlink:href="http://www.deegree.org"/>
              <ows:HoursOfService>24x7</ows:HoursOfService>
              <ows:ContactInstructions>Do not hesitate to call</ows:ContactInstructions>
            </ows:ContactInfo>
            <ows:Role>PointOfContact</ows:Role>
          </ows:ServiceContact>
        </ows:ServiceProvider>
        <ows:OperationsMetadata>
          <ows:Operation name="GetCapabilities">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?"/>
              </ows:HTTP>
            </ows:DCP>
            <ows:Constraint name="GetEncoding">
              <ows:AllowedValues>
                <ows:Value>KVP</ows:Value>
              </ows:AllowedValues>
            </ows:Constraint>
          </ows:Operation>
          <ows:Operation name="GetTile">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?"/>
              </ows:HTTP>
            </ows:DCP>
            <ows:Constraint name="GetEncoding">
              <ows:AllowedValues>
                <ows:Value>KVP</ows:Value>
              </ows:AllowedValues>
            </ows:Constraint>
          </ows:Operation>
          <ows:Operation name="GetFeatureInfo">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?"/>
              </ows:HTTP>
            </ows:DCP>
            <ows:Constraint name="GetEncoding">
              <ows:AllowedValues>
                <ows:Value>KVP</ows:Value>
              </ows:AllowedValues>
            </ows:Constraint>
          </ows:Operation>
          <ows:Constraint name="GetEncoding">
            <ows:AllowedValues>
              <ows:Value>KVP</ows:Value>
            </ows:AllowedValues>
          </ows:Constraint>
        </ows:OperationsMetadata>
        <Contents>
          <Layer>
            <ows:Title>cite</ows:Title>
            <ows:WGS84BoundingBox>
              <ows:LowerCorner>-180.000000 -90.000000</ows:LowerCorner>
              <ows:UpperCorner>180.000000 90.000000</ows:UpperCorner>
            </ows:WGS84BoundingBox>
            <ows:Identifier>cite</ows:Identifier>
            <Style>
              <ows:Identifier>default</ows:Identifier>
            </Style>
            <Format>image/png</Format>
            <InfoFormat>application/vnd.ogc.gml</InfoFormat>
            <InfoFormat>text/xml</InfoFormat>
            <InfoFormat>text/plain</InfoFormat>
            <InfoFormat>text/html</InfoFormat>
            <InfoFormat>application/gml+xml; version=2.1</InfoFormat>
            <InfoFormat>application/gml+xml; version=3.0</InfoFormat>
            <InfoFormat>application/gml+xml; version=3.1</InfoFormat>
            <InfoFormat>application/gml+xml; version=3.2</InfoFormat>
            <InfoFormat>text/xml; subtype=gml/2.1.2</InfoFormat>
            <InfoFormat>text/xml; subtype=gml/3.0.1</InfoFormat>
            <InfoFormat>text/xml; subtype=gml/3.1.1</InfoFormat>
            <InfoFormat>text/xml; subtype=gml/3.2.1</InfoFormat>
            <TileMatrixSetLink>
              <TileMatrixSet>InspireCrs84Quad</TileMatrixSet>
            </TileMatrixSetLink>
          </Layer>
          <!-- [ ... other layers ... ] -->
          <TileMatrixSet>
            <!-- optional bounding box of data in this CRS -->
            <ows:Identifier>InspireCrs84Quad</ows:Identifier>
            <ows:SupportedCRS>urn:ogc:def:crs:OGC:1.3:CRS84</ows:SupportedCRS>
            <TileMatrix>
              <ows:Identifier>0</ows:Identifier>
              <ScaleDenominator>2.795411320143589E8</ScaleDenominator>
              <!-- top left point of tile matrix bounding box -->
              <TopLeftCorner>-180.0 90.0</TopLeftCorner>
              <!-- width and height of each tile in pixel units -->
              <TileWidth>256</TileWidth>
              <TileHeight>256</TileHeight>
              <!-- width and height of matrix in tile units -->
              <MatrixWidth>2</MatrixWidth>
              <MatrixHeight>1</MatrixHeight>
            </TileMatrix>
            <TileMatrix>
              <ows:Identifier>1</ows:Identifier>
              <ScaleDenominator>1.397705660071794E8</ScaleDenominator>
              <TopLeftCorner>-180.0 90.0</TopLeftCorner>
              <TileWidth>256</TileWidth>
              <TileHeight>256</TileHeight>
              <MatrixWidth>4</MatrixWidth>
              <MatrixHeight>2</MatrixHeight>
            </TileMatrix>
            <!-- ***************************************** -->
            <!-- [... TileMatrix entries 2-16 removed ...] -->
            <!-- ***************************************** -->
            <TileMatrix>
              <ows:Identifier>17</ows:Identifier>
              <ScaleDenominator>2132.729583849784</ScaleDenominator>
              <TopLeftCorner>-180.0 90.0</TopLeftCorner>
              <TileWidth>256</TileWidth>
              <TileHeight>256</TileHeight>
              <MatrixWidth>262144</MatrixWidth>
              <MatrixHeight>131072</MatrixHeight>
            </TileMatrix>
          </TileMatrixSet>
        </Contents>
        <Themes>
          <Theme>
            <ows:Title>Root theme</ows:Title>
            <ows:Identifier>base</ows:Identifier>
            <Theme>
              <ows:Title>cite</ows:Title>
              <ows:Identifier>cite</ows:Identifier>
              <LayerRef>cite</LayerRef>
            </Theme>
          </Theme>
        </Themes>
      </Capabilities>



Example GetCapabilities Response: SOAP
--------------------------------------

An example of a compliant WMTS service's ServiceMetadata document in response to a procedural-oriented SOAP-encoded GetCapabilities request is presented below. This example was adapted from an example in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification.

.. code-block:: properties

      <?xml version="1.0" encoding="UTF-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:xsd="http://www.w3.org/2001/XMLSchema"
          xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
      		<Capabilities xmlns="http://www.opengis.net/wmts/1.0"
      			xmlns:ows="http://www.opengis.net/ows/1.1"
      			xmlns:xlink="http://www.w3.org/1999/xlink"
      			xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      			xmlns:gml="http://www.opengis.net/gml"
      			xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_response.xsd"
      			version="1.0.0">
    			<ows:ServiceIdentification>
    				<ows:Title>World example Web Map Tile Service</ows:Title>
    				<ows:Abstract>Example service that contrains some world layers
    					in the urn:ogc:def:wkss:OGC:1.0:GlobalCRS84Pixel Well-known
    					scale set</ows:Abstract>
    				<ows:Keywords>
    					<ows:Keyword>World</ows:Keyword>
    					<ows:Keyword>Global</ows:Keyword>
    					<ows:Keyword>Digital Elevation Model</ows:Keyword>
    					<ows:Keyword>Administrative Boundaries</ows:Keyword>
    				</ows:Keywords>
    				<ows:ServiceType>OGC WMTS</ows:ServiceType>
    				<ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
    				<ows:Fees>none</ows:Fees>
    				<ows:AccessConstraints>none</ows:AccessConstraints>
    			</ows:ServiceIdentification>
    			<ows:ServiceProvider>
    				<ows:ProviderName>UAB-CREAF-MiraMon</ows:ProviderName>
    				<ows:ProviderSite xlink:href="http://www.creaf.uab.es/miramon"/>
    				<ows:ServiceContact>
    					<ows:IndividualName>Joan Maso Pau</ows:IndividualName>
    					<ows:PositionName>Senior Software Engineer</ows:PositionName>
    					<ows:ContactInfo>
    						<ows:Phone>
    							<ows:Voice>+34 93 581 1312</ows:Voice>
    							<ows:Facsimile>+34 93 581 4151</ows:Facsimile>
    						</ows:Phone>
    						<ows:Address>
    							<ows:DeliveryPoint>Fac Ciencies UAB</ows:DeliveryPoint>
    							<ows:City>Bellaterra</ows:City>
    							<ows:AdministrativeArea>Barcelona</ows:AdministrativeArea>
    							<ows:PostalCode>08193</ows:PostalCode>
    							<ows:Country>Spain</ows:Country>
    							<ows:ElectronicMailAddress>joan.maso@uab.es</ows:ElectronicMailAddress>
    						</ows:Address>
    					</ows:ContactInfo>
    				</ows:ServiceContact>
    			</ows:ServiceProvider>
    			<ows:OperationsMetadata>
    				<ows:Operation name="GetCapabilities">
    					<ows:DCP>
    						<ows:HTTP>
    							<ows:Post xlink:href="http://www.opengis.uab.es/cgi-bin/world/MiraMon5_0.cgi?">
    								<ows:Constraint name="PostEncoding">
    									<ows:AllowedValues>
    										<ows:Value>SOAP</ows:Value>
    									</ows:AllowedValues>
    								</ows:Constraint>
    							</ows:Post>
    						</ows:HTTP>
    					</ows:DCP>
    				</ows:Operation>
    				<ows:Operation name="GetTile">
    					<ows:DCP>
    						<ows:HTTP>
    							<ows:Post xlink:href="http://www.opengis.uab.es/cgi-bin/world/MiraMon5_0.cgi?">
    								<ows:Constraint name="PostEncoding">
    									<ows:AllowedValues>
    										<ows:Value>SOAP</ows:Value>
    									</ows:AllowedValues>
    								</ows:Constraint>
    							</ows:Post>
    						</ows:HTTP>
    					</ows:DCP>
    				</ows:Operation>
    			</ows:OperationsMetadata>
    			<Contents>
    				<Layer>
    					<ows:Title>etopo2</ows:Title>
    					<ows:Abstract>ETOPO2 - 2 minute Worldwide Bathymetry/Topography
    						Data taken from National Geophysical Data Center(NGDC) CD-ROM, ETOPO2 Global 2' Elevations, September 2001.
                <!-- ************************************************* -->
                <!-- [... additional Abstract information removed ...] -->
                <!-- ************************************************* -->
              </ows:Abstract>
    					<ows:WGS84BoundingBox>
    						<ows:LowerCorner>-180 -90</ows:LowerCorner>
    						<ows:UpperCorner>180 90</ows:UpperCorner>
    					</ows:WGS84BoundingBox>
    					<ows:Identifier>etopo2</ows:Identifier>
    					<ows:Metadata xlink:href="http://www.opengis.uab.es/SITiled/world/etopo2/metadata.htm"/>
    					<Style isDefault="true">
    						<ows:Title>default</ows:Title>
    						<ows:Identifier>default</ows:Identifier>
    						<LegendURL format="image/png" xlink:href="http://www.opengis.uab.es/SITiled/world/etopo2/legend.png"/>
    					</Style>
    					<Format>image/png</Format>
    					<InfoFormat>application/gml+xml; version=3.1</InfoFormat>
    					<TileMatrixSetLink>
    						<TileMatrixSet>WholeWorld_CRS_84</TileMatrixSet>
    					</TileMatrixSetLink>
    					<ResourceURL format="image/png" resourceType="tile" template="http://www.opengis.uab.es/SITiled/world/etopo2/default/WholeWorld_CRS_84/{TileMatrix}/{TileRow}/{TileCol}.png"/>
    					<ResourceURL format="application/gml+xml; version=3.1" resourceType="FeatureInfo" template="http://www.opengis.uab.es/SITiled/world/etopo2/default/WholeWorld_CRS_84/{TileMatrix}/{TileRow}/{TileCol}/{J}/{I}.xml"/>
    				</Layer>
    				<Layer>
    					<ows:Title>Administrative Boundaries</ows:Title>
    					<ows:Abstract>The sub Country Administrative Units 1998
                GeoDataset represents a small-scale world political map.
                <!-- ************************************************* -->
                <!-- [... additional Abstract information removed ...] -->
                <!-- ************************************************* -->
              </ows:Abstract>
    					<ows:WGS84BoundingBox>
    						<ows:LowerCorner>-180 -90</ows:LowerCorner>
    						<ows:UpperCorner>180 84</ows:UpperCorner>
    					</ows:WGS84BoundingBox>
    					<ows:Identifier>AdminBoundaries</ows:Identifier>
    					<ows:Metadata xlink:href="http://www.opengis.uab.es/SITiled/world/AdminBoundaries/metadata.htm"/>
    					<Style isDefault="true">
    						<ows:Title>default</ows:Title>
    						<ows:Identifier>default</ows:Identifier>
    					</Style>
    					<Format>image/png</Format>
    					<TileMatrixSetLink>
    						<TileMatrixSet>World84-90_CRS_84</TileMatrixSet>
    					</TileMatrixSetLink>
    					<ResourceURL format="image/png" resourceType="tile" template="http://www.opengis.uab.es/SITiled/world/AdminBoundaries/default/World84-90_CRS_84/{TileMatrix}/{TileRow}/{TileCol}.png"/>
    					<ResourceURL format="application/gml+xml; version=3.1" resourceType="FeatureInfo" template="http://www.opengis.uab.es/SITiled/world/AdminBoundaries/default/World84-90_CRS_84/{TileMatrix}/{TileRow}/{TileCol}/{J}/{I}.xml"/>
    				</Layer>
    				<TileMatrixSet>
    					<!-- optional bounding box of data in this CRS -->
    					<ows:Identifier>WholeWorld_CRS_84</ows:Identifier>
    					<ows:SupportedCRS>urn:ogc:def:crs:OGC:1.3:CRS84</ows:SupportedCRS>
    					<WellKnownScaleSet>urn:ogc:def:wkss:OGC:1.0:GlobalCRS84Pixel</WellKnownScaleSet>
    					<TileMatrix>
    						<ows:Identifier>2g</ows:Identifier>
    						<ScaleDenominator>795139219.951954</ScaleDenominator>
    						<!-- top left point of tile matrix bounding box -->
    						<TopLeftCorner>-180 90</TopLeftCorner>
    						<!-- width and height of each tile in pixel units -->
    						<TileWidth>320</TileWidth>
    						<TileHeight>200</TileHeight>
    						<!-- width and height of matrix in tile units -->
    						<MatrixWidth>1</MatrixWidth>
    						<MatrixHeight>1</MatrixHeight>
    					</TileMatrix>
    					<TileMatrix>
    						<ows:Identifier>1g</ows:Identifier>
    						<ScaleDenominator>397569609.975977</ScaleDenominator>
    						<TopLeftCorner>-180 90</TopLeftCorner>
    						<TileWidth>320</TileWidth>
    						<TileHeight>200</TileHeight>
    						<MatrixWidth>2</MatrixWidth>
    						<MatrixHeight>1</MatrixHeight>
    					</TileMatrix>
              <!-- *********************************************** -->
              <!-- [... Additional TileMatrix entries removed ...] -->
              <!-- *********************************************** -->
    				</TileMatrixSet>
            <!-- ************************************************** -->
            <!-- [... Additional TileMatrixSet entries removed ...] -->
            <!-- ************************************************** -->
    			</Contents>
    			<Themes>
    				<Theme>
    					<ows:Title>Foundation</ows:Title>
    					<ows:Abstract>World reference data</ows:Abstract>
    					<ows:Identifier>Foundation</ows:Identifier>
    					<Theme>
    						<ows:Title>Digital Elevation Model</ows:Title>
    						<ows:Identifier>DEM</ows:Identifier>
    						<LayerRef>etopo2</LayerRef>
    					</Theme>
    					<Theme>
    						<ows:Title>Administrative Boundaries</ows:Title>
    						<ows:Identifier>AdmBoundaries</ows:Identifier>
    						<LayerRef>AdminBoundaries</LayerRef>
    					</Theme>
    				</Theme>
    			</Themes>
    			<WSDL xlink:role="http://schemas.xmlsoap.org/wsdl/1.0" xlink:show="none" xlink:type="simple" xlink:href="wmtsConcrete.wsdl"/>
    		</Capabilities>
    	</soap:Body>
    </soap:Envelope>


Example GetCapabilities Response: Resource-Oriented
---------------------------------------------------

An example of a compliant WMTS service's ServiceMetadata document in response to a resource-oriented request for a resource representation is presented below. This example was adapted from an example in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification.

.. code-block:: properties

      <?xml version="1.0" encoding="UTF-8"?>
        <soap:Envelope >

      <?xml version="1.0" encoding="UTF-8"?>
      <Capabilities xmlns="http://www.opengis.net/wmts/1.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gml="http://www.opengis.net/gml" xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_response.xsd" version="1.0.0">
      	<ows:ServiceIdentification>
      		<ows:Title>World example Web Map Tile Service</ows:Title>
      		<ows:Abstract>Example service that contrains some world layers in the
      				urn:ogc:def:wkss:OGC:1.0:GlobalCRS84Pixel Well-known scale set</ows:Abstract>
      		<ows:Keywords>
      			<ows:Keyword>World</ows:Keyword>
      			<ows:Keyword>Global</ows:Keyword>
      			<ows:Keyword>Digital Elevation Model</ows:Keyword>
      			<ows:Keyword>Administrative Boundaries</ows:Keyword>
      		</ows:Keywords>
      		<ows:ServiceType>OGC WMTS</ows:ServiceType>
      		<ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
      		<ows:Fees>none</ows:Fees>
      		<ows:AccessConstraints>none</ows:AccessConstraints>
      	</ows:ServiceIdentification>
      	<ows:ServiceProvider>
      		<ows:ProviderName>UAB-CREAF-MiraMon</ows:ProviderName>
      		<ows:ProviderSite xlink:href="http://www.creaf.uab.es/miramon"/>
      		<ows:ServiceContact>
      			<ows:IndividualName>Joan Maso Pau</ows:IndividualName>
      			<ows:PositionName>Senior Software Engineer</ows:PositionName>
      			<ows:ContactInfo>
      				<ows:Phone>
      					<ows:Voice>+34 93 581 1312</ows:Voice>
      					<ows:Facsimile>+34 93 581 4151</ows:Facsimile>
      				</ows:Phone>
      				<ows:Address>
      					<ows:DeliveryPoint>Fac Ciencies UAB</ows:DeliveryPoint>
      					<ows:City>Bellaterra</ows:City>
      					<ows:AdministrativeArea>Barcelona</ows:AdministrativeArea>
      					<ows:PostalCode>08193</ows:PostalCode>
      					<ows:Country>Spain</ows:Country>
      					<ows:ElectronicMailAddress>joan.maso@uab.es</ows:ElectronicMailAddress>
      				</ows:Address>
      			</ows:ContactInfo>
      		</ows:ServiceContact>
      	</ows:ServiceProvider>
      	<ows:OperationsMetadata>
      		<ows:Operation name="GetCapabilities">
      			<ows:DCP>
      				<ows:HTTP>
      					<ows:Get xlink:href="http://www.opengis.uab.es/cgi-bin/world/MiraMon5_0.cgi?">
      						<ows:Constraint name="GetEncoding">
      							<ows:AllowedValues>
      								<ows:Value>KVP</ows:Value>
      							</ows:AllowedValues>
      						</ows:Constraint>
      					</ows:Get>
      				</ows:HTTP>
      			</ows:DCP>
      		</ows:Operation>
      		<ows:Operation name="GetTile">
      			<ows:DCP>
      				<ows:HTTP>
      					<ows:Get xlink:href="http://www.opengis.uab.es/cgi-bin/world/MiraMon5_0.cgi?">
      						<ows:Constraint name="GetEncoding">
      							<ows:AllowedValues>
      								<ows:Value>KVP</ows:Value>
      							</ows:AllowedValues>
      						</ows:Constraint>
      					</ows:Get>
      				</ows:HTTP>
      			</ows:DCP>
      		</ows:Operation>
      	</ows:OperationsMetadata>
      	<Contents>
        <!-- ************************************************************* -->
        <!-- [... Contents identical to GetCapabilities Response: SOAP...] -->
        <!-- ************************************************************* -->
      	</Contents>
      	<Themes>
        <!-- *********************************************************** -->
        <!-- [... Themes identical to GetCapabilities Response: SOAP...] -->
        <!-- *********************************************************** -->
      	</Themes>
      	<ServiceMetadataURL xlink:href="http://www.opengis.uab.es/SITiled/world/1.0.0/WMTSCapabilities.xml"/>
      </Capabilities>


- - -
- - -
LEFT OFF
- - -
- - -

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
