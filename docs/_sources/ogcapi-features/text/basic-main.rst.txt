An Introduction to OGC API - Features
==================

Introduction
------------

OGC API - Features is a multi-part standard that offers the capability to create, modify, and query spatial data on the Web and specifies requirements and recommendations for APIs that want to follow a standard way of sharing feature data. The specification is a multi-part document. The Core part of the specification describes the mandatory capabilities that every implementing service has to support and is restricted to read-access to spatial data. Additional capabilities that address specific needs will be specified in additional parts. Envisaged future capabilities include, for example, support for creating and modifying data, more complex data models, richer queries, and additional coordinate reference systems.

Background
--------------------

History
    While in draft form and prior to February 2019, OGC API - Features was referred to as WFS3.0.
Versions
    1.0.0 is the current latest version
Test Suite
  Test suites are available for:
      - `OGC API - Features 1.0.0 <https://github.com/opengeospatial/ets-ogcapi-features10>`_
Implementations
    Implementations can be found on the Compliance Database here <http://www.opengeospatial.org/resource/products/byspec>

Usage
^^^^^^

Part 1 of this standard specifies discovery and query operations that are implemented using the HTTP GET method. Support for additional methods (in particular POST, PUT, DELETE, PATCH) will be specified in additional parts. Government agencies, private organisations and academic institutes use this standard to publish vector geospatial datasets in a way that makes it easier for receiving organisations to compile new maps or conduct analysis on the supplied data.

OGC API - Features provides a standard interface for requesting vector geospatial data consisting of geographic features and their properties. The benefit of this is that client applications can request source data from multiple implementations of the API, and then render the data for display or process the data further as part of a workflow. The standard enables the data to be accessed consistently with other data. Feature properties encoded using common data types such as text strings, date and time can also be accessed consistently.

Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- OGC Web Feature Service Interface Standard (WFS): The WFS standard is more appropriate when working with client applications that only support classic OGC Web Services. Note as well that WFS adopts the Geography Markup Language (`GML <https://www.ogc.org/standards/gml>`_) as a default data format. In contrast, OGC API - Features includes recommendations to support `HTML <https://html.spec.whatwg.org>`_ and `GeoJSON <https://geojson.org>`_ as encodings, where practical. Implementations of OGC API - Features may also optionally support GML.


Overview of Resources
----------------------------

OGC API - Features defines the resources listed in the following table.


.. csv-table:: Overview of OGC API - Features resources
   :header: "Resource ", "Path", "Purpose"
   :widths: 20, 20, 10

   "Landing page", "/", "This is the top-level resource, which serves as an entry point."
   "Conformance declaration", "/conformance", "This resource presents information about the functionality that is implemented by the server."
   "Feature collections", "/collections", "This resource lists the feature collections that are offered through the API."
   "Feature collection", "/collections/{collectionId}", "This resource describes the feature collection identified in the path."
   "Features", "/collections/{collectionId}/items", "This resource presents the features that are contained in the collection."
   "Feature", "/collections/{collectionId}/items/{featureId}", "This resource presents the feature that is identified in the part"



Example
-------

This `demonstration server <https://services.interactive-instruments.de/t15/daraa/>`_ publishes vector geospatial data through an interface that conforms to OGC API - Features.

An example request that can be used to retrieve data from the Vegetation surface feature collection is https://services.interactive-instruments.de/t15/daraa/collections/VegetationSrf/items?f=html

Note that the response to the request is HTML in this case.

Alternatively, the same data can be retrieved in JSON format, through the request https://services.interactive-instruments.de/t15/daraa/collections/VegetationSrf/items?f=json

Copy the JSON returned by the VegetationSrf feature collection and paste it into the free `geojson.io <https://geojson.io>`_ viewer to see the data rendered. A screenshot is shown below.

.. image:: ../img/geojsonviewer.png
      :height: 654
      :width: 1049


Of course, a client application that supports OGC API - Features would be able to retrieve the data without the need to copy-and-paste manually.
