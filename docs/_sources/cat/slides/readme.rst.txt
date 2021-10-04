exercise-metadata-object.rst
-------------------------------------------
   - Exercise for users to understand how to assign properties to things
   - Issue about naming properties in a different way
   
exercise-opensearch.rst
----------------------------------------------

`request <http://demo.pycsw.org/gisdata/csw?service=CSW&version=3.0.0&request=GetCapabilities&mode=opensearch&service=CSW&version=3.0.0&request=GetRecords&elementsetname=full&typenames=csw:Record&resulttype=results&q=California>`_. The request looks as follows:

.. code-block:: properties

   http://demo.pycsw.org/gisdata/csw?
   service=CSW&
   version=3.0.0&
   request=GetCapabilities&
   mode=opensearch&
   service=CSW&
   version=3.0.0&
   request=GetRecords&
   elementsetname=full&
   typenames=csw:Record&
   resulttype=results&
   q=California


Result:
.. code-block:: properties
   
   ...
   <os:Query role="request"/>
   <os:totalResults>72</os:totalResults>
   <os:startIndex>1</os:startIndex>
   <os:itemsPerPage>10</os:itemsPerPage>
   ...
