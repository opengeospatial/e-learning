Radius Query Resources of OGC API - EDR
================

A radius is a region specified with a geographic position and radial distance. An illustration, created using NASA Web WorldWind, is shown below.

.. image:: ../img/radius.png
   :width: 80%

The `radius` query resource returns data for a defined radius. The resource offers a convenience mechanism for querying the API by radius.

The path to the resource is shown below:

`/collections/{collectionId}/radius`

The paths accepts the following parameters:

- coords
- within
- width-units
- z
- parameter-name
- datetime
- crs
- f

An example request is shown below.

`http://example.org/edr/collections/obs_demo/radius?coords=POINT(-0.095882%2051.512983)&within=50&within-units=km&parameter-name=Wind%20Direction&datetime=2022-01-19T04:00Z/2022-01-19T06:00Z&crs=CRS84&f=GeoJSON`
