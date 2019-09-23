# Cisco PSIRT API intel

###API Reference

https://developer.cisco.com/docs/psirt/#!api-reference/api-reference

###Registered Application

-Visit - https://apiconsole.cisco.com/apps/register/
-Register app
-Select API - Cisco PSIRT openVuln API


###Obtain auth token

-Template

curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=<client_id>" -d "client_secret=<client_secret>" -d "grant_type=client_credentials" https://cloudsso.cisco.com/as/token.oauth2

-Example

curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=<XXXX>” -d "client_secret=<XXXX>“ -d "grant_type=client_credentials" https://cloudsso.cisco.com/as/token.oauth2

-Result Example -

{"access_token”:”<XXXX>”,”token_type":"Bearer","expires_in":3599}

###Make API Call


-All current advisories
curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer <XXXX>” https://api.cisco.com/security/advisories/all

-Last 10 published advisories

curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer <XXXX>“ https://api.cisco.com/security/advisories/latest/10

-Single returned advisory(latest)
curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer <XXXX>” https://api.cisco.com/security/advisories/latest/1

-Focus on specific product ID

curl -X GET "https://api.cisco.com/security/advisories/product?product="

Cisco ASR 9000 Series Aggregation Services Routers

curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer <XXXX>” https://api.cisco.com/security/advisories/product?product=ASR

curl -X GET -s -k -H "Accept: application/json" -H "Authorization: Bearer <XXXX>” https://api.cisco.com/security/advisories/product?product=communications_manager

