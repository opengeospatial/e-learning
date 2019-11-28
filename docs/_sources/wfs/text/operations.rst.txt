WFS - Operations
================

This section provides detailed information about the types of operations that a WFS server offers. The list includes operations offered by different configurations (formally referred to as conformance classes) of WFS servers.

.. list-table:: WFS Operations
   :widths: 30 80
   :header-rows: 1

   * - **Operation**
     - **Description**
   * - ``GetCapabilities``
     - Retrieves metadata about the service, including supported operations and parameters, and a list of the available feature types.
   * - ``DescribeFeatureType``
     - Returns a description of the structure of feature types and feature properties offered or accepted by an instance of a WFS.
   * - ``GetFeature``
     - Returns a selection of feature instances from a data store published through the WFS.
   * - ``ListStoredQueries``
     - Returns a list of the queries that have been stored inside the WFS instance.
   * - ``DescribeStoredQueries``
     - Returns a description of the queries that have been stored inside the WFS instance.
   * - ``GetPropertyValue`` (optional)
     - Retrieves the value of a feature property or part of the value of a complex feature property for a set of feature instances
   * - ``GetFeatureWithLock`` (optional)
     - Serves a similar function to a GetFeature request but with the additional ability to lock a feature, presumably for subsequent updating or changes.
   * - ``LockFeature`` (optional)
     - Locks a set of feature instances such that no other operations may modify the data while the lock is in place.
   * - ``Transaction`` (optional)
     - Allows the feature instances and their properties to modified or deleted.
   * - ``CreateStoredQuery`` (optional)
     - Creates and stores a query that can be rapidly and easily triggered by a client at a later point in time.
   * - ``DropStoredQuery`` (optional)
     - Deletes a previously stored query from the server.

The following are examples of requests that can be sent to operations offered by simple and basic WFS configurations.

.. _wfs_getcap:

GetCapabilities
------------------------

Request
^^^^^^^

A WFS server responding to a **GetCapabilities** request returns metadata about the service, including supported operations and parameters, and a list of the available feature types.

An example of a GetCapabilities request is:

.. code-block:: properties

  http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?
  SERVICE=WFS&
  REQUEST=GetCapabilities&
  VERSION=2.0.0



`This is a link to a GetCapabilities request. <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?SERVICE=WFS&REQUEST=GetCapabilities&VERSION=2.0.0>`_

There are three parameters (and values) being passed to the WFS server, ``SERVICE=WFS``, ``VERSION=2.0.0``, and ``REQUEST=GetCapabilities``.

- The ``SERVICE`` parameter tells the server that a WFS request is forthcoming.
- The ``VERSION`` parameter tells the server what version of the service is being requested.
- The ``REQUEST`` parameter tells the server that the operation requested is the `GetCapabilities` operation.

The WFS standard requires that requests always includes these three parameters.
The table bellow summarizes the parameters and values required to perform the request.

.. list-table:: Parameters of the GetCapabilities Operation
   :widths: 15 15 70
   :header-rows: 1

   * - **Parameter**
     - **Required**
     - **Description**
   * - ``SERVICE``
     - Yes
     - Service name. Value is ``WFS``.
   * - ``VERSION``
     - Yes
     - Service version. Value is one of ``1.0.0``, ``1.1.0``, ``2.0.0``, ``2.0.2``.
   * - ``REQUEST``
     - Yes
     - Operation name. Value is ``GetCapabilities``.

Response
^^^^^^^^
The response is a Capabilities XML document with a detailed description of the WFS service.  It contains three main sections:

.. list-table:: Sections Capabilities Document
   :widths: 20 80
   :header-rows: 1

   * - **Service**
     - Contains service metadata such as the service name, keywords, and contact information for the organization operating the server.
   * - **FeatureTypeList**
     - Lists and describes the feature types that are provided by the service.
   * - **Operations**
     - Lists the available operations that can be requested from the service.



An example GetCapabilities response from a WFS is shown below, with some sections omitted for brevity.

.. code-block:: xml


      <WFS_Capabilities version="2.0.0" xmlns="http://www.opengis.net/wfs/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:ogc="http://www.opengis.net/ogc" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd">
        <ows:ServiceIdentification>
          <ows:Title>WFS 2.0.0 CITE Setup</ows:Title>
          <ows:Abstract></ows:Abstract>
          <ows:ServiceType codeSpace="http://www.opengeospatial.org/">WFS</ows:ServiceType>
          <ows:ServiceTypeVersion>2.0.0</ows:ServiceTypeVersion>
        </ows:ServiceIdentification>
        <ows:OperationsMetadata>
          <ows:Operation name="GetCapabilities">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?"/>
                <ows:Post xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200"/>
              </ows:HTTP>
            </ows:DCP>
            <ows:Parameter name="AcceptVersions">
              <ows:AllowedValues>
                <ows:Value>2.0.0</ows:Value>
              </ows:AllowedValues>
            </ows:Parameter>
          </ows:Operation>
          <ows:Operation name="GetFeature">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?"/>
                <ows:Post xlink:href="http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200"/>
              </ows:HTTP>
            </ows:DCP>
          </ows:Operation>
      </ows:OperationsMetadata>
        <FeatureTypeList>
          <FeatureType>
            <Name xmlns:gn="urn:x-inspire:specification:gmlas:GeographicalNames:3.0">gn:NamedPlace</Name>
            <Title>gn:NamedPlace</Title>
            <DefaultCRS>urn:ogc:def:crs:EPSG::4326</DefaultCRS>
            <OutputFormats>
              <Format>application/xml; subtype="gml/3.2.1"</Format>
            </OutputFormats>
            <ows:WGS84BoundingBox>
              <ows:LowerCorner>-180.000000 -90.000000</ows:LowerCorner>
              <ows:UpperCorner>180.000000 90.000000</ows:UpperCorner>
            </ows:WGS84BoundingBox>
          </FeatureType>
          <FeatureType>
            <Name xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0">ps:ProtectedSite</Name>
            <Title>ps:ProtectedSite</Title>
            <DefaultCRS>urn:ogc:def:crs:EPSG::4326</DefaultCRS>
            <OutputFormats>
              <Format>application/xml; subtype="gml/3.2.1"</Format>
            </OutputFormats>
            <ows:WGS84BoundingBox>
              <ows:LowerCorner>4.486395 51.604992</ows:LowerCorner>
              <ows:UpperCorner>5.928631 51.680515</ows:UpperCorner>
            </ows:WGS84BoundingBox>
          </FeatureType>
        </FeatureTypeList>
        <fes:Spatial_Capabilities>
          <fes:GeometryOperands xmlns:gml="http://www.opengis.net/gml" xmlns:gml32="http://www.opengis.net/gml">
            <fes:GeometryOperand name="gml:Box"/>
            <fes:GeometryOperand name="gml:Envelope"/>
            <fes:GeometryOperand name="gml:Point"/>
            <fes:GeometryOperand name="gml:LineString"/>
            <fes:GeometryOperand name="gml:Curve"/>
            <fes:GeometryOperand name="gml:Polygon"/>
          </fes:GeometryOperands>
          <fes:SpatialOperators>
            <fes:SpatialOperator name="BBOX"/>
            <fes:SpatialOperator name="Intersects"/>
            <fes:SpatialOperator name="Contains"/>
            <fes:SpatialOperator name="Beyond"/>
          </fes:SpatialOperators>
        </fes:Spatial_Capabilities>
      </WFS_Capabilities>

.. _wfs_getfeature:


GetFeature
-------------


A WFS server responding to a **GetFeature** request returns a collection of geographic feature instances filtered according to a criteria set by the requesting client.

The requests can be sent through HTTP GET or HTTP POST. For simplicity, the following example requests are sent through through HTTP GET only.

Request
^^^^^^^

The most simple GetFeature request is one that downloads the feature collection without any constraints to filter the content by. An example of this type of request is shown below. The ``GetFeature`` request queries the server with a set of parameters describing the geographic features to return. The TYPENAMES parameter determines the collection of feature instances to return.

.. code-block:: properties

      http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?
      SERVICE=WFS&
      VERSION=2.0.0&
      REQUEST=GetFeature&
      TYPENAMES=ps:ProtectedSite



`This is a link to an example of a simple GetFeature request. <hhttp://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=ps:ProtectedSite>`_

Response
^^^^^^^^

An extract of the response resulting from the above request is shown below.

.. code-block:: xml

      <wfs:FeatureCollection
         timeStamp="2017-09-21T18:59:13"
         numberMatched="16"
         numberReturned="16"
         next="https://wfst.axl.aero/AxlRest/wfs?SERVICE=WFS&amp;VERSION=2.0.2&amp;REQUEST=GetFeature&amp;TYPENAMES=ps:ProtectedSite&amp;STARTINDEX=2&amp;COUNT=1"
         xmlns:gts="http://www.isotc211.org/2005/gts"
         xmlns:wfs="http://www.opengis.net/wfs/2.0"
         xmlns:sch="http://purl.oclc.org/dsdl/schematron"
         xmlns:xml="http://www.w3.org/XML/1998/namespace"
         xmlns:base="urn:x-inspire:specification:gmlas:BaseTypes:3.2"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:gco="http://www.isotc211.org/2005/gco"
         xmlns:fes="http://www.opengis.net/fes/2.0"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:ows="http://www.opengis.net/ows/1.1"
         xmlns:gmx="http://www.isotc211.org/2005/gmx"
         xmlns:gss="http://www.isotc211.org/2005/gss"
         xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0"
         xmlns:gsr="http://www.isotc211.org/2005/gsr"
         xmlns:gn="urn:x-inspire:specification:gmlas:GeographicalNames:3.0"
         xmlns:smil20="http://www.w3.org/2001/SMIL20/"
         xmlns:sqm="http://axl.avitech.aero/aviWfsSqm/1.0"
         xmlns:gml="http://www.opengis.net/gml/3.2"
         xmlns:smil20lang="http://www.w3.org/2001/SMIL20/Language"
         xmlns:gmd="http://www.isotc211.org/2005/gmd"
         xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd">
      <wfs:member xmlns:wfs="http://www.opengis.net/wfs/2.0">
        <!-- oldId=none ;oldTime=1487178040 ; oldExpiry=0 ;  ; currentTime=1506020133 ; expired=true;-->
        <ps:ProtectedSite xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0" gml:id="PS_PROTECTEDSITE_16cbb8db-cce1-4e8b-8733-83d53a910ebe">
      ...
        </ps:ProtectedSite>
      </wfs:member></wfs:FeatureCollection>

Count parameter
^^^^^^^^^^^^^^^

Additional parameters can be added to further filter or convert the response from the WFS. The information needed to specify values for parameters, including other parameters that we shall introduce below, can be obtained from the Capabilities document.

To include additional parameters to the GetFeature request above, simply add an ampersand (&) at the end of the URL, then add the name of the parameter, an equal sign and the value to assign to the parameter. For example, the following GetFeature request limits the number of features returned by the server to a single feature instance. The number to limit the response by is determined by the value of the count parameter.

.. code-block:: properties

      https://wfst.axl.aero/AxlRest/wfs?
      service=WFS&
      version=2.0.0&
      request=GetFeature&
      TypeNames=ps:ProtectedSite&
      count=1


`This is a link to the request shown above. <https://wfst.axl.aero/AxlRest/wfs?service=WFS&version=2.0.0&request=GetFeature&TypeNames=ps:ProtectedSite&count=1>`_

The response generated by the request is shown below. Notice that the number of returned feature instances is 1 (shown by the numberReturned attribute in the root wfs:FeatureCollection element).

.. code-block:: xml

      <wfs:FeatureCollection
         timeStamp="2017-09-21T18:55:33"
         numberMatched="16"
         numberReturned="1"
         next="https://wfst.axl.aero/AxlRest/wfs?SERVICE=WFS&amp;VERSION=2.0.2&amp;REQUEST=GetFeature&amp;TYPENAMES=ps:ProtectedSite&amp;STARTINDEX=2&amp;COUNT=1"
         xmlns:gts="http://www.isotc211.org/2005/gts"
         xmlns:wfs="http://www.opengis.net/wfs/2.0"
         xmlns:sch="http://purl.oclc.org/dsdl/schematron"
         xmlns:xml="http://www.w3.org/XML/1998/namespace"
         xmlns:base="urn:x-inspire:specification:gmlas:BaseTypes:3.2"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:gco="http://www.isotc211.org/2005/gco"
         xmlns:fes="http://www.opengis.net/fes/2.0"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:ows="http://www.opengis.net/ows/1.1"
         xmlns:gmx="http://www.isotc211.org/2005/gmx"
         xmlns:gss="http://www.isotc211.org/2005/gss"
         xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0"
         xmlns:gsr="http://www.isotc211.org/2005/gsr"
         xmlns:gn="urn:x-inspire:specification:gmlas:GeographicalNames:3.0"
         xmlns:smil20="http://www.w3.org/2001/SMIL20/"
         xmlns:sqm="http://axl.avitech.aero/aviWfsSqm/1.0"
         xmlns:gml="http://www.opengis.net/gml/3.2"
         xmlns:smil20lang="http://www.w3.org/2001/SMIL20/Language"
         xmlns:gmd="http://www.isotc211.org/2005/gmd"
         xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd">
      <wfs:member xmlns:wfs="http://www.opengis.net/wfs/2.0">
        <!-- oldId=none ;oldTime=1487178040 ; oldExpiry=0 ;  ; currentTime=1506020133 ; expired=true;-->
        <ps:ProtectedSite xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0" gml:id="PS_PROTECTEDSITE_16cbb8db-cce1-4e8b-8733-83d53a910ebe">
          <gml:name>ProtectedSite1</gml:name>
          <ps:geometry>
            <gml:MultiSurface gml:id="PS_PROTECTEDSITE_16cbb8db-cce1-4e8b-8733-83d53a910ebe_PS_GEOMETRY" srsName="urn:ogc:def:crs:EPSG::4326">
              <gml:surfaceMember>
                <gml:Polygon gml:id="GEOMETRY_7fd8f3e7-d283-4ce5-9722-e612bf465a3b" srsName="urn:ogc:def:crs:EPSG::4326">
                  <gml:exterior>
                    <gml:LinearRing>
                      <gml:posList>
      										51.628734 5.507951 51.629015 5.508402 51.629694 5.507409 51.628721 5.507150 51.628734
      										5.507951
      									</gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </ps:geometry>
          <ps:inspireID>
            <base:Identifier>
              <base:localId>FB8DCB4E-03BB-4E8A-BB9D-04A44295DF58</base:localId>
              <base:namespace>NL.9930.EHS</base:namespace>
            </base:Identifier>
          </ps:inspireID>
          <ps:siteDesignation>
            <ps:DesignationType>
              <ps:designationScheme>ecologischeHoofdstructuur</ps:designationScheme>
              <ps:designation>ecologischeHoofdstructuur</ps:designation>
              <ps:percentageUnderDesignation>100</ps:percentageUnderDesignation>
            </ps:DesignationType>
          </ps:siteDesignation>
        </ps:ProtectedSite>
      </wfs:member></wfs:FeatureCollection>


Bounding Box (BBOX) parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another parameter that can be added to a GetFeature request is that of the Bounding Box (BBOX). This parameter is a comma-separated list of four numbers that indicate the minimum and maximum bounding coordinates of the feature instances that should be returned. An example of the use of the BBOX parameter is shown below.

.. code-block:: properties

      http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?service=WFS&version=2.0.0&request=GetFeature&TypeNames=ps:ProtectedSite&BBOX=51.607317,5.106151,51.629884,5.228022

`This is a link to the request shown above. <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?service=WFS&version=2.0.0&request=GetFeature&TypeNames=ps:ProtectedSite&BBOX=51.607317,5.106151,51.629884,5.228022>`_

The response returned by the request above is shown below. The response is presented here with some content missing for brevity.

.. code-block:: xml

  <wfs:FeatureCollection xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wfs="http://www.opengis.net/wfs/2.0" timeStamp="2017-09-21T18:14:50Z" xmlns:gml="http://www.opengis.net/gml/3.2" numberMatched="1" numberReturned="1">
  <wfs:member>
  <ps:ProtectedSite xmlns:ps="urn:x-inspire:specification:gmlas:ProtectedSites:3.0" gml:id="PS_PROTECTEDSITE_a367af0b-9457-4445-9cbd-eb48ae7a844a">
  ...
  </ps:ProtectedSite>
  </wfs:member>
  </wfs:FeatureCollection>

PropetyName parameter
^^^^^^^^^^^^^^^^^^^^^


Another parameter that can be added to a GetFeature request is the propertyName. This parameter returns feature instances with only the specified property included. This functionality is particularly useful in situations where feature types with several properties are being served over a network with limited bandwidth. The client application can pick and choose which properties they want returned within the feature instances. An example of the use of this parameter is shown below.

.. code-block:: properties

      https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=getfeature&service=wfs&typenames=ci:City&count=3&propertyName=inhabitants

`This is a link to the request shown above. <https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=getfeature&service=wfs&typenames=ci:City&count=3&propertyName=inhabitants>`_

The response returned by the request above is shown below.

.. code-block:: xml

  <wfs:FeatureCollection timeStamp="2017-09-21T21:17:32.296+02:00" numberReturned="3" numberMatched="unknown" xmlns="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <wfs:member>
  <City gml:id="City.10">
  <location>
  <gml:Point gml:id="city.id.10.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
  <gml:pos>486890.340 5881020.962</gml:pos>
  </gml:Point>
  </location>
  <inhabitants>547300</inhabitants>
  </City>
  </wfs:member>
  <wfs:member>
  <City gml:id="City.11">
  <location>
  <gml:Point gml:id="city.id.11.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
  <gml:pos>364883.268 5620035.394</gml:pos>
  </gml:Point>
  </location>
  <inhabitants>324800</inhabitants>
  </City>
  </wfs:member>
  <wfs:member>
  <City gml:id="City.9">
  <location>
  <gml:Point gml:id="city.id.9.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
  <gml:pos>361905.275 5702287.179</gml:pos>
  </gml:Point>
  </location>
  <inhabitants>574600</inhabitants>
  </City>
  </wfs:member>
  </wfs:FeatureCollection>


sortBy parameter
^^^^^^^^^^^^^^^^

The results returned by a WFS can also be organised in a particular order through the sortBy parameter. This parameter returns feature instances in a sequence determined by the specified parameter. This functionality is particularly useful in situations where feature types have properties representing quantities or populations. An example of the use of this parameter is shown below.

.. code-block:: properties

      https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=getfeature&service=wfs&typenames=ci:City&sortBy=inhabitants&propertyName=inhabitants

`The link to the request above is shown below. <https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=getfeature&service=wfs&typenames=ci:City&sortBy=inhabitants&propertyName=inhabitants>`_

The response resulting from the request above is shown below. Some content has been omitted for brevity.

.. code-block:: xml

      <?xml version="1.0" encoding="utf-8"?>
      <wfs:FeatureCollection timeStamp="2017-09-21T21:17:32.296+02:00" numberReturned="11" numberMatched="unknown" xmlns="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <wfs:member>
      <City gml:id="City.11">
      <location>
      <gml:Point gml:id="city.id.11.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
      <gml:pos>364883.268 5620035.394</gml:pos>
      </gml:Point>
      </location>
      <inhabitants>324800</inhabitants>
      </City>
      </wfs:member>
      <wfs:member>
      <City gml:id="City.10">
      <location>
      <gml:Point gml:id="city.id.10.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
      <gml:pos>486890.340 5881020.962</gml:pos>
      </gml:Point>
      </location>
      <inhabitants>547300</inhabitants>
      </City>
      </wfs:member>
      <wfs:member>
      <City gml:id="City.9">
      <location>
      <gml:Point gml:id="city.id.9.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
      <gml:pos>361905.275 5702287.179</gml:pos>
      </gml:Point>
      </location>
      <inhabitants>574600</inhabitants>
      </City>
      </wfs:member>
      </wfs:FeatureCollection>

srsName parameter
^^^^^^^^^^^^^^^^^

This parameter is used to specify the spatial reference system to encode feature geometries in. The spatial reference systems allowed for each feature type can be identified from the GetCapabilities response.

.. code-block:: properties

      https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=getfeature&service=wfs&typenames=ci:City&count=1&srsName=urn:ogc:def:crs:EPSG::4326

`The link to the request above is shown below. <https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=getfeature&service=wfs&typenames=ci:City&count=1&srsName=urn:ogc:def:crs:EPSG::4326>`_

The response resulting from the request above is shown below. Some content has been omitted for brevity.

.. code-block:: xml

      <wfs:FeatureCollection timeStamp="2017-09-21T21:26:02.213+02:00" numberReturned="1" numberMatched="unknown" xmlns="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <wfs:boundedBy>
      <gml:Envelope srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2">
      <gml:lowerCorner>52.521400003005 13.405700006106</gml:lowerCorner>
      <gml:upperCorner>52.521400003005 13.405700006106</gml:upperCorner>
      </gml:Envelope>
      </wfs:boundedBy>
      <wfs:member>
      <City gml:id="City.1">
      <name>Berlin</name>
      <location>
      <gml:Point gml:id="city.id.1.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2">
      <gml:pos>52.521400003005 13.405700006106</gml:pos>
      </gml:Point>
      </location>
      <country>Germany</country>
      <inhabitants>3460700</inhabitants>
      <lzi>2011-03-17T15:32:54Z</lzi>
      <function>capital</function>
      </City>
      </wfs:member>
      </wfs:FeatureCollection>

featureId parameter
^^^^^^^^^^^^^^^^^^^

This parameter is used to filter the features returned by the request.

.. code-block:: properties

      http://localhost:8080/geoserver/wfs?
      request=GetFeature&
      version=2.0.0&
      typeName=topp:states&
      FEATUREID=states.3

`The link to the request above is shown below. <http://localhost:8080/geoserver/wfs?request=GetFeature&version=2.0.0&typeName=topp:states&FEATUREID=states.3>`_

The response resulting from the request above is shown below. Some content has been omitted for brevity.

.. code-block:: xml

      <wfs:FeatureCollection xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:topp="http://www.openplans.org/topp" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" numberMatched="1" numberReturned="1" timeStamp="2017-09-21T19:38:52.788Z">
      <wfs:member>
      <topp:states gml:id="states.3">
      <topp:the_geom>
      <gml:MultiSurface srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2">
      <gml:surfaceMember><gml:Polygon><gml:exterior><gml:LinearRing><gml:posList>38.557476 -75.70742 38.649551 -75.71106 38.83017 -75.724937 39.141548 -75.752922 39.247753 -75.761658 38.450451 -75.093094 38.455208 -75.350204 38.463066 -75.69915 38.557476 -75.70742</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></gml:surfaceMember>
      </gml:MultiSurface>
      </topp:the_geom>
      <topp:STATE_NAME>Delaware</topp:STATE_NAME>
      <topp:SAMP_POP>102776.0</topp:SAMP_POP>
      </topp:states>
      </wfs:member>
      </wfs:FeatureCollection>


query action
^^^^^^^^^^^^

Up to now, we have only presented GetFeature request examples sent as URLs through the HTTP Get method. It is also possible to send the body of the request as an XML document through the HTTP Post method.

The following is an example of a GetFeature request that contains a query action and is sent through the HTTP Post method.

The request is sent to the following URL `https://services.interactive-instruments.de/ogc-reference/simple/wfs <https://services.interactive-instruments.de/ogc-reference/simple/wfs>`_

.. code-block:: xml

      <wfs:GetFeature service="WFS" version="2.0.0"
          xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:ci="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:fes="http://www.opengis.net/fes/2.0"
          xmlns:sf="http://www.openplans.org/spearfish" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd">
          <wfs:Query typeNames="ci:City">
          <wfs:PropertyName resolve="local">ci:inhabitants</wfs:PropertyName>
              <fes:Filter>
                  <fes:PropertyIsLessThan>
                     <fes:ValueReference>ci:inhabitants</fes:ValueReference>
                     <fes:Literal>400000</fes:Literal>
                  </fes:PropertyIsLessThan>
              </fes:Filter>
          </wfs:Query>
      </wfs:GetFeature>



The response returned by the request above is shown below.

.. code-block:: xml

      <wfs:FeatureCollection timeStamp="2017-09-22T09:56:55.908+02:00" numberReturned="1" numberMatched="unknown" xmlns="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities https://services.interactive-instruments.de/ogc-reference/schema/demo/cities/4.1/Cities.xsd http://www.opengis.net/wfs/2.0 https://services.interactive-instruments.de/ogc-reference/schema/ogc/wfs/2.0/wfs.xsd http://www.opengis.net/gml/3.2 https://services.interactive-instruments.de/ogc-reference/schema/ogc/gml/3.2.1/gml.xsd http://www.opengis.net/gml/3.2 https://services.interactive-instruments.de/ogc-reference/schema/ogc/gml/3.2.1/gml.xsd">
      <wfs:boundedBy>
      <gml:Envelope srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
      <gml:lowerCorner>364883.268 5620035.394</gml:lowerCorner>
      <gml:upperCorner>364883.268 5620035.394</gml:upperCorner>
      </gml:Envelope>
      </wfs:boundedBy>
      <wfs:member>
      <City gml:id="City.11">
      <name>Bonn</name>
      <location>
      <gml:Point gml:id="city.id.11.location.Geom_0" srsName="urn:ogc:def:crs:EPSG::25832" srsDimension="2">
      <gml:pos>364883.268 5620035.394</gml:pos>
      </gml:Point>
      </location>
      <country>Germany</country>
      <inhabitants>324800</inhabitants>
      </City>
      </wfs:member>
      </wfs:FeatureCollection>

.. _wfs_getpropertyvalue:

GetPropertyValue
---------------

Returns the value of the feature property specified in the request. This operation is most useful when the server is being accessed over networks with limited bandwidth because it returns only the property value rather than the complete feature instance data.

Request
^^^^^^^

The following is an example of a GetPropertyValue request that contains a query action and is sent through the HTTP POST method.

The request is sent to the following URL `https://services.interactive-instruments.de/ogc-reference/simple/wfs <https://services.interactive-instruments.de/ogc-reference/simple/wfs>`_

.. code-block:: xml

      <wfs:GetPropertyValue service="WFS" version="2.0.0"
         valueReference="ci:inhabitants"
         resolve="local"
         resolveDepth="*"
          xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:ci="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:fes="http://www.opengis.net/fes/2.0"
          xmlns:sf="http://www.openplans.org/spearfish" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd">
          <wfs:Query typeNames="ci:City">
              <fes:Filter>
                  <fes:PropertyIsLessThan>
                     <fes:ValueReference>ci:inhabitants</fes:ValueReference>
                     <fes:Literal>400000</fes:Literal>
                  </fes:PropertyIsLessThan>
              </fes:Filter>
          </wfs:Query>
      </wfs:GetPropertyValue>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

      <wfs:ValueCollection timeStamp="2017-09-22T10:06:30.991+02:00" numberReturned="1" numberMatched="unknown" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <wfs:member>324800</wfs:member>
      </wfs:ValueCollection>

.. _wfs_describefeaturetype:

DescribeFeatureType
-------------------

Returns a description of the structure, including properties, of the feature type specified in the request.

Request
^^^^^^^

An example of a DescribeFeatureType request is:

.. code-block:: properties

      https://services.interactive-instruments.de/ogc-reference/simple/wfs?
      version=2.0.0&
      request=describeFeatureType&
      service=wfs&
      typenames=ci:City


`This is a link to the request presented above. <https://services.interactive-instruments.de/ogc-reference/simple/wfs?version=2.0.0&request=describeFeatureType&service=wfs&typenames=ci:City>`_

Response
^^^^^^^^
The response is an XML schema definition document with a detailed description of the specified feature type. Note that in some cases the XML schema definition document may import externally hosted definitions.

.. code-block:: xml

      <schema targetNamespace="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" xmlns:ci="http://www.interactive-instruments.de/namespaces/demo/cities/4.1/cities" xmlns:gml="http://www.opengis.net/gml/3.2">
      <import namespace="http://www.opengis.net/gml/3.2" schemaLocation="https://services.interactive-instruments.de/ogc-reference/schema/ogc/gml/3.2.1/gml.xsd"/>
      <element name="City" substitutionGroup="ci:NamedGeoObject" type="ci:CityType"/>
      <element abstract="true" name="NamedGeoObject" substitutionGroup="gml:AbstractFeature" type="ci:NamedGeoObjectType"/>
      <complexType name="CityType">
      <complexContent>
      <extension base="ci:NamedGeoObjectType">
      <sequence>
      <element name="location" type="gml:PointPropertyType"/>
      <element maxOccurs="unbounded" minOccurs="0" name="alternativeName" type="ci:AlternativeNamePropertyType"/>
      <element name="country" type="string"/>
      <element name="inhabitants" type="integer"/>
      <element name="lzi" type="dateTime"/>
      <element name="function" nillable="true" type="string"/>
      <element maxOccurs="unbounded" minOccurs="0" name="district" type="gml:ReferenceType"/>
      <element maxOccurs="unbounded" minOccurs="0" name="passingRiver" type="gml:ReferenceType"/>
      </sequence>
      </extension>
      </complexContent>
      </complexType>
      <complexType name="NamedGeoObjectType">
      <complexContent>
      <extension base="gml:AbstractFeatureType">
      <sequence>
      <element minOccurs="0" name="name" type="string"/>
      </sequence>
      </extension>
      </complexContent>
      </complexType>
      <complexType name="AlternativeNamePropertyType">
      <sequence>
      <element ref="ci:AlternativeName"/>
      </sequence>
      </complexType>
      <element name="AlternativeName" substitutionGroup="gml:AbstractObject" type="ci:AlternativeNameType"/>
      <complexType name="AlternativeNameType">
      <sequence>
      <element name="name" type="string"/>
      <element name="language" type="string"/>
      </sequence>
      </complexType>
      </schema>


Stored Queries
--------------

With a brief single-line URL, stored queries allow client applications to invoke what may originally have been a query formed of multiple lines of XML.

A stored query expression may be used in a GetPropertyValue, GetFeature, GetFeatureWithLock or LockFeature operation. Parameters can be passed to the stored query to be acted upon by the requested operation.

All servers shall implement the ability to list, describe and execute a stored query that fetches features based on their identifier. Additional stored queries may also be offered.

.. _wfs_liststoredqueries:

ListStoredQueries
---------------

Returns a list of the queries that have been stored inside the server.

Request
^^^^^^^

An example of a ListStoredQueries request is:

.. code-block:: properties

      http://localhost:8080/geoserver/wfs?
      request=ListStoredQueries&
      version=2.0.0

`This is a link to the request presented above. <http://localhost:8080/geoserver/wfs?request=ListStoredQueries&version=2.0.0>`_

Response
^^^^^^^^
The response is an XML document that presents the identifier and name of each query stored in the server. The identifier is used when calling the stored query through the STOREDQUERY_ID parameter in a GetFeature request for example.

.. code-block:: xml

            <wfs:ListStoredQueriesResponse xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <wfs:StoredQuery id="urn:ogc:def:query:OGC-WFS::GetFeatureById">
            <wfs:Title xml:lang="en">Get feature by identifier</wfs:Title>
            <wfs:ReturnFeatureType/>
            </wfs:StoredQuery>
            </wfs:ListStoredQueriesResponse>


.. _wfs_describestoredqueries:

DescribeStoredQueries
---------------------

Returns a description of the stored queries referenced in the request parameters.

Request
^^^^^^^

An example of a DescribeStoredQueries request is:

.. code-block:: properties

      http://localhost:8080/geoserver/wfs?
      request=DescribeStoredQueries&
      STOREDQUERY_ID=urn:ogc:def:query:OGC-WFS::GetFeatureById&
      version=2.0.0

`This is a link to the request presented above. <http://localhost:8080/geoserver/wfs?request=DescribeStoredQueries&version=2.0.0&STOREDQUERY_ID=urn:ogc:def:query:OGC-WFS::GetFeatureById>`_

Response
^^^^^^^^
The response is an XML document that describes the stored query specified by the identifier specified by the STOREDQUERY_ID parameter.

.. code-block:: xml

            <wfs:DescribeStoredQueriesResponse xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <wfs:StoredQueryDescription id="urn:ogc:def:query:OGC-WFS::GetFeatureById">
            <wfs:Title xml:lang="en">Get feature by identifier</wfs:Title>
            <wfs:Parameter name="ID" type="xs:string"/>
            <wfs:QueryExpressionText isPrivate="true" language="urn:ogc:def:queryLanguage:OGC-WFS::WFS_QueryExpression" returnFeatureTypes=""/>
            </wfs:StoredQueryDescription>
            </wfs:DescribeStoredQueriesResponse>

.. _wfs_transaction:

Transaction
-----------

This optional operation allows the feature instances and their properties to be updated or deleted. The operation can also be used to insert new features. The WFS standard does not enforce any particular security model, therefore implementations are expected to implement a security model appropriate for their own infrastructure.


Request
^^^^^^^

An example request is shown below. Since the request modifies data, we suggest installing a local instance of a WFS. The following example was tested against a WFS instance hosted locally at <http://localhost:8080/geoserver/wfs>

.. code-block:: xml

            <wfs:Transaction version="2.0.0" service="WFS"
             xmlns="http://www.someserver.com/myns"
             xmlns:fes="http://www.opengis.net/fes/2.0"
             xmlns:topp="http://www.openplans.org/topp"
             xmlns:wfs="http://www.opengis.net/wfs/2.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0.0/wfs.xsd">
             <wfs:Update typeName="topp:tasmania_roads">
             <wfs:Property>
             <wfs:ValueReference>TYPE</wfs:ValueReference>
             <wfs:Value>road</wfs:Value>
             </wfs:Property>
             <fes:Filter>
             <fes:ResourceId rid="tasmania_roads.1"/>
             </fes:Filter>
             </wfs:Update>
            </wfs:Transaction>

Response
^^^^^^^^
The response is an XML document that confirms whether the transaction was successful.

.. code-block:: xml

          <wfs:TransactionResponse xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://localhost:8080/geoserver/schemas/wfs/2.0/wfs.xsd">
          <wfs:TransactionSummary>
          <wfs:totalInserted>0</wfs:totalInserted>
          <wfs:totalUpdated>1</wfs:totalUpdated>
          <wfs:totalReplaced>0</wfs:totalReplaced>
          <wfs:totalDeleted>0</wfs:totalDeleted>
          </wfs:TransactionSummary>
          <wfs:UpdateResults><wfs:Feature>
          <fes:ResourceId rid="tasmania_roads.1"/>
          </wfs:Feature>
          </wfs:UpdateResults>
          </wfs:TransactionResponse>


.. _wfs_getfeaturewithlock:

GetFeatureWithLock
------------------

Serves a similar function to a GetFeature request but with the additional ability to lock a feature, presumably for subsequent updating or changes.

Request
^^^^^^^

An example request is shown below. Since the request modifies the state of a data source, we suggest using a local instance of a WFS. The following example was tested against a WFS instance hosted locally at <http://localhost:8080/geoserver/wfs>

.. code-block:: xml

            <wfs:GetFeatureWithLock service="WFS" version="2.0.0"
             handle="GetFeatureWithLock-tc1" expiry="5" resultType="results"
             xmlns:topp="http://www.openplans.org/topp"
             xmlns:fes="http://www.opengis.net/fes/2.0"
             xmlns:wfs="http://www.opengis.net/wfs/2.0"
             valueReference="the_geom"  count="1">
              <wfs:Query typeNames="topp:states"/>
            </wfs:GetFeatureWithLock>

Response
^^^^^^^^
The response is a feature collection similar to that received from a GetFeature response. The example below has been shortened for brevity.

.. code-block:: xml

          <wfs:FeatureCollection xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:topp="http://www.openplans.org/topp" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" lockId="GetFeatureWithLock-tc1_6badb1c771c6ee70" numberMatched="49" numberReturned="1" timeStamp="2017-09-29T07:25:43.601Z" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://localhost:8080/geoserver/schemas/wfs/2.0/wfs.xsd http://www.openplans.org/topp http://localhost:8080/geoserver/wfs?service=WFS&amp;version=2.0.0&amp;request=DescribeFeatureType&amp;typeName=topp%3Astates http://www.opengis.net/gml/3.2 http://localhost:8080/geoserver/schemas/gml/3.2.1/gml.xsd">
          <wfs:member>
          <topp:states gml:id="states.1">
          <topp:the_geom>
          <gml:MultiSurface srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2"><gml:surfaceMember><gml:Polygon><gml:exterior><gml:LinearRing><gml:posList>37.51099 -88.071564 37.476273 -88.087883 37.628479 -88.157631 37.583572 -88.134171 37.51099 -88.071564</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></gml:surfaceMember></gml:MultiSurface>
          </topp:the_geom>
          <topp:STATE_NAME>Illinois</topp:STATE_NAME>
          <topp:STATE_FIPS>17</topp:STATE_FIPS>
          <topp:SAMP_POP>1747776.0</topp:SAMP_POP>
          </topp:states>
          </wfs:member>
          </wfs:FeatureCollection>


.. _wfs_lockfeature:

LockFeature
-----------

Locks a set of feature instances such that no other operations may modify the data while the lock is in place.

Request
^^^^^^^

An example request is shown below. Since the request modifies the state of a data source, we suggest using a local instance of a WFS. The following example was tested against a WFS instance hosted locally at <http://localhost:8080/geoserver/wfs>

.. code-block:: xml

            <wfs:LockFeature
               service="WFS"
               version="2.0.0"
               expiry="5"
               xmlns:topp="http://www.openplans.org/topp"
               xmlns:wfs="http://www.opengis.net/wfs/2.0"
               xmlns:ogc="http://www.opengis.net/ogc"
               xmlns:fes="http://www.opengis.net/fes/2.0"
               xmlns:gml="http://www.opengis.net/gml"
               xmlns:myns="http://www.example.com/myns"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >
               <wfs:Query typeNames="topp:states">
                    <fes:Filter>
                        <fes:PropertyIsEqualTo>
                           <fes:ValueReference>topp:STATE_NAME</fes:ValueReference>
                           <fes:Literal>Illinois</fes:Literal>
                        </fes:PropertyIsEqualTo>
                    </fes:Filter>
               </wfs:Query>
            </wfs:LockFeature>

Response
^^^^^^^^
The response is a feature collection similar to that received from a GetFeature response. The example below has been shortened for brevity.

.. code-block:: xml

          <wfs:LockFeatureResponse xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" lockId="GeoServer_5dcc3c771e1b15c" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://localhost:8080/geoserver/schemas/wfs/2.0/wfs.xsd">
              <wfs:FeaturesLocked><fes:ResourceId rid="states.1"/></wfs:FeaturesLocked>
          </wfs:LockFeatureResponse>

.. _wfs_createstoredquery:

CreateStoredQuery
-----------------

Creates and stores a query that can be rapidly and easily triggered by a client at a later point in time.

Request
^^^^^^^

An example request is shown below. Since the request persists a query, we suggest using a local instance of a WFS. The following example was tested against a WFS instance hosted locally at <http://localhost:8080/geoserver/wfs>

.. code-block:: xml

            <wfs:CreateStoredQuery service='WFS' version='2.0.0'
             xmlns:wfs='http://www.opengis.net/wfs/2.0'
             xmlns:fes='http://www.opengis.org/fes/2.0'
             xmlns:gml='http://www.opengis.net/gml/3.2'
             xmlns:myns='http://www.someserver.com/myns'
             xmlns:xsd='http://www.w3.org/2001/XMLSchema'
             xmlns:topp='http://www.openplans.org/topp'>
              <wfs:StoredQueryDefinition id='stateStoredQuery'>
                <wfs:Parameter name='stateName' type='xsd:String'/>
                <wfs:QueryExpressionText
                 returnFeatureTypes='topp:states'
                 language='urn:ogc:def:queryLanguage:OGC-WFS::WFS_QueryExpression'
                 isPrivate='false'>
                  <wfs:Query typeNames='topp:states'>
                    <fes:Filter>
                        <fes:PropertyIsEqualTo>
                           <fes:ValueReference>topp:STATE_NAME</fes:ValueReference>
                           <fes:Literal>${stateName}</fes:Literal>
                        </fes:PropertyIsEqualTo>
                    </fes:Filter>
                  </wfs:Query>
                </wfs:QueryExpressionText>
              </wfs:StoredQueryDefinition>
            </wfs:CreateStoredQuery>

Response
^^^^^^^^
An example response is shown below.

.. code-block:: xml

          <wfs:CreateStoredQueryResponse xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" status="OK" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://localhost:8080/geoserver/schemas/wfs/2.0/wfs.xsd"/>


.. _wfs_dropstoredquery:

DropStoredQuery
-----------------

Deletes a previously stored query from the server.

Request
^^^^^^^

An example request is shown below. Since the request deletes a previously stored query, we suggest installing a local instance of a WFS. The following example was tested against a WFS instance hosted locally at <http://localhost:8080/geoserver/wfs>

.. code-block:: xml

            <wfs:DropStoredQuery
             xmlns:wfs='http://www.opengis.net/wfs/2.0'
             service='WFS' id='myStoredQuery'/>

Response
^^^^^^^^

An example response is shown below:

.. code-block:: xml

          <wfs:DropStoredQueryResponse xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" status="OK" xsi:schemaLocation="http://www.opengis.net/wfs/2.0 http://localhost:8080/geoserver/schemas/wfs/2.0/wfs.xsd"/>


.. _wfs_exceptions:

Exceptions
---------------

When a request from a client to a WFS Server is not performed properly, a Server needs to report an exception.
Where an exception occurs, the server will return a report containing details of the exception.

The following exception report is an example of what is returned when a request for a feature type that is not supported is sent to the server.

.. code-block:: xml

      <ows:ExceptionReport xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd" version="2.0.0">
      <ows:Exception exceptionCode="InvalidParameterValue" locator="typeName">
      <ows:ExceptionText>Feature type with name 'AllProtectedSite' is not served by this WFS.</ows:ExceptionText>
      </ows:Exception>
      </ows:ExceptionReport>


References
-----------------

- `Deegree WFS reference <http://download.deegree.org/documentation/3.3.20/html/>`_
- `GeoServer WFS reference <http://docs.geoserver.org/stable/en/user/services/wfs/reference.html>`_
- `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
