WMS - Operations
================

Background
--------------------

History
  WMS version 1.0.0 in April 2000, followed by version 1.1.0 in June 2001,and version 1.1.1 in January 2002. The OGC released WMS version 1.3.0 in January 2004.
Versions
  1.3 is the current latest version
Test Suite
  Test suites are available for:
      - `WMS 1.1.1 <http://cite.opengeospatial.org/teamengine/>`_
      - `WMS 1.3.0 <http://cite.opengeospatial.org/teamengine/>`_
Implementations
   Implementations can be found at the OGC database. `here <http://www.opengeospatial.org/resource/products/byspec>`_

Usage
^^^^^^
Through a highly configurable interface the WMS standard makes map images (but not source data) available in standard image formats. Government agencies publish all kinds of official map cartography using this standard. Other large organizations use this standard to enable independent departments to interact more easily internally. Anybody using this standard can use it to overlay map images from many different sources regardless of the underlying software.

WMS provides a standard interface for requesting a geospatial map image.  The benefit of this is that WMS clients can request images from multiple WMS servers, and then combine them into a single view for the user.  The standard guarantees that these images can all be overlaid on one another using a common geospatial coordinate reference system.  Numerous servers and clients support WMS.


Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- OGC Web Map Tile Service Interface Standard (WMTS): The WMTS standard is a better fit For highly scalable systems (many simultaneous requests) that only need static maps. It complements the WMS standard with cachable static map tiles. WMS servers can be used as data sources or rendering engines for WMTS services.
- OGC Web Feature Service (WFS): The WFS standard is a better fit for extended query functionality of spatial data. It provides programmatic access to the geographic feature data. WMS and WFS often go together. An organization publishing both WMS and WFS often use the same data source.
- OGC Styled Layer Descriptor Interface Standard (SLD): The SLD standard allows the user to modify the cartographic appearance of a map image. It is an optional feature of the OGC WMS standard.
- OGC Symbology Encoding (SE): The SE standard describes how to define map symbology. It is used to modify the cartographic appearance of map images. It is an optional feature of the OGC WMS and SLD standards.

This section provides detailed information about the types of WMS requests a client is able to perform to a WMS server.

.. list-table:: WMS Operations
   :widths: 30 80
   :header-rows: 1

   * - **Operation**
     - **Description**
   * - ``GetCapabilities``
     - Retrieves metadata about the service, including supported operations and parameters, and a list of the available layers.
   * - ``GetMap``
     - Retrieves a map image for a specified area and content.
   * - ``GetFeatureInfo`` (optional)
     - Retrieves the underlying data, including geometry and attribute values, for a pixel location on a map.
   * - ``DescribeLayer`` (optional)
     - Indicates the WFS or WCS to retrieve additional information about the layer.
   * - ``GetLegendGraphic`` (optional)
     - Retrieves a legend for a map.



.. _wms_getcap:

GetCapabilities
------------------------

Request
^^^^^^^

A WMS server responding to a **GetCapabilities** request returns metadata about the service, including supported operations and parameters, and a list of the available layers.

An example of a GetCapabilities request is:

.. code-block:: properties

  https://ows.terrestris.de/osm/service?
  REQUEST=GetCapabilities&
  SERVICE=WMS&VERSION=1.3.0


`This is a link to a GetCapabilities request. <https://ows.terrestris.de/osm/service?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0>`_

There are three parameters (and values) being passed to the WMS server, ``SERVICE=WMS``, ``VERSION=1.3``, and ``REQUEST=GetCapabilities``.

- The ``SERVICE`` parameter tells the server that a WMS request is forthcoming.
- The ``VERSION`` parameter tells the server what version of the WMS is being requested.
- The ``REQUEST`` parameter tells the server that the operation requested is the `GetCapabilities` operation.

The WMS standard requires that requests always includes these three parameters.
The table bellow summarizes the parameters and values required to perform the request.

.. list-table:: Parameters of the GetCapabilities Operation
   :widths: 15 15 70
   :header-rows: 1

   * - **Parameter**
     - **Required**
     - **Description**
   * - ``SERVICE``
     - Yes
     - Service name. Value is ``WMS``.
   * - ``VERSION``
     - Yes
     - Service version. Value is one of ``1.0.0``, ``1.1.0``, ``1.1.1``, ``1.3``.
   * - ``REQUEST``
     - Yes
     - Operation name. Value is ``GetCapabilities``.

Response
^^^^^^^^
The response is a Capabilities XML document with a detailed description of the WMS service.  It contains three main sections:

.. list-table:: Sections Capabilities Document
   :widths: 20 80
   :header-rows: 1

   * - **Service**
     - Contains service metadata such as the service name, keywords, and contact information for the organization operating the server.
   * - **Request**
     - Describes the operations the WMS service provides and the parameters and output formats for each operation.
   * - **Layer**
     - Lists the available coordinate systems and layers.
       In some servers (e.g. Geoserver) layers are named in the form "namespace:layer".
       Each layer provides service metadata such as title, abstract and keywords.

.. _wms_getmap:


GetCapabilities Layer Style Section
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The GetCapabilites response contains a *Layer* section, which details about the style available to that layer.
In the example bellow the available style is *default*.


.. code-block:: xml


      <Layer queryable="0" opaque="0" cascaded="0">
        <Name>nationalparks</Name>
        <Title>National Parks</Title>
        <EX_GeographicBoundingBox>
          <westBoundLongitude>-4.43064</westBoundLongitude>
          <eastBoundLongitude>1.99728</eastBoundLongitude>
          <southBoundLatitude>50.3532</southBoundLatitude>
          <northBoundLatitude>55.5917</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:27700"
               minx="246828" miny="56378.4" maxx="652374" maxy="633117"/>
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="110" height="22">
            <Format>image/png</Format>
            <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink"
               xlink:type="simple"
               xlink:href="..."/>
          </LegendURL>
        </Style>
      </Layer>




GetMap
-------------

Request
^^^^^^^

A WMS server responding to a **GetMap** request returns a map image for a specified area and content.

The core parameters specify one or more layers and styles to appear on the map, a bounding box for the map extent, a target spatial reference system, and a width, height, and format for the output.
The information needed to specify values for parameters such as ``layers``, ``styles`` and ``Spatial Reference Systems (SRS)`` can be obtained from the Capabilities document.

The response is a map image, or other map output artifact, depending on the format requested.

An example of a GetMap request is:

.. code-block:: properties

      https://ows.terrestris.de/osm/service?
      REQUEST=GetMap&
      SERVICE=WMS&
      VERSION=1.3.0&
      LAYERS=OSM-WMS&
      STYLES=&
      CRS=EPSG:4326&
      BBOX=51.49451,-0.11377,51.53267,-0.06971&
      WIDTH=400&
      HEIGHT=300&
      FORMAT=image/png&
      TRANSPARENT=TRUE


`This is a link to a GetMap request. <https://ows.terrestris.de/osm/service?REQUEST=GetMap&SERVICE=WMS&VERSION=1.3.0&LAYERS=OSM-WMS&STYLES=&CRS=EPSG:4326&BBOX=51.49451,-0.11377,51.53267,-0.06971&WIDTH=400&HEIGHT=300&FORMAT=image/png&TRANSPARENT=TRUE>`_

The getMap request accesses a server offered by Terrestris. The request retrieves a map created from OpenStreetMap data

The coordinate reference system (CRS) is EPSG:4326, which is the World Geodetic System 1984 (WGS84) coordinate reference system. The image is returned in a PNG transparent format with width 400 and height 300 pixels.

The table bellow summarizes the available parameters and values.

.. list-table:: Standard Parameters for the GetMap Operation
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Required?**
     - **Description**
   * - ``service``
     - Yes
     - Service name. Value is ``WMS``.
   * - ``version``
     - Yes
     - Service version. Value is one of ``1.0.0``, ``1.1.0``, ``1.1.1``, ``1.3``.
   * - ``request``
     - Yes
     - Operation name. Value is ``GetMap``.
   * - ``layers``
     - Yes
     - Layers to display on map.
       Value is a comma-separated list of layer names.
   * - ``styles``
     - Yes
     - Styles in which layers are to be rendered.
       Value is a comma-separated list of style names,
       or empty if default styling is required.
       Style names may be empty in the list, to use default layer styling.
   * - ``srs`` *or* ``crs``
     - Yes
     - Spatial Reference System for map output.
       Value is in form ``EPSG:nnn``.
       ``crs`` is the parameter key used in WMS 1.3.0.
   * - ``bbox``
     - Yes
     - Bounding box for map extent.
       Value is ``minx,miny,maxx,maxy`` in units of the SRS.
   * - ``width``
     - Yes
     - Width of map output, in pixels.
   * - ``height``
     - Yes
     - Height of map output, in pixels.
   * - ``format``
     - Yes
     - Format for the map output.
   * - ``transparent``
     - No
     - Whether the map background should be transparent.
       Values are ``true`` or ``false``.
       Default is ``false``
   * - ``bgcolor``
     - No
     - Background color for the map image.
       Value is in the form ``RRGGBB``.
       Default is ``FFFFFF`` (white).
   * - ``exceptions``
     - No
     - Format in which to report exceptions.
       Default value is ``application/vnd.ogc.se_xml``.
   * - ``time``
     - No
     - Time value or range for map data.
   * - ``sld``
     - No
     - A URL referencing a StyledLayerDescriptor XML file
       which controls or enhances map layers and styling
   * - ``sld_body``
     - No
     - A URL-encoded StyledLayerDescriptor XML document
       which controls or enhances map layers and styling



Another WMS request examples is as follows:

.. code-block:: properties

   http://localhost:8080/geoserver/wms?
   request=GetMap
   &service=WMS
   &version=1.1.1
   &layers=topp%3Astates
   &styles=population
   &srs=EPSG%3A4326
   &bbox=-145.15104058007,21.731919794922,-57.154894212888,58.961058642578&
   &width=780
   &height=330
   &format=image%2Fpng


The request specifies the ``topp:states`` layer to be output as a PNG map image in SRS EPGS:4326 and using default styling `population`.


A WMS request can also be sent via HTTP POST as an XML document, as follows:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <ogc:GetMap xmlns:ogc="http://www.opengis.net/ows"
               xmlns:gml="http://www.opengis.net/gml"
      version="1.1.1" service="WMS">
      <StyledLayerDescriptor version="1.0.0">
         <NamedLayer>
           <Name>topp:states</Name>
           <NamedStyle><Name>population</Name></NamedStyle>
         </NamedLayer>
      </StyledLayerDescriptor>
      <BoundingBox srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
         <gml:coord><gml:X>-130</gml:X><gml:Y>24</gml:Y></gml:coord>
         <gml:coord><gml:X>-55</gml:X><gml:Y>50</gml:Y></gml:coord>
      </BoundingBox>
      <Output>
         <Format>image/png</Format>
         <Size><Width>550</Width><Height>250</Height></Size>
      </Output>
   </ogc:GetMap>


Response
^^^^^^^^

The response of a GetMap request is an image.

.. image:: ../img/getmap-demo.png
      :width: 70%

If the request is wrong the server will return an error message.

Time
^^^^

The ``TIME`` parameter allows filtering a dataset by temporal slices as well as spatial tiles for rendering.
The TIME attribute for WMS GetMap requests is described in version 1.3 of the WMS specification.

Specifying a time
"""""""""""""""""

The format used for specifying a time in the WMS TIME parameter is based on `ISO-8601 <http://en.wikipedia.org/wiki/ISO_8601>`_.
The precision might varied depending on the server.

The parameter is::

  TIME=<timestring>

Times follow the general format::

  yyyy-MM-ddThh:mm:ss.SSSZ

where:

* ``yyyy``: 4-digit year
* ``MM``: 2-digit month
* ``dd``: 2-digit day
* ``hh``: 2-digit hour
* ``mm``: 2-digit minute
* ``ss``: 2-digit second
* ``SSS``: 3-digit millisecond

The day and intraday values are separated with a capital ``T``, and the entire string is suffixed with a ``Z``, indicating `UTC <http://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_ for the time zone. (The WMS specification does not provide for other time zones.)

WMS Servers will apply the ``TIME`` value to all temporally enabled layers in the ``LAYERS`` parameter of the GetMap request.

Layers without a temporal component will be served normally, allowing clients to include reference information like political boundaries along with temporal data.



.. list-table:: Examples of Time Values for the TIME parameter in GetMap requests
   :header-rows: 1

   * - Description
     - Time specification
   * - December 12, 2001 at 6:00 PM
     - ``2001-12-12T18:00:00.0Z``
   * - May 5, 1993 at 11:34 PM
     - ``1993-05-05T11:34:00.0Z``

Specifying an absolute interval
""""""""""""""""""""""""""""""""""""""

A client may request information over a continuous interval instead of a single instant by specifying a start and end time, separated by a ``/`` character.

In this scenario the start and end are *inclusive*; that is, samples from exactly the endpoints of the specified range will be included in the rendered tile.

.. list-table:: Examples of Time Values for Absolute Intervals
   :widths: 30 70
   :header-rows: 1

   * - Description
     - Time specification
   * - The month of September 2002
     - ``2002-09-01T00:00:00.0Z/2002-09-30T23:59:59.999Z``
   * - The entire day of December 25, 2010
     - ``2010-12-25T00:00:00.0Z/2010-12-25T23:59:59.999Z``

Specifying a relative interval
""""""""""""""""""""""""""""""""""""""

A client may request information over a relative time interval instead of a set time range by specifying a start or end time with an associated duration, separated by a ``/`` character.

One end of the interval must be a time value, but the other may be a duration value as defined by the ISO 8601 standard.  The special keyword ``PRESENT`` may be used to specify a time relative to the present server time.

.. list-table:: Examples of Time Values for Relative Intervals
   :header-rows: 1

   * - Description
     - Time specification
   * - The month of September 2002
     - ``2002-09-01T00:00:00.0Z/P1M``
   * - The entire day of December 25, 2010
     - ``2010-12-25T00:00:00.0Z/P1D``
   * - The entire day preceding December 25, 2010
     - ``P1D/2010-12-25T00:00:00.0Z``
   * - 36 hours preceding the current time
     - ``PT36H/PRESENT``

Reduced accuracy times
""""""""""""""""""""""""""""""

The WMS specification also allows time specifications to be truncated by omitting some of the time string. Usually servers will treat the time as a range whose length is equal to the *most precise unit specified* in the time string.
For example, if the time specification omits all fields except year, it identifies a range one year long starting at the beginning of that year.

.. list-table:: Examples of Time Values for Reduced Accuracy Times
   :header-rows: 1
   :widths: 15 15 70

   * - Description
     - Reduced Accuracy Time
     - Equivalent Range
   * - The month of September 2002
     - ``2002-09``
     - ``2002-09-01T00:00:00.0Z/2002-09-30T23:59:59.999Z``
   * - The day of December 25, 2010
     - ``2010-12-25``
     - ``2010-12-25T00:00:00.0Z/2010-12-25T23:59:59.999Z``

Reduced accuracy times with ranges
""""""""""""""""""""""""""""""""""""""""""""""

Reduced accuracy times are also allowed when specifying ranges. The ranges are inclusive.
Some servers (e.g GeoServer) effectively expands the start and end times as described above, and then includes any samples from after the beginning of the start interval and before the end of the end interval.

.. list-table:: Examples of Time Values for Reduced Accuracy Times with Ranges
   :header-rows: 1
   :widths: 20 35 45

   * - Description
     - Reduced Accuracy Time
     - Equivalent Range
   * - The months of September through December 2002
     - 2002-09/2002-12
     - 2002-09-01T00:00:00.0Z/ 2002-12-31T23:59:59.999Z
   * - 12PM through 6PM, December 25, 2010
     - 2010-12-25T12/ 2010-12-25T18
     - 2010-12-25T12:00:00.0Z/ 2010-12-25T18:59:59.999Z

Specifying a list of times
""""""""""""""""""""""""""""""

Some Servers, such a GeoServer can also accept a list of discrete time values. This is useful for some applications such as animations, where one time is equal to one frame.

The elements of a list are separated by commas.

If the list is evenly spaced (for example, daily or hourly samples) then the list may be specified as a range, using a start time, end time, and period separated by slashes.

.. list-table:: Examples of List with Time Values
   :header-rows: 1
   :widths: 20 40 40

   * - Description
     - List notation
     - Equivalent range notation
   * - Noon every day for August 12-14, 2012
     - TIME=2012-08-12T12:00:00.0Z, 2012-08-13T12:00:00.0Z, 2012-08-14T12:00:00.0Z
     - TIME=2012-08-12T12:00:00.0Z/ 2012-08-18:T12:00:00.0Z/ P1D
   * - Midnight on the first of September, October, and November 1999
     - TIME=1999-09-01T00:00:00.0Z, 1999-10-01T00:00:00.0Z, 1999-11-01T00:00:00.0Z
     - TIME=1999-09-01T00:00:00.0Z/ 1999-11-01T00:00:00.0Z/ P1M

Specifying a periodicity
""""""""""""""""""""""""""""""""

The periodicity is also specified in ISO-8601 format: a capital P followed by one or more interval lengths, each consisting of a number and a letter identifying a time unit:

.. list-table::
   :header-rows: 1

   * - Unit
     - Abbreviation
   * - Years
     - ``Y``
   * - Months
     - ``M``
   * - Days
     - ``D``
   * - Hours
     - ``H``
   * - Minutes
     - ``M``
   * - Seconds
     - ``S``

The Year/Month/Day group of values must be separated from the Hours/Minutes/Seconds group by a ``T`` character. The T itself may be omitted if hours, minutes, and seconds are all omitted. Additionally, fields which contain a 0 may be omitted entirely.

Fractional values are permitted, but only for the most specific value that is included.

The period must divide evenly into the interval defined by the start/end times. So if the start/end times denote 12 hours, a period of 1 hour would be allowed, but a period of 5 hours would not.

For example, the multiple representations listed below are all equivalent.

* One hour: P0Y0M0DT1H0M0S, PT1H0M0S or PT1H
* 90 minutes: P0Y0M0DT1H30M0S, PT1H30M or P90M
* 18 months: P1Y6M0DT0H0M0S, P1Y6M0D, P0Y18M0DT0H0M0S or P18M

GetFeatureInfo
--------------------------

Request
^^^^^^^

A WMS server responding to a **GetFeatureInfo** request returns the underlying data, including geometry and attribute values, for a pixel location on a map.
It is similar to the WFS GetFeature operation, but less flexible in both input and output.
The one advantage of ``GetFeatureInfo`` is that the request uses an (x,y) pixel value from a returned WMS image.
This is easier to use for a naive client that is not able to perform true geographic referencing.

The standard parameters for the GetFeatureInfo operation are:

.. list-table:: Parameters for the GetFeatureInfo Operation
   :widths: 20 20 60
   :header-rows: 1

   * - **Parameter**
     - **Required**
     - **Description**
   * - ``SERVICE``
     - Yes
     - Service name. Value is ``WMS``.
   * - ``VERSION``
     - Yes
     - Service version. Value is one of ``1.0.0``, ``1.1.0``, ``1.1.1``, ``1.3``.
   * - ``REQUEST``
     - Yes
     - Operation name. Value is ``GetFeatureInfo``.
   * - ``QUERY_LAYERS``
     - Yes
     - Comma separated list of layers to be queried`
   * - ``INFO_FORMAT``
     - No
     - Format for the feature information response (MIME type).
   * - ``FEATURE_COUNT``
     - No
     - Maximum number of features to return.
       Default is 1.
   * - ``i``
     - Yes
     - Pixel column point on the map. 0 is left side.
       ``x`` is the parameter key used in WMS 1.1.0.
   * - ``j``
     - Yes
     - Pixel row on the map. 0 is the top.
       ``y`` is the parameter key used in WMS 1.1.0.
   * - ``EXCEPTIONS``
     - No
     - Format in which to report exceptions.
       The default value is ``application/vnd.ogc.se_xml``.

Example formats are as follows:

.. list-table:: Formats for ``INFO_FORMAT`` parameter in a the GetFeatureInfo Request
   :widths: 10 60 30
   :header-rows: 1

   * - **Format**
     - **Syntax**
     - **Notes**
   * - TEXT
     - ``info_format=text/plain``
     - Simple text output. (The default format)
   * - GML 2
     - ``info_format=application/vnd.ogc.gml``
     - Works only for Simple Features
   * - GML 3
     - ``info_format=application/vnd.ogc.gml/3.1.1``
     - Works for both Simple and Complex Features
   * - HTML
     - ``info_format=text/html``
     - Uses HTML templates that are defined on the server.
   * - JSON
     - ``info_format=application/json``
     - Simple JSON representation.


An example request for feature information from the ``topp:states`` layer in HTML format is:

.. code-block:: properties

   http://localhost:8080/geoserver/wms?
   request=GetFeatureInfo
   &service=WMS
   &version=1.1.1
   &layers=topp%3Astates
   &styles=
   &srs=EPSG%3A4326
   &format=image%2Fpng
   &bbox=-145.151041%2C21.73192%2C-57.154894%2C58.961059
   &width=780
   &height=330
   &query_layers=topp%3Astates
   &info_format=text%2Fhtml
   &feature_count=50
   &x=353
   &y=145
   &exceptions=application%2Fvnd.ogc.se_xml

An example request for feature information in GeoJSON format is:

.. code-block:: properties

   http://localhost:8080/geoserver/wms?
   &INFO_FORMAT=application/json
   &REQUEST=GetFeatureInfo
   &EXCEPTIONS=application/vnd.ogc.se_xml
   &SERVICE=WMS
   &VERSION=1.1.1
   &WIDTH=970&HEIGHT=485&X=486&Y=165&BBOX=-180,-90,180,90
   &LAYERS=COUNTRYPROFILES:grp_administrative_map
   &QUERY_LAYERS=COUNTRYPROFILES:grp_administrative_map
   &TYPENAME=COUNTRYPROFILES:grp_administrative_map

The result will be:

.. code-block:: properties

   {
   "type":"FeatureCollection",
   "features":[
      {
         "type":"Feature",
         "id":"dt_gaul_geom.fid-138e3070879",
         "geometry":{
            "type":"MultiPolygon",
            "coordinates":[
               [
                  [
                     [
                        XXXXXXXXXX,
                        XXXXXXXXXX
                     ],
                     ...
                     [
                        XXXXXXXXXX,
                        XXXXXXXXXX
                     ]
                  ]
               ]
            ]
         },
         "geometry_name":"at_geom",
         "properties":{
            "bk_gaul":X,
            "at_admlevel":0,
            "at_iso3":"XXX",
            "ia_name":"XXXX",
            "at_gaul_l0":X,
            "bbox":[
               XXXX,
               XXXX,
               XXXX,
               XXXX
            ]
         }
      }
   ],
   "crs":{
      "type":"EPSG",
      "properties":{
         "code":"4326"
      }
   },
   "bbox":[
      XXXX,
      XXXX,
      XXXX,
      XXXX
   ]
   }


.. _wms_describelayer:


Exceptions
---------------

When a request from a client to a WMS Server is not performed properly, a Server needs to report an exception.
Formats in which a WMS Server can report exceptions are shown in the table bellow.

.. list-table:: Exceptions
   :widths: 15 50 35
   :header-rows: 1

   * - **Format**
     - **Syntax**
     - **Notes**
   * - XML
     - ``application/vnd.ogc.se_xml``
     - The error is described in XML.
   * - PNG
     - ``application/vnd.ogc.se_inimage``
     - The error is return as an image.
   * - Blank
     - ``application/vnd.ogc.se_blank``
     - A blank image is returned.
   * - JSON
     - ``application/json``
     - The error is reported as a simple JSON representation.

References
-----------------

- `GeoServer WMS reference <http://docs.geoserver.org/stable/en/user/services/wms/reference.html>`_
  - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
- `GeoServer  Time Support in GeoServer WMS  <http://docs.geoserver.org/stable/en/user/_sources/services/wms/time.txt>`_
  - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
