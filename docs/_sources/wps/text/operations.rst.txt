WPS - Operations
================

This section provides detailed information about the types of operations that a WPS server offers.

.. list-table:: WPS Operations
   :widths: 30 80
   :header-rows: 1

   * - **Operation**
     - **Description**
   * - ``GetCapabilities``
     - Returns service metadata that lists the processes that are offered by the WPS service.
   * - ``DescribeProcess``
     - Returns detailed descriptions of the processes that are offered by the WPS, including descriptions of the inputs and outputs.
   * - ``Execute``
     - Runs a specified process implemented by a server, using the input parameter values provided and returning the output values produced.
   * - ``GetStatus`` (optional)
     - Returns the status of an asynchronously executed job.
   * - ``GetResult`` (optional)
     - Returns the result of a finished processing job that was invoked asynchronously.
   * - ``Dismiss`` (optional)
     - Allows a client to terminate asynchronous processing jobs.

The following are examples of requests that can be sent to operations offered by WPS. The examples can be trialled using tools such as `CURL <https://curl.haxx.se/>`_ , `wget <https://www.gnu.org/software/wget/>`_ or `JMeter <http://jmeter.apache.org/>`_.

.. _wps_getcap:

GetCapabilities
------------------------

Request
^^^^^^^

A WPS server responding to a **GetCapabilities** request returns metadata about the service, including supported operations and processes. Additional metadata describing each process can also be referenced from the capabilities document.

An example of a GetCapabilities request that is sent through the HTTP Get method is:

.. code-block:: properties

  http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?
  service=WPS&
  version=2.0.0&
  request=GetCapabilities


The link to the **GetCapabilities** request is `here <http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?service=WPS&version=2.0.0&request=GetCapabilities>`_

There are three parameters (and values) being passed to the WPS server, ``SERVICE=WPS``, ``VERSION=2.0.0``, and ``REQUEST=GetCapabilities``.

- The ``SERVICE`` parameter tells the server that a WPS request is forthcoming.
- The ``VERSION`` parameter tells the server what version of the service is being requested.
- The ``REQUEST`` parameter tells the server that the operation requested is the `GetCapabilities` operation.

The WPS standard requires that a request always includes these three parameters.
The table below summarizes the parameters and values required to perform the request.

.. list-table:: Parameters of the GetCapabilities Operation
   :widths: 15 15 70
   :header-rows: 1

   * - **Parameter**
     - **Required**
     - **Description**
   * - ``SERVICE``
     - Yes
     - Service name. Value is ``WPS``.
   * - ``VERSION``
     - Yes
     - Service version. Value is one of ``1.0.0``, ``2.0.0``, ``2.0.1``
   * - ``REQUEST``
     - Yes
     - Operation name. Value is ``GetCapabilities``.


Response
^^^^^^^^
The response is a Capabilities XML document with a detailed description of the WPS service.  It contains three main sections:

.. list-table:: Sections Capabilities Document
   :widths: 20 80
   :header-rows: 1

   * - **ServiceIdentification**
     - Contains service metadata such as the service name, keywords, and contact information for the organization operating the server.
   * - **ServiceProvider**
     - Identifies the entity, organization or individual that is offering of the service.
   * - **OperationsMetadata**
     - Lists the available operations, and their endpoints, that can be requested from the service.
   * - **Contents**
     - Lists the available processes that can be requested from the service.



An example GetCapabilities response from a WPS is shown below, with some sections omitted for brevity.

.. code-block:: xml

      <wps:Capabilities xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ows="http://www.opengis.net/ows/2.0" xmlns:xlin="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd" service="WPS" version="2.0.0">
        <ows:ServiceIdentification>
          <ows:Title>52°North WPS 4.0.0-beta.4-SNAPSHOT</ows:Title>
          <ows:Abstract>Service based on the 52°North implementation of WPS</ows:Abstract>
          <ows:Keywords>
            <ows:Keyword>WPS</ows:Keyword>
            <ows:Keyword>geospatial</ows:Keyword>
            <ows:Keyword>geoprocessing</ows:Keyword>
          </ows:Keywords>
          <ows:ServiceType>WPS</ows:ServiceType>
          <ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
          <ows:ServiceTypeVersion>2.0.0</ows:ServiceTypeVersion>
          <ows:Fees>NONE</ows:Fees>
          <ows:AccessConstraints>NONE</ows:AccessConstraints>
        </ows:ServiceIdentification>
        <ows:ServiceProvider>
          <ows:ProviderName>52North</ows:ProviderName>
          <ows:ProviderSite xlin:href="http://www.52north.org/"/>
          <ows:ServiceContact>
            <ows:IndividualName>Your name</ows:IndividualName>
            <ows:ContactInfo>
              <ows:Address>
                <ows:DeliveryPoint/>
                <ows:City/>
                <ows:AdministrativeArea/>
                <ows:PostalCode/>
                <ows:Country/>
                <ows:ElectronicMailAddress/>
              </ows:Address>
            </ows:ContactInfo>
          </ows:ServiceContact>
        </ows:ServiceProvider>
        <ows:OperationsMetadata>
          <ows:Operation name="GetCapabilities">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?"/>
                <ows:Post xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService"/>
              </ows:HTTP>
            </ows:DCP>
          </ows:Operation>
          <ows:Operation name="DescribeProcess">
            <ows:DCP>
              <ows:HTTP>
                <ows:Get xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?"/>
                <ows:Post xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService"/>
              </ows:HTTP>
            </ows:DCP>
          </ows:Operation>
          <ows:Operation name="Execute">
            <ows:DCP>
              <ows:HTTP>
                <ows:Post xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService"/>
              </ows:HTTP>
            </ows:DCP>
          </ows:Operation>
        </ows:OperationsMetadata>
        <ows:Languages>
          <ows:Language>en-US</ows:Language>
        </ows:Languages>
        <wps:Contents>
          <wps:ProcessSummary processVersion="1.1.0" jobControlOptions="sync-execute async-execute" outputTransmission="value reference">
            <ows:Title>org.n52.wps.server.algorithm.SimpleBufferAlgorithm</ows:Title>
            <ows:Identifier>org.n52.wps.server.algorithm.SimpleBufferAlgorithm</ows:Identifier>
            <ows:Metadata xlin:role="Process description" xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?service=WPS&amp;request=DescribeProcess&amp;version=2.0.0&amp;identifier=org.n52.wps.server.algorithm.SimpleBufferAlgorithm"/>
          </wps:ProcessSummary>
          <wps:ProcessSummary processVersion="1.0.0" jobControlOptions="sync-execute async-execute" outputTransmission="value reference">
            <ows:Title>org.n52.wps.server.algorithm.coordinatetransform.CoordinateTransformAlgorithm</ows:Title>
            <ows:Identifier>org.n52.wps.server.algorithm.coordinatetransform.CoordinateTransformAlgorithm</ows:Identifier>
            <ows:Metadata xlin:role="Process description" xlin:href="http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?service=WPS&amp;request=DescribeProcess&amp;version=2.0.0&amp;identifier=org.n52.wps.server.algorithm.coordinatetransform.CoordinateTransformAlgorithm"/>
          </wps:ProcessSummary>
        </wps:Contents>
      </wps:Capabilities>




.. _wps_describeprocess:

DescribeProcess
---------------

Returns detailed descriptions of processes offered by the service. Note that this operation can retrieve descriptions of one or more processes through a single invocation.

Request
^^^^^^^

An example of a DescribeProcess request that returns descriptions of all processes offered by a service when sent through the HTTP Post method is below. In the case of the example server, the request is sent to the endpoint <http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService>.

.. code-block:: xml

      <wps:DescribeProcess service="WPS" version="2.0.0"
        xmlns:ows="http://www.opengis.net/ows/2.0"
        xmlns:wps="http://www.opengis.net/wps/2.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd ">
        <ows:Identifier>all</ows:Identifier>
      </wps:DescribeProcess>

`This is a link to the equivalent request sent through the HTTP Get method. <http://geoprocessing.demo.52north.org:8080/wps/WebProcessingService?service=WPS&version=2.0.0&request=DescribeProcess&Identifier=all>`_

Response
^^^^^^^^
The response is an XML document that describes the processes offered by the service in great detail. Notice how the input and output data types are described in terms of both the mime type, the schema and the number of allowed occurrences. This level of detail is required to ensure that a process accurately identifies the type of data that it is receiving. It is up to developers to decide how strict their WPS implementations should be in matching inputs to the declared mime types. However, to ensure trust in provided WPS services and reduce the risk of errors during invocation, it is recommended that the services enforce the declared mime types.

.. code-block:: xml

            <wps:ProcessOfferings xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ows="http://www.opengis.net/ows/2.0" xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd">
              <wps:ProcessOffering processVersion="1.1.0" jobControlOptions="sync-execute async-execute" outputTransmission="value reference">
                <wps:Process>
                  <ows:Title>org.n52.wps.server.algorithm.SimpleBufferAlgorithm</ows:Title>
                  <ows:Identifier>org.n52.wps.server.algorithm.SimpleBufferAlgorithm</ows:Identifier>
                  <wps:Input minOccurs="1" maxOccurs="1">
                    <ows:Title>width</ows:Title>
                    <ows:Identifier>width</ows:Identifier>
                    <ns:LiteralData xmlns:ns="http://www.opengis.net/wps/2.0">
                      <ns:Format default="true" mimeType="text/plain"/>
                      <ns:Format mimeType="text/xml"/>
                      <LiteralDataDomain>
                        <ows:AnyValue/>
                        <ows:DataType ows:reference="xs:double"/>
                      </LiteralDataDomain>
                    </ns:LiteralData>
                  </wps:Input>
                  <wps:Input minOccurs="1" maxOccurs="1">
                    <ows:Title>data</ows:Title>
                    <ows:Identifier>data</ows:Identifier>
                    <ns:ComplexData xmlns:ns="http://www.opengis.net/wps/2.0">
                      <ns:Format default="true" mimeType="application/vnd.google-earth.kml+xml" schema="http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd"/>
                      <ns:Format mimeType="text/xml; subtype=gml/3.1.1" schema="http://schemas.opengis.net/gml/3.1.1/base/feature.xsd"/>
                    </ns:ComplexData>
                  </wps:Input>
                  <wps:Output>
                    <ows:Title>result</ows:Title>
                    <ows:Identifier>result</ows:Identifier>
                    <ns:ComplexData xmlns:ns="http://www.opengis.net/wps/2.0">
                      <ns:Format default="true" mimeType="application/vnd.google-earth.kml+xml" schema="http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd"/>
                      <ns:Format mimeType="application/x-zipped-shp"/>
                      <ns:Format mimeType="text/xml; subtype=gml/3.1.1" schema="http://schemas.opengis.net/gml/3.1.1/base/feature.xsd"/>
                      <ns:Format mimeType="text/xml; subtype=gml/3.2.1" schema="http://schemas.opengis.net/gml/3.2.1/base/feature.xsd"/>
                    </ns:ComplexData>
                  </wps:Output>
                </wps:Process>
              </wps:ProcessOffering>
            </wps:ProcessOfferings>

.. _wps_execute:


Execute
-------

A WPS server responding to an **Execute** request returns the outputs of the process identified in the request. The inputs may be included directly in the **Execute** request or be passed to the process by reference using web-accessible resources. Typically, if the input is a large file then it is advisable to pass the input data by reference. This means that the WPS can retrieve the input data from the web-accessible resource without having to receive a large request payload.

The requests can be sent through HTTP GET or HTTP POST. As some of the inputs are GML, the following examples use HTTP Post.

Request
^^^^^^^

The following request invokes the ``org.n52.wps.server.algorithm.SimpleBufferAlgorithm`` process. It receives the input data by reference. Notice as well that although the first input in this case is a reference to a WFS **GetFeature** request, the second input is a literal value of "0.05" that specifies the width of the buffer. This shows the ability to accept different input data types on the same process (that is, some inputs may be geospatial data and others may not).

.. code-block:: xml

      <wps:Execute xmlns:wps="http://www.opengis.net/wps/2.0"
      xmlns:ows="http://www.opengis.net/ows/2.0" xmlns:xlink="http://www.w3.org/1999/xlink"
	    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	    xsi:schemaLocation="http://www.opengis.net/wps/2.0 ../wps.xsd" service="WPS"
	    version="2.0.0" response="document" mode="sync">
	    <ows:Identifier>org.n52.wps.server.algorithm.SimpleBufferAlgorithm</ows:Identifier>
		  <wps:Input id="data">
			   <wps:Reference schema="http://schemas.opengis.net/gml/3.1.1/base/feature.xsd" xlink:href="http://geoprocessing.demo.52north.org:8080/geoserver/wfs?SERVICE=WFS&amp;VERSION=1.0.0&amp;REQUEST=GetFeature&amp;TYPENAME=topp:tasmania_roads&amp;SRS=EPSG:4326&amp;OUTPUTFORMAT=GML3"/>
		  </wps:Input>
      <wps:Input id="width">
         <wps:Data><wps:LiteralValue>0.05</wps:LiteralValue></wps:Data>
      </wps:Input>
	   <wps:Output id="result" transmission="value"/>
     </wps:Execute>



Response
^^^^^^^^
The outputs may be returned in the form of an XML response document, or in any other format. The output data may either be embedded within the response document or stored as web-accessible resources. Since the value of the mode attribute in the **Execute** request above is set to ``sync`` the process is invoked synchronously.

An extract of the response resulting from the above request is shown below.

.. code-block:: xml

      <wps:Result xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd">
      <wps:JobID>3a097ae3-d3c0-4ba4-8b85-e6a4af3fe636</wps:JobID>
        <wps:Output id="result">
          <wps:Data schema="http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd" mimeType="application/vnd.google-earth.kml+xml">
            <kml:kml xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:kml="http://earth.google.com/kml/2.1">
              <kml:Document id="featureCollection">
                <kml:Placemark id="ID1">
                  <kml:MultiGeometry>
                    <kml:Polygon>
                      <kml:outerBoundaryIs>
                        <kml:LinearRing>
                          <kml:coordinates>146.57855346804192,-41.201323558388665 146.64342790226314,-41.20524509998472 146.65545052760172,-41.207469488788114 146.6665738407718,-41.21254524781518 146.7890489128575,-41.287748008872335 146.81360198036376,-41.298092497969215  146.44470390635928,-41.19754809396683 146.45373301674724,-41.19373380981566 146.46333276523418,-41.19175430811803 146.4731342388694,-41.19168566001405 146.57855346804192,-41.201323558388665</kml:coordinates>
                        </kml:LinearRing>
                      </kml:outerBoundaryIs>
                    </kml:Polygon>
                  </kml:MultiGeometry>
                </kml:Placemark>
                <kml:Placemark id="ID2">
                  <kml:MultiGeometry>
                    <kml:Polygon>
                      <kml:outerBoundaryIs>
                        <kml:LinearRing>
                          <kml:coordinates>146.99490433143592,-43.3611141137045 147.0000918323004,-43.37843435045301 147.0019192637801,-43.38754567654801 147.00515426378007,-43.41827767654801 147.00521997262746,-43.428079170328616 147.00337224231984,-43.43770515031479 146.9996820800968,-43.44678569549397 146.994291296823,-43.45497184560737 146.98740705727656,-43.461949011496955 146.97929391892245,-43.46744906459044  147.032123580848,-43.29463771588537 147.02899786454023,-43.30636277236813 147.01726386454024,-43.33555677236813 147.01282892777223,-43.34410434310771 147.00683769376235,-43.351643225300926 146.99951238847504,-43.35789378784619 146.99490433143592,-43.3611141137045</kml:coordinates>
                        </kml:LinearRing>
                    </kml:Polygon>
                  </kml:MultiGeometry>
                </kml:Placemark>
            </kml:kml>
        </wps:Output>
      </wps:Result>


When the value of the mode attribute in the Execute element is set to ``async`` the process is invoked asynchronously. An example response from an asynchronous invocation is below.

.. code-block:: xml

            <wps:StatusInfo xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd">
              <wps:JobID>45fa64bd-5ed6-4d69-863b-4402a6df641c</wps:JobID>
              <wps:Status>Accepted</wps:Status>
            </wps:StatusInfo>​


GetStatus
---------

Returns the status of an asynchronously executed job.

Request
^^^^^^^

The request accepts a job identifier (JobID) taken from an **Execute** response.

.. code-block:: xml

            <wps:GetStatus service="WPS" version="2.0.0"
              xmlns:wps="http://www.opengis.net/wps/2.0"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://www.opengis.net/wps/2.0 ../wps.xsd ">
              <wps:JobID>336d5fa5-3bd6-4ee9-81ea-c6bccd2d443e</wps:JobID>
            </wps:GetStatus>​​​​​​​​​​

Response
^^^^^^^^

The response reports on the status of the job. An example response is shown below.

.. code-block:: xml

            <wps:StatusInfo xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd" xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
              <wps:JobID>336d5fa5-3bd6-4ee9-81ea-c6bccd2d443e</wps:JobID>
              <wps:Status>Succeeded</wps:Status>
            </wps:StatusInfo>​


GetResult
---------

Returns the result of a finished processing job that was invoked asynchronously.

Request
^^^^^^^

The request accepts a job identifier (JobID) taken from an **Execute** response.

.. code-block:: xml

            <wps:GetResult service="WPS" version="2.0.0"
              xmlns:wps="http://www.opengis.net/wps/2.0"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://www.opengis.net/wps/2.0 ../wps.xsd ">
              <wps:JobID>336d5fa5-3bd6-4ee9-81ea-c6bccd2d443e</wps:JobID>
            </wps:GetResult>​​​​​​​​​​​​​



Response
^^^^^^^^

The response provides the output from the job that was identified in the request.

.. code-block:: xml

      <wps:Result xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd" xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <wps:JobID>336d5fa5-3bd6-4ee9-81ea-c6bccd2d443e</wps:JobID>
        <wps:Output id="result">
          <wps:Data schema="http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd" mimeType="application/vnd.google-earth.kml+xml">
            <kml:kml xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:kml="http://earth.google.com/kml/2.1">
              <kml:Document id="featureCollection">
                <kml:Placemark id="ID1">
                  <kml:MultiGeometry>
                    <kml:Polygon>
                      <kml:outerBoundaryIs>
                        <kml:LinearRing>
                          <kml:coordinates>146.57855346804192,-41.201323558388665 146.64342790226314,-41.20524509998472 146.65545052760172,-41.207469488788114 146.6665738407718,-41.21254524781518 146.7890489128575,-41.287748008872335 146.81360198036376,-41.298092497969215 146.82208938998681,-41.30267821480601 146.84599365099683,-41.31875219671369  146.45373301674724,-41.19373380981566 146.46333276523418,-41.19175430811803 146.4731342388694,-41.19168566001405 146.57855346804192,-41.201323558388665</kml:coordinates>
                        </kml:LinearRing>
                      </kml:outerBoundaryIs>
                    </kml:Polygon>
                  </kml:MultiGeometry>
                </kml:Placemark>
                <kml:Placemark id="ID2">
                  <kml:MultiGeometry>
                    <kml:Polygon>
                      <kml:outerBoundaryIs>
                        <kml:LinearRing>
                          <kml:coordinates>146.99490433143592,-43.3611141137045 147.0000918323004,-43.37843435045301 147.0019192637801,-43.38754567654801 147.00515426378007,-43.41827767654801 147.00521997262746,-43.428079170328616 147.00337224231984,-43.43770515031479 146.9996820800968,-43.44678569549397 146.994291296823,-43.45497184560737  148.09120661289265,-42.06815547459541 148.09679739523438,-42.076206359689074 148.10071010249564,-42.08519325681052 148.10279437153065,-42.094770804543295 148.1029701050493,-42.10457094309916 148.10123054971098,-42.114217058649416 148.07632854971098,-42.20194005864941</kml:coordinates>
                        </kml:LinearRing>
                      </kml:outerBoundaryIs>
                    </kml:Polygon>
                  </kml:MultiGeometry>
                </kml:Placemark>
              </kml:Document>
            </kml:kml>
          </wps:Data>
        </wps:Output>
      </wps:Result>​



Dismiss
---------

This operation may be provided by WPS extensions to allow clients to instruct a server to terminate a job.

Request
^^^^^^^

The request accepts a job identifier (JobID) taken from an **Execute** response.

.. code-block:: xml

            <wps:Dismiss service=“WPS” version=“2.0.0”
              xmlns:wps=“http://www.opengis.net/wps/2.0”
              xmlns:xsi=“http://www.w3.org/2001/XMLSchema-instance”
              xsi:schemaLocation="http://www.opengis.net/wps/2.0 ../wps.xsd ">
              <wps:JobID>FB6DD4B0-A2BB-11E3-A5E2-0800200C9A66</wps:JobID>
            </wps:Dismiss>

Response
^^^^^^^^

The response reports on the status of the job. An example response is shown below. Notice that if the job has been successfully terminated the status is reported as "Dismissed".

.. code-block:: xml

            <wps:StatusInfo xsi:schemaLocation="http://www.opengis.net/wps/2.0 http://schemas.opengis.net/wps/2.0/wps.xsd" xmlns:wps="http://www.opengis.net/wps/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
              <wps:JobID>FB6DD4B0-A2BB-11E3-A5E2-0800200C9A66</wps:JobID>
              <wps:Status>Dismissed</wps:Status>
            </wps:StatusInfo>​



Exceptions
---------------

When a request from a client to a WPS Server is not performed properly, a Server needs to report an exception.
Where an exception occurs, the server will return a report containing details of the exception.

The following exception report is an example of what is returned when a request for a feature type that is not supported is sent to the server.

.. code-block:: xml

      <ows:ExceptionReport xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd" version="2.0.0">
      <ows:Exception exceptionCode="NoSuchProcess" locator="MyIncorrectProcessName">
      <ows:ExceptionText>One of the identifiers passed does not match with any of the processes offered by this server</ows:ExceptionText>
      </ows:Exception>
      </ows:ExceptionReport>


References
-----------------


`52North WPS reference <http://52north.org/communities/geoprocessing/wps/index.html>`_
