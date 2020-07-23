WFS - Introduction
==================

Introduction
------------
The OGC Web Feature Service (WFS) Interface Standard defines a set of interfaces for accessing geographic information at the feature and feature property level over the Internet. A feature is an abstraction of real world phenomena, that is it is a representation of anything that can be found in the world. The attributes or characteristics of a geographic feature are referred to as feature properties. WFS offer the means to retrieve or query geographic features in a manner independent of the underlying data stores they publish. Where a WFS is authorized to do so, the service can also update or delete geographic features. An instance of a WFS is also able to store queries in order to enable client applications to retrieve or execute the queries at a later point in time.


Background
--------------------

History
    WFS version 1.0.0 in May 2002, followed by version 1.1.0 in May 2005,and version 2.0.0 in November 2010. Version 2.0.0 is the basis of ISO 19142. The OGC released WFS version 2.0.2 in July 2014.
Versions
    2.0.2 is the current latest version
Test Suite
  Test suites are available for:
      - `WFS 1.1.0 <https://github.com/opengeospatial/ets-wfs11>
      - `WFS 2.0.0 <https://github.com/opengeospatial/ets-wfs20>
Implementations
    Implementations can be found at the OGC database. here <http://www.opengeospatial.org/resource/products/byspec>

Usage
^^^^^^
The WFS standard makes geographic feature data available through a highly configurable interface. By default, the data returned by a WFS is in Geography Markup Language (GML) which is written as eXtensible Markup Language (XML). However, emerging versions of the standard will also support the JavaScript Object Notation (JSON). Government agencies, private organisations and academic institutes use this standard to publish vector geospatial datasets in a way that makes it easier for receiving organisations to compile new maps or conduct analysis on the supplied data.

WFS provides a standard interface for requesting vector geospatial data consisting of geographic features and their properties. The benefit of this is that WFS clients can request source data from multiple WFS servers, and then render the data for display on the client or process the data further as part of a workflow. The standard guarantees that the data can be accessed consistently with other data. Feature properties encoded using common data types such as text strings, date and time can also be accessed consistently.

Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- OGC Web Map Service Interface Standard (WMS): The WMS standard is more appropriate where a rendered map is required rather than the source vector data.
- OGC Web Map Tile Service Interface Standard (WMTS): The WMTS standard is a better fit where static rendered maps are required by highly scalable systems that issue many simultaneous requests.
- OGC Web Coverage Service Interface Standard (WCS): The WCS standard is more appropriate where source coverage data such as raster images are required.
- OGC Geography Markup Language (GML): This standard is used by WFS as the default encoding format for published data.

Overview of WFS Operations
----------------------------

WFS specifies a number of different operations, of which the following are required to be supported by all servers:

GetCapabilities
   Returns a document that describes the functionality and resources offered by the WFS service that is provided by the server.
DescribeFeatureType
   Returns a description of the structure of feature types and feature properties offered or accepted by an instance of a WFS.
ListStoredQueries
   Returns a list of the queries that have been stored inside the WFS instance.
DescribeStoredQueries
   Returns a description of the queries that have been stored inside the WFS instance.
GetFeature
   Returns a selection of feature instances from a data store published through the WFS.

The following optional operations may also be offered by a WFS server:

GetPropertyValue
   Retrieves the value of a feature property or part of the value of a complex feature property for a set of feature instances
GetFeatureWithLock
   Serves a similar function to a GetFeature request but with the additional ability to lock a feature, presumably for subsequent updating or changes.
LockFeature
   Locks a set of feature instances such that no other operations may modify the data while the lock is in place.
Transaction
   Allows the feature instances and their properties to be inserted, updated or deleted.
CreateStoredQuery
   Creates and stores a query that can be rapidly and easily triggered by a client at a later point in time.
DropStoredQuery
   Deletes a previously stored query from the server.



Example
-------

This `WFS Demo server <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?service=WFS&request=GetCapabilities>`_ publishes some sample data on sites protected for archeological, environmental or other conservation purposes.

An example ``GetFeature`` request that can be used to retrieve data from the service is shown below.

.. code-block:: properties

      http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?
      SERVICE=WFS&
      VERSION=2.0.0&
      REQUEST=GetFeature&
      TYPENAMES=ps:ProtectedSite

`Link to the GetFeature request <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=ps:ProtectedSite>`_

The ``GetFeature`` request queries the server with a set of parameters describing the geographic features to return. The names and identifiers of the available geographic feature datasets are obtained from the capabilities document that is returned by a GetCapabilities response.

The data returned by the GetFeature request can be rendered by a desktop Geographic Information System (GIS) or forwarded to an OGC WMS for rendering. Alternatively, it can be forwarded to an OGC WPS for further processing.


Client Usage
------------

A client needs to know the location of the WFS service to be able to interact with the server. The location is usually called the 'end point' of the service. The end point is typically the URI of the GetCapabilities request, however the capabilities document returned by the service may present alternative URI end points for other operations. For example:


The URL of this link is composed of the following parameters and values:

.. code-block:: properties

  http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?
  SERVICE=WFS&
  REQUEST=GetCapabilities&
  VERSION=2.0.0

`Link to the GetCapabilities request <http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wfs200?SERVICE=WFS&REQUEST=GetCapabilities&VERSION=2.0.0>`_


References
----------

`Deegree WFS reference <http://download.deegree.org/documentation/3.3.20/html/>`_
