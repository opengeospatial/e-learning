Introduction to Distributed Computing and Web Services
======================================================



Publishing geospatial data
--------------------------

.. image:: ../img/first-map.jpg
      :height: 654
      :width: 1049  
  
Publishing geospatial data
--------------------------

.. image:: ../img/mobile-map.jpg
      :height: 654
      :width: 1049  

What changed?
-------------

What changed?
-------------

.. image:: ../img/technology.jpg
      :height: 654
      :width: 1049  

What is this?
-------------
.. image:: ../img/internet-colors.jpg
      :height: 654
      :width: 1049  
      
Internet
--------
.. image:: ../img/internet-colors.jpg
      :height: 654
      :width: 1049  

World Wide Web
--------------
* Enabled by Internet
* All **Information** from computers connected around the world.
* Some of these nodes are **servers**

How do we connect to the Web and nodes talk to each other?
-----------------------------
- URL
- HTTP


Uniform Resource Locator (URL)
------------------------------
- http://my.umbc.edu/
- ftp://ftp.funet.fi/pub/standards/RFC/rfc959.txt
- mailto:bermud@me.com

Every node can be identified by a URL
-----------------------
.. image:: ../img/internet-colors.jpg
      :height: 654
      :width: 1049 


Protocols (allow the nodes to connect to each other)
---------
.. image:: ../img/protocols.jpg
      :height: 654
      :width: 1049 

HTTP protocol for performing requests to servers
---------------
- Defines how to connect to servers
- Defines how to download data form servers 
- Most use:  HTTP GET and HTTP POST

HTTP GET is a URL
-----------------

.. code-block:: properties

   http://localhost:8080/geoserver/topp/ows?
   service=WFS&version=1.0.0&request=GetCapabilities
   

   
HTTP key/value pairs
------------------------------

.. code-block:: properties

   http://localhost:8080/geoserver/topp/ows?
   
   service=WFS &
   version=1.0.0 &
   request=GetCapabilities

 - ? goes after the key value pairs
 - & separates the key value pairs
 - " " no white spaces nor space returns   
   
HTTP POST
---------

POST requests involves custom clients and sending of XML encoded data to a server. It is more verbose than HTTP GET. Every GET request here has an equivalent POST request, but the opposite is not true.

::
 
   <?xml version="1.0"?> 
      <wfs:GetCapabilities
         service="WFS"
         version="1.0.0"
        ... 
      
Encodings 
---------
When connecting to a node (server) **encodings** provide the format (arrangement of data elements) and syntax of the data and messages sent to and by the server. 

   - A file in XML 
   - An image in JPG 
   - A temporary binary object in JAVA

Operation, interfaces and services
--------------------
- A well define HTTP GET request is called an **operation**.  
- An **Interface** is a set of operations.
- A **Service** is a set of interfaces

Service
-------
**Distinct part of the functionality** that is provided by an entity through interfaces (ISO 19119:2005). A service can define interfaces to for example:
  
   - manage travel reservations    
   - get bank transactions
   - query maps


Vacuum cleaning robot analogy
------------------------------

A good analogy to a service is a vacuum cleaning robot. It provides a service, 
with a set of interfaces and a set of operations.

.. image:: ../img/roomba-service.jpg
      :width: 70%       
 
Service, interface and operations analogy
------------------------------------------------------------------
      
.. image:: ../img/romba.jpg
      :width: 90%
  

What operations can be defined to request a map on the Web?
-----------------

Anybody can define an operation such as:

- getMap
- getImage
- get2dmap
- getLocation



Heterogeneous services
------------------------

.. image:: ../img/client-services.jpg
      :height: 654
      :width: 1049  
      
Heterogeneous services (lot of effort!)
----------------------


.. image:: ../img/clients-services.jpg
      :height: 654
      :width: 1049


      
Agreement of services is great!
------------------------------------------------------

.. image:: ../img/common-interface.jpg
      :height: 654
      :width: 1049         

If we have a common shared agreed interface ...
--------------------------------

we can define an operation using HTTP to get a map such as:

.. code-block:: properties

      http://myServer?
      VERSION=1.3.0& 
      REQUEST=GetMap& 
      ...   

**This is what OGC standards do (e.g. WMS)!**


Standards enable interoperability
-----------------------------------
*Increase ability to access, fuse and apply* diverse content when and where needed is critical to situational awareness and disaster planning/ response in cross-boundary and cross-domain settings

.. image:: ../img/issues.jpg
      :height: 600
      :width: 1200  





   
   