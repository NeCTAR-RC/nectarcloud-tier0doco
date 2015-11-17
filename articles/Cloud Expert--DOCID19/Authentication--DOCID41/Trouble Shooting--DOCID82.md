## Debugging Dashboard Authentication

The NeCTAR Dashboard uses [Australian Access Federation][aaf] for its authentication.
If you have any problems with the login, you can contact the IT helpdesk in your
local organization or institution. You can log a ticket in the NeCTAR
[helpdesk][helpdesk]. You can also submit a help request to aaf
[helpdesk][aafhelp] for help.



## Debugging API Authentication

You must first send an authentication request to OpenStack Identity service to
get an authentication token before you can access API services. To request an
authentication token, you must supply the credentials in the authentication request.

The credentials are a combination of username, password and project name. You also
need to get the authentication URL for credentials validation.

You need to make sure you have the correct Credentials download from the NeCTAR
Dashboard. Before you use them, please check the username, projet name and the
API endpoints. You can reference these information from the script file you
obtained from the NeCTAR Dashboard.

After you send the username/password and project name to the authentication URL,
You will get a authentication token. Then, you need to include the token in the
X-Auth-Token HTTP header. If you access multiple API services, you must get a
token for each API service. The token has a limited time and can become invalid
for other reasons.

### Authentication and API request workflow

- Send a request with credentials to get a token from the Identity endpoint. If
 the request succeeds, the server returns an authentication token.

- Send API requests and include the token in the X-Auth-Token HTTP header. The
 following HTTP requests use the same token until the requests complete.
 
- If a 401 Unauthorized error returned, the request requires a new token.

### Debug Authentication

The below use cURL commands to show your how to debug authentication request.
For information about cURL, see [http://curl.haxx.se/][curl]. For information
about the OpenStack APIs, see [OpenStack API Reference][api].


To get a valid token, you need 3 parameters:

- username

- password

- project name/project id

The below shows a code to get token:


```

curl -s -X POST https://keystone.rc.nectar.org.au:5000/v2.0/tokens \

            -H "Content-Type: application/json" \
            
            -d '{"auth": {"tenantName": "'"$OS_TENANT_NAME"'", "passwordCredentials":
            
            {"username": "'"$OS_USERNAME"'", "password": "'"$OS_PASSWORD"'"}}}' \
            
            | python -m json.tool

```

You need to replace the username, password and tenantname with the values in
the authentication script file you obtained from the NeCTAR Dashboard.

The response would look like below:


```

{
    "access": {
        "metadata": {
            "is_admin": 0,
            "roles": [
                "22",
                "143"
            ]
        },
        "serviceCatalog": [
            {
                "endpoints": [
                    {
                        "adminURL": "https://nova.rc.abc:8774/v1.1/",
                        "internalURL": "https://nova.rc.abc:8774/v1.1/",
                        "publicURL": "https://nova.rc.abc:8774/v1.1/",
                        "region": "Melbourne"
                    }
                ],
                "endpoints_links": [],
                "name": "Compute Service",
                "type": "compute"
            }
        ],
        "token": {
            "audit_ids": [
                "SUtsLIdWQJ634dfdsfdsffdszVe6D2ijg"
            ],
            "expires": "2015-10-15T10:08:53Z",
            "id": "MIIUsdfsfsd2AYJKoZIhvcNAQcCoIIUyTCCFMUCAQ.........eaL6Z8h",
            "issued_at": "2015-10-15T04:08:53.231576",
            "tenant": {
                "allocation_id": 170,
                "description": null,
                "enabled": true,
                "expires": "2018-07-01",
                "id": "e4c1e4e82cd5495d89d52d694ea62e50sdadsweqe",
                "name": "Marine-VL"
            }
        },
        "user": {
            "id": "",
            "name": "",
            "roles": [
                {
                    "name": "Member"
                },
                {
                    "name": "TenantManager"
                }
            ],
            "roles_links": [],
            "username": ""
        }
    }
}

```

Then you can use the token obtained from this output in the API for authentication.

Following is an example of how to use the token in using Nova API to list flavors:


```

curl -s -H \

            "X-Auth-Token:token" \
            
            http://8.21.28.222:8774/v2/tenant_id/flavors \
            
            | python -m json.tool

```

You need to replace the token and the URL. You can find the Nova API endpoint
URL from the NeCTAR [Dashboard][dashboard]. The above request would return the
following output:


```

{
    "flavors": [
        {
            "id": "1",
            "links": [
                {
                    "href": "http://8.21.28.222:8774/v2/f9828a18c6484624b571e85728780ba8/flavors/1",
                    "rel": "self"
                },
                {
                    "href": "http://8.21.28.222:8774/f9828a18c6484624b571e85728780ba8/flavors/1",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.tiny"
        },
        {
            "id": "2",
            "links": [
                {
                    "href": "http://8.21.28.222:8774/v2/f9828a18c6484624b571e85728780ba8/flavors/2",
                    "rel": "self"
                },
                {
                    "href": "http://8.21.28.222:8774/f9828a18c6484624b571e85728780ba8/flavors/2",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.small"
        },
        {
            "id": "3",
            "links": [
                {
                    "href": "http://8.21.28.222:8774/v2/f9828a18c6484624b571e85728780ba8/flavors/3",
                    "rel": "self"
                },
                {
                    "href": "http://8.21.28.222:8774/f9828a18c6484624b571e85728780ba8/flavors/3",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.medium"
        },
        {
            "id": "4",
            "links": [
                {
                    "href": "http://8.21.28.222:8774/v2/f9828a18c6484624b571e85728780ba8/flavors/4",
                    "rel": "self"
                },
                {
                    "href": "http://8.21.28.222:8774/f9828a18c6484624b571e85728780ba8/flavors/4",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.large"
        },
        {
            "id": "5",
            "links": [
                {
                    "href": "http://8.21.28.222:8774/v2/f9828a18c6484624b571e85728780ba8/flavors/5",
                    "rel": "self"
                },
                {
                    "href": "http://8.21.28.222:8774/f9828a18c6484624b571e85728780ba8/flavors/5",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.xlarge"
        }
    ]
}

```


[aaf]: http://aaf.edu.au/
[helpdesk]: https://support.nectar.org.au/support/home
[aafhelp]: http://support.aaf.edu.au/home
[curl]: http://curl.haxx.se/
[api]: http://developer.openstack.org/api-ref.html
[dashboard]: https://dashboard.rc.nectar.org.au
