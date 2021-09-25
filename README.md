# API Rest for manage users
---
## Overview:

this repository contains a simple API Rest for manage users, this app is essentially a CRUD

## how run this project:

1. Clone this repository
2. Create you file .env based on the .env.example
3. you build the container with the following command from the root of the directory
  * `docker-compose build`
4. now run the container with the command
 * `docker-compose up`
5. then you create a superuser using
 * `python manage.py createsuperuser`
 **note**: this is necessary for creating other users since this action required to be login
6. now go to your browser to http://localhost:8000/api/v1/users/

## End-points
### User
#### POST - create
 * For the create method the following URL is used:
http://localhost:8000/api/v1/users/
**note**:
* The data is inserted with the following JSON format:
```javascript
{
    "username": "",
    "first_name": "",
    "last_name": "",
    "date_birth": null,
    "mobile_phone": "",
    "email": "",
    "address": "",
    "session_active": false,
    "password": ""
}
```
---
#### GET, PUT and DELETE - user
http://localhost:8000/api/v1/users/{#id}

### List
http://localhost:8000/api/v1/users/