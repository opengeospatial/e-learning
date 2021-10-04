SOS - Operations
================

This section provides detailed information about the types of operations that an SOS server offers. Before presenting the operations, it is worth reviewing the terminology used by SOS.

Consider a situation where sensors have been deployed at an industrial estate to monitor carbon monoxide emissions. Each sensor has been placed in a separate building. In this case, each building is a feature-of-interest, each physical sensor represents a procedure and each building's carbon monoxide emission is an observed property. The act of measuring the carbon monoxide emission at a point in time is an observation.

* Feature: Abstraction of real-world phenomena.

* Measurement: Set of operations having the object of determining the value of a quantity.

* Observed Property: Facet or attribute of an object referenced by a name which is observed by a procedure.

* Observation: Act of observing a property.

* Observation Offering: An Observation Offering groups collections of observations produced by one procedure, e.g., a sensor system, and lists the basic metadata for the associated observations including the observed properties of the observations.

* Procedure: Method, algorithm, instrument, sensor, or system of these which may be used in making an observation.

* Sensor: Entity that provides information about an observed property as its output. A sensor uses a combination of physical, chemical or biological means in order to estimate the underlying observed property. At the end of the measuring chain electronic devices produce signals to be processed.

* Sensor System: System whose components are sensors. A sensor system as a whole may itself be referred to as a sensor with an own management and sensor output interface. In addition, the components of a sensor system are individually addressable.

The above concepts are applied by SOS through the series of operations listed in the following table.

.. list-table:: SOS Operations
   :widths: 30 80
   :header-rows: 1

   * - **Operation**
     - **Description**
   * - ``GetCapabilities``
     - Returns service metadata that lists the observation offerings that are available from the SOS service.
   * - ``DescribeSensor``
     - Returns a description of the procedures or sensors associated with an SOS.
   * - ``GetObservation``
     - Returns observation data that has been collected by the procedure or sensor.
   * - ``GetFeatureOfInterest`` (optional)
     - Returns a description of the features of interest for which the SOS offers observations.
   * - ``GetObservationById`` (optional)
     - Allows the client application to retrieve an observation by passing a pointer to that observation.
   * - ``InsertSensor`` (optional)
     - Registers a new sensor system in the SOS.
   * - ``DeleteSensor`` (optional)
     - Deletes a new sensor system from the SOS.
   * - ``InsertObservation`` (optional)
     - Allows client applications to insert new observations for a registered sensor system.
   * - ``InsertResultTemplate`` (optional)
     - Allows client applications to upload a template for result values such that result values that conform to the template can be inserted into the SOS using subsequent calls of the InsertResult operation.
   * - ``InsertResult`` (optional)
     - Allows a client application to insert new observations for a sensor system by inserting only the results of the observations and reusing other metadata provided by a template.
   * - ``GetResultTemplate`` (optional)
     - Returns a result template that describes the exact structure used by a specific procedure or sensor to generate a new observation result.
   * - ``GetResult`` (optional)
     - Allows retrieving just the result values of observations without the entire metadata of the observation.



The following are examples of requests that can be sent to operations offered by SOS. The examples can be trialled using tools such as `CURL <https://curl.haxx.se/>`_ , `wget <https://www.gnu.org/software/wget/>`_ or `JMeter <http://jmeter.apache.org/>`_.

.. _sos_getcap:

GetCapabilities
------------------------

This operation returns metadata and other descriptive information about the SOS.

Request
^^^^^^^

Consistent with other OGC web services a **GetCapabilities** request accepts the service identifier, version number and request identifier as parameters. An example of a GetCapabilities request that is sent through the HTTP Get method is:

.. code-block:: properties

  http://sensorweb.demo.52north.org/52n-sos-webapp/service?
  service=SOS&
  version=2.0.0&
  request=GetCapabilities


The link to the **GetCapabilities** request is `here <http://sensorweb.demo.52north.org/52n-sos-webapp/service?service=SOS&request=GetCapabilities&version=2.0.0>`_

In the example above, the parameters (and values) being passed to the SOS server, ``SERVICE=SOS``, ``VERSION=2.0.0``, and ``REQUEST=GetCapabilities``.

- The ``SERVICE`` parameter tells the server that an SOS request is forthcoming.
- The ``VERSION`` parameter tells the server what version of the service is being requested.
- The ``REQUEST`` parameter tells the server that the operation requested is the `GetCapabilities` operation.

The table below summarizes the parameters and values required to perform the request.

.. list-table:: Parameters of the GetCapabilities Operation
   :widths: 15 15 70
   :header-rows: 1

   * - **Parameter**
     - **Description**
   * - ``SERVICE``
     - Service name. Value is ``SOS``.
   * - ``VERSION``
     - Service version. Value is one of ``1.0.0``, ``2.0.0``
   * - ``REQUEST``
     - Operation name. Value is ``GetCapabilities``.


Response
^^^^^^^^
The response is a Capabilities XML document with a detailed description of the SOS service.  It contains three main sections:

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
     - Lists the available procedures, sensors and observation offerings that can be requested from the service.



An example GetCapabilities response from an SOS is shown below, with some sections omitted for brevity.

.. code-block:: xml

        <sos:Capabilities xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fes="http://www.opengis.net/fes/2.0" xmlns:swes="http://www.opengis.net/swes/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/fes/2.0 http://schemas.opengis.net/filter/2.0/filterAll.xsd http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swes.xsd http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosGetCapabilities.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsAll.xsd">
          <ows:ServiceIdentification>
            <ows:Title xml:lang="eng">52N SOS</ows:Title>
            <ows:Abstract xml:lang="eng">52North Sensor Observation Service - Data Access for the Sensor Web</ows:Abstract>
            <ows:ServiceType>SOS</ows:ServiceType>
            <ows:ServiceTypeVersion>2.0.0</ows:ServiceTypeVersion>
            <ows:Profile>http://www.opengis.net/spec/SOS/1.0/conf/core</ows:Profile>
            <ows:Profile>http://www.opengis.net/spec/SWE/2.0/conf/core</ows:Profile>
            <ows:Fees>NONE</ows:Fees>
            <ows:AccessConstraints>NONE</ows:AccessConstraints>
          </ows:ServiceIdentification>
          <ows:ServiceProvider>
            <ows:ProviderName>52North</ows:ProviderName>
            <ows:ProviderSite xlink:href="http://52north.org/swe"/>
            <ows:ServiceContact>
              <ows:IndividualName>Oliver Twist</ows:IndividualName>
              <ows:ContactInfo>
                <ows:Phone>
                  <ows:Voice>+49(0)251/396 371-0</ows:Voice>
                </ows:Phone>
              </ows:ContactInfo>
            </ows:ServiceContact>
          </ows:ServiceProvider>
          <ows:OperationsMetadata>
            <ows:Operation name="DescribeSensor">
              <ows:DCP>
                <ows:HTTP>
                  <ows:Get xlink:href="http://sensorweb.demo.52north.org/52n-sos-webapp/service/kvp?">
                    <ows:Constraint name="Content-Type">
                      <ows:AllowedValues>
                        <ows:Value>application/x-kvp</ows:Value>
                      </ows:AllowedValues>
                    </ows:Constraint>
                  </ows:Get>
                  <ows:Post xlink:href="http://sensorweb.demo.52north.org/52n-sos-webapp/service/pox">
                    <ows:Constraint name="Content-Type">
                      <ows:AllowedValues>
                        <ows:Value>application/xml</ows:Value>
                        <ows:Value>text/xml</ows:Value>
                      </ows:AllowedValues>
                    </ows:Constraint>
                  </ows:Post>
                </ows:HTTP>
              </ows:DCP>
              <ows:Parameter name="procedure">
                <ows:AllowedValues>
                  <ows:Value>urn:x-sos:def:procedure:x-sos::Bad_Vöslau-Airquality</ows:Value>
                  <ows:Value>urn:x-sos:def:procedure:x-sos::Biedermannsdorf-Airquality</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="procedureDescriptionFormat">
                <ows:AllowedValues>
                  <ows:Value>http://www.opengis.net/sensorML/1.0.1</ows:Value>
                  <ows:Value>http://www.opengis.net/waterml/2.0/observationProcess</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="validTime">
                <ows:AnyValue/>
              </ows:Parameter>
            </ows:Operation>
            <ows:Operation name="GetCapabilities">
              <ows:DCP>
                <ows:HTTP>
                  <ows:Get xlink:href="http://sensorweb.demo.52north.org/52n-sos-webapp/service/kvp?">
                    <ows:Constraint name="Content-Type">
                      <ows:AllowedValues>
                        <ows:Value>application/x-kvp</ows:Value>
                      </ows:AllowedValues>
                    </ows:Constraint>
                  </ows:Get>
                  <ows:Post xlink:href="http://sensorweb.demo.52north.org/52n-sos-webapp/service/pox">
                    <ows:Constraint name="Content-Type">
                      <ows:AllowedValues>
                        <ows:Value>application/xml</ows:Value>
                        <ows:Value>text/xml</ows:Value>
                      </ows:AllowedValues>
                    </ows:Constraint>
                  </ows:Post>
                </ows:HTTP>
              </ows:DCP>
              <ows:Parameter name="AcceptFormats">
                <ows:AllowedValues>
                  <ows:Value>application/xml</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="AcceptVersions">
                <ows:AllowedValues>
                  <ows:Value>1.0.0</ows:Value>
                  <ows:Value>2.0.0</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="Sections">
                <ows:AllowedValues>
                  <ows:Value>All</ows:Value>
                  <ows:Value>Contents</ows:Value>
                  <ows:Value>FilterCapabilities</ows:Value>
                  <ows:Value>InsertionCapabilities</ows:Value>
                  <ows:Value>OperationsMetadata</ows:Value>
                  <ows:Value>ServiceIdentification</ows:Value>
                  <ows:Value>ServiceProvider</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="updateSequence">
                <ows:AnyValue/>
              </ows:Parameter>
            </ows:Operation>
            <ows:Operation name="GetObservation">
              <ows:DCP>
                <ows:HTTP>
                  <ows:Get xlink:href="http://sensorweb.demo.52north.org/52n-sos-webapp/service/kvp?">
                    <ows:Constraint name="Content-Type">
                      <ows:AllowedValues>
                        <ows:Value>application/x-kvp</ows:Value>
                      </ows:AllowedValues>
                    </ows:Constraint>
                  </ows:Get>
                  <ows:Post xlink:href="http://sensorweb.demo.52north.org/52n-sos-webapp/service/pox">
                    <ows:Constraint name="Content-Type">
                      <ows:AllowedValues>
                        <ows:Value>application/xml</ows:Value>
                        <ows:Value>text/xml</ows:Value>
                      </ows:AllowedValues>
                    </ows:Constraint>
                  </ows:Post>
                </ows:HTTP>
              </ows:DCP>
              <ows:Parameter name="featureOfInterest">
                <ows:AllowedValues>
                  <ows:Value>http%3A%2F%2Fedusvr218.geo.sbg.ac.at%3A8080%2Fgeoserver%2Fsos%2Fows%3Fservice%3DWFS%26version%3D1.0.0%26request%3DGetFeature%26typeName%3Dsos%3Aaustria%26outputFormat%3Dapplication%2Fjson%26CQL_FILTER%3DLOCALNAME%3D%27Ober%C3%B6sterreich%27</ows:Value>
                  <ows:Value>http%3A//edusvr218.geo.sbg.ac.at%3A8080/geoserver/sos/ows%3Fservice%3DWFS%26version%3D1.0.0%26request%3DGetFeature%26typeName%3Dsos%3Aaustria%26outputFormat%3Dapplication%252Fgml%252Bxml%253B%2520version%253D3.2%26CQL_FILTER%3DLOCALNAME%3D%27Steiermark%27</ows:Value>
                  <ows:Value>http://edusvr218.geo.sbg.ac.at:8080/geoserver/sos/ows?service=WFS&amp;version=1.0.0&amp;request=GetFeature&amp;typeName=sos:austria&amp;outputFormat=application/json&amp;CQL_FILTER=LOCALNAME='Niederösterreich'</ows:Value>
                  <ows:Value>http://edusvr218.geo.sbg.ac.at:8080/geoserver/sos/ows?service=WFS&amp;version=1.0.0&amp;request=GetFeature&amp;typeName=sos:austria&amp;outputFormat=application/json&amp;CQL_FILTER=LOCALNAME='Steiermark'</ows:Value>
                  <ows:Value>http://wfs.example.org?request=getFeature&amp;featureid=river1</ows:Value>
                  <ows:Value>urn:x-sos:def:foi:x-sos::Hochwurzen</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="observedProperty">
                <ows:AllowedValues>
                  <ows:Value>urn:ogc:def:phenomenon:OGC:carbonMonoxide</ows:Value>
                  <ows:Value>urn:ogc:def:phenomenon:OGC:nitrogenDioxide</ows:Value>
                  <ows:Value>urn:ogc:def:phenomenon:OGC:nitrogenMonoxide</ows:Value>
                  <ows:Value>urn:ogc:def:phenomenon:OGC:nitrogenOxide</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="offering">
                <ows:AllowedValues>
                  <ows:Value>urn:x-sos:def:offering:x-sos::Bad_Vöslau-Airquality</ows:Value>
                  <ows:Value>urn:x-sos:def:offering:x-sos::Biedermannsdorf-Airquality</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="procedure">
                <ows:AllowedValues>
                  <ows:Value>urn:x-sos:def:procedure:x-sos::Bad_Vöslau-Airquality</ows:Value>
                  <ows:Value>urn:x-sos:def:procedure:x-sos::Biedermannsdorf-Airquality</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="responseFormat">
                <ows:AllowedValues>
                  <ows:Value>application/json</ows:Value>
                  <ows:Value>http://www.opengis.net/om/2.0</ows:Value>
                  <ows:Value>http://www.opengis.net/waterml-dr/2.0</ows:Value>
                  <ows:Value>http://www.opengis.net/waterml/2.0</ows:Value>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="spatialFilter">
                <ows:AllowedValues>
                  <ows:Range>
                    <ows:MinimumValue>0.0 -122.6819</ows:MinimumValue>
                    <ows:MaximumValue>52.0464393 13.72376</ows:MaximumValue>
                  </ows:Range>
                </ows:AllowedValues>
              </ows:Parameter>
              <ows:Parameter name="temporalFilter">
                <ows:AllowedValues>
                  <ows:Range>
                    <ows:MinimumValue>2012-11-19T17:45:15.000Z</ows:MinimumValue>
                    <ows:MaximumValue>2012-11-19T17:45:15.000Z</ows:MaximumValue>
                  </ows:Range>
                </ows:AllowedValues>
              </ows:Parameter>
            </ows:Operation>
            <ows:Parameter name="crs">
              <ows:AllowedValues>
                <ows:Value>http://www.opengis.net/def/crs/EPSG/0/4326</ows:Value>
              </ows:AllowedValues>
            </ows:Parameter>
            <ows:Parameter name="language">
              <ows:AllowedValues>
                <ows:Value>eng</ows:Value>
              </ows:AllowedValues>
            </ows:Parameter>
            <ows:Parameter name="service">
              <ows:AllowedValues>
                <ows:Value>SOS</ows:Value>
              </ows:AllowedValues>
            </ows:Parameter>
            <ows:Parameter name="version">
              <ows:AllowedValues>
                <ows:Value>2.0.0</ows:Value>
              </ows:AllowedValues>
            </ows:Parameter>
          </ows:OperationsMetadata>
          <sos:extension>
            <sos:InsertionCapabilities>
              <sos:procedureDescriptionFormat>http://www.opengis.net/sensorML/1.0.1</sos:procedureDescriptionFormat>
              <sos:procedureDescriptionFormat>http://www.opengis.net/waterml/2.0/observationProcess</sos:procedureDescriptionFormat>
              <sos:featureOfInterestType>SamplingPoint</sos:featureOfInterestType>
              <sos:featureOfInterestType>http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint</sos:featureOfInterestType>
              <sos:supportedEncoding>http://www.opengis.net/swe/2.0/TextEncoding</sos:supportedEncoding>
            </sos:InsertionCapabilities>
          </sos:extension>
          <sos:filterCapabilities>
            <fes:Filter_Capabilities>
              <fes:Spatial_Capabilities/>
              <fes:Temporal_Capabilities/>
            </fes:Filter_Capabilities>
          </sos:filterCapabilities>
          <sos:contents>
            <sos:Contents>
              <swes:offering>
                <sos:ObservationOffering xmlns:ns="http://www.opengis.net/sos/2.0">
                  <swes:identifier>urn:x-sos:def:offering:x-sos::Bad_Vöslau-Airquality</swes:identifier>
                  <swes:procedure>urn:x-sos:def:procedure:x-sos::Bad_Vöslau-Airquality</swes:procedure>
                  <swes:procedureDescriptionFormat>http://www.opengis.net/sensorML/1.0.1</swes:procedureDescriptionFormat>
                  <swes:procedureDescriptionFormat>http://www.opengis.net/waterml/2.0/observationProcess</swes:procedureDescriptionFormat>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:ozone</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:radiation</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:temperature</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:windDirection</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:windSpeedPeak</swes:observableProperty>
                  <swes:relatedFeature>
                    <swes:FeatureRelationship>
                      <swes:role>http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SpatialSamplingFeature</swes:role>
                      <swes:target xlink:href="http://edusvr218.geo.sbg.ac.at:8080/geoserver/sos/ows?service=WFS&amp;version=1.0.0&amp;request=GetFeature&amp;typeName=sos:austria&amp;outputFormat=application/json&amp;CQL_FILTER=LOCALNAME='Niederösterreich'"/>
                    </swes:FeatureRelationship>
                  </swes:relatedFeature>
                  <sos:responseFormat>application/json</sos:responseFormat>
                  <sos:responseFormat>http://www.opengis.net/om/2.0</sos:responseFormat>
                  <sos:responseFormat>http://www.opengis.net/waterml-dr/2.0</sos:responseFormat>
                  <sos:responseFormat>http://www.opengis.net/waterml/2.0</sos:responseFormat>
                  <sos:observationType>http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement</sos:observationType>
                  <sos:featureOfInterestType>http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint</sos:featureOfInterestType>
                </sos:ObservationOffering>
              </swes:offering>
              <swes:offering>
                <sos:ObservationOffering xmlns:ns="http://www.opengis.net/sos/2.0">
                  <swes:identifier>urn:x-sos:def:offering:x-sos::Biedermannsdorf-Airquality</swes:identifier>
                  <swes:procedure>urn:x-sos:def:procedure:x-sos::Biedermannsdorf-Airquality</swes:procedure>
                  <swes:procedureDescriptionFormat>http://www.opengis.net/sensorML/1.0.1</swes:procedureDescriptionFormat>
                  <swes:procedureDescriptionFormat>http://www.opengis.net/waterml/2.0/observationProcess</swes:procedureDescriptionFormat>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:nitrogenDioxide</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:nitrogenMonoxide</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:ozone</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:particulatesPm10Kont10k</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:radiation</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:temperature</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:windDirection</swes:observableProperty>
                  <swes:observableProperty>urn:ogc:def:phenomenon:OGC:windSpeedPeak</swes:observableProperty>
                  <swes:relatedFeature>
                    <swes:FeatureRelationship>
                      <swes:role>http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SpatialSamplingFeature</swes:role>
                      <swes:target xlink:href="http://edusvr218.geo.sbg.ac.at:8080/geoserver/sos/ows?service=WFS&amp;version=1.0.0&amp;request=GetFeature&amp;typeName=sos:austria&amp;outputFormat=application/json&amp;CQL_FILTER=LOCALNAME='Niederösterreich'"/>
                    </swes:FeatureRelationship>
                  </swes:relatedFeature>
                  <sos:responseFormat>application/json</sos:responseFormat>
                  <sos:responseFormat>http://www.opengis.net/om/2.0</sos:responseFormat>
                  <sos:responseFormat>http://www.opengis.net/waterml-dr/2.0</sos:responseFormat>
                  <sos:responseFormat>http://www.opengis.net/waterml/2.0</sos:responseFormat>
                  <sos:observationType>http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement</sos:observationType>
                  <sos:featureOfInterestType>http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint</sos:featureOfInterestType>
                </sos:ObservationOffering>
              </swes:offering>
            </sos:Contents>
          </sos:contents>
        </sos:Capabilities>



.. _sos_describesensor:

DescribeSensor
---------------

This operation returns detailed descriptions of procedures or sensors offered by the service.

Request
^^^^^^^

An example of a DescribeSensor request that returns descriptions of all procedures and sensors offered by a service when sent through the HTTP Post method is below. In the case of the example, the request is sent to the following URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

.. code-block:: xml

      <swes:DescribeSensor
          xmlns:swes="http://www.opengis.net/swes/2.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:gml="http://www.opengis.net/gml/3.2" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swes.xsd">
          <swes:procedure>http://www.52north.org/test/procedure/1</swes:procedure>
          <swes:procedureDescriptionFormat>http://www.opengis.net/sensorML/1.0.1</swes:procedureDescriptionFormat>
      </swes:DescribeSensor>

`This is a link to the equivalent request sent through the HTTP Get method. <http://sensorweb.demo.52north.org/52n-sos-webapp/service?service=SOS&version=2.0.0&request=DescribeSensor&procedure=http%3A%2F%2Fwww.52north.org%2Ftest%2Fprocedure%2F1&procedureDescriptionFormat=http%3A%2F%2Fwww.opengis.net%2FsensorML%2F1.0.1>`_

Response
^^^^^^^^
The response is an XML document that describes the sensor or procedure offered by the service in great detail.

.. code-block:: xml

        <swes:DescribeSensorResponse xmlns:swes="http://www.opengis.net/swes/2.0"
        	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gml="http://www.opengis.net/gml/3.2"
        	xsi:schemaLocation="http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swesDescribeSensor.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd http://www.opengis.net/gml http://schemas.opengis.net/gml/3.1.1/base/gml.xsd http://www.opengis.net/sensorML/1.0.1 http://schemas.opengis.net/sensorML/1.0.1/sensorML.xsd http://www.opengis.net/swe/1.0.1 http://schemas.opengis.net/sweCommon/1.0.1/swe.xsd">
        	<swes:procedureDescriptionFormat>http://www.opengis.net/sensorML/1.0.1</swes:procedureDescriptionFormat>
        	<swes:description>
        		<swes:SensorDescription>
        			<swes:validTime>
        				<gml:TimePeriod gml:id="tp_EFC4679D70D0562D4184FD2890FF638639C6D274">
        					<gml:beginPosition>2017-01-26T20:31:03.555Z</gml:beginPosition>
        					<gml:endPosition indeterminatePosition="unknown" />
        				</gml:TimePeriod>
        			</swes:validTime>
        			<swes:data>
        				<sml:SensorML xmlns:sml="http://www.opengis.net/sensorML/1.0.1"
        					version="1.0.1">
        					<sml:member>
        						<sml:System xmlns:xlink="http://www.w3.org/1999/xlink"
        							xmlns:gml="http://www.opengis.net/gml" xmlns:swe="http://www.opengis.net/swe/1.0.1"
        							xmlns:sos="http://www.opengis.net/sos/2.0">
        							<sml:keywords>
        								<sml:KeywordList>
        									<sml:keyword>http://www.52north.org/test/offering/1
        									</sml:keyword>
        								</sml:KeywordList>
        							</sml:keywords>
        							<sml:identification>
        								<sml:IdentifierList>
        									<sml:identifier name="uniqueID">
        										<sml:Term definition="urn:ogc:def:identifier:OGC:1.0:uniqueID">
        											<sml:value>http://www.52north.org/test/procedure/1
        											</sml:value>
        										</sml:Term>
        									</sml:identifier>
        								</sml:IdentifierList>
        							</sml:identification>
        							<sml:validTime>
        								<gml:TimePeriod>
        									<gml:beginPosition>2017-01-26T20:31:03.555Z</gml:beginPosition>
        									<gml:endPosition indeterminatePosition="unknown" />
        								</gml:TimePeriod>
        							</sml:validTime>
        							<sml:capabilities name="featuresOfInterest">
        								<swe:SimpleDataRecord>
        									<swe:field name="featureOfInterestID">
        										<swe:Text
        											definition="http://www.opengis.net/def/featureOfInterest/identifier">
        											<swe:value>http://www.52north.org/test/featureOfInterest/9
        											</swe:value>
        										</swe:Text>
        									</swe:field>
        								</swe:SimpleDataRecord>
        							</sml:capabilities>
        							<sml:capabilities name="observedBBOX">
        								<swe:DataRecord>
        									<swe:field name="observedBBOX">
        										<swe:Envelope definition="urn:ogc:def:property:OGC:1.0:observedBBOX"
        											referenceFrame="4326">
        											<swe:lowerCorner>
        												<swe:Vector>
        													<swe:coordinate name="easting">
        														<swe:Quantity axisID="x">
        															<swe:uom code="degree" />
        															<swe:value>7.65196881225419</swe:value>
        														</swe:Quantity>
        													</swe:coordinate>
        													<swe:coordinate name="northing">
        														<swe:Quantity axisID="y">
        															<swe:uom code="degree" />
        															<swe:value>51.9351011001049</swe:value>
        														</swe:Quantity>
        													</swe:coordinate>
        												</swe:Vector>
        											</swe:lowerCorner>
        											<swe:upperCorner>
        												<swe:Vector>
        													<swe:coordinate name="easting">
        														<swe:Quantity axisID="x">
        															<swe:uom code="degree" />
        															<swe:value>7.65196881225419</swe:value>
        														</swe:Quantity>
        													</swe:coordinate>
        													<swe:coordinate name="northing">
        														<swe:Quantity axisID="y">
        															<swe:uom code="degree" />
        															<swe:value>51.9351011001049</swe:value>
        														</swe:Quantity>
        													</swe:coordinate>
        												</swe:Vector>
        											</swe:upperCorner>
        										</swe:Envelope>
        									</swe:field>
        								</swe:DataRecord>
        							</sml:capabilities>
        							<sml:capabilities name="offerings">
        								<swe:SimpleDataRecord>
        									<swe:field name="field_0">
        										<swe:Text definition="http://www.opengis.net/def/offering/identifier">
        											<swe:value>http://www.52north.org/test/offering/1</swe:value>
        										</swe:Text>
        									</swe:field>
        								</swe:SimpleDataRecord>
        							</sml:capabilities>
        							<sml:contact/>
        							<sml:position name="sensorPosition">
        								<swe:Position fixed="false" referenceFrame="urn:ogc:def:crs:EPSG::4326">
        									<swe:location>
        										<swe:Vector>
        											<swe:coordinate name="northing">
        												<swe:Quantity axisID="y">
        													<swe:uom code="degree" />
        													<swe:value>51.883906</swe:value>
        												</swe:Quantity>
        											</swe:coordinate>
        											<swe:coordinate name="easting">
        												<swe:Quantity axisID="x">
        													<swe:uom code="degree" />
        													<swe:value>7.727958</swe:value>
        												</swe:Quantity>
        											</swe:coordinate>
        											<swe:coordinate name="altitude">
        												<swe:Quantity axisID="z">
        													<swe:uom code="m" />
        													<swe:value>52.0</swe:value>
        												</swe:Quantity>
        											</swe:coordinate>
        										</swe:Vector>
        									</swe:location>
        								</swe:Position>
        							</sml:position>
        							<sml:inputs>
        								<sml:InputList>
        									<sml:input name="test_observable_property_1">
        										<swe:ObservableProperty
        											definition="http://www.52north.org/test/observableProperty/1" />
        									</sml:input>
        								</sml:InputList>
        							</sml:inputs>
        							<sml:outputs>
        								<sml:OutputList>
        									<sml:output name="test_observable_property_1">
        										<swe:Category
        											definition="http://www.52north.org/test/observableProperty/1">
        											<swe:codeSpace xlink:href="test_unit_1" />
        										</swe:Category>
        									</sml:output>
        									<sml:output name="test_observable_property_9_1">
        										<swe:Category
        											definition="http://www.52north.org/test/observableProperty/9_1">
        											<swe:codeSpace xlink:href="NOT_DEFINED" />
        										</swe:Category>
        									</sml:output>
        									<sml:output name="test_observable_property_9_2">
        										<swe:Count
        											definition="http://www.52north.org/test/observableProperty/9_2" />
        									</sml:output>
        									<sml:output name="test_observable_property_9_4">
        										<swe:Text definition="http://www.52north.org/test/observableProperty/9_4" />
        									</sml:output>
        									<sml:output name="test_observable_property_9_3">
        										<swe:Quantity
        											definition="http://www.52north.org/test/observableProperty/9_3">
        											<swe:uom code="NOT_DEFINED" />
        										</swe:Quantity>
        									</sml:output>
        									<sml:output name="test_observable_property_9_5">
        										<swe:Boolean
        											definition="http://www.52north.org/test/observableProperty/9_5" />
        									</sml:output>
        								</sml:OutputList>
        							</sml:outputs>
        							<sml:components/>
        						</sml:System>
        					</sml:member>
        				</sml:SensorML>
        			</swes:data>
        		</swes:SensorDescription>
        	</swes:description>
        </swes:DescribeSensorResponse>

.. _sos_getobservation:


GetObservation
--------------

This operation returns observation data that has been collected by a procedure or sensor. The requests can be sent through HTTP GET or HTTP POST.

Request
^^^^^^^

The following request returns observations from the offering that has the identifier <http://www.52north.org/test/offering/1>. The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

.. code-block:: xml

        <sos:GetObservation
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:fes="http://www.opengis.net/fes/2.0"
            xmlns:gml="http://www.opengis.net/gml/3.2"
            xmlns:swe="http://www.opengis.net/swe/2.0"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:swes="http://www.opengis.net/swes/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd">
            <sos:offering>http://www.52north.org/test/offering/1</sos:offering>
        </sos:GetObservation>


Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:GetObservationResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:om="http://www.opengis.net/om/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosGetObservation.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd http://www.opengis.net/om/2.0 http://schemas.opengis.net/om/2.0/observation.xsd">
          <sos:observationData>
            <om:OM_Observation gml:id="o_F382128D5FCE0479D86020E0A48D6AE1A9F4FCB2">
              <gml:description>test description for this observation</gml:description>
              <gml:identifier codeSpace="http://www.opengis.net/def/nil/OGC/0/unknown">http:/www.tsuruoka-nct.ac.jp/test/observation/0</gml:identifier>
              <om:type xlink:href="http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"/>
              <om:phenomenonTime>
                <gml:TimeInstant gml:id="phenomenonTime_430">
                  <gml:timePosition>2012-11-19T17:45:15.000Z</gml:timePosition>
                </gml:TimeInstant>
              </om:phenomenonTime>
              <om:resultTime xlink:href="#phenomenonTime_430"/>
              <om:procedure xlink:href="http://www.tsuruoka-nct.ac.jp/test/procedure/0"/>
              <om:observedProperty xlink:href="http://www.tsuruoka-nct.ac.jp/test/observableProperty/Temperature"/>
              <om:featureOfInterest xlink:href="http://www.52north.org/test/featureOfInterest/9"/>
              <om:result xmlns:ns="http://www.opengis.net/gml/3.2" uom="test_unit_9_3" xsi:type="ns:MeasureType">0.28</om:result>
            </om:OM_Observation>
          </sos:observationData>
        </sos:GetObservationResponse>


GetFeatureOfInterest
--------------------

This operation returns a description of the features of interest for which the SOS offers observations.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^
An example request for retrieving a feature of interest is shown below.

.. code-block:: xml

        <sos:GetFeatureOfInterest
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:fes="http://www.opengis.net/fes/2.0"
            xmlns:gml="http://www.opengis.net/gml/3.2"
            xmlns:swe="http://www.opengis.net/swe/2.0"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:swes="http://www.opengis.net/swes/2.0" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd">
        </sos:GetFeatureOfInterest>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:GetFeatureOfInterestResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sams="http://www.opengis.net/samplingSpatial/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:sf="http://www.opengis.net/sampling/2.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosGetFeatureOfInterest.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd http://www.opengis.net/samplingSpatial/2.0 http://schemas.opengis.net/samplingSpatial/2.0/spatialSamplingFeature.xsd http://www.opengis.net/sampling/2.0 http://schemas.opengis.net/sampling/2.0/samplingFeature.xsd">
          <sos:featureMember xlink:href="http%3A%2F%2Fedusvr218.geo.sbg.ac.at%3A8080%2Fgeoserver%2Fsos%2Fows%3Fservice%3DWFS%26version%3D1.0.0%26request%3DGetFeature%26typeName%3Dsos%3Aaustria%26outputFormat%3Dapplication%2Fjson%26CQL_FILTER%3DLOCALNAME%3D%27Ober%C3%B6sterreich%27"/>
          <sos:featureMember>
            <sams:SF_SpatialSamplingFeature gml:id="ssf_BF81F22EFF9BA44E8FFFF909C410DCC44114CB28">
              <gml:identifier codeSpace="http://www.opengis.net/def/nil/OGC/0/unknown">http://www.52north.org/test/featureOfInterest/1</gml:identifier>
              <sf:type xlink:href="http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"/>
              <sf:sampledFeature xlink:href="http://www.52north.org/test/featureOfInterest/world"/>
              <sams:shape>
                <ns:Point xmlns:ns="http://www.opengis.net/gml/3.2" ns:id="point_ssf_BF81F22EFF9BA44E8FFFF909C410DCC44114CB28">
                  <ns:pos srsName="http://www.opengis.net/def/crs/EPSG/0/4326">51.883906 7.727958</ns:pos>
                </ns:Point>
              </sams:shape>
            </sams:SF_SpatialSamplingFeature>
          </sos:featureMember>
          <sos:featureMember>
            <sams:SF_SpatialSamplingFeature gml:id="ssf_1CCABA770D81080DA1DE0C5C3C3F0E7C4360BE52">
              <gml:identifier codeSpace="http://www.opengis.net/def/nil/OGC/0/unknown">http://www.52north.org/test/featureOfInterest/2</gml:identifier>
              <sf:type xlink:href="http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"/>
              <sf:sampledFeature xlink:href="http://www.52north.org/test/featureOfInterest/world"/>
              <sams:shape>
                <ns:Point xmlns:ns="http://www.opengis.net/gml/3.2" ns:id="point_ssf_1CCABA770D81080DA1DE0C5C3C3F0E7C4360BE52">
                  <ns:pos srsName="http://www.opengis.net/def/crs/EPSG/0/4326">34.056517 -117.195711</ns:pos>
                </ns:Point>
              </sams:shape>
            </sams:SF_SpatialSamplingFeature>
          </sos:featureMember>
          <sos:featureMember xlink:href="http://edusvr218.geo.sbg.ac.at:8080/geoserver/sos/ows?service=WFS&amp;version=1.0.0&amp;request=GetFeature&amp;typeName=sos:austria&amp;outputFormat=application/json&amp;CQL_FILTER=LOCALNAME='Steiermark'"/>
          <sos:featureMember xlink:href="http://www.52north.org/test/featureOfInterest/world"/>
          <sos:featureMember xlink:href="http://edusvr218.geo.sbg.ac.at:8080/geoserver/sos/ows?service=WFS&amp;version=1.0.0&amp;request=GetFeature&amp;typeName=sos:austria&amp;outputFormat=application/json&amp;CQL_FILTER=LOCALNAME='Niederösterreich'"/>
        </sos:GetFeatureOfInterestResponse>

GetObservationById
------------------

This operation allows the client application to retrieve an observation by passing a pointer to that observation.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for retrieving an observation by its unique identifier is shown below.

.. code-block:: xml

        <sos:GetObservationById
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd">
            <sos:observation>http:/www.tsuruoka-nct.ac.jp/test/observation/0</sos:observation>
        </sos:GetObservationById>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:GetObservationByIdResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:om="http://www.opengis.net/om/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosGetObservationById.xsd http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd http://www.opengis.net/om/2.0 http://schemas.opengis.net/om/2.0/observation.xsd">
          <sos:observation>
            <om:OM_Observation gml:id="o_C7AE0B68DEEEDE476BC203F558A8CC1EAF43ED71">
              <gml:description>test description for this observation</gml:description>
              <gml:identifier codeSpace="http://www.opengis.net/def/nil/OGC/0/unknown">http:/www.tsuruoka-nct.ac.jp/test/observation/0</gml:identifier>
              <om:type xlink:href="http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"/>
              <om:phenomenonTime>
                <gml:TimeInstant gml:id="phenomenonTime_430">
                  <gml:timePosition>2012-11-19T17:45:15.000Z</gml:timePosition>
                </gml:TimeInstant>
              </om:phenomenonTime>
              <om:resultTime xlink:href="#phenomenonTime_430"/>
              <om:procedure xlink:href="http://www.tsuruoka-nct.ac.jp/test/procedure/0"/>
              <om:observedProperty xlink:href="http://www.tsuruoka-nct.ac.jp/test/observableProperty/Temperature"/>
              <om:featureOfInterest xlink:href="http://www.52north.org/test/featureOfInterest/9"/>
              <om:result xmlns:ns="http://www.opengis.net/gml/3.2" uom="test_unit_9_3" xsi:type="ns:MeasureType">0.28</om:result>
            </om:OM_Observation>
          </sos:observation>
        </sos:GetObservationByIdResponse>


InsertSensor
------------

This operation registers a new sensor system in the SOS.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for registering a sensor or procedure in an SOS is shown below.

.. code-block:: xml

        <swes:InsertSensor
            xmlns:swes="http://www.opengis.net/swes/2.0"
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:swe="http://www.opengis.net/swe/1.0.1"
            xmlns:sml="http://www.opengis.net/sensorML/1.0.1"
            xmlns:gml="http://www.opengis.net/gml"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosInsertSensor.xsd   http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swes.xsd">
            <swes:procedureDescriptionFormat>http://www.opengis.net/sensorML/1.0.1</swes:procedureDescriptionFormat>
            <swes:procedureDescription>
                <sml:SensorML version="1.0.1">
                    <sml:member>
                        <sml:System>
                            <sml:identification>
                                <sml:IdentifierList>
                                    <sml:identifier name="uniqueID">
                                        <sml:Term definition="urn:ogc:def:identifier:OGC:1.0:uniqueID">
                                            <sml:value>http://www.52north.org/test/procedure/11</sml:value>
                                        </sml:Term>
                                    </sml:identifier>
                                </sml:IdentifierList>
                            </sml:identification>
                            <sml:capabilities name="offerings">
                                <swe:SimpleDataRecord>
                                    <!-- Field name or gml:name is used for the offering's name -->
                                    <swe:field name="Offering for sensor 11">
                                        <swe:Text definition="urn:ogc:def:identifier:OGC:offeringID">
                                            <gml:name>Offering for sensor 9</gml:name>
                                            <swe:value>http://www.52north.org/test/offering/11</swe:value>
                                        </swe:Text>
                                    </swe:field>
                                </swe:SimpleDataRecord>
                            </sml:capabilities>
                            <sml:capabilities name="parentProcedures">
                                <!-- Special capabilities used to specify parent procedures. -->
                                <!-- Parsed and removed during InsertSensor/UpdateSensorDescription,
        							added during DescribeSensor. -->
                                <swe:SimpleDataRecord>
                                    <swe:field name="parentProcedure">
                                        <swe:Text>
                                            <swe:value>http://www.52north.org/test/procedure/1</swe:value>
                                        </swe:Text>
                                    </swe:field>
                                </swe:SimpleDataRecord>
                            </sml:capabilities>
                            <sml:capabilities name="featuresOfInterest">
                                <!-- Special capabilities used to specify features of interest. -->
                                <!-- Parsed and removed during InsertSensor/UpdateSensorDescription,
        							added during DescribeSensor. -->
                                <swe:SimpleDataRecord>
                                    <swe:field name="featureOfInterestID">
                                        <swe:Text>
                                            <swe:value>http://www.52north.org/test/featureOfInterest/9
        									</swe:value>
                                        </swe:Text>
                                    </swe:field>
                                </swe:SimpleDataRecord>
                            </sml:capabilities>
                            <sml:position name="sensorPosition">
                                <swe:Position referenceFrame="urn:ogc:def:crs:EPSG::4326">
                                    <swe:location>
                                        <swe:Vector gml:id="STATION_LOCATION">
                                            <swe:coordinate name="easting">
                                                <swe:Quantity axisID="x">
                                                    <swe:uom code="degree"/>
                                                    <swe:value>7.651968812254194</swe:value>
                                                </swe:Quantity>
                                            </swe:coordinate>
                                            <swe:coordinate name="northing">
                                                <swe:Quantity axisID="y">
                                                    <swe:uom code="degree"/>
                                                    <swe:value>51.935101100104916</swe:value>
                                                </swe:Quantity>
                                            </swe:coordinate>
                                            <swe:coordinate name="altitude">
                                                <swe:Quantity axisID="z">
                                                    <swe:uom code="m"/>
                                                    <swe:value>52.0</swe:value>
                                                </swe:Quantity>
                                            </swe:coordinate>
                                        </swe:Vector>
                                    </swe:location>
                                </swe:Position>
                            </sml:position>
                            <sml:inputs>
                                <sml:InputList>
                                    <sml:input name="test_observable_property_9">
                                        <swe:ObservableProperty definition="http://www.52north.org/test/observableProperty/9"/>
                                    </sml:input>
                                </sml:InputList>
                            </sml:inputs>
                            <sml:outputs>
                                <sml:OutputList>
                                    <sml:output name="test_observable_property_9_1">
                                        <swe:Category definition="http://www.52north.org/test/observableProperty/9_1">
                                            <swe:codeSpace xlink:href="NOT_DEFINED"/>
                                        </swe:Category>
                                    </sml:output>
                                </sml:OutputList>
                            </sml:outputs>
                        </sml:System>
                    </sml:member>
                </sml:SensorML>
            </swes:procedureDescription>
            <!-- multiple values possible -->
            <swes:observableProperty>http://www.52north.org/test/observableProperty/9_1</swes:observableProperty>
            <swes:metadata>
                <sos:SosInsertionMetadata>
                    <sos:observationType>http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement</sos:observationType>
                    <sos:observationType>http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CategoryObservation</sos:observationType>
                    <sos:observationType>http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation</sos:observationType>
                    <!-- multiple values possible -->
                    <sos:featureOfInterestType>http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint</sos:featureOfInterestType>
                </sos:SosInsertionMetadata>
            </swes:metadata>
        </swes:InsertSensor>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <swes:InsertSensorResponse xmlns:swes="http://www.opengis.net/swes/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swesInsertSensor.xsd">
          <swes:assignedProcedure>http://www.52north.org/test/procedure/11</swes:assignedProcedure>
          <swes:assignedOffering>http://www.52north.org/test/offering/11</swes:assignedOffering>
        </swes:InsertSensorResponse>

DeleteSensor
------------

This operation deletes a new sensor system from the SOS.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for deleting a sensor or procedure from an SOS is shown below.

.. code-block:: xml

        <swes:DeleteSensor
            xmlns:swes="http://www.opengis.net/swes/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swes.xsd">
            <swes:procedure>http://www.52north.org/test/procedure/11</swes:procedure>
        </swes:DeleteSensor>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <swes:DeleteSensorResponse xmlns:swes="http://www.opengis.net/swes/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swesDeleteSensor.xsd">
          <swes:deletedProcedure>http://www.52north.org/test/procedure/11</swes:deletedProcedure>
        </swes:DeleteSensorResponse>

InsertObservation
-----------------

This operation allows client applications to insert new observations for a registered sensor system.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for inserting an observation into an SOS is shown below.

.. code-block:: xml

        <sos:InsertObservation
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:swes="http://www.opengis.net/swes/2.0"
            xmlns:swe="http://www.opengis.net/swe/2.0"
            xmlns:sml="http://www.opengis.net/sensorML/1.0.1"
            xmlns:gml="http://www.opengis.net/gml/3.2"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:om="http://www.opengis.net/om/2.0"
            xmlns:sams="http://www.opengis.net/samplingSpatial/2.0"
            xmlns:sf="http://www.opengis.net/sampling/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd          http://www.opengis.net/samplingSpatial/2.0 http://schemas.opengis.net/samplingSpatial/2.0/spatialSamplingFeature.xsd">
            <!-- multiple offerings are possible -->
            <sos:offering>http://www.52north.org/test/offering/9</sos:offering>
            <sos:observation>
                <om:OM_Observation gml:id="o1">
                    <gml:description>test description for this observation</gml:description>
                    <gml:identifier codeSpace="">http://www.52north.org/test/observation/10</gml:identifier>
                    <om:type xlink:href="http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"/>
                    <om:phenomenonTime>
                        <gml:TimeInstant gml:id="phenomenonTime">
                            <gml:timePosition>2017-07-31T17:45:15.000+00:00</gml:timePosition>
                        </gml:TimeInstant>
                    </om:phenomenonTime>
                    <om:resultTime xlink:href="#phenomenonTime"/>
                    <om:procedure xlink:href="http://www.52north.org/test/procedure/9"/>
                    <om:observedProperty xlink:href="http://www.52north.org/test/observableProperty/9_3"/>
                    <om:featureOfInterest>
                        <sams:SF_SpatialSamplingFeature gml:id="ssf_test_feature_9">
                            <gml:identifier codeSpace="">http://www.52north.org/test/featureOfInterest/9</gml:identifier>
                            <gml:name>52°North</gml:name>
                            <sf:type xlink:href="http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"/>
                            <sf:sampledFeature xlink:href="http://www.52north.org/test/featureOfInterest/1"/>
                            <sams:shape>
                                <gml:Point gml:id="test_feature_9">
                                    <gml:pos srsName="http://www.opengis.net/def/crs/EPSG/0/4326">51.935101100104916 7.651968812254194</gml:pos>
                                </gml:Point>
                            </sams:shape>
                        </sams:SF_SpatialSamplingFeature>
                    </om:featureOfInterest>
                    <om:result xsi:type="gml:MeasureType" uom="test_unit_9_3">0.28</om:result>
                </om:OM_Observation>
            </sos:observation>
        </sos:InsertObservation>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:InsertObservationResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosInsertObservation.xsd"/>

InsertResultTemplate
--------------------

This operation allows client applications to upload a template for result values such that result values that conform to the template can be inserted into the SOS using subsequent calls of the InsertResult operation.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example for uploading a result template into an SOS is shown below.

.. code-block:: xml

        <sos:InsertResultTemplate
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:swes="http://www.opengis.net/swes/2.0"
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:swe="http://www.opengis.net/swe/2.0"
            xmlns:sml="http://www.opengis.net/sensorML/1.0.1"
            xmlns:gml="http://www.opengis.net/gml/3.2"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:om="http://www.opengis.net/om/2.0"
            xmlns:sams="http://www.opengis.net/samplingSpatial/2.0"
            xmlns:sf="http://www.opengis.net/sampling/2.0"
            xmlns:xs="http://www.w3.org/2001/XMLSchema" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosInsertResultTemplate.xsd http://www.opengis.net/om/2.0 http://schemas.opengis.net/om/2.0/observation.xsd  http://www.opengis.net/samplingSpatial/2.0 http://schemas.opengis.net/samplingSpatial/2.0/spatialSamplingFeature.xsd">
            <sos:proposedTemplate>
                <!-- Before using this example, make sure that all preconditions are fulfilled,
        			e.g. perform InsertSensor example. -->
                <sos:ResultTemplate>
                    <swes:identifier>http://www.52north.org/test/procedure/9/template/11</swes:identifier>
                    <sos:offering>http://www.52north.org/test/offering/11</sos:offering>
                    <sos:observationTemplate>
                        <om:OM_Observation gml:id="sensor2obsTemplate">
                            <om:type xlink:href="http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"/>
                            <om:phenomenonTime nilReason="template"/>
                            <om:resultTime nilReason="template"/>
                            <om:procedure xlink:href="http://www.52north.org/test/procedure/11"/>
                            <om:observedProperty xlink:href="http://www.52north.org/test/observableProperty/9_3"/>
                            <om:featureOfInterest>
                                <sams:SF_SpatialSamplingFeature gml:id="sf_test_feature_9">
                                    <gml:identifier codeSpace="">http://www.52north.org/test/featureOfInterest/9</gml:identifier>
                                    <gml:name>52°North</gml:name>
                                    <sf:type xlink:href="http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"/>
                                    <sf:sampledFeature xlink:href="http://www.opengis.net/def/nil/OGC/0/unknown"/>
                                    <sams:shape>
                                        <gml:Point gml:id="point_sf_test_feature_9">
                                            <gml:pos srsName="http://www.opengis.net/def/crs/EPSG/0/4326">51.935101100104916 7.651968812254194</gml:pos>
                                        </gml:Point>
                                    </sams:shape>
                                </sams:SF_SpatialSamplingFeature>
                            </om:featureOfInterest>
                            <om:result/>
                        </om:OM_Observation>
                    </sos:observationTemplate>
                    <sos:resultStructure>
                        <swe:DataRecord>
                            <swe:field name="phenomenonTime">
                                <swe:Time definition="http://www.opengis.net/def/property/OGC/0/PhenomenonTime">
                                    <swe:uom xlink:href="http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"/>
                                </swe:Time>
                            </swe:field>
                            <swe:field name="test_observable_property_9">
                                <swe:Quantity definition="http://www.52north.org/test/observableProperty/9_3">
                                    <swe:uom code="test_unit_1"/>
                                </swe:Quantity>
                            </swe:field>
                        </swe:DataRecord>
                    </sos:resultStructure>
                    <sos:resultEncoding>
                        <swe:TextEncoding tokenSeparator="#" blockSeparator="@"/>
                    </sos:resultEncoding>
                </sos:ResultTemplate>
            </sos:proposedTemplate>
        </sos:InsertResultTemplate>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:InsertResultTemplateResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosInsertResultTemplate.xsd">
          <sos:acceptedTemplate>http://www.52north.org/test/procedure/9/template/11</sos:acceptedTemplate>
        </sos:InsertResultTemplateResponse>

InsertResult
------------

This operation allows a client application to insert new observations for a sensor system by inserting only the results of the observations and reusing other metadata provided by a template.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for inserting the result of an observation is shown below.

.. code-block:: xml

        <sos:InsertResult
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd">
            <sos:template>http://www.52north.org/test/procedure/9/template/11</sos:template>
            <sos:resultValues>15@2012-11-19T13:30:00+02:00#159.15@2012-11-19T13:31:00+02:00#159.15@2012-11-19T13:32:00+02:00#159.85@2012-11-19T13:33:00+02:00#160.5@2012-11-19T13:34:00+02:00#160.9@2012-11-19T13:35:00+02:00#160.7@2012-11-19T13:36:00+02:00#160.5@2012-11-19T13:37:00+02:00#160.6@2012-11-19T13:38:00+02:00#160.5@2012-11-19T13:39:00+02:00#160.4@2012-11-19T13:40:00+02:00#160.34@2012-11-19T13:41:00+02:00#160.25@2012-11-19T13:42:00+02:00#159.79@2012-11-19T13:43:00+02:00#159.56@2012-11-19T13:44:00+02:00#159.25@</sos:resultValues>
        </sos:InsertResult>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:InsertResultResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosInsertResult.xsd"/>

GetResultTemplate
-----------------

This operation returns a result template that describes the exact structure used by a specific procedure or sensor to generate a new observation result.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for retrieving a result template is shown below.

.. code-block:: xml

        <sos:GetResultTemplate
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd">
            <sos:offering>http://www.52north.org/test/offering/11</sos:offering>
            <sos:observedProperty>http://www.52north.org/test/observableProperty/9_3</sos:observedProperty>
        </sos:GetResultTemplate>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:GetResultTemplateResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/swes/2.0 http://schemas.opengis.net/swes/2.0/swes.xsd http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosGetResultTemplate.xsd">
          <sos:resultStructure>
            <swe:DataRecord xmlns:swes="http://www.opengis.net/swes/2.0" xmlns:sml="http://www.opengis.net/sensorML/1.0.1" xmlns:om="http://www.opengis.net/om/2.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:sf="http://www.opengis.net/sampling/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:swe="http://www.opengis.net/swe/2.0" xmlns:sams="http://www.opengis.net/samplingSpatial/2.0">
              <swe:field name="phenomenonTime">
                <swe:Time definition="http://www.opengis.net/def/property/OGC/0/PhenomenonTime">
                  <swe:uom xlink:href="http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"/>
                </swe:Time>
              </swe:field>
              <swe:field name="test_observable_property_9">
                <swe:Quantity definition="http://www.52north.org/test/observableProperty/9_3">
                  <swe:uom code="test_unit_1"/>
                </swe:Quantity>
              </swe:field>
            </swe:DataRecord>
          </sos:resultStructure>
          <sos:resultEncoding>
            <swe:TextEncoding xmlns:swes="http://www.opengis.net/swes/2.0" xmlns:sml="http://www.opengis.net/sensorML/1.0.1" xmlns:om="http://www.opengis.net/om/2.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:sf="http://www.opengis.net/sampling/2.0" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:swe="http://www.opengis.net/swe/2.0" xmlns:sams="http://www.opengis.net/samplingSpatial/2.0" tokenSeparator="#" blockSeparator="@"/>
          </sos:resultEncoding>
        </sos:GetResultTemplateResponse>

GetResult
---------

This operation allows retrieving just the result values of observations without the entire metadata of the observation.  The request is sent through HTTP POST to the URL <http://sensorweb.demo.52north.org/52n-sos-webapp/service>.

Request
^^^^^^^

An example request for retrieving the result values of observations is shown below.

.. code-block:: xml

        <sos:GetResult
            xmlns:sos="http://www.opengis.net/sos/2.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="SOS" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sos.xsd">
            <sos:offering>http://www.52north.org/test/offering/11</sos:offering>
            <sos:observedProperty>http://www.52north.org/test/observableProperty/9_3</sos:observedProperty>
        </sos:GetResult>

Response
^^^^^^^^

The response resulting from the above request is shown below.

.. code-block:: xml

        <sos:GetResultResponse xmlns:sos="http://www.opengis.net/sos/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sos/2.0 http://schemas.opengis.net/sos/2.0/sosGetResult.xsd">
          <sos:resultValues xmlns:xs="http://www.w3.org/2001/XMLSchema" xsi:type="xs:string">15@2012-11-19T11:30:00.000Z#159.15@2012-11-19T11:31:00.000Z#159.15@2012-11-19T11:32:00.000Z#159.85@2012-11-19T11:33:00.000Z#160.5@2012-11-19T11:34:00.000Z#160.9@2012-11-19T11:35:00.000Z#160.7@2012-11-19T11:36:00.000Z#160.5@2012-11-19T11:37:00.000Z#160.6@2012-11-19T11:38:00.000Z#160.5@2012-11-19T11:39:00.000Z#160.4@2012-11-19T11:40:00.000Z#160.34@2012-11-19T11:41:00.000Z#160.25@2012-11-19T11:42:00.000Z#159.79@2012-11-19T11:43:00.000Z#159.56@2012-11-19T11:44:00.000Z#159.25</sos:resultValues>
        </sos:GetResultResponse>

Exceptions
---------------

When a request from a client to an SOS Server is not performed properly, a server needs to report an exception.
Where an exception occurs, the server will return a report containing details of the exception.

The following exception report is an example of what is returned when a request for an offering that is not supported is sent to the server.

.. code-block:: xml

      <ows:ExceptionReport xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="2.0.0" xsi:schemaLocation="http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsAll.xsd">
        <ows:Exception exceptionCode="InvalidParameterValue" locator="offering">
          <ows:ExceptionText>The value 'http://www.52north.org/test/offering/999' of the parameter 'offering' is invalid</ows:ExceptionText>
        </ows:Exception>
      </ows:ExceptionReport>

References
-----------------


`52North SOS reference <http://52north.org/communities/sensorweb/sos/>`_
