Coffee Shop Project Backend

Version: 1.0.0

Author: alone

Stack: FastAPI, Postgresql, SqlAlchemy, JWT Authentication

Status: Done

Backend

Auth endpoint

- /login - Login POST

- /register - Register POST

Users endpoint

- /api/v1/users/ - Get all users [Permission Only stuff] GET

- /api/v1/users/me/ - Get info about target user [Permission Only stuff] GET

- /api/v1/users/user/exists/ - Get exists status about target user True or False [Permission Public] GET

Coffee endpoint

- /api/v1/coffee/ - Get all coffee [Permission Public] GET

- /api/v1/coffee/ - Create new coffee [Permission Only stuff] POST

- /api/v1/coffee/id/ - Get coffee by id [Permission Public] GET

- /api/v1/coffee/id/ - Delete coffee by id [Permission Only stuff] DELETE

Orders endpoint

- /api/v1/oirders/ - Get all orders [Permission Only stuff] GET

- /api/v1/coffee/ - Create new order [Permission Only stuff] POST

- /api/v1/coffee/id/ - Get order by id [Permission Only stuff] GET

- /api/v1/coffee/id/ - Update order status by id [Permission Only stuff] PATCH

HomePage endpoin

- / - Home Page GET
