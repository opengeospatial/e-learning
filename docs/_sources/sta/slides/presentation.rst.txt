SensorThings API
===================

Overview
----------------
Interface for Internet of Things

Demo Server and examples
------------------------------------------------
- `Demo From SensorUp <http://developers.sensorup.com/docs/>`_
- Link: http://toronto-bike-snapshot.sensorup.com/v1.0/
- Behaves like a GetCapabilities. 
- Provides URLs to interrogate further the service

Return Base Resource Path
----------------------------------------
http://toronto-bike-snapshot.sensorup.com/v1.0/

.. code-block:: properties

  {  
    "value":[  
        {  
            "name":"Things",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/Things"
        },
        {  
            "name":"Locations",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/Locations"
        },
        {  
            "name":"HistoricalLocations",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/HistoricalLocations"
        },
        {  
            "name":"Datastreams",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/Datastreams"
        },
        
        
 
Return Base Resource Path (Cont)
----------------------------------------------------

.. code-block:: properties
        
        
        {  
            "name":"Sensors",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/Sensors"
        },
        {  
            "name":"Observations",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/Observations"
        },
        {  
            "name":"ObservedProperties",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/ObservedProperties"
        },
        {  
            "name":"FeaturesOfInterest",
            "url":"http://pm25-march.singapore2017.sensorup.com/v1.0/FeaturesOfInterest"
        }
    ]
   }
   
 
Which *Things* are available in the server?
----------------------------------------------------------------------------------
 
http://toronto-bike-snapshot.sensorup.com/v1.0/Things
 
 .. code-block:: properties

   {  
  "@iot.count":199,
  "@iot.nextLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/
         Things?$top=100&$skip=100",
  "value":[  
    {  
      "@iot.id":206047,
      "@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Things(206047)",
      "description":"Bloor St / Brunswick Ave Toronto bike share station with data
                of available bikes and available docks",
      "name":"7061:Bloor St / Brunswick Ave",
      "properties":{  

      },
      ...

Getting a *Datastream* for a  thing
------------------------------------------------------------------------
http://toronto-bike-snapshot.sensorup.com/v1.0/Things(206047)/Datastreams

.. code-block:: properties

   {  
    "@iot.count":2,
    "value":[  
    {  
      "@iot.id":206051,
      "@iot.selfLink":
          "http://toronto-bike-snapshot.sensorup.com/v1.0/Datastreams(206051)",
      "description":
          "... available docks count for the Toronto bike share station Bloor St ",
      "name":"7061:Bloor St / Brunswick Ave:available_docks",
      "observationType":
          "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation",
      "unitOfMeasurement":{  
        "symbol":"{TOT}",
        "name":"dock count",
        "definition":"http://unitsofmeasure.org/ucum.html#para-50"
      },
      ....

Note: Datastreams define the unit of measurement
--------------------------------------------------------------------------
 
 
 .. code-block:: properties
 
      "observationType":
          "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation",
      "unitOfMeasurement":{  
        "symbol":"{TOT}",
        "name":"dock count",
        "definition":"http://unitsofmeasure.org/ucum.html#para-50"
      },
 
   
Getting the *Observations* related to a stream
--------------------------------------------------------------------


http://toronto-bike-snapshot.sensorup.com/v1.0/Datastreams(206051)/Observations


.. code-block:: properties

   {  
  "@iot.count":3511,
  "@iot.nextLink":
         "http://toronto-bike-snapshot.sensorup.com/...",
  "value":[  
    {  
      "@iot.id":1595467,
      "@iot.selfLink":
         "http://toronto-bike-snapshot.sensorup.com/v1.0/Observations(1595467)",
      "phenomenonTime":"2017-02-16T21:55:12.233Z",
      "result":"23",
      "resultTime":null,
      "Datastream@iot.navigationLink":
         "http://toronto-bike-snapshot.sensorup.com/v1.0/Observations(1595467)/Datastream",
      "FeatureOfInterest@iot.navigationLink":
         "http://toronto-bike-snapshot.sensorup.com/v1.0/Observations(1595467)/FeatureOfInterest"
    },
    
    
Complex Query
------------------------------

- Expands Datastreams and observations in one query
- Feature of Interest = 7000:Ft. York / Capreol Crt.
- Start time =  2017-01-01T11:30:00.000Z
- End time = 2017-03-01T11:30:00.000Z

`Link <http://toronto-bike-snapshot.sensorup.com/v1.0/Things?$expand=Datastreams/Observations/FeatureOfInterest&$filter=Datastreams/Observations/FeatureOfInterest/name eq '7000:Ft. York / Capreol Crt.' and Datastreams/Observations/phenomenonTime ge 2017-01-01T11:30:00.000Z and Datastreams/Observations/phenomenonTime le 2017-03-01T11:30:00.000Z>`_


 .. code-block:: properties
 
   http://toronto-bike-snapshot.sensorup.com/v1.0/Things?
   $expand=Datastreams/Observations/FeatureOfInterest&
   $filter=Datastreams/Observations/FeatureOfInterest/
   name eq '7000:Ft. York / Capreol Crt.' and
   Datastreams/Observations/phenomenonTime ge 2017-01-01T11:30:00.000Z 
   and
   Datastreams/Observations/phenomenonTime le 2017-03-01T11:30:00.000Z
 
Complex Query Response
------------------------------
 
 .. code-block:: properties

   {  
  "@iot.count":1,
  "value":[  
    {  
      "@iot.id":5,
      "@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Things(5)",
      "description":
            "Ft. York / Capreol Crt. Toronto bike share station available bikes and docks",
      "name":"7000:Ft. York / Capreol Crt.",
      "properties":{  

      },
      "Datastreams":[  
        {  
          "@iot.id":9,
          "@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Datastreams(9)",
          "description":
               "...available docks count for the Toronto bike share station Ft. York / Capreol Crt.",
          "name":"7000:Ft. York / Capreol Crt.:available_docks",
          "observationType":
               "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation",
          "unitOfMeasurement":{  
            "symbol":"{TOT}",
            "name":"dock count",
            "definition":"http://unitsofmeasure.org/ucum.html#para-50"
          },
          
Complex Query Response  (cont)
----------------------------------------------------------          
  .. code-block:: properties
 
         "Observations@iot.nextLink":
                  ".../v1.0/Datastreams(9)/Observations?$top=100&$skip=100",
          "Observations":[  
            {  
              "@iot.id":1595545,
              "@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Observations(1595545)",
              "phenomenonTime":"2017-02-16T21:55:12.797Z",
              "result":"10",
              "resultTime":null,
              "Datastream@iot.navigationLink":
                     ".... /v1.0/Observations(1595545)/Datastream",
              "FeatureOfInterest":{  
                "@iot.id":10,
                "@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/FeaturesOfInterest(10)",
                "description":"  ...

 

  