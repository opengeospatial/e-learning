Information Resources of OGC API - Environmental Data Retrieval
================

This section provides basic information about the types of resources that OGC API - Environmental Data Retrieval offers.

Each resource provides **links** that relate to resources. This enables a client application to navigate the resources, from the landing page through to the individual features. The server identifies the relationship between a resource and other linked resources through a **link relation type**, represented by the attribute 'rel'. The link relation types used by implementations of the **OGC API - Environmental Data Retrieval** can be found in `Section 6.2 <https://docs.ogc.org/is/19-086r4/19-086r4.html#toc22>`_ of the standard.

.. _ogcapiedr_landingpage:

Landing Page
------------------------

The landing page is the top-level resource that serves as an entry point. A client application needs to know the location of the landing page of the server. From the landing page, the client application can retrieve links to the Conformance declaration, Collection and API definition paths. An example landing page is at http://labs.metoffice.gov.uk/edr

The link to the API definition is identified through the 'service-desc' and 'service-doc' link relation types.

The link to the Conformance declaration is identified through the 'conformance' link relation type.

The link to the Collections is identified through the  'data' link relation type.


An extract from the landing page of a demo server is shown below.

.. code-block:: json

  {
  "title": "Environmental Data Retrevial API concept demonstrator",
  "description": "Example EDR API (not for operational use)",
  "keywords": [
    "position",
    "area",
    "cube",
    "trajectory",
    "weather",
    "data",
    "api"
  ],
  "terms_of_service": "None",
  "provider": {
    "name": "Organization Name",
    "url": "http://example.org"
  },
  "contact": {
    "email": "you@example.org",
    "phone": "+001-234-567-89",
    "fax": "+001-234-567-89",
    "hours": "Hours of Service",
    "instructions": "During hours of service.  Off on weekends.",
    "address": "Mailing Address",
    "postalcode": "Zip or Postal Code",
    "city": "City",
    "stateorprovince": "Administrative Area",
    "country": "Country"
  },
  "links": [
    {
      "href": "http://labs.metoffice.gov.uk/edr/api",
      "hreflang": "en",
      "rel": "service-doc",
      "type": "application/vnd.oai.openapi+json;version=3.0",
      "title": "",
      "variables": null
    },
    {
      "href": "http://labs.metoffice.gov.uk/edr/conformance",
      "hreflang": "en",
      "rel": "conformance",
      "type": "application/json",
      "title": "",
      "variables": null
    },
    {
      "href": "http://labs.metoffice.gov.uk/edr/collections",
      "hreflang": "en",
      "rel": "collection",
      "type": "application/json",
      "title": "",
      "variables": null
    }
  ]
}


.. _ogcapiedr_conformance:

Conformance declaration
------------------------

An implementation of OGC API - Environmental Data Retrieval describes the capabilities that it supports by declaring which conformance classes it implements. The Conformance declaration states the conformance classes from standards or community specifications, identified by a URI, that the API conforms to. Clients can then use this information, although they are not required to. Accessing the Conformance declaration using HTTP GET returns the list of URIs of conformance classes implemented by the server. Conformance classes describe the behavior a server should implement in order to meet one or more sets of requirements specified in a standard.

Below is an extract from the response to the request http://labs.metoffice.gov.uk/edr/conformance

.. code-block:: json

  {
   "conformsTo":[
      "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core",
      "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/collections",
      "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/core",
      "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/oas30",
      "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/html",
      "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/geojson",
      "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/coveragejson",
      "http://www.opengis.net/spec/ogcapi-edr-1/1.0/conf/wkt"
   ]
}



.. _ogcapiedr_collections:

Collections metadata
------------------------

Data offered through an implementation of **OGC API - Environmental Data Retrevial** is organized into one or more feature collections. The 'Collections' resource provides information about and access to the list of collections.

For each collection, there is a link to the detailed description of the collection (represented by the path **/collections/{collectionId}** and link relation **self**).

The following information is provided by the server to describe each collection:

* A local identifier for the collection that is unique for the dataset
* A list of coordinate reference systems (CRS) in which geometries may be returned by the server
* An optional title and description for the collection
* An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection
* An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').

For each collection, there are links to retrieve data according to supported query patterns (represented by the path **/collections/{collectionId}/{queryType}** and link relation **data**).

For each collection, there is a link to the metadata about items available in the collection (represented by the path **/collections/{collectionId}/items** and link relation **items**) and other information about the collection.

Below is an extract from the response to the request http://labs.metoffice.gov.uk/edr/collections

.. code-block:: json

  {
    "links": [
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections",
        "hreflang": "en",
        "rel": "self",
        "type": "application/json"
      },
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections?f=html",
        "hreflang": "en",
        "rel": "alternate",
        "type": "text/html"
      },
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections?f=xml",
        "hreflang": "en",
        "rel": "alternate",
        "type": "application/xml"
      }
    ],
    "collections": [
      {
        "id": "metar_demo",
        "title": "Metar observations EDR demonstrator",
        "description": "API to access 24 hours of Global Metar Observation data (not for operational use)",
        "keywords": [
          "Metar observation",
          "ICAO identifier",
          "Wind Direction",
          "Wind Speed",
          "Wind Gust",
          "Visibility",
          "Air Temperature",
          "Dew point",
          "Runway Visibility",
          "Weather",
          "Sky condition",
          "Mean Sea Level Pressure",
          "Station Level Pressure",
          "description",
          "restrictions",
          "collection",
          "position",
          "radius",
          "area",
          "location"
        ],
        "links": [
          {
            "href": "https://www.aviationweather.gov/metar/help",
            "hreflang": "en",
            "rel": "service-doc",
            "type": "text/html",
            "title": ""
          },
          {
            "href": "https://www.weather.gov/disclaimer",
            "hreflang": "en",
            "rel": "restrictions",
            "type": "text/html",
            "title": ""
          },
          {
            "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/",
            "hreflang": "en",
            "rel": "collection",
            "type": "collection",
            "title": ""
          },
          {
            "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/position",
            "hreflang": "en",
            "rel": "data"
          },
          {
            "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/radius",
            "hreflang": "en",
            "rel": "data"
          },
          {
            "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/area",
            "hreflang": "en",
            "rel": "data"
          },
          {
            "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/locations",
            "hreflang": "en",
            "rel": "data"
          }
        ],
        "extent": {
          "spatial": {
            "bbox": [
              -180.0,
              -89.9,
              180.0,
              89.9
            ],
            "crs": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
          },
          "temporal": {
            "interval": [
              "R36/2021-10-03T01:00Z/PT1H"
            ],
            "trs": "TIMECRS[\"DateTime\",TDATUM[\"Gregorian Calendar\"],CS[TemporalDateTime,1],AXIS[\"Time (T)\",future]"
          }
        },
        "data_queries": {
          "position": {
            "link": {
              "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/position",
              "hreflang": "en",
              "rel": "data",
              "variables": {
                "title": "Position query",
                "query_type": "position",
                "output_formats": [
                  "CoverageJSON",
                  "GeoJSON",
                  "IWXXM"
                ],
                "default_output_format": "GeoJSON",
                "crs_details": [
                  {
                    "crs": "CRS84",
                    "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
                  }
                ]
              }
            }
          },
          "radius": {
            "link": {
              "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/radius",
              "hreflang": "en",
              "rel": "data",
              "variables": {
                "title": "Radius query",
                "description": "Radius query",
                "query_type": "radius",
                "output_formats": [
                  "CoverageJSON",
                  "GeoJSON",
                  "IWXXM"
                ],
                "default_output_format": "GeoJSON",
                "within_units": [
                  "km",
                  "miles"
                ],
                "crs_details": [
                  {
                    "crs": "CRS84",
                    "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
                  }
                ]
              }
            }
          },
          "area": {
            "link": {
              "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/area",
              "hreflang": "en",
              "rel": "data",
              "variables": {
                "title": "Area query",
                "query_type": "area",
                "output_formats": [
                  "CoverageJSON",
                  "GeoJSON",
                  "IWXXM"
                ],
                "default_output_format": "CoverageJSON",
                "crs_details": [
                  {
                    "crs": "CRS84",
                    "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
                  }
                ]
              }
            }
          },
          "locations": {
            "link": {
              "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/locations",
              "hreflang": "en",
              "rel": "data",
              "variables": {
                "title": "Location query",
                "description": "Location query",
                "query_type": "locations",
                "output_formats": [
                  "CoverageJSON",
                  "GeoJSON",
                  "CSV"
                ],
                "default_output_format": "GeoJSON",
                "crs_details": [
                  {
                    "crs": "CRS84",
                    "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
                  }
                ]
              }
            }
          }
        },
        "crs": [
          "CRS84"
        ],
        "output_formats": [
          "CoverageJSON",
          "GeoJSON",
          "IWXXM"
        ],
        "parameter_names": {
          "Metar observation": {
            "type": "Parameter",
            "description": "Source Metar observation",
            "unit": {
              "label": "",
              "symbol": {
                "value": "",
                "type": "http://codes.wmo.int/wmdr/DataFormat/FM-15-metar"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/wmdr/DataFormat/FM-15-metar",
              "label": "Metar observation"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "ICAO identifier": {
            "type": "Parameter",
            "description": "ICAO identifier",
            "unit": {
              "label": "",
              "symbol": {
                "value": "",
                "type": "https://en.wikipedia.org/wiki/ICAO_airport_code"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/bufr4/b/01/_063",
              "label": "ICAO identifier"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Wind Direction": {
            "type": "Parameter",
            "description": "Wind Direction",
            "unit": {
              "label": "degree true",
              "symbol": {
                "value": "\u00b0",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/degree"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/common/quantity-kind/_aerodromeMeanWindDirection",
              "label": "Wind Direction"
            },
            "measurementType": {
              "method": "mean",
              "period": "-PT10M/PT0M"
            }
          },
          "Wind Speed": {
            "type": "Parameter",
            "description": "Wind Speed",
            "unit": {
              "label": "mph",
              "symbol": {
                "value": "mph",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/mph"
              }
            },
            "observedProperty": {
              "id": " http://codes.wmo.int/common/quantity-kind/aerodromeMeanWindSpeed",
              "label": "Wind Speed"
            },
            "measurementType": {
              "method": "mean",
              "period": "-PT10M/PT0M"
            }
          },
          "Wind Gust": {
            "type": "Parameter",
            "description": "Wind Gust",
            "unit": {
              "label": "mph",
              "symbol": {
                "value": "mph",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/mph"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/common/quantity-kind/_aerodromeMaximumWindGustSpeed",
              "label": "Wind Gust"
            },
            "measurementType": {
              "method": "maximum",
              "period": "-PT10M/PT0M"
            }
          },
          "Visibility": {
            "type": "Parameter",
            "description": "Visibility",
            "unit": {
              "label": "m",
              "symbol": {
                "value": "m",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/m"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/common/quantity-kind/_horizontalVisibility",
              "label": "Visibility"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Air Temperature": {
            "type": "Parameter",
            "description": "",
            "unit": {
              "label": "degC",
              "symbol": {
                "value": "\u00b0C",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/degC"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/common/quantity-kind/_airTemperature",
              "label": "Air Temperature"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Dew point": {
            "type": "Parameter",
            "description": "",
            "unit": {
              "label": "degC",
              "symbol": {
                "value": "\u00b0C",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/degC"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/common/quantity-kind/_dewPointTemperature",
              "label": "Dew point"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Runway Visibility": {
            "type": "Parameter",
            "description": "Runway Visibile Range",
            "unit": {
              "label": "m",
              "symbol": {
                "value": "m",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/m"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/common/quantity-kind/_runwayVisualRangeRvr",
              "label": "Runway Visibility"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Weather": {
            "type": "Parameter",
            "description": "Aerodrome recent weather",
            "unit": {
              "label": "weather",
              "symbol": {
                "value": "",
                "type": "http://codes.wmo.int/49-2/AerodromeRecentWeather"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/49-2/AerodromeRecentWeather",
              "label": "Weather"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Sky condition": {
            "type": "Parameter",
            "description": "Sky condition",
            "unit": {
              "label": "sky",
              "symbol": {
                "value": "",
                "type": "http://{server}"
              }
            },
            "observedProperty": {
              "id": "",
              "label": "Sky condition"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Mean Sea Level Pressure": {
            "type": "Parameter",
            "description": "",
            "unit": {
              "label": "hPa",
              "symbol": {
                "value": "hPa",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/hPa"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/bufr4/b/10/_051",
              "label": "Mean Sea Level Pressure"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          },
          "Station Level Pressure": {
            "type": "Parameter",
            "description": "",
            "unit": {
              "label": "hPa",
              "symbol": {
                "value": "hPa",
                "type": "http://labs.metoffice.gov.uk/edr/metadata/units/hPa"
              }
            },
            "observedProperty": {
              "id": "http://codes.wmo.int/bufr4/b/10/_004",
              "label": "Station Level Pressure"
            },
            "measurementType": {
              "method": "instantaneous",
              "period": "PT0M"
            }
          }
        }
      }
    ]
  }

.. _ogcapiedr_collection:

Single collection metadata
------------------------

The **Collection** resource provides detailed information about the collection identified in a request. Some of the information returned includes the supported geographic extent, data queries, coordinate reference systems, output formats, and parameter names.

Below is an extract from the response to the request http://labs.metoffice.gov.uk/edr/collections/metar_demo?f=json

.. code-block:: json

  {
    "id": "metar_demo",
    "title": "Metar observations EDR demonstrator",
    "description": "API to access 24 hours of Global Metar Observation data (not for operational use)",
    "keywords": [
      "Metar observation",
      "ICAO identifier",
      "Wind Direction",
      "Wind Speed",
      "Wind Gust",
      "Visibility",
      "Air Temperature",
      "Dew point",
      "Runway Visibility",
      "Weather",
      "Sky condition",
      "Mean Sea Level Pressure",
      "Station Level Pressure",
      "description",
      "restrictions",
      "collection",
      "position",
      "radius",
      "area",
      "location"
    ],
    "links": [
      {
        "href": "http://labs.metoffice.gov.uk/collections/metar_demo",
        "hreflang": "en",
        "rel": "self",
        "type": "application/json"
      },
      {
        "href": "http://labs.metoffice.gov.uk/collections/metar_demo?f=html",
        "hreflang": "en",
        "rel": "alternate",
        "type": "text/html"
      },
      {
        "href": "http://labs.metoffice.gov.uk/collections/metar_demo?f=xml",
        "hreflang": "en",
        "rel": "alternate",
        "type": "application/xml"
      },
      {
        "href": "https://www.aviationweather.gov/metar/help",
        "hreflang": "en",
        "rel": "service-doc",
        "type": "text/html",
        "title": ""
      },
      {
        "href": "https://www.weather.gov/disclaimer",
        "hreflang": "en",
        "rel": "restrictions",
        "type": "text/html",
        "title": ""
      },
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/position",
        "hreflang": "en",
        "rel": "data"
      },
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/radius",
        "hreflang": "en",
        "rel": "data"
      },
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/area",
        "hreflang": "en",
        "rel": "data"
      },
      {
        "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/locations",
        "hreflang": "en",
        "rel": "data"
      }
    ],
    "extent": {
      "spatial": {
        "bbox": [
          -180.0,
          -89.9,
          180.0,
          89.9
        ],
        "crs": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
      },
      "temporal": {
        "interval": [
          "R36/2021-10-03T03:00Z/PT1H"
        ],
        "trs": "TIMECRS[\"DateTime\",TDATUM[\"Gregorian Calendar\"],CS[TemporalDateTime,1],AXIS[\"Time (T)\",future]"
      }
    },
    "data_queries": {
      "position": {
        "link": {
          "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/position",
          "hreflang": "en",
          "rel": "data",
          "variables": {
            "title": "Position query",
            "query_type": "position",
            "output_formats": [
              "CoverageJSON",
              "GeoJSON",
              "IWXXM"
            ],
            "default_output_format": "GeoJSON",
            "crs_details": [
              {
                "crs": "CRS84",
                "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
              }
            ]
          }
        }
      },
      "radius": {
        "link": {
          "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/radius",
          "hreflang": "en",
          "rel": "data",
          "variables": {
            "title": "Radius query",
            "description": "Radius query",
            "query_type": "radius",
            "output_formats": [
              "CoverageJSON",
              "GeoJSON",
              "IWXXM"
            ],
            "default_output_format": "GeoJSON",
            "within_units": [
              "km",
              "miles"
            ],
            "crs_details": [
              {
                "crs": "CRS84",
                "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
              }
            ]
          }
        }
      },
      "area": {
        "link": {
          "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/area",
          "hreflang": "en",
          "rel": "data",
          "variables": {
            "title": "Area query",
            "query_type": "area",
            "output_formats": [
              "CoverageJSON",
              "GeoJSON",
              "IWXXM"
            ],
            "default_output_format": "CoverageJSON",
            "crs_details": [
              {
                "crs": "CRS84",
                "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
              }
            ]
          }
        }
      },
      "locations": {
        "link": {
          "href": "http://labs.metoffice.gov.uk/edr/collections/metar_demo/locations",
          "hreflang": "en",
          "rel": "data",
          "variables": {
            "title": "Location query",
            "description": "Location query",
            "query_type": "locations",
            "output_formats": [
              "CoverageJSON",
              "GeoJSON",
              "CSV"
            ],
            "default_output_format": "GeoJSON",
            "crs_details": [
              {
                "crs": "CRS84",
                "wkt": "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]]"
              }
            ]
          }
        }
      }
    },
    "crs": [
      "CRS84"
    ],
    "output_formats": [
      "CoverageJSON",
      "GeoJSON",
      "IWXXM"
    ],
    "parameter_names": {
      "Metar observation": {
        "type": "Parameter",
        "description": "Source Metar observation",
        "unit": {
          "label": "",
          "symbol": {
            "value": "",
            "type": "http://codes.wmo.int/wmdr/DataFormat/FM-15-metar"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/wmdr/DataFormat/FM-15-metar",
          "label": "Metar observation"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "ICAO identifier": {
        "type": "Parameter",
        "description": "ICAO identifier",
        "unit": {
          "label": "",
          "symbol": {
            "value": "",
            "type": "https://en.wikipedia.org/wiki/ICAO_airport_code"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/bufr4/b/01/_063",
          "label": "ICAO identifier"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Wind Direction": {
        "type": "Parameter",
        "description": "Wind Direction",
        "unit": {
          "label": "degree true",
          "symbol": {
            "value": "\u00b0",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/degree"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/common/quantity-kind/_aerodromeMeanWindDirection",
          "label": "Wind Direction"
        },
        "measurementType": {
          "method": "mean",
          "period": "-PT10M/PT0M"
        }
      },
      "Wind Speed": {
        "type": "Parameter",
        "description": "Wind Speed",
        "unit": {
          "label": "mph",
          "symbol": {
            "value": "mph",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/mph"
          }
        },
        "observedProperty": {
          "id": " http://codes.wmo.int/common/quantity-kind/aerodromeMeanWindSpeed",
          "label": "Wind Speed"
        },
        "measurementType": {
          "method": "mean",
          "period": "-PT10M/PT0M"
        }
      },
      "Wind Gust": {
        "type": "Parameter",
        "description": "Wind Gust",
        "unit": {
          "label": "mph",
          "symbol": {
            "value": "mph",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/mph"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/common/quantity-kind/_aerodromeMaximumWindGustSpeed",
          "label": "Wind Gust"
        },
        "measurementType": {
          "method": "maximum",
          "period": "-PT10M/PT0M"
        }
      },
      "Visibility": {
        "type": "Parameter",
        "description": "Visibility",
        "unit": {
          "label": "m",
          "symbol": {
            "value": "m",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/m"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/common/quantity-kind/_horizontalVisibility",
          "label": "Visibility"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Air Temperature": {
        "type": "Parameter",
        "description": "",
        "unit": {
          "label": "degC",
          "symbol": {
            "value": "\u00b0C",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/degC"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/common/quantity-kind/_airTemperature",
          "label": "Air Temperature"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Dew point": {
        "type": "Parameter",
        "description": "",
        "unit": {
          "label": "degC",
          "symbol": {
            "value": "\u00b0C",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/degC"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/common/quantity-kind/_dewPointTemperature",
          "label": "Dew point"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Runway Visibility": {
        "type": "Parameter",
        "description": "Runway Visibile Range",
        "unit": {
          "label": "m",
          "symbol": {
            "value": "m",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/m"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/common/quantity-kind/_runwayVisualRangeRvr",
          "label": "Runway Visibility"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Weather": {
        "type": "Parameter",
        "description": "Aerodrome recent weather",
        "unit": {
          "label": "weather",
          "symbol": {
            "value": "",
            "type": "http://codes.wmo.int/49-2/AerodromeRecentWeather"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/49-2/AerodromeRecentWeather",
          "label": "Weather"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Sky condition": {
        "type": "Parameter",
        "description": "Sky condition",
        "unit": {
          "label": "sky",
          "symbol": {
            "value": "",
            "type": "http://{server}"
          }
        },
        "observedProperty": {
          "id": "",
          "label": "Sky condition"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Mean Sea Level Pressure": {
        "type": "Parameter",
        "description": "",
        "unit": {
          "label": "hPa",
          "symbol": {
            "value": "hPa",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/hPa"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/bufr4/b/10/_051",
          "label": "Mean Sea Level Pressure"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      },
      "Station Level Pressure": {
        "type": "Parameter",
        "description": "",
        "unit": {
          "label": "hPa",
          "symbol": {
            "value": "hPa",
            "type": "http://labs.metoffice.gov.uk/edr/metadata/units/hPa"
          }
        },
        "observedProperty": {
          "id": "http://codes.wmo.int/bufr4/b/10/_004",
          "label": "Station Level Pressure"
        },
        "measurementType": {
          "method": "instantaneous",
          "period": "PT0M"
        }
      }
    }
  }
