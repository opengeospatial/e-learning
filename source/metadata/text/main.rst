Metadata - Introduction
==================

Introduction
------------
Metadata can be thought of as descriptive information about data, services and other information resources. It is typically published through a Catalogue Service for the Web (CSW), however other OGC web services also offer high level metadata about the resources they publish.

Geospatial data resources are typically described using metadata written according to the OGC Abstract Specification Topic 11 – Metadata (which is published by the International Organisation as ISO 19115-1:2014). Metadata documents conforming to ISO 19115-1:2014 are serialized in XML following the schema described in ISO 19115-3:2016.


Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- OGC Catalogue Service for Web (CSW): This standard describes the interface that is mostly used for publishing metadata.
- OGC Geography Markup Language (GML): This standard is used by ISO 19115-3:2016 for describing the geographic extent of the resource represented by the metadata.

Usage and value of metadata
--------------------

Metadata enables organizations to retain their knowhow.

Metadata enables developers to effectively and efficiently integrate data, services and other information resources.

Metadata enables users to very quickly discover data and how to access it.

Overview of Concepts relating to Metadata
--------------------

Imagine receiving a set of cans without any labels to indicate what is in the can, or who produced the can and its contents. For illustrative purposes, see the cans shown below.


.. image:: ../img/cans.jpg
      :height: 654
      :width: 1049


* What is Missing ?*

.. image:: ../img/nutrition_label.jpg
      :height: 654
      :width: 1049

A dataset or a service without any metadata is much like a can without any descriptive labeling on it.


Metadata can help data users and data providers answer the following questions.

Who?
--------------
- Who collected the data?
- Who processed the data?
- Who wrote the metadata?
- Who to contact for questions?
- Who to contact to order?
- Who owns the data?

What?
---------------
- What are the data about?
- What project were they collected under?
- What are the constraints on their use?
- What is the quality?
- What are appropriate uses?
- What parameters were measured?
- What format are the data in?

Why?
--------------
- Why were the data collected?

Where?
-----

- Where were the data collected?
- Where were the data processed?
- Where are the data located?

When?
----
- When were the data collected?
- When were the data processed?

How?
---
- How were the data collected?
- How were the data processed?
- How do I access the data?
- How do I order the data?
- How much do the data cost?
- How was the quality assessed?

Example Metadata
----------------------------

An example **GetCapabilities** request that can be used to identify the coverages that are available from the service is shown below.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=getcapabilities

An example **DescribeCoverage** request is shown below. Note that the response is a CoverageDescription XML document. This file would inform the client application about the structure of the coverage, for example dimensions if the coverage is gridded.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=DescribeCoverage&coverageid=MER_FRS_1PNUPA20090701_124435_000005122080_00224_38354_6861_RGB

An example **GetCoverage** request that can be used to retrieve data from the service is shown below.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=getcoverage&coverageid=MER_FRS_1PNUPA20090701_124435_000005122080_00224_38354_6861_RGB
