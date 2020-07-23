Resources of OGC API - Features
================

This section provides detailed information about the types of resources that OGC API - Features offers.

.. _ogcapif_landingpage:

Landing Page
------------------------

A client application needs to know the location of the landing page of the server. From the landing page, the client application can then retrieve links to the conformance and collection paths. An example landing page is at https://services.interactive-instruments.de/t15/daraa?f=json

An extract from the landing page is shown below.

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

An implementation of OGC API - Features describes the capabilities that it supports by declaring which conformance classes it implements. Conformance classes describe the behavior a server should implement in order to meet one or more sets of requirements specified in a standard.

Below is an extract from the response to the request https://services.interactive-instruments.de/t15/daraa/conformance?f=json

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


.. _ogcapif_feature:

Feature
------------------------

Below is an extract from the response to the request https://services.interactive-instruments.de/t15/daraa/collections/AeronauticCrv/items/1?f=json

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
