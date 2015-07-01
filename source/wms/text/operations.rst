WMS - Operations
==================

The following are the WMS operations


WMS requests can perform the following operations: 

.. list-table::
   :widths: 20 80

   * - **Operation**
     - **Description**
   * - ``Exceptions``
     - If an exception occur
   * - ``GetCapabilities``
     - Retrieves metadata about the service, including supported operations and parameters, and a list of the available layers
   * - ``GetMap``
     - Retrieves a map image for a specified area and content
   * - ``GetFeatureInfo`` (optional)
     - Retrieves the underlying data, including geometry and attribute values, for a pixel location on a map
   * - ``DescribeLayer`` (optional)
     - Indicates the WFS or WCS to retrieve additional information about the layer.
   * - ``GetLegendGraphic`` (optional)
     - Retrieves a generated legend for a map 

Exceptions
----------

Formats in which WMS can report exceptions. The supported values for exceptions are:

.. list-table::
   :widths: 15 35 50
   
   * - **Format**
     - **Syntax**
     - **Notes**
   * - XML
     - ``EXCEPTIONS=application/vnd.ogc.se_xml``
     - Xml output. (The default format)
   * - PNG
     - ``EXCEPTIONS=application/vnd.ogc.se_inimage``
     - Generates an image
   * - Blank
     - ``EXCEPTIONS=application/vnd.ogc.se_blank``
     - Generates a blank image
   * - JSON
     - ``EXCEPTIONS=application/json``
     - Simple Json representation.
   * - JSONP
     - ``EXCEPTIONS=text/javascript``
     - Return a JsonP in the form: paddingOutput(...jsonp...). See :ref:`wms_vendor_parameters` to change the callback name. Note that this format is disabled by default (See :ref:`wms_global_variables`).

.. _wms_getcap:

GetCapabilities
---------------

The **GetCapabilities** operation requests metadata about the operations, services, and data ("capabilities") that are offered by a WMS server. 

The parameters for the GetCapabilities operation are:

.. list-table::
   :widths: 20 10 70
   
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
     - Operation name. Value is ``GetCapabilities``.


A example GetCapabilities request is:

.. code-block:: xml
 
   http://localhost:8080/geoserver/wms?
   service=wms&
   version=1.1.1&
   request=GetCapabilities
    
There are three parameters being passed to the WMS server, ``service=wms``, ``version=1.1.1``, and ``request=GetCapabilities``.  
The ``service`` parameter tells the WMS server that a WMS request is forthcoming.  
The ``version`` parameter refers to which version of WMS is being requested.  
The ``request`` parameter specifies the GetCapabilities operation.
The WMS standard requires that requests always includes these three parameters.  


The response is a Capabilities XML document that is a detailed description of the WMS service.  
It contains three main sections:

.. list-table::
   :widths: 20 80
   
   * - **Service**
     - Contains service metadata such as the service name, keywords, and contact information for the organization operating the server.
   * - **Request**
     - Describes the operations the WMS service provides and the parameters and output formats for each operation.  
   * - **Layer**
     - Lists the available coordinate systems and layers.  
       In some servers (e.g. Geoserver) layers are named in the form "namespace:layer".  
       Each layer provides service metadata such as title, abstract and keywords.

.. _wms_getmap:

GetMap
------

The **GetMap** operation requests that the server generate a map.  
The core parameters specify one or more layers and styles to appear on the map,
a bounding box for the map extent,
a target spatial reference system,
and a width, height, and format for the output.
The information needed to specify values for parameters such as ``layers``, ``styles`` and ``srs`` can be obtained from the Capabilities document.  

The response is a map image, or other map output artifact, depending on the format requested.

The standard parameters for the GetMap operation are:

.. list-table::
   :widths: 20 10 70
   
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
       See :ref:`wms_output_formats` for supported values.
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
     - A URL referencing a :ref:`StyledLayerDescriptor <styling>` XML file
       which controls or enhances map layers and styling
   * - ``sld_body``
     - No
     - A URL-encoded :ref:`StyledLayerDescriptor <styling>` XML document
       which controls or enhances map layers and styling     



Example WMS request for ``topp:states`` layer to be output as a PNG map image in SRS EPGS:4326 and using default styling is:

.. code-block:: xml

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


Example WMS request using a GetMap XML document is:

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

Time
....

This parameter allows filtering a dataset by temporal slices as well as spatial tiles for rendering. The TIME attribute for WMS GetMap requests is described in version 1.3 of the WMS specification.

Specifying a time
+++++++++++++++++++

The format used for specifying a time in the WMS TIME parameter is based on `ISO-8601 <http://en.wikipedia.org/wiki/ISO_8601>`_. The precision might varied depending on the server. 

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

The day and intraday values are separated with a capital ``T``, and the entire thing is suffixed with a ``Z``, indicating `UTC <http://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_ for the time zone. (The WMS specification does not provide for other time zones.)

WMS Servers will apply the ``TIME`` value to all temporally enabled layers in the ``LAYERS`` parameter of the GetMap request.

Layers without a temporal component will be served normally, allowing clients to include reference information like political boundaries along with temporal data.

.. list-table::
   :header-rows: 1

   * - Description
     - Time specification
   * - December 12, 2001 at 6:00 PM
     - ``2001-12-12T18:00:00.0Z``
   * - May 5, 1993 at 11:34 PM
     - ``1993-05-05T11:34:00.0Z``

Specifying an absolute interval
++++++++++++++++++++++++++++++++

A client may request information over a continuous interval instead of a single instant by specifying a start and end time, separated by a ``/`` character.

In this scenario the start and end are *inclusive*; that is, samples from exactly the endpoints of the specified range will be included in the rendered tile.

.. list-table::
   :header-rows: 1

   * - Description
     - Time specification
   * - The month of September 2002
     - ``2002-09-01T00:00:00.0Z/2002-09-30T23:59:59.999Z``
   * - The entire day of December 25, 2010
     - ``2010-12-25T00:00:00.0Z/2010-12-25T23:59:59.999Z``

Specifying a relative interval
+++++++++++++++++++++++++++++++

A client may request information over a relative time interval instead of a set time range by specifying a start or end time with an associated duration, separated by a ``/`` character.

One end of the interval must be a time value, but the other may be a duration value as defined by the ISO 8601 standard.  The special keyword ``PRESENT`` may be used to specify a time relative to the present server time.

.. list-table::
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

.. note::
   
   The final example could be paired with the KML service to provide a :ref:`google_earth` network link which is always updated with the last 36 hours of data.

Reduced accuracy times
+++++++++++++++++++++++++++++++

The WMS specification also allows time specifications to be truncated by omitting some of the time string. usually servers will treat the time as a range whose length is equal to the *most precise unit specified* in the time string. For example, if the time specification omits all fields except year, it identifies a range one year long starting at the beginning of that year.

.. list-table::
   :header-rows: 1

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
+++++++++++++++++++++++++++++++++++++

Reduced accuracy times are also allowed when specifying ranges. Some servers (e.g GeoServer) effectively expands the start and end times as described above, and then includes any samples from after the beginning of the start interval and before the end of the end interval.

.. note:: Again, the ranges are inclusive.

.. list-table::
   :header-rows: 1

   * - Description
     - Reduced Accuracy Time
     - Equivalent Range
   * - The months of September through December 2002
     - ``2002-09/2002-12``
     - ``2002-09-01T00:00:00.0Z/2002-12-31T23:59:59.999Z``
   * - 12PM through 6PM, December 25, 2010
     - ``2010-12-25T12/2010-12-25T18``
     - ``2010-12-25T12:00:00.0Z/2010-12-25T18:59:59.999Z``

.. note:: In the last example, note that the result may not be intuitive, as it includes all times from 6PM to 6:59PM.

Specifying a list of times
+++++++++++++++++++++++++++++++

GooServer can also accept a list of discrete time values. This is useful for some applications such as animations, where one time is equal to one frame. 

The elements of a list are separated by commas.

If the list is evenly spaced (for example, daily or hourly samples) then the list may be specified as a range, using a start time, end time, and period separated by slashes.

.. list-table::
   :header-rows: 1

   * - Description
     - List notation
     - Equivalent range notation
   * - Noon every day for August 12-14, 2012
     - ``TIME=2012-08-12T12:00:00.0Z,2012-08-13T12:00:00.0Z,2012-08-14T12:00:00.0Z``
     - ``TIME=2012-08-12T12:00:00.0Z/2012-08-18:T12:00:00.0Z/P1D``
   * - Midnight on the first of September, October, and November 1999
     - ``TIME=1999-09-01T00:00:00.0Z,1999-10-01T00:00:00.0Z,1999-11-01T00:00:00.0Z``
     - ``TIME=1999-09-01T00:00:00.0Z/1999-11-01T00:00:00.0Z/P1M``

Specifying a periodicity
+++++++++++++++++++++++++++++++

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

.. note:: The period must divide evenly into the interval defined by the start/end times. So if the start/end times denote 12 hours, a period of 1 hour would be allowed, but a period of 5 hours would not. 

For example, the multiple representations listed below are all equivalent.

* One hour::

        P0Y0M0DT1H0M0S

        PT1H0M0S

        PT1H

* 90 minutes::

        P0Y0M0DT1H30M0S

        PT1H30M

        P90M

* 18 months::

        P1Y6M0DT0H0M0S

        P1Y6M0D

        P0Y18M0DT0H0M0S

        P18M

  .. note:: ``P1.25Y3M`` would not be acceptable, because fractional values are only permitted in the most specific value given, which in this case would be months. 


GetFeatureInfo
--------------

The **GetFeatureInfo** operation requests the spatial and attribute data for the features
at a given location on a map.  
It is similar to the WFS GetFeature operation, but less flexible in both input and output.
 
The one advantage of ``GetFeatureInfo`` is that the request uses an (x,y) pixel value from a returned WMS image.  
This is easier to use for a naive client that is not able to perform true geographic referencing.

The standard parameters for the GetFeatureInfo operation are:

.. list-table::
   :widths: 20 10 70
   
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
     - Operation name. Value is ``GetFeatureInfo``.
   * - ``layers``
     - Yes
     - See :ref:`wms_getmap`
   * - ``styles``
     - Yes
     - See :ref:`wms_getmap`
   * - ``srs`` *or* ``crs``
     - Yes
     - See :ref:`wms_getmap`
   * - ``bbox``
     - Yes
     - See :ref:`wms_getmap`
   * - ``width``
     - Yes
     - See :ref:`wms_getmap`
   * - ``height``
     - Yes
     - See :ref:`wms_getmap`
   * - ``query_layers``
     - Yes
     - Comma-separated list of one or more layers to query.
   * - ``info_format``
     - No
     - Format for the feature information response.  See below for values.
   * - ``feature_count``
     - No
     - Maximum number of features to return.
       Default is 1.
   * - ``x`` or ``i``
     - Yes
     - X ordinate of query point on map, in pixels. 0 is left side.
       ``i`` is the parameter key used in WMS 1.3.0.
   * - ``y`` or ``j``
     - Yes
     - Y ordinate of query point on map, in pixels. 0 is the top.
       ``j`` is the parameter key used in WMS 1.3.0.
   * - ``exceptions``
     - No
     - Format in which to report exceptions.
       The default value is ``application/vnd.ogc.se_xml``.

Example formats are as follows:

.. list-table::
   :widths: 15 35 50
   
   * - **Format**
     - **Syntax**
     - **Notes**
   * - TEXT
     - ``info_format=text/plain``
     - Simple text output. (The default format)
   * - GML 2
     - ``info_format=application/vnd.ogc.gml`` 
     - Works only for Simple Features (see :ref:`app-schema.complex-features`)
   * - GML 3
     - ``info_format=application/vnd.ogc.gml/3.1.1``
     - Works for both Simple and Complex Features (see :ref:`app-schema.complex-features`)
   * - HTML
     - ``info_format=text/html``
     - Uses HTML templates that are defined on the server. See :ref:`tutorials_getfeatureinfo` for information on how to template HTML output. 
   * - JSON
     - ``info_format=application/json``
     - Simple Json representation.
   * - JSONP
     - ``info_format=text/javascript``
     - Returns a JsonP in the form: ``parseResponse(...json...)``. See :ref:`wms_vendor_parameters` to change the callback name. Note that this format is disabled by default (See :ref:`wms_global_variables`).

.. list-table::
   :widths: 20 10 70
   
   * - **Parameter**
     - **Required?**
     - **Description**
   * - ``buffer``
     - No
     - width of search radius around query point.
   * - ``cql_filter``
     - No
     - Filter for returned data, in ECQL format
   * - ``filter``
     - No
     - Filter for returned data, in OGC Filter format
   * - ``propertyName``
     - No
     - Feature properties to be returned

An example request for feature information from the ``topp:states`` layer in HTML format is:

.. code-block:: xml

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

.. code-block:: xml

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

.. code-block:: xml
   
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

DescribeLayer
-------------

The **DescribeLayer** operation is used primarily by clients that understand SLD-based WMS.  
In order to make an SLD one needs to know the structure of the data.  
WMS and WFS both have operations to do this, so the **DescribeLayer** operation just routes the client to the appropriate service.

The standard parameters for the DescribeLayer operation are:

.. list-table::
   :widths: 20 10 70
   
   * - **Parameter**
     - **Required?**
     - **Description**
   * - ``service``
     - Yes
     - Service name. Value is ``WMS``.
   * - ``version``
     - Yes
     - Service version. Value is ``1.1.1``.
   * - ``request``
     - Yes
     - Operation name. Value is ``DescribeLayer``.
   * - ``layers``
     - Yes
     - See :ref:`wms_getmap`
   * - ``exceptions``
     - No
     - Format in which to report exceptions.
       The default value is ``application/vnd.ogc.se_xml``.


A server can be configured to support any format for `DescribeLayer`` response. Here are some examples from GeoServer:

.. list-table::
   :widths: 15 35 50
   
   * - **Format**
     - **Syntax**
     - **Notes**
   * - TEXT
     - ``output_format=text/xml``
     - Same as default.
   * - GML 2
     - ``output_format=application/vnd.ogc.wms_xml``
     - The default format.
   * - JSON
     - ``output_format=application/json``
     - Simple Json representation.
   * - JSONP
     - ``output_format=text/javascript``
     - Return a JsonP in the form: paddingOutput(...jsonp...). See :ref:`wms_vendor_parameters` to change the callback name.  Note that this format is disabled by default (See :ref:`wms_global_variables`).
     

An example request in XML (default) format on a layer is:

.. code-block:: xml

   http://localhost:8080/geoserver/topp/wms?service=WMS
   &version=1.1.1
   &request=DescribeLayer
   &layers=topp:coverage

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE WMS_DescribeLayerResponse SYSTEM "http://localhost:8080/geoserver/schemas/wms/1.1.1/WMS_DescribeLayerResponse.dtd">
   <WMS_DescribeLayerResponse version="1.1.1">
      <LayerDescription name="topp:coverage" owsURL="http://localhost:8080/geoserver/topp/wcs?" owsType="WCS">
         <Query typeName="topp:coverage"/>
      </LayerDescription>
   </WMS_DescribeLayerResponse>

An example request for feature description in JSON format on a layer group is:

.. code-block:: xml

   http://localhost:8080/geoserver/wms?service=WMS
   &version=1.1.1
   &request=DescribeLayer
   &layers=sf:roads,topp:tasmania_roads,nurc:mosaic
   &outputFormat=application/json
   

The result will be:

.. code-block:: xml

   {
   version: "1.1.1",
   layerDescriptions: [
   {
      layerName: "sf:roads",
      owsURL: "http://localhost:8080/geoserver/wfs/WfsDispatcher?",
      owsType: "WFS",
      typeName: "sf:roads"
   },
   {
      layerName: "topp:tasmania_roads",
      owsURL: "http://localhost:8080/geoserver/wfs/WfsDispatcher?",
      owsType: "WFS",
      typeName: "topp:tasmania_roads"
   },
   {
      layerName: "nurc:mosaic",
      owsURL: "http://localhost:8080/geoserver/wcs?",
      owsType: "WCS",
      typeName: "nurc:mosaic"
   }
   ]
   }


.. _wms_getlegendgraphic:

GetLegendGraphic
----------------

The **GetLegendGraphic** operation provides a mechanism for generating legend graphics as images, beyond the LegendURL reference of WMS Capabilities.  
It generates a legend based on the style defined on the server, or alternatively based on a user-supplied SLD.  


References
------------

- `GeoServer WMS reference <http://docs.geoserver.org/stable/en/user/services/wms/reference.html>`_ - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
- `GeoServer  Time Support in GeoServer WMS  <http://docs.geoserver.org/stable/en/user/_sources/services/wms/time.txt>`_ - `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_





