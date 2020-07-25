Resources of OGC API - Features
================

This section provides basic information about the types of resources that OGC API - Features offers.

Each resource provides **links** to relates resources. This enables a client application to navigate the resources, from the landing page through to the individual features. The server identifies the relationship between a resource and other linked resources through a **link relation type**, represented by the attribute 'rel'. The link relation types used by implementations of the **OGC API - Features - Part 1: Core** can be found in `Section 5.2 <http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_link_relations>`_ of the standard.

.. _ogcapif_landingpage:

Landing Page
------------------------

The landing page is the top-level resource that serves as an entry point. A client application needs to know the location of the landing page of the server. From the landing page, the client application can then retrieve links to the Conformance declaration, Collection and API definition paths. An example landing page is at https://services.interactive-instruments.de/t15/daraa?f=json

The link to the API definition is identified through the 'service-desc' and 'service-doc' link relation types.

The link to the Conformance declaration is identified through the 'conformance' link relation type.

The link to the Collections is identified through the  'data' link relation type.


An extract from the landing page of a demo server is shown below.

.. code-block:: json

  {
  "title" : "Daraa",
  "description" : "This is a test dataset from the Open Portrayal Framework thread of the OGC Testbed-15 initiative.",
  "links" : [ {
    "rel" : "self",
    "type" : "application/json",
    "title" : "This document",
    "href" : "https://services.interactive-instruments.de/t15/daraa?f=json"
  }, {
    "rel" : "service-desc",
    "type" : "application/vnd.oai.openapi+json;version=3.0",
    "title" : "Formal definition of the API in OpenAPI 3.0",
    "href" : "https://services.interactive-instruments.de/t15/daraa/api?f=json"
  }, {
    "rel" : "conformance",
    "title" : "OGC API conformance classes implemented by this server",
    "href" : "https://services.interactive-instruments.de/t15/daraa/conformance"
  }, {
    "rel" : "data",
    "title" : "Access the data",
    "href" : "https://services.interactive-instruments.de/t15/daraa/collections"
  }
  ]
  }


.. _ogcapif_conformance:

Conformance declaration
------------------------

An implementation of OGC API - Features describes the capabilities that it supports by declaring which conformance classes it implements. The Conformance declaration states the conformance classes from standards or community specifications, identified by a URI, that the API conforms to. Clients can then use this information, although they are not required to. Accessing the Conformance declaration using HTTP GET returns the list of URIs of conformance classes implemented by the server. Conformance classes describe the behavior a server should implement in order to meet one or more sets of requirements specified in a standard.

Below is an extract from the response to the request https://services.interactive-instruments.de/t15/daraa/conformance?f=json

Notice that the example shows a link relation type called 'alternate' which identifies a way to retrieve an alternative representation of the information provided by the resource. In this case the 'alternate' link relation is referencing an HTML representation of the conformance declaration.

.. code-block:: json

  {
  "links" : [ {
    "rel" : "self",
    "type" : "application/json",
    "title" : "This document",
    "href" : "https://services.interactive-instruments.de/t15/daraa/conformance?f=json"
  }, {
    "rel" : "alternate",
    "type" : "text/html",
    "title" : "This document as HTML",
    "href" : "https://services.interactive-instruments.de/t15/daraa/conformance?f=html"
  } ],
  "conformsTo" : [ "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",  "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html", "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30", "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core" ]
  }



.. _ogcapif_collections:

Feature collections
------------------------

Data offered through an implementation of **OGC API - Features - Part 1: Core** is organized into one or more feature collections. The 'Collections' resource provides information about and access to the list of collections.

For each collection, there is a link to the detailed description of the collection (represented by the path **/collections/{collectionId}** and link relation **self**).

For each collection, there is a link to the features in the collection (represented by the path **/collections/{collectionId}/items** and link relation **items**) and other information about the collection. The following information is provided by the server to describe each collection:

* A local identifier for the collection that is unique for the dataset
* A list of coordinate reference systems (CRS) in which geometries may be returned by the server
* An optional title and description for the collection
* An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection
* An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').

Below is an extract from the response to the request https://services.interactive-instruments.de/t15/daraa/collections?f=json

.. code-block:: json

  {
    "title" : "Daraa",
    "description" : "This is a test dataset from the Open Portrayal Framework thread of the OGC Testbed-15 initiative",
    "links" : [ {
      "rel" : "self",
      "type" : "application/json",
      "title" : "This document",
      "href" : "https://services.interactive-instruments.de/t15/daraa/collections?f=json"
    }],
    "collections" : [ {
      "title" : "Aeronautic (Curves)",
      "description" : "Aeronautical Facilities: Information about an area specifically designed and constructed for landing, accommodating, and launching military and/or civilian aircraft, rockets, missiles and/or spacecraft.<br/>Aeronautical Aids to Navigation: Information about electronic equipment, housings, and utilities that provide positional information for direction or otherwise assisting in the navigation of airborne aircraft.",
      "links" : [{
      "rel" : "self",
      "title" : "The 'Aeronautic (Curves)' feature collection",
      "href" : "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv"
    }, {
      "rel" : "items",
      "type" : "application/geo+json",
      "title" : "Access the features in the collection 'Aeronautic (Curves)'",
      "href" : "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items?f=json"
    }],
      "id" : "AeronauticCrv",
      "extent" : {
        "spatial" : {
          "bbox" : [ [ 36.395158, 32.6933011, 36.4308137, 32.7173334 ] ],
          "crs" : "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      },
      "crs" : [ "#/crs" ],
      "storageCrs" : "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    },  {
      "title" : "Other (Points)",
      "links" : [{
      "rel" : "self",
      "title" : "The 'Other (Points)' feature collection",
      "href" : "https://services.interactive-instruments.de/t15/daraa/collections/o2s_p"
    }, {
      "rel" : "items",
      "type" : "application/geo+json",
      "title" : "Access the features in the collection 'Other (Points)'",
      "href" : "https://services.interactive-instruments.de/t15/daraa/collections/o2s_p/items?f=json"
    }],
      "id" : "o2s_p",
      "extent" : {
        "spatial" : {
          "bbox" : [ [ 35.9396036, 32.5449626, 36.443695, 32.9846485 ] ],
          "crs" : "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      },
      "crs" : [ "#/crs" ],
      "storageCrs" : "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    } ]
  }


.. _ogcapif_collection:

Feature collection
------------------------

The **Collection** resource provides detailed information about the collection identified in a request.

Below is an extract from the response to the request https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/?f=json

.. code-block:: json

  {
  "title" : "Aeronautic (Curves)",
  "description" : "Aeronautical Facilities: Information about an area specifically designed and constructed for landing, accommodating, and launching military and/or civilian aircraft, rockets, missiles and/or spacecraft.<br/>Aeronautical Aids to Navigation: Information about electronic equipment, housings, and utilities that provide positional information for direction or otherwise assisting in the navigation of airborne aircraft.",
  "links" : [ {
    "rel" : "self",
    "type" : "application/json",
    "title" : "This document",
    "href" : "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv?f=json"
  }, {
    "rel" : "items",
    "type" : "application/geo+json",
    "title" : "Access the features in the collection 'Aeronautic (Curves)'",
    "href" : "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items?f=json"
  } ],
  "id" : "AeronauticCrv",
  "extent" : {
    "spatial" : {
      "bbox" : [ [ 36.395158, 32.6933011, 36.4308137, 32.7173334 ] ],
      "crs" : "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    },
    "temporal" : {
      "interval" : [ [ null, null ] ],
      "trs" : "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
    }
  },
  "crs" : [ "http://www.opengis.net/def/crs/OGC/1.3/CRS84", "http://www.opengis.net/def/crs/EPSG/0/3395", "http://www.opengis.net/def/crs/EPSG/0/3857", "http://www.opengis.net/def/crs/EPSG/0/4326" ],
  "storageCrs" : "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
}


.. _ogcapif_features:

Features
------------------------

The Features resource returns a document consisting of features contained by the collection identified in a request. The features included in the response are determined by the server based on the query parameters of the request. To support access to larger collections without overloading the client, the API supports paged access with links to the next page, if more features are selected than the page size.

Below is an extract from the response to the request https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items?f=json

.. code-block:: json

  {
    "type": "FeatureCollection",
    "links": [],
    "numberReturned": 10,
    "numberMatched": 20,
    "timeStamp": "2020-07-23T17:58:40Z",
    "features": [{
            "type": "Feature",
            "id": "1",
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [[[36.4251993, 32.7137029], [36.4270026, 32.7114543]]]
            },
            "properties": {
                "F_CODE": "GB075",
                "ZI001_SDV": "2011-03-16T14:51:12Z",
                "UFI": "2d008c34-4458-4226-b335-cf903d261ce9",
                "ZI005_FNA": "No Information",
                "FCSUBTYPE": 100454
            }
        }, {
            "type": "Feature",
            "id": "2",
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [[[36.4252966, 32.7137689], [36.4251993, 32.7137029], [36.4231106, 32.7125398], [36.4208881, 32.7113022], [36.4031334, 32.7013331], [36.400909, 32.700077]]]
            },
            "properties": {
                "F_CODE": "GB075",
                "ZI001_SDV": "2015-09-11T19:15:35Z",
                "UFI": "1257bf27-3f91-461d-8a3b-a95af2ea1f5a",
                "ZI005_FNA": "No Information",
                "FCSUBTYPE": 100454
            }
        }]
  }

Note that this document is a valid GeoJSON document.


Additional parameters may be used to select only a subset of the features in the collection.

A **bbox** or **datetime** parameter may be used to select only the subset of the features in the collection that are within the bounding box specified by the **bbox** parameter or the time interval specified by the **datetime** parameter. An example request that uses the **bbox** parameter is https://services.interactive-instruments.de/t15/daraa/collections/VegetationSrf/items?f=json&bbox=36.0832432,32.599852,36.1168237,32.6283697

.. note::  The effect of the bbox parameter can be easily seen when comparing the HTML response from `applying <https://services.interactive-instruments.de/t15/daraa/collections/VegetationSrf/items?f=html&bbox=36.0832432,32.599852,36.1168237,32.6283697>`_ the bbox parameter to the response `without <https://services.interactive-instruments.de/t15/daraa/collections/VegetationSrf/items?f=html>`_ any bbox parameter.

The **limit** parameter may be used to control the page size by specifying the maximum number of features that should be returned in the response. An example request that uses the **limit** parameter is https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items?f=json&limit=2

Each page may include information about the number of selected and returned features ('numberMatched' and 'numberReturned') as well as links to support paging (link relation 'next').


.. _ogcapif_feature:

Feature
------------------------

The Feature resource is used for retrieving an individual feature, its geometric representation and other properties. In the example below, the feature with an 'id' of 1 is retrieved. The response is retrieved through the request https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items/1?f=json



.. code-block:: json

  {
    "type": "Feature",
    "links": [{
            "href": "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items/1?f=json",
            "rel": "self",
            "type": "application/geo+json",
            "title": "This document"
        }, {
            "href": "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items/1?f=html",
            "rel": "alternate",
            "type": "text/html",
            "title": "This document as HTML"
        }, {
            "href": "https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv?f=json",
            "rel": "collection",
            "type": "application/json",
            "title": "The collection the feature belongs to"
        }],
    "id": "1",
    "geometry": {
        "type": "MultiLineString",
        "coordinates": [[[36.4251993, 32.7137029], [36.4270026, 32.7114543]]]
    },
    "properties": {
        "F_CODE": "GB075",
        "ZI001_SDV": "2011-03-16T14:51:12Z",
        "UFI": "2d008c34-4458-4226-b335-cf903d261ce9",
        "ZI005_FNA": "No Information",
        "FCSUBTYPE": 100454
    }
  }
