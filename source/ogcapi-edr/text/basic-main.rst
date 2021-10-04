An Introduction to OGC API - Environmental Data Retrieval
==================

Introduction
------------

OGC API - Environmental Data Retrieval is a standard that provides a family of lightweight interfaces to access Environmental Data resources. The standard, which is also called the Environmental Data Retrieval (EDR) API, addresses two fundamental operations; discovery and query. Discovery operations allow the API to be interrogated to determine its capabilities and retrieve information (metadata) about this distribution of a resource. This includes the API definition of the server as well as metadata about the Environmental Data resources provided by the server. Query operations allow Environmental Data resources to be retrieved from the underlying data store based upon simple selection criteria, defined by this standard and selected by the client.


.. note::  This tutorial module is not intended to be a replacement to the actual **OGC API - Environmental Data Retrieval** standard. The tutorial intentionally focuses on a subset of capabilities in order to get the student started with using the standard. Please refer to the **OGC API - Environmental Data Retrieval** standard for additional detail.


Background
--------------------

History
    Version 1.0.0 was published on 2021-08-13.
Versions
    **OGC API - Environmental Data Retrieval** version 1.0.0 is the current latest version
Test Suite
    A draft test suite is available for:
      - `OGC API - Environmental Data Retrieval <https://github.com/opengeospatial/ets-ogcapi-edr10>`_
Implementations
    Implementations can be found on the OGC Product Database here <http://www.opengeospatial.org/resource/products/byspec>

Usage
^^^^^^

**OGC API - Environmental Data Retrieval** provides a family of lightweight query interfaces to access spatio-temporal data resources by requesting data at a Position, within an Area, along a Trajectory or through a Corridor. A spatio-temporal data resource is a collection of spatio-temporal data that can be sampled using the EDR query pattern geometries.

The standard provides a standard interface for requesting vector geospatial data consisting of geographic features and their properties. The benefit of this is that client applications can request source data from multiple implementations of the API, and then render the data for display or process the data further as part of a workflow. The standard enables the data to be accessed consistently with other data. Feature properties encoded using common data types such as text strings, date and time can also be accessed consistently.

Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- OGC API-Features: The EDR API is completely compatible with OGC API — Features — Part 1: Core (OGC 17-069r3), in that it supports Collections and Items. It extends the Collection functionality by allowing ‘Instances’, a form of ‘collection of collections’. The EDR API also supports the retrieval of spatiotemporal data by named location as well as coordinates.

- Moving Features: The Moving Features Standards are concerned with things that move along a trajectory, and simultaneously change their orientation through rigid body rotation. The EDR API does not have the concept of orientation, or foliation or prisms. Moving Features and EDR API do share a common conceptual definition, from ISO, of a Trajectory, but the Moving Features Standards encode trajectories in GML, CSV and Moving Features JSON, whereas the EDR API encodes trajectories in WKT.

- Web Coverage Service (WCS) and Coverage Implementation Schema (CIS): The primary messaging mechanism of the EDR API is JSON, including CoverageJSON, over HTTP(S). Implementations of the EDR API are described using the OpenAPI V3.0 specification. The EDR API is consistent with the WCS and CIS standards but does not require the end user or developer to use the terms Domain and RangeSet. The EDR API can also be used to generate a single query against a collection of coverages, providing the data coordinate reference systems are consistent.

- The OGC SensorThings API: SensorThings API follows OData’s specification for requesting entities. In contrast, the EDR API makes use of the OpenAPI V3.0 specification for describing resource paths, query options, JSON schema, and other aspects. Further, the EDR API allows for retrieval of coverage data and HTML responses – both of which are not supported by the SensorThings API.

- Sensor Observation Service (SOS): The EDR API allows for retrieval of coverage data and HTML responses – both of which are not supported by the SOS standard. Further, SOS implementations use the GetCapabilities operation for providing descriptions of available resources. In contrast, the EDR API uses OpenAPI definition documents for describing available interfaces.

Overview of Resources
----------------------------

**OGC API - Environmental Data Retrieval Standard** defines the resources listed in the following table.


.. csv-table:: Overview of OGC API - Features resources
   :header: "Resource ", "Path", "Purpose"
   :widths: 20, 20, 10

   "Landing page", "{root}/", "This is the top-level resource, which serves as an entry point."
   "Conformance declaration", "{root}/conformance", "This resource presents information about the functionality that is implemented by the server."
   "API definition", "{root}/api", "This resource provides metadata about the API itself. Note use of **/api** on the server is optional and the API definition may be hosted on completely separate server"
   "All Collections metadata", "{root}/collections", "Metadata describing the collections of data available from this API."
   "Collection metadata", "{root}/collections/{collectionId}", "Metadata describing the collection of data which has the unique identifier {collectionId}"
   "Items metadata", "{root}/collections/{collectionId}/items", "Retrieve metadata about available items"
   "Query data", "{root}/collections/{collectionId}/{queryType}", "Retrieve data according to the query pattern"
   "Query instances", "{root}/collections/{collectionId}/instances", "Retrieve metadata about instances of a collection"


Example
-------

This `demonstration server <http://labs.metoffice.gov.uk/edr/static/html/query.html>`_ publishes environmental data through an interface that conforms to OGC API - Environmental Data Retrieval.
