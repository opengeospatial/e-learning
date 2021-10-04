Resources of OGC API - Environmental Data Retrieval
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

**TBA**
