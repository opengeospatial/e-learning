Area Query Resources of OGC API - EDR
================

An area is a region specified with a geographic envelope that may have vertical dimension. An illustration, created using NASA Web WorldWind, is shown below.

.. image:: ../img/area.png
   :width: 80%


The `area` query resource returns data for the defined area. The resource offers a convenience mechanism for querying the API by area, using a Well Known Text (WKT) POLYGON geometry.

The path to the resource is shown below:

`/collections/{collectionId}/area`

The paths accepts the following parameters:

- coords
- z
- parameter-name
- datetime
- crs
- f

An example request is shown below.

`http://example.org/edr/collections/gfs-pressure_at_height/area?coords=POLYGON((-0.898132%2051.179362,-0.909119%2051.815488,0.552063%2051.818884,0.560303%2051.191414,-0.898132%2051.179362))&parameter-name=Pressure_height_above_ground&datetime=2022-01-19T06:00Z/2022-01-19T12:00Z&z=80/80&crs=CRS84&f=CoverageJSON`
