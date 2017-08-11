WMTS - Operations
======================

Background
------------------
Usage
^^^^^^^

WMTS provides a standards-based solution to serve digital maps using predefined image tiles. The service advertises the tiles it has available through a standardized declaration in the ServiceMetadata document common to all OGC web services. This declaration defines the tiles available in each layer (i.e., each type of content), in each graphical representation style, in each format, in each coordinate reference system, at each scale, and over each geographic fragment of the total covered area. The ServiceMetadata document also declares the communication protocols and encodings through which clients can interact with the server. Clients can interpret the ServiceMetadata document to request specific tiles.

The WMTS standard complements the existing Web Map Service standard of the OGC. The WMS standard focuses on flexibility in the client request enabling clients to obtain exactly the final image they want. A WMS client can request that a server create a map by overlaying an arbitrary number of map layers offered by the server, over an arbitrary geographic bound, with an arbitrary background color at an arbitrary scale, in any supported coordinate reference system. The client may also request that the map layers be rendered using a specific server advertised style, or even use a style provided by the client when the WMS server implements the OGC Styled Layers Descriptor (SLD) standard. However, all this flexibility comes at a price: server image processing must scale with the number of connected clients and there is only limited potential to cache images between the server and client since most images are different.

As web service clients have become more powerful, it has become possible to consider an alternative strategy by which a client requests predefined map image tiles. Though these tiles might not be exactly at the desired positions, the client and can perform image overlays themselves, clipping and mosaicking the provided tiles into a final image. This approach enables servers to scale based on communication processing abilities rather than image processing abilities because servers can pre-render some or all of their images and utilize image caching strategies. The fixed set of images also enables network providers to cache images between the client and the server, reducing latency and bandwidth use.

Prior to WMTS, some WMS server providers had developed their own tiling structures built by constraining WMS GetMap requests to a fixed set and then advertising those constraints in their service metadata. Although this mechanism enabled those servers to scale as just described, the tiling structure and the advertising and discovery mechanisms were not standardized, forcing a specialized client interface for each service.

WMTS offers a standardized approach to declaring the images that can be requested from a server, enabling a single client type to be developed for all servers.


Relationship to Other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The `OGC Web Map Service Interface Standard (WMS) <http://www.opengeospatial.org/standards/wms>`_ is a better fit for rendering custom maps and provides an ideal solution for dynamic data or custom styled maps, particularly when combined with the OGC Style Layer Descriptor (SLD) standard. WMS servers can be used as data sources or rendering engines for WMTS services.

- The `OGC Web Feature Service Interface Standard (WFS) <http://www.opengeospatial.org/standards/wfs>`_ is a better fit for extended query functionality of spatial data. It provides programmatic access to the geographic feature data. An organization publishing both WMS and WFS often use the same data source.


History and Versions
^^^^^^^^^^^^^^^^^^^^^^

WMTS was built to assist in developing scalable, high performance services for web based distribution of cartographic maps. It can accommodate both resource-oriented (REST-like) and procedural-oriented architectural styles (KVP and SOAP encoding). While developing a profile of WMS was initially considered, limiting a WMS in the ways important to allow efficient access to cacheable tiles proved awkward while forcing implementors to read both a standard and a profile seemed less efficient than developing a standalone specification.

WMTS version 1.0.0 (Document reference number OGC 07-057r7) was released in 2007, and the Web Map Tile Service Simple Profile was released in 2013.

A beta version of the `OGC Web Map Tile Service 1.0.0 - Executable Test Suite <http://cite.opengeospatial.org/te2/about/wmts/1.0.0/site>`_ was available as of July 2017. Updates can be found at the `OGC Compliance Program Available Tests and Roadmap <http://cite.opengeospatial.org/roadmap>`_.

Information regarding WMTS implementations can be found under `OGC Implementation Statistics <http://www.opengeospatial.org/resource/products/byspec>`_.

TBD: provide a table about what are the changes in the standard regading the operations



Overview of WMTS Resources and Operations
--------------------------------------------------------------------

A WMTS abstract specification describes the semantics of the resources offered by the servers and requested by the client. It specifies the semantics of the ServiceMetadata document, of the Tile images or representations, and of the optional FeatureInfo documents providing descriptions of the maps at specific locations.

Client-server exchange mechanisms are specified under two distinct architectural styles. Under the first "procedural-oriented" style, the requests and responses for GetCapabilities, GetTile and (optional) GetFeatureInfo operations use the encodings of Key-Value Pairs (KVP), "plain-old XML" (POX) messages, or XML messages embedded in SOAP envelopes. Under the second "resource-oriented" style, request mechanisms and an endpoint publishing strategy are specified to enable an approach more closely resembling that of `REpresentational State Transfer (REST) <http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_, particularly `Richardson Maturity Model Level 1 <http://docs.opengeospatial.org/guides/16-057r1.html#_rest_and_open_geospatial_resources>`_. This approach is based on web URL endpoints that enable clients to directly access the ServiceMetadata, Tile, and FeatureInfo resources as documents (i.e., the request is implicit in the URL itself).

Under a resource-oriented style, a scalable WMTS service could be created using no image processing logic at all by pre-rendering images and relying only on an ordinary web server to return the static ServiceMetadata XML document and provide the image tile files. The images are considered by the HTTP protocol to be standard web resources, and providers could leverage their existing technologies to improve the flow of those resources to requesting clients.

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


Overview WMTS Operations
--------------------------------------------------------------

WMTS specifies several resource / request operation types, two of which are required in a compliant implementation (GetCapabilities and GetTile) and another which is optional (GetFeatureInfo).

GetCapabilities
   The GetCapabilities response is characterized in a "ServiceMetadata" document, which describes how to identify WMTS resources or generate WMTS request operations. The primary content of the metadata is TileMatrixSet summary information and detailed content such as bounding box, supported coordinate reference system (CRS), whether a well-known scale set is available, and TileMatrix data about any of a number of levels. An optional "Themes" section, when present, obviates the need to specify any inheritance rules for layer properties. Under the resource-oriented style, an appropriate resource name such as "WMTSGetCapabilities.xml" would be chosen.

GetTile
   The GetTile operation in procedural-oriented style allows WMTS clients to take the information from the GetCapabilities response and request a particular Tile of a particular TileMatrixSet in a predefined format. Under the resource-oriented style, the client merely requests the representation of any offered Tile resource by performing a request to the address following the standard semantics of the transport protocol.

(Optional) GetFeatureInfo
   GetFeatureInfo requests may be made about the features at or near a particular pixel location. Requests must specify the tile along with a pixel location on that tile, and the WMTS server may choose which information to provide about nearby features. `WMTS Clause 7.3.1 <http://www.opengeospatial.org/standards/wmts>`_ recommends Level 0 of the `Geography Markup Language (GML) Simple Features Profile <http://portal.opengeospatial.org/files/?artifact_id=42729>`_ as a supported document format for FeatureInfo resources.

Get Capabilities Examples
-------------------------------------

Example GetCapabilities Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the procedural-oriented style, a WMTS client can request a ServiceMetadata document using KVP with HTTP GET in the following manner. This example was adapted from the WMTS 1.0.0 Reference Implementation at the OGC `Compliance Testing GitHub Wiki <https://github.com/opengeospatial/cite/wiki/Reference-Implementations>`. The URL has been wrapped to improve readability.

.. code-block:: properties

      http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wmts100?
      service=WMTS&
      request=GetCapabilities

The same request using SOAP would have the following form:

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
      	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      	xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
      		<GetCapabilities xmlns="http://www.opengis.net/wmts/1.0"
      			xmlns:ows="http://www.opengis.net/ows/1.1"
      			xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_request.xsd"
      			service="WMTS">
      			<ows:AcceptVersions>
      				<ows:Version>1.0.0</ows:Version>
      			</ows:AcceptVersions>
      			<ows:AcceptFormats>
      				<ows:OutputFormat>application/xml</ows:OutputFormat>
      			</ows:AcceptFormats>
      		</GetCapabilities>
      	</soap:Body>
      </soap:Envelope>

Under a resource-oriented style, a representative example would be:

.. code-block:: properties

      http://your.domain.com/1.0.0/WMTSCapabilities.xml


Example GetCapabilities Response: POX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An example of a compliant WMTS service's POX response to a procedural-oriented GetCapabilities KVP request operation is presented below.

The following figure provides a summary-level depiction of the major content blocks:

.. image:: ../img/GetCapabilities-POX.png
      :width: 70%

This response declares the service's support for GetCapabilities operations using KVP with HTTP GET. WMTS services in practice might contain many more Layers, TileMatrixSets, and Themes than just the several shown here.

This example was adapted from content in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification. The corresponding XML schema can be found in the same location. Some of the lengthy XML content has been removed and replaced by brief comments in order to reduce the space consumed by the full response.

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <Capabilities xmlns="http://www.opengis.net/wmts/1.0"
        xmlns:ows="http://www.opengis.net/ows/1.1"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:gml="http://www.opengis.net/gml"
        xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_response.xsd"
        version="1.0.0">
      <ows:ServiceIdentification>
        <ows:Title>World example Web Map Tile Service</ows:Title>
        <ows:Abstract>Example service that constrains some world layers
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


Example GetCapabilities Response: SOAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An example of a compliant WMTS service's ServiceMetadata document in response to a procedural-oriented SOAP-encoded GetCapabilities request can be found in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification. An abbreviated representation of the XML content is presented below. The primary difference here is the presence of the SOAP envelope.

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:xsd="http://www.w3.org/2001/XMLSchema"
          xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
        <!-- ****************************** -->
        <!-- [... Capabilities go here ...] -->
        <!-- ****************************** -->
      	</soap:Body>
      </soap:Envelope>


Example GetCapabilities Response: Resource-Oriented
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sample ServiceMetadata document in response to a resource-oriented request for a resource representation can be found in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification. The content is virtually identical to that presented for the POX response.


Example GetCapabilities Request and Response Using JSON in JavaScript
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The WMTS Specification is silent regarding `JavaScript Object Notation (JSON) <http://www.json.org/>`_. Hence including a JSON encoding in source code (e.g., JavaScript) invoking a request (or receiving a response) would have no bearing on an implementation's compliance with the WMTS standard. However, the OGC `Testbed 12 initiative <http://www.opengeospatial.org/projects/initiatives/testbed12>`_ provided instructive guidance in two documents, an engineering report and a user guide. The `JavaScript JSON JSON- LD Engineering Report <http://docs.opengeospatial.org/per/16-051.html>`_ provides JSON examples that were adapted for use here in the WMTS case. Likewise, the `JSON and GeoJSON User Guide <http://docs.opengeospatial.org/guides/16-122r1.html>`_ includes WMS-based JavaScript examples, that have also been adapted for WMTS.

This example assumes the existence of a WMTS service that has implemented an “acceptFormats” parameter as described in Clause “7.3.5 AcceptFormats parameter” of `06-121r9 OGC Web Services Common Implementation Specification <http://www.opengeospatial.org/standards/common>`_. The service in this case must be able to provide a JSON response. Under this assumption, a KVP GET request that includes a WMTS GetCapabilities operation could start with the following JavaScript "loadJSON" invocation.

The first parameter identifies the URL (wrapped for readability) of the service endpoint where the request will be routed, including the acceptable JSON response type. The second parameter indicates that the "ShowCapabilities" function should be called back upon successful completion of the HTTP GET request. The third parameter identifies the callback for an HTTP failure path.

.. code-block:: javascript

  loadJSON("http://your.domain.com?
      request=GetCapabilities&
      service=WMTS&
      acceptsFormats=application/json",
    ShowCapabilities,
    function(xhr) { alert(xhr); }
  )


Representative JavaScript code for the loadJSON function appears below. Invocation of this function will, under an HTTP-success execution path, de-serialize the content of a JSON response into JavaScript variables by invoking "JSON.parse()".

.. code-block:: javascript

  function loadJSON(path, success, error)
  {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
      {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            if (success)
              {
                var data;
                try {
                  data = JSON.parse(xhr.responseText);
                } catch (e) {
                  if (error)
                    return error("JSON file: \""+ path + "\". " + e);
                }
                success(data);
              }
          } else {
            if (error)
              error("JSON file: \""+ path + "\". " + xhr.statusText);
          }
      }
    };
    xhr.open("GET", path, true);
    xhr.send();
  }


Representative JavaScript code for the ShowCapabilities function appears below. Due to the loadJSON() code to perform JSON.parse() on the xhr.responseText, the "capabilities" JavaScript variable will contain the response values, with subordinate key names matching what the element names would have been in a corresponding XML response.

.. code-block:: javascript

  function ShowCapabilities(capabilities)
  {
      if (capabilities.serviceIdentification.serviceTypeVersion!=“1.0.0” ||
          capabilities.serviceIdentification.serviceType.code!="WMTS")
          alert("This is not a compatible WMTS JSON server");
      alert("The provider name is: " +
          capabilities.serviceProvider.providerName);
  }


More friendly user output for the loadJSON() error cases could be provided if something like the following JSON string were to be supplied by the WMTS service (reporting two HTTP exceptions in this example).

.. code-block:: json

  {
    "type": "ExceptionReport",
    "version": "1.0.0",
    "lang": "en",
    "exception": [{
      "type": "Exception",
      "exceptionCode": "MissingParameterValue",
      "exceptionText": "Service parameter missing",
      "locator": "service"
      },{
      "type": "Exception",
      "exceptionCode": "InvalidParameterValue",
      "exceptionText": "Version number not supported",
      "locator": "version”
    }]
  }


GetTile Examples
--------------------------------

Example GetTile Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the procedural-oriented style, a WMTS client can issue a GetTile request using KVP with HTTP GET in the following manner. The URL has been wrapped to improve readability.

.. code-block:: properties

      http://your.domain.com/services/wmts100?
      service=WMTS&
      request=GetTile&
      version=1.0.0&
      Layer=coastlines&
      Style=blue&
      Format=image/png&
      TileMatrixSet=coastlinesInCrs84&
      TileMatrix=5e6&
      TileRow=42&
      TileCol=112

The same request using SOAP would have the following form:

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
      	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      	xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
      		<GetTile xmlns="http://www.opengis.net/wmts/1.0"
      			xmlns:ows="http://www.opengis.net/ows/1.1"
      			xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetTile_request.xsd"
      			service="WMTS" version="1.0.0">
      			<Layer>coastlines</Layer>
      			<Style>blue</Style>
      			<Format>image/png</Format>
      			<DimensionNameValue name="TIME">2007-06</DimensionNameValue>
      			<TileMatrixSet>coastlinesInCrs84</TileMatrixSet>
      			<TileMatrix>5e6</TileMatrix>
      			<TileRow>42</TileRow>
      			<TileCol>112</TileCol>
      		</GetTile>
      	</soap:Body>
      </soap:Envelope>

Under a resource-oriented style, a representative example would be:

.. code-block:: properties

      http://your.domain.com/coastlines/blue/2007-06/coastlinesInCrs84/5e6/42/112.png


Example GetTiles Response: KVP Request and Resource-Oriented
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In response to a URL containing KVPs (or under a resource-oriented style), a tile map that complies with the requested parameters (or a representation of the requested tile resource) would be returned.


Example GetTiles Response: SOAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An example of a compliant WMTS service's response to a procedural-oriented SOAP-encoded GetTiles request is presented below. This example was adapted from an example in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification.

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
      	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      	xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
      		<BinaryPayload xmlns="http://www.opengis.net/wmts/1.0"
      			xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsPayload_response.xsd">
      			<Format>image/png</Format>
      			<BinaryContent>
      				<![CDATA[iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABGdBTUEAALGP
      C/xhBQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9YGARc5KB0XV+IA
      AAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAF1J
      REFUGNO9zL0NglAAxPEfdLTs4BZM4DIO4C7OwQg2JoQ9LE1exdlYvBBeZ7jq
      ch9//q1uH4TLzw4d6+ErXMMcXuHWxId3KOETnnXXV6MJpcq2MLaI97CER3N0
      vr4MkhoXe0rZigAAAABJRU5ErkJggg==]]>
      			</BinaryContent>
      		</BinaryPayload>
      	</soap:Body>
      </soap:Envelope>

GetFeatureInfo Examples
--------------------------------------------

Example GetFeatureInfo Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the procedural-oriented style, a WMTS client can issue a GetFeatureInfo request using KVP with HTTP GET in the following manner. The URL has been wrapped to improve readability.

.. code-block:: properties

      http://your.domain.com/services/wmts100?
      service=WMTS&
      request=GetFeatureInfo&
      version=1.0.0&
      Layer=coastlines&
      Style=blue&
      Format=image/png&
      TileMatrixSet=coastlinesInCrs84&
      TileMatrix=5e6&
      TileRow=42&
      TileCol=112
      J=23
      I=35
      InfoFormat=text/html


The same request using SOAP would have the following form. Note that the following tagged content is identical to that under the GetTile request above: <Layer>, <Style>, <Format>, <DimensionNameValue name="TIME">, <TileMatrixSet>, <TileMatrix>, <TileRow>, and <TileCol>.

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
      	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      	xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
      		<GetFeatureInfo  xmlns="http://www.opengis.net/wmts/1.0"
      			xmlns:ows="http://www.opengis.net/ows/1.1"
      			xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetFeatureInfo_request.xsd"
      			service="WMTS" version="1.0.0">
      			<GetTile service="WMTS" version="1.0.0">
      				<Layer>coastlines</Layer>
      				<Style>blue</Style>
      				<Format>image/png</Format>
      				<DimensionNameValue name="TIME">2007-06</DimensionNameValue>
      				<TileMatrixSet>coastlinesInCrs84</TileMatrixSet>
      				<TileMatrix>5e6</TileMatrix>
      				<TileRow>42</TileRow>
      				<TileCol>112</TileCol>
      			</GetTile>
      			<J>23</J>
      			<I>35</I>
      			<InfoFormat>text/html</InfoFormat>
      		</GetFeatureInfo>
      	</soap:Body>
      </soap:Envelope>


Under a resource-oriented style, a representative example would be:

.. code-block:: properties

      http://your.domain.com/coastlines/blue/2007-06/coastlinesInCrs84/5e6/42/112/23/35.png


Example GetFeatureInfo Response: KVP Request and Resource-Oriented
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An example of a compliant WMTS service's POX response to a procedural-oriented GetFeatureInfo KVP request operation is presented below. This example was adapted from content in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification. The corresponding XML schema can be found in the same location. The content of a response to a resource-oriented request for a resource representation would be virtually identical.

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <ReguralGridedElevations xmlns="http://www.opengis.uab.es/SITiled/world/etopo2" xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.uab.es/SITiled/world/etopo2 wmtsGetFeatureInfo_response_GML.xsd">
      	<gml:featureMember>
      		<GridPoint_etopo2>
      			<elevation>503.0</elevation>
      			<TileRow>1</TileRow>
      			<TileCol>2</TileCol>
      			<J>86</J>
      			<I>132</I>
      			<Geometry>
      				<gml:Point srsDimension="2" srsName="urn:ogc:def:crs:OGC:1.3:CRS84">
      					<gml:pos>2.50 42.22</gml:pos>
      				</gml:Point>
      			</Geometry>
      		</GridPoint_etopo2>
      	</gml:featureMember>
      </ReguralGridedElevations>


Example GetFeatureInfo Response: SOAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An example of a compliant WMTS service's response to a procedural-oriented SOAP-encoded GetFeatureInfo request is presented below. This example was adapted from an example in the `WMTS Schemas <http://schemas.opengis.net/wmts/>`_, which are part of the WMTS Specification.

.. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
      	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      	xsi:schemaLocation="http://www.w3.org/2003/05/soap-envelope http://www.w3.org/2003/05/soap-envelope">
      	<soap:Body>
      		<FeatureInfoResponse xmlns="http://www.opengis.net/wmts/1.0"
      			xmlns:gml="http://www.opengis.net/gml"
      			xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetFeatureInfo_response.xsd">
      			<ReguralGridedElevations xmlns="http://www.opengis.uab.es/SITiled/world/etopo2"
      				xmlns:gml="http://www.opengis.net/gml"
      				xsi:schemaLocation="http://www.opengis.uab.es/SITiled/world/etopo2 wmtsGetFeatureInfo_response_GML.xsd">
      				<gml:featureMember>
      					<GridPoint_etopo2>
      						<elevation>503.0</elevation>
      						<TileRow>42</TileRow>
      						<TileCol>112</TileCol>
      						<J>23</J>
      						<I>35</I>
      					</GridPoint_etopo2>
      				</gml:featureMember>
      			</ReguralGridedElevations>
      		</FeatureInfoResponse>
      	</soap:Body>
      </soap:Envelope>




... ... LEFT OFF ... ...


References
--------------------

`Ref name <ref_link>`_ - `license name <license_Link>`_
`GeoServer  WMS reference <http://docs.geoserver.org/stable/en/user/services/wms/reference.html>`_ - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
