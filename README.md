
# Getting Started with Swagger Petstore

## Introduction

This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

Find out more about Swagger: [http://swagger.io](http://swagger.io)

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install repo-test-sdk==1.1.9
```

You can also view the package at:
https://pypi.python.org/pypi/repo-test-sdk/1.1.9

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `password` | `string` |  |

The API client can be initialized as follows:

```python
from swaggerpetstore.swaggerpetstore_client import SwaggerpetstoreClient
from swaggerpetstore.configuration import Environment

client = SwaggerpetstoreClient(
    password='Password'
)
```

## Authorization

This API uses `Custom Authentication`.

## List of APIs

* [Pet](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/controllers/pet.md)
* [Store](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/controllers/store.md)
* [User](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/controllers/user.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/pyhton-new/tree/1.1.9/doc/http-request.md)

