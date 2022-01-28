Query Resources of OGC API - Environmental Data Retrieval
================

Query resources are spatio-temporal queries which support operation of the API for the access and use of the spatio-temporal data resources.

Query resources share several common parameters, which makes it easier for developers to implement the queries.

Where the query applies to a collection, the pattern is as follows:

`/collections/{collectionId}/{queryType}`

The parameter `queryType` can be one of the following:

- position
- area
- cube
- trajectory
- corridor
- radius
- instances
- locations
- items

Where the query applies to an instance, the pattern is as follows:

`/collections/{collectionId}/instances/{instanceId}/{queryType}`
