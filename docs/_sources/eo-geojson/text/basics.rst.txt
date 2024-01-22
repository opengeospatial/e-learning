Basics of OGC EO Dataset Metadata GeoJSON
==============================================

The metadata encoding defined in the OGC EO Dataset Metadata GeoJSON(-LD) standard satisfies the following design goals:

* Feature-based GeoJSON model: The model maximizes reuse of pre-existing standardized property names. 
* Simplicity: The standard provides a simpler, overarching exchange format integrating comments from the Committee on Earth Observation Satellites (CEOS) Working Group on Information Systems and Services (WGISS) community.
* Multiple use cases: The metadata model supports metadata for an acquisition, for a simple product derived from one acquisition, or for a synthetic product.

This tutorial focuses only on the EO GeoJSON encoding.

Configuring GeoServer for EO-GeoJSON
------------------------------------

At the time of writing this tutorial, GeoServer is the Reference Implementation for this standard. GeoServer can be configured to export metadata conforming to the the OGC EO Dataset Metadata GeoJSON(-LD) standard by installing the `Features-Templating Extension <https://docs.geoserver.org/main/en/user/community/features-templating/index.html>`_. 

The following instructions have been tested with GeoServer 2.24.

Once the Feature Templating extension has been installed, configure a data source such as the following properties file to serve the metadata as a GeoServer layer.

For simplicity, name it `metadata` and place it in the `cite` namespace, so that it can be accessed through the identifier `cite:metadata`.

.. code-block:: properties
  :linenos:


   _=id:Integer,identifier:String,status:String,title:String,date:String,updated:String,platform_id:String,platform_name:String,described_by:String,location:Geometry:srid=4326
   metadata.1=1|http://example.org/record/1|ARCHIVED|Example metadata 1|2021-01-26T11:30:18Z|2021-01-26T11:30:18Z|https://earth.esa.int/concept/sentinel-1|Sentinel-1|http://geoserver.org|POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
   metadata.2=2|http://example.org/record/2|ARCHIVED|Example metadata 2|2021-01-26T11:30:18Z|2021-01-26T11:30:18Z|https://earth.esa.int/concept/sentinel-2|Sentinel-2|http://geoserver.org|POLYGON ((50 30, 60 60, 40 60, 30 40, 50 30))

Thereafter, add a feature template as described `here <https://docs.geoserver.org/main/en/user/community/features-templating/configuration.html#add-features-templates-to-geoserver>`_.

.. code-block:: json
  :linenos:


    {
    "type": "Feature",
    "id": "${identifier}",
    "geometry": "${location}",
    "properties": {
        "status": "${status}",    
            "identifier": "${identifier}",
            "title": "${title}",
            "date": "${date}",
            "updated": "${updated}",   
            "acquisitionInformation": [
                {
                    "platform": {
                        "id": "${platform_id}",
                        "platformShortName": "${platform_name}"
                    },
            "acquisitionParameters": {
            "beginningDateTime": "${date}",
            "endingDateTime": "${date}",
            "acquisitionType": "NOMINAL"
            }
                }
            ],
        "productInformation": {
        "availabilityTime": "${updated}"
        },   
        "offerings": [
            {
                "code":"http://www.opengis.net/spec/owc-geojson/1.0/req/wms",
                "operations": [
                {
                    "code":"urn:oasis:names:specification:docbook:dtd:xml:4.1.2",
                    "method":"GET",
                    "href":"http://example.org/wms?REQUEST=GetCapabilities&version=1.3.0&service=WMS"
                }
                ]
            }		
        ],          
            "links": {
                "describedBy": [
                    {
                        "href": "https://zenodo.org/record/1209633"
                    }
                ]
            }
    }
    }

Once the feature template has been added to GeoServer, next associate the template with the layer containing the metadata (`cite:metadata`) and set the template to be applied to the GeoJSON output format.

You can now access the layer through the following URL:

http://localhost:8080/geoserver/cite/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=cite%3Ametadata&maxFeatures=50&outputFormat=application%2Fjson

The response should be as shown below.

.. code-block:: json
  :linenos:


    {
    "type": "FeatureCollection",
    "features": [
        {
        "type": "Feature",
        "id": "http://example.org/record/1",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
            [
                [
                30,
                10
                ],
                [
                40,
                40
                ],
                [
                20,
                40
                ],
                [
                10,
                20
                ],
                [
                30,
                10
                ]
            ]
            ]
        },
        "properties": {
            "status": "ARCHIVED",
            "identifier": "http://example.org/record/1",
            "title": "Example metadata 1",
            "date": "2021-01-26T11:30:18Z",
            "updated": "2021-01-26T11:30:18Z",
            "acquisitionInformation": [
            {
                "platform": {
                "id": "https://earth.esa.int/concept/sentinel-1",
                "platformShortName": "Sentinel-1"
                },
                "acquisitionParameters": {
                "beginningDateTime": "2021-01-26T11:30:18Z",
                "endingDateTime": "2021-01-26T11:30:18Z",
                "acquisitionType": "NOMINAL"
                }
            }
            ],
            "productInformation": {
            "availabilityTime": "2021-01-26T11:30:18Z"
            },
            "offerings": [
            {
                "code": "http://www.opengis.net/spec/owc-geojson/1.0/req/wms",
                "operations": [
                {
                    "code": "urn:oasis:names:specification:docbook:dtd:xml:4.1.2",
                    "method": "GET",
                    "href": "http://example.org/wms?REQUEST=GetCapabilities&version=1.3.0&service=WMS"
                }
                ]
            }
            ],
            "links": {
            "describedBy": [
                {
                "href": "https://zenodo.org/record/1209633"
                }
            ]
            }
        }
        },
        {
        "type": "Feature",
        "id": "http://example.org/record/2",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
            [
                [
                50,
                30
                ],
                [
                60,
                60
                ],
                [
                40,
                60
                ],
                [
                30,
                40
                ],
                [
                50,
                30
                ]
            ]
            ]
        },
        "properties": {
            "status": "ARCHIVED",
            "identifier": "http://example.org/record/2",
            "title": "Example metadata 2",
            "date": "2021-01-26T11:30:18Z",
            "updated": "2021-01-26T11:30:18Z",
            "acquisitionInformation": [
            {
                "platform": {
                "id": "https://earth.esa.int/concept/sentinel-2",
                "platformShortName": "Sentinel-2"
                },
                "acquisitionParameters": {
                "beginningDateTime": "2021-01-26T11:30:18Z",
                "endingDateTime": "2021-01-26T11:30:18Z",
                "acquisitionType": "NOMINAL"
                }
            }
            ],
            "productInformation": {
            "availabilityTime": "2021-01-26T11:30:18Z"
            },
            "offerings": [
            {
                "code": "http://www.opengis.net/spec/owc-geojson/1.0/req/wms",
                "operations": [
                {
                    "code": "urn:oasis:names:specification:docbook:dtd:xml:4.1.2",
                    "method": "GET",
                    "href": "http://example.org/wms?REQUEST=GetCapabilities&version=1.3.0&service=WMS"
                }
                ]
            }
            ],
            "links": {
            "describedBy": [
                {
                "href": "https://zenodo.org/record/1209633"
                }
            ]
            }
        }
        }
    ],
    "totalFeatures": 2,
    "numberMatched": 2,
    "numberReturned": 2,
    "timeStamp": "2024-01-22T18:33:21.068Z",
    "crs": {
        "type": "name",
        "properties": {
        "name": "urn:ogc:def:crs:EPSG::4326"
        }
    }
    }