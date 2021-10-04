Networking Basics
============================

URL
---
The Uniform Resource Locator (URL) or hyperlink is a string that provides a reference to a resource on the Web. A Web resource can be anything: a page, file, image, or as explained bellow an HTTP GET request. Some examples are as follows:

- http://www.opengeospatial.org
- ftp://ftp.funet.fi/pub/standards/RFC/rfc959.txt
- Mailto: standards-team@ogc.org

The first identifies and provides access to the OGC website. The second identifies and provides access to a text-only document and the third one identifies and provides access to an email address.


Encodings
---------
Encodings provide the format (arrangement of data elements) and syntax of the data and messages, or data send to and by a server.

Messages are files or data streams. The format identifies and determines what type of computer program can be used to read or interact with the file or data stream. For example:
   
   - A file in XML requires a program that can read XML.
   - An image in JPG requires a program that can read JPG images.
   - A temporary binary object in JAVA, requires a Java program that can understand this type of object.

Web Services operate through interfaces and operations that allow the exchange of information with certain encodings.


HTTP
----
The World Wide Web Consortium (W3C) defines protocols for exchanging information on the Web. OGC relies on W3C protocols  to develop interfaces for Geospatial Web services. The two most common ones are as follows:

HTTP GET
^^^^^^^^

The HTTP GET (hereafter GET) method is used to requests a representation of a specified resource via a URL. The request takes the form of:

.. code-block:: properties

	http://www.example.com/wfsserver?
		name1=value1&
		name2=value2&


The above request sends  the key/value pairs of *name1=value1* and *name2=value2* to the server located at  http://www.example.com/wfsserver. The allowed names and values refer to server-specific settings. A fair amount a data can be passed through a GET request, as there is no official limit to the length of a URL. But sending too much data through a GET request can become unwieldy, not to mention rather hard to read. The pro side of a GET request is that it is very compact, and can be sent via a Web browser.


HTTP POST
^^^^^^^^^

An HTTP POST is a request that submits data (usually from an HTML form) to be processed by a server.

POST requests involves custom clients and sending of XML encoded data to a server. It is more verbose than HTTP GET. Every GET request here has an equivalent POST request, but the opposite is not true.

The following two example provide an equivalent HTTP request represented as an HTTP GET and as an HTTP POST.

HTTP GET:

    http://localhost:8080/geoserver/wfs?request=GetCapabilities&VERSION=1.0.0&SERVICE=WFS

HTTP POST:

.. code-block:: xml

   <?xml version="1.0"?>
      <wfs:GetCapabilities
      service="WFS"
      version="1.0.0"

      xmlns:wfs="http://www.opengis.net/wfs"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net
         wfs/1.0.0/WFS-basic.xsd"
   />


Service, Interfaces and Operations
-----------------------------------

It is important to distinguish between service interfaces and operations,
as many of OGC standards are based on these concepts.

Service
^^^^^^^

A Service is a set of interfaces provided by an entity. The service provides a
functionality that distinguishes the entity from other entities [ISO19119:2015]_.
In this context, an entity is a server on the web,
that provides a service, in most cases via HTTP.


Interface
^^^^^^^^^
An interface specifies a set of calls to an object (i.e. server) to execute a process
(e.g., transformation or query). Usually it defines the name of the operations,
the list of parameters and allowed values.

Operation
^^^^^^^^^

In the context of Web services, an operation is a request to a server. For example,
an HTTP GET request is a specific operation. An operation is defined by a service interface.


Vacuum Cleaning Robot Analogy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A good analogy to a service is a vacuum cleaning robot. It provides a service,
with a set of interfaces and a set of operations.

.. image:: ../img/roomba-service.jpg
   :width: 50%

The following can be depicted:

Service
   The robot provides the functionality to clean a room, via a set of interfaces.

Interface
   The robot provides two interfaces: 1) to select the room, 2) an electrical interface.

Operation
   The interface room selection provides three operations to set how the robot will move around a room:

      1. S: Small room
      2. M: Medium room
      3. L: Large room

Service, Interface and Operations
------------------------------------------------------------------

.. image:: ../img/romba.jpg
      :width: 70%


In an OGC Web Service
^^^^^^^^^^^^^^^^^^^^^

A WFS service is a service that provides the functionality to retrieve geospatial features. For example if we were interested in data about points of interest, each point of interest  can have a location,  name and other properties.

We can depict the following:

Service
   WFS 1.1

Interface
   Two types:
      - Basic
      - Transaction

Operations
   For the Basic Interface:
      - GetFeature
      - DescribeFeature
