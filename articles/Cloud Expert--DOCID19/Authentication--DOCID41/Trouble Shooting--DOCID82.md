## Debugging Dashboard Authentication

The NeCTAR Dashboard uses [Australian Access Federation][aaf] for its authentication.
If you have any problems with the login, you can contact the IT helpdesk in your
local organization or institution. You can log a ticket in the NeCTAR
[helpdesk][helpdesk]. You can also submit a help request to aaf
[helpdesk][aafhelp] for help.


[aaf]: http://aaf.edu.au/
[helpdesk]: https://support.nectar.org.au/support/home
[aafhelp]: http://support.aaf.edu.au/home

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
            "id": "MIIUsdfsfsd2AYJKoZIhvcNAQcCoIIUyTCCFMUCAQExDTALBglghkgBZQMEAgEwghOnBgkqhkiG9sdfdsfsfdsw0BBwGgghOYBIITlHsiYWNjZXNzIjp7InRva2VuIjp7Imlzcdsfdsfsd3VlZF9hdCI6IjIwMTsdfsdfUtMTAtMTVUMDQ6MDg6NTMuMjMxNTc2IiwiZXhwaXJlcyI6IjIwMTUtMTAtMTVUMTA6MDg6NTNaIiwiaWQiOiJwbGFjZWhvbGRlciIsInRlbmFudCI6eyJkZXNjcmlwdGlvbiI6bnVsbCwiYWxsb2NhdGlvbl9pZCI6MTcwLCJleHBpcmVzIjoiMjAxOC0wNy0wMSIsImVuYWJsZWQiOnRydWUsImlkIjoiZTRjMWU0ZTgyY2Q1NDk1ZDg5ZDUyZDY5NGVhNjJlNTAiLCJuYW1lIjoiTWFyaW5lLVZMIn0sImF1ZGl0X2lkcyI6WyJTVXRzTElkV1FKNjM0elZlNkQyaWpnIl19LCJzZXJ2aWNlQ2F0YWxvZyI6W3siZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8vZGVzaWduYXRlLnJjLm5lY3Rhci5vcmcuYXU6OTAwMS92MSIsInJlZ2lvbiI6Ik1lbGJvdXJuZSIsInB1YmxpY1VSTCI6Imh0dHBzOi8vZGVzaWduYXRlLnJjLm5lY3Rhci5vcmcuYXU6OTAwMS92MSIsImludGVybmFsVVJMIjoiaHR0cHM6Ly9kZXNpZ25hdGUucmMubmVjdGFyLm9yZy5hdTo5MDAxL3YxIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoiZG5zIiwibmFtZSI6IkROUyBTZXJ2aWNlIn0seyJlbmRwb2ludHMiOlt7ImFkbWluVVJMIjoiaHR0cHM6Ly9ub3ZhLnJjLm5lY3Rhci5vcmcuYXU6ODc3NC92MS4xL2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwicmVnaW9uIjoiTWVsYm91cm5lIiwicHVibGljVVJMIjoiaHR0cHM6Ly9ub3ZhLnJjLm5lY3Rhci5vcmcuYXU6ODc3NC92MS4xL2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwiaW50ZXJuYWxVUkwiOiJodHRwczovL25vdmEucmMubmVjdGFyLm9yZy5hdTo4Nzc0L3YxLjEvZTRjMWU0ZTgyY2Q1NDk1ZDg5ZDUyZDY5NGVhNjJlNTAifV0sImVuZHBvaW50c19saW5rcyI6W10sInR5cGUiOiJjb21wdXRlIiwibmFtZSI6IkNvbXB1dGUgU2VydmljZSJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8vbmV1dHJvbi5yYy5uZWN0YXIub3JnLmF1Ojk2OTYvIiwicmVnaW9uIjoiTWVsYm91cm5lIiwicHVibGljVVJMIjoiaHR0cHM6Ly9uZXV0cm9uLnJjLm5lY3Rhci5vcmcuYXU6OTY5Ni8iLCJpbnRlcm5hbFVSTCI6Imh0dHBzOi8vbmV1dHJvbi5yYy5uZWN0YXIub3JnLmF1Ojk2OTYvIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoibmV0d29yayIsIm5hbWUiOiJuZXR3b3JrIn0seyJlbmRwb2ludHMiOlt7ImFkbWluVVJMIjoiaHR0cHM6Ly9jaW5kZXIucmMubmVjdGFyLm9yZy5hdTo4Nzc2L3YyL2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwicmVnaW9uIjoiTWVsYm91cm5lIiwicHVibGljVVJMIjoiaHR0cHM6Ly9jaW5kZXIucmMubmVjdGFyLm9yZy5hdTo4Nzc2L3YyL2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwiaW50ZXJuYWxVUkwiOiJodHRwczovL2NpbmRlci5yYy5uZWN0YXIub3JnLmF1Ojg3NzYvdjIvZTRjMWU0ZTgyY2Q1NDk1ZDg5ZDUyZDY5NGVhNjJlNTAifV0sImVuZHBvaW50c19saW5rcyI6W10sInR5cGUiOiJ2b2x1bWV2MiIsIm5hbWUiOiJWb2x1bWUgU2VydmljZSB2MiJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8vc3dpZnQucmMubmVjdGFyLm9yZy5hdTo4ODg4LyIsInJlZ2lvbiI6Ik1lbGJvdXJuZSIsInB1YmxpY1VSTCI6Imh0dHBzOi8vc3dpZnQucmMubmVjdGFyLm9yZy5hdTo4ODg4LyIsImludGVybmFsVVJMIjoiaHR0cHM6Ly9zd2lmdC5yYy5uZWN0YXIub3JnLmF1Ojg4ODgvIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoiczMiLCJuYW1lIjoiUzMgU2VydmljZSJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHA6Ly9nbGFuY2UucmMubmVjdGFyLm9yZy5hdTo5MjkyL3YxIiwicmVnaW9uIjoiTWVsYm91cm5lIiwicHVibGljVVJMIjoiaHR0cDovL2dsYW5jZS5yYy5uZWN0YXIub3JnLmF1OjkyOTIvdjEiLCJpbnRlcm5hbFVSTCI6Imh0dHA6Ly9nbGFuY2UucmMubmVjdGFyLm9yZy5hdTo5MjkyL3YxIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoiaW1hZ2UiLCJuYW1lIjoiSW1hZ2UgU2VydmljZSJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8vY2VpbG9tZXRlci5yYy5uZWN0YXIub3JnLmF1Ojg3NzcvIiwicmVnaW9uIjoiTWVsYm91cm5lIiwicHVibGljVVJMIjoiaHR0cHM6Ly9jZWlsb21ldGVyLnJjLm5lY3Rhci5vcmcuYXU6ODc3Ny8iLCJpbnRlcm5hbFVSTCI6Imh0dHBzOi8vY2VpbG9tZXRlci5yYy5uZWN0YXIub3JnLmF1Ojg3NzcvIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoibWV0ZXJpbmciLCJuYW1lIjoiTWV0ZXJpbmcgU2VydmljZSJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8vaGVhdC5yYy5uZWN0YXIub3JnLmF1OjgwMDAvdjEiLCJyZWdpb24iOiJNZWxib3VybmUiLCJwdWJsaWNVUkwiOiJodHRwczovL2hlYXQucmMubmVjdGFyLm9yZy5hdTo4MDAwL3YxIiwiaW50ZXJuYWxVUkwiOiJodHRwczovL2hlYXQucmMubmVjdGFyLm9yZy5hdTo4MDAwL3YxIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoiY2xvdWRmb3JtYXRpb24iLCJuYW1lIjoiQ2xvdWRmb3JtYXRpb24gU2VydmljZSJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8vY2luZGVyLnJjLm5lY3Rhci5vcmcuYXU6ODc3Ni92MS9lNGMxZTRlODJjZDU0OTVkODlkNTJkNjk0ZWE2MmU1MCIsInJlZ2lvbiI6Ik1lbGJvdXJuZSIsInB1YmxpY1VSTCI6Imh0dHBzOi8vY2luZGVyLnJjLm5lY3Rhci5vcmcuYXU6ODc3Ni92MS9lNGMxZTRlODJjZDU0OTVkODlkNTJkNjk0ZWE2MmU1MCIsImludGVybmFsVVJMIjoiaHR0cHM6Ly9jaW5kZXIucmMubmVjdGFyLm9yZy5hdTo4Nzc2L3YxL2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIn1dLCJlbmRwb2ludHNfbGlua3MiOltdLCJ0eXBlIjoidm9sdW1lIiwibmFtZSI6IlZvbHVtZSBTZXJ2aWNlIn0seyJlbmRwb2ludHMiOlt7ImFkbWluVVJMIjoiaHR0cHM6Ly9ub3ZhLnJjLm5lY3Rhci5vcmcuYXU6ODc3My9zZXJ2aWNlcy9BZG1pbiIsInJlZ2lvbiI6Ik1lbGJvdXJuZSIsInB1YmxpY1VSTCI6Imh0dHBzOi8vbm92YS5yYy5uZWN0YXIub3JnLmF1Ojg3NzMvc2VydmljZXMvQ2xvdWQiLCJpbnRlcm5hbFVSTCI6Imh0dHBzOi8vbm92YS5yYy5uZWN0YXIub3JnLmF1Ojg3NzMvc2VydmljZXMvQ2xvdWQifV0sImVuZHBvaW50c19saW5rcyI6W10sInR5cGUiOiJlYzIiLCJuYW1lIjoiRUMyIFNlcnZpY2UifSx7ImVuZHBvaW50cyI6W3siYWRtaW5VUkwiOiJodHRwczovL2hlYXQucmMubmVjdGFyLm9yZy5hdTo4MDA0L3YxL2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwicmVnaW9uIjoiTWVsYm91cm5lIiwicHVibGljVVJMIjoiaHR0cHM6Ly9oZWF0LnJjLm5lY3Rhci5vcmcuYXU6ODAwNC92MS9lNGMxZTRlODJjZDU0OTVkODlkNTJkNjk0ZWE2MmU1MCIsImludGVybmFsVVJMIjoiaHR0cHM6Ly9oZWF0LnJjLm5lY3Rhci5vcmcuYXU6ODAwNC92MS9lNGMxZTRlODJjZDU0OTVkODlkNTJkNjk0ZWE2MmU1MCJ9XSwiZW5kcG9pbnRzX2xpbmtzIjpbXSwidHlwZSI6Im9yY2hlc3RyYXRpb24iLCJuYW1lIjoiT3JjaGVzdHJhdGlvbiBTZXJ2aWNlIn0seyJlbmRwb2ludHMiOlt7ImFkbWluVVJMIjoiaHR0cHM6Ly9zd2lmdC5yYy5uZWN0YXIub3JnLmF1Ojg4ODgvdjEuMC8iLCJyZWdpb24iOiJNZWxib3VybmUiLCJwdWJsaWNVUkwiOiJodHRwczovL3N3aWZ0LnJjLm5lY3Rhci5vcmcuYXU6ODg4OC92MS9BVVRIX2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwiaW50ZXJuYWxVUkwiOiJodHRwczovL3N3aWZ0LnJjLm5lY3Rhci5vcmcuYXU6ODg4OC92MS9BVVRIX2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIn0seyJhZG1pblVSTCI6Imh0dHBzOi8vdmF1bHQubWVsYm91cm5lLnZpY25vZGUub3JnLmF1Ojg4ODgvdjEuMC8iLCJyZWdpb24iOiJWaWNOb2RlIiwicHVibGljVVJMIjoiaHR0cHM6Ly92YXVsdC5tZWxib3VybmUudmljbm9kZS5vcmcuYXU6ODg4OC92MS9BVVRIX2U0YzFlNGU4MmNkNTQ5NWQ4OWQ1MmQ2OTRlYTYyZTUwIiwiaW50ZXJuYWxVUkwiOiJodHRwczovL3ZhdWx0Lm1lbGJvdXJuZS52aWNub2RlLm9yZy5hdTo4ODg4L3YxL0FVVEhfZTRjMWU0ZTgyY2Q1NDk1ZDg5ZDUyZDY5NGVhNjJlNTAifSx7ImFkbWluVVJMIjoiaHR0cHM6Ly9zd2lmdC5zYS5uZWN0YXIub3JnLmF1Ojg4ODgvdjEuMC8iLCJyZWdpb24iOiJTQSIsInB1YmxpY1VSTCI6Imh0dHBzOi8vc3dpZnQuc2EubmVjdGFyLm9yZy5hdTo4ODg4L3YxL0FVVEhfZTRjMWU0ZTgyY2Q1NDk1ZDg5ZDUyZDY5NGVhNjJlNTAiLCJpbnRlcm5hbFVSTCI6Imh0dHBzOi8vc3dpZnQuc2EubmVjdGFyLm9yZy5hdTo4ODg4L3YxL0FVVEhfZTRjMWU0ZTgyY2Q1NDk1ZDg5ZDUyZDY5NGVhNjJlNTAifV0sImVuZHBvaW50c19saW5rcyI6W10sInR5cGUiOiJvYmplY3Qtc3RvcmUiLCJuYW1lIjoiT2JqZWN0IFN0b3JhZ2UgU2VydmljZSJ9LHsiZW5kcG9pbnRzIjpbeyJhZG1pblVSTCI6Imh0dHBzOi8va2V5c3RvbmUucmMubmVjdGFyLm9yZy5hdTozNTM1Ny92Mi4wLyIsInJlZ2lvbiI6Ik1lbGJvdXJuZSIsInB1YmxpY1VSTCI6Imh0dHBzOi8va2V5c3RvbmUucmMubmVjdGFyLm9yZy5hdTo1MDAwL3YyLjAvIiwiaW50ZXJuYWxVUkwiOiJodHRwczovL2tleXN0b25lLnJjLm5lY3Rhci5vcmcuYXU6NTAwMC92Mi4wLyJ9XSwiZW5kcG9pbnRzX2xpbmtzIjpbXSwidHlwZSI6ImlkZW50aXR5IiwibmFtZSI6IklkZW50aXR5IFNlcnZpY2UifV0sInVzZXIiOnsidXNlcm5hbWUiOiJYaWFvLkZ1QHV0YXMuZWR1LmF1Iiwicm9sZXNfbGlua3MiOltdLCJpZCI6IjMxNSIsInJvbGVzIjpbeyJuYW1lIjoiTWVtYmVyIn0seyJuYW1lIjoiVGVuYW50TWFuYWdlciJ9XSwibmFtZSI6IlhpYW8uRnVAdXRhcy5lZHUuYXUifSwibWV0YWRhdGEiOnsiaXNfYWRtaW4iOjAsInJvbGVzIjpbIjIiLCIxNCJdfX19MYIBBDCCAQACAQEwXDBXMQswCQYDVQQGEwJVUzEOMAwGA1UECBMFVW5zZXQxDjAMBgNVBAcTBVVuc2V0MQ4wDAYDVQQKEwVVbnNldDEYMBYGA1UEAxMPd3d3LmV4YW1wbGUuY29tAgEDMAsGCWCGSAFlAwQCATANBgkqhkiGdsfsfsfdfdss9w0BAQEFAASBgKCY1zMegj6ZkXsdfdsfs8pZn7MPQ2Xno8dbOS2e0nZ-SdS07CGS1csdfsdfsOGHZe1gO-4Te-adu+1aL0GEYTgNpeW+sfdsfBk0k5+vCoVgqub6lpx2Dl0Knxak4bY3PH8bRz1G5NWvNBQ18-F6HUIbkyptv1n9EMmPl0YU0jXXGNYAuctgi0rTeaL6Z8h",
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

Then you can use the token obtained from the above in the API for authentication.

The below shows a example of how to use the token in using Nova API to list flavors:

```
curl -s -H \
            "X-Auth-Token:token" \
            http://8.21.28.222:8774/v2/tenant_id/flavors \
            | python -m json.tool

```

You need to replace the token and the URL. You can find the Nova API endpoint
URL from the NeCTAR [Dashboard][dashboard]. The above request would return the
below output:

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


[curl]: http://curl.haxx.se/
[api]: http://developer.openstack.org/api-ref.html
[dashboard]: https://dashboard.rc.nectar.org.au
