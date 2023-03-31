# plotting 
- index page : where the user can see all the records
    - ps : not all the data should should be in the index page but only the essential data and a link to another page that contains more info about the record like (pic before and after)

- in the index page i should make a button to create a new record 

- learn more page : it will contain all the data about each record (all the data) + a button to update / maybe ill add the delete button there or in the index page
    - ps : the create page is like the updates only the requests are different

# Web API Documentation

This document outlines the available endpoints for the web API. All endpoints are prefixed with /api.
## Endpoints
- Create a new distribution
``
POST /distributions
``

- List all distributions
``
GET /distributions
``

- Get a distribution by ID 
``
GET /distributions/<int:distribution_id>
``

- Update a distribution 
``
PUT /distributions/<int:distribution_id>
``

- Delete a distribution 
``
DELETE /distributions/<int:distribution_id>
``

- Add a device to a distribution 
``
POST /distributions/<int:distribution_id>/devices
``

- List all devices in a distribution
``
GET /distributions/<int:distribution_id>/devices
``

- Get a device by ID 
``
GET /distributions/<int:distribution_id>/devices/<int:device_id>
``

- Update a device 
``
PUT /distributions/<int:distribution_id>/devices/<int:device_id>
``

- Delete a device 
``
DELETE /distributions/<int:distribution_id>/devices/<int:device_id>
``
