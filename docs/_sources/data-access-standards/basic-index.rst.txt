Data Access Standards
=======================

Knowing how to ask an application a question is just as important as being able to read the response of the application. Without a well defined way of creating, retrieving, updating or deleting geospatial information offered by a service, it would be almost impossible to invoke any of this behavior in an application. Further, an application accessible over a network would need to be able to describe itself and the resources it offers in order for another application across the network to know what behavior is supported and what resources are available.

OGC web services such as the Web Feature Service (WFS) and Web Coverage Service (WCS) provide the means to access geospatial data across a network in order to perform operations such as creating, retrieval, updating or deleting resources. The web services specialise in specific types of resources, for example WFS specialises in vector feature data, whereas WCS specialises in coverages e.g. gridded raster data.

In situations where the data is being collected by sensors and being transmitted across a network in real time or near-real time, the Sensor Observation Service (SOS) and SensorThings API standards offer an interface that allows interoperable data access. The SOS standard provides an interface that supports access to XML-encoded information about sensor models, observations and features of interest to a sensor. In contrast, the SensorThings API provides an interface that supports access to JSON-encoded information about the aforementioned resources. SensorThings API is based on Representational State Transfer (REST) principles and has been designed with the Internet-of-Things (IoT) as a key driver.

Contents:

.. toctree::
   :maxdepth: 1
   :name: acc

   ../ogcapi-features/text/basic-index.rst
   ../wfs/text/basic-index.rst
   ../wcs/text/basic-index.rst
   ../sta/text/index.rst
   ../sos/text/index.rst
