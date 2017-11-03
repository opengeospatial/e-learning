Styled Layer Descriptor (SLD)
============================

Geospatial data (vector and raster) have no intrinsic visual component.
----------------------------------------------------------------------------------------------------------------------------------------------


.. code-block:: xml

    <Bridge>
      <span>100</span>
      <height>200</height>
      <gml:centerLineOf>
        <gml:LineString>
           <gml:pos>100 200</gml:pos>
           <gml:pos>200 200</gml:pos>
        </gml:LineString>
      </gml:centerLineOf>
    </Bridge>

How are we supposed to render the bridge line?
--------------------------------------------------------------------------------------------
- How thick is the line?
- What color?
- What type of line?


SLD enables configuration of how to portray data
------------------------------------------------------------------------------------------------
The Styled Layer Descriptor (SLD) is a standard that enables an application  to configure in an XML document how to portray vector data in a WMS.

SLD Example
-----------------------

SLD XML document describing how point data can be styled as blue circles with a diameter of 5 pixels.

.. image:: ../img/sld-point.jpg
      :width: 50%
