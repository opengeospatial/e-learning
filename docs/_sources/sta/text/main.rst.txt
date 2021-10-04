SensorThings - Introduction
===============================

Introduction
------------

The Internet of Things (IoT) is a global information infrastructure that enables advanced services by interconnecting both physical and virtual "things" based on existing and evolving interoperable information and communication technologies [ITU-T].
To facilitate geospatial interoperability between devices in the IoT, the OGC has published the OGC SensorThings API.

The OGC SensorThings API is a multi-part standard for an open and geospatial-enabled approach for interconnecting devices, data, and applications of the Internet of Things (IoT). The first part of the standard describes the interface for Sensing. The second part describes the interface for Tasking. The Sensing part standardizes the management and retrieval of observations and metadata from heterogeneous IoT sensor systems. The Tasking part, which is to be developed in the future, is expected to provide a standard way for parameterizing - also called tasking - of IoT devices that can be instructed to carry out observations or perform other functions.


Background
--------------------

History
    SensorThings API Part 1: Sensing version 1.0 in July 2016.
Test Suite
  Test suites are available for:
      - SensorThings API Part 1 version 1.0 <https://github.com/opengeospatial/ets-sta10>
Implementations
    Implementations are listed on the OGC website here <http://www.opengeospatial.org/resource/products/byspec>

Usage
^^^^^^

The SensorThings API allows for the access and dissemination of sensor-collected data about any object of the physical world (physical things) or the information world (virtual things) that is capable of being identified and integrated into communication networks. The data is accessed through a resource-centric interface that is based on Representational state transfer (REST) principles. The data returned by the API is serialized in JavaScript Object Notation (JSON).

The benefit of adopting REST and JSON for the SensorThings API is that they offer greater efficiency in devices of constrained Size, Weight and Power (SWaP) such as microcomputers, smart home controllers, nano-Unmanned Aerial Vehicles (UAVs), smartphones, smart watches and tablets. The use of REST also makes it easier for web developers and the applications they implement to access data through resource-centric Uniform Resource Locator (URL) patterns.

Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Sensor Observation Service Interface Standard (SOS): The SensorThings API is designed specifically to enable the dissemination of observations from resource-constrained IoT devices and the Web developer community. In contrast to SOS, the SensorThings API uses approaches that are considered more efficient for example, REST, JSON and the Message Queuing Telemetry Transport (MQTT).
- Web Feature Service Interface Standard (WFS) : The WFS standard is designed to allow for serving feature types of any kind. Other than requiring the data to be serializable in Geography Markup Language (GML), WFS does not place any other significant constraints. In contrast, SensorThings API formalized how specific entities and concepts should be represented and serialized.

Resources Offered
-----------------

Rather than operations, it is more appropriate to discuss what the SensorThings API offers through the entities it provides as resources. The following is a list entities supported by the API:

Thing
   The OGC SensorThings API follows the ITU-T definition, i.e., with regard to the Internet of Things, a thing is an object of the physical world (physical things) or the information world (virtual things) that is capable of being identified and integrated into communication networks [ITU-T].
Location
   The Location entity locates the Thing or the Things it associated with. A Thing’s Location entity is defined as the last known location of the Thing.
HistoricalLocation
   A Thing’s HistoricalLocation entity set provides the times of the current (i.e., last known) and previous locations of the Thing.
Datastream
  A Datastream groups a collection of Observations measuring the same ObservedProperty and produced by the same Sensor.
Sensor
   A Sensor is an instrument that observes a property or phenomenon with the goal of producing an estimate of the value of the property.
ObservedProperty
   An ObservedProperty specifies the phenomenon of an Observation.
Observation
   An Observation is the act of measuring or otherwise determining the value of a property.
FeatureOfInterest
   The phenomenon against which an observation is made is a property of the feature of interest.


Example
-------

This `SensorThings API server<http://toronto-bike-snapshot.sensorup.com/v1.0/>`_publishes sample data about available bikes and docks from a Toronto bike share station.

An example request to retrieve sensors through the API is shown below.

http://toronto-bike-snapshot.sensorup.com/v1.0/Sensors

The response, which is presented below, reports that there are two sensors: one for tracking how many docks are available in a bike station and another sensor for tracking how many bikes are available in a bike station.

.. code-block:: javascript

        {"@iot.count":2,
        	"value":[
        		{"@iot.id":4,"@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Sensors(4)","description":"A sensor for tracking how many docks are available in a bike station","name":"available_docks","encodingType":"text/plan","metadata":"https://member.bikesharetoronto.com/stations","Datastreams@iot.navigationLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Sensors(4)/Datastreams"
        		      },
        		{"@iot.id":3,"@iot.selfLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Sensors(3)","description":"A sensor for tracking how many bikes are available in a bike station","name":"available_bikes","encodingType":"text/plan","metadata":"https://member.bikesharetoronto.com/stations","Datastreams@iot.navigationLink":"http://toronto-bike-snapshot.sensorup.com/v1.0/Sensors(3)/Datastreams"
        		      }
                   ]
        }


The data returned by the service can be rendered by a desktop Geographic Information System (GIS) or a web application. Alternatively, it can be forwarded to an OGC WPS for further processing.


Client Usage
------------

A client needs to know the location of the SensorThings API service to be able to interact with the server.  The location is usually called the 'end point' of the service and is represented by the service root URI. Resources available through the service can be accessed by appending a resource path and, optionally query options.

For example, the first line of the following URL is the service root URI. The second line is the resource path. The third line is the query option.

.. code-block:: properties

  http://toronto-bike-snapshot.sensorup.com/v1.0
  /Datastreams(206051)/Observations(1593917)
  ?$select=result

`The link to the request is <http://toronto-bike-snapshot.sensorup.com/v1.0/Datastreams(206051)/Observations(1593917)?$select=result>`_


References
----------

`ITU-T, Overview of the Internet of things <http://www.itu.int/ITU-T/recommendations/rec.aspx?rec=y.2060>`_

`SensorUp SensorThings API <https://www.sensorup.com/>`_
