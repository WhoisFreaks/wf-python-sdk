# Reference
## Credits
<details><summary><code>client.credits.<a href="src/whoisfreaks/credits/client.py">credits_usage_api</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You need credits to use Whois and DNS APIs. You can use this API to see your remaining credits for your API Key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.credits.credits_usage_api(api_key='YOUR_API_KEY', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Dns
<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">live_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Live DNS information for a domain or an IP address
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.live_dns_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='all', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">ns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get NS information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.ns_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='ns', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">mx_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get MX information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.mx_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='mx', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">historical_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Historical DNS information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.historical_dns_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='all', page=1, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">reverse_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Reverse DNS info for a DNS record
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.reverse_dns_lookup(api_key='YOUR_API_KEY', value='8.8.8.8', type='a', page=1, format='json', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">bulk_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Bulk DNS information for multiple domains or IP addresses
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.bulk_dns_lookup(api_key='YOUR_API_KEY', type='all', format='json', domain_names=['whoisfreaks.com', 'jfreaks.com'], ip_addresses=['1.1.1.1', '8.8.8.8'], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_addresses:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DomainAvailability
<details><summary><code>client.domain_availability.<a href="src/whoisfreaks/domain_availability/client.py">domain_availability_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check availability of a Domain Name
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.domain_availability.domain_availability_lookup(api_key='YOUR_API_KEY', domain='whoisfreaks.com', sug=True, count=10, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sug:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domain_availability.<a href="src/whoisfreaks/domain_availability/client.py">bulk_domain_availability_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check availability of multiple Domain Names
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.domain_availability.bulk_domain_availability_lookup(api_key='YOUR_API_KEY', domain_names=['whoisfreaks.com', 'jfreaks.com'], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domain_availability.<a href="src/whoisfreaks/domain_availability/client.py">bulk_domain_availability_lookup_with_custom_tl_ds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check availability of multiple Domain Names with custom TLDs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.domain_availability.bulk_domain_availability_lookup_with_custom_tl_ds(api_key='YOUR_API_KEY', domain='whoisfreaks.com', tld=['us', 'pk'], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tld:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FileStatus
<details><summary><code>client.file_status.<a href="src/whoisfreaks/file_status/client.py">file_status_api</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Whois Files Status API provides comprehensive details about the availability and update status of various Whois datasets. It includes several key datasets, such as:
- Newly registered domains: Includes cleaned gTLDs, cleaned ccTLDs, gTLDs, DNS records, and ccTLDs.
- Expired domains: Covers both cleaned and regular expired domains.
- Dropped domains: Details on domains that have been removed or dropped.

In addition to these datasets, the API offers information on the update frequency of Whois and DNS data. Updates are available in three time intervals:
- Daily: Regularly updated Whois and DNS data.
- Weekly: Whois and DNS data refreshed on a weekly basis.
- Monthly: Monthly updates are provided for Whois data, though DNS updates may not always be available.
This structure enables users to track the currency and availability of various domain datasets, ensuring access to the latest WHOIS and DNS information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.file_status.file_status_api()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ssl
<details><summary><code>client.ssl.<a href="src/whoisfreaks/ssl/client.py">ssl_live_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve live SSL certificate details for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.ssl.ssl_live_lookup(api_key='YOUR_API_KEY', domain_name='google.com', chain=True, ssl_raw=True, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**ssl_raw:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Whois
<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">live_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get live WHOIS information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.live_lookup(api_key='YOUR_API_KEY', domain_name='888starzci.ci', whois='live', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**whois:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">historical_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get historical WHOIS records for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.historical_lookup(api_key='YOUR_API_KEY', domain_name='whoisfreaks.com', whois='historical', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**whois:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">reverse_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a reverse WHOIS lookup based on registrant information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.reverse_lookup(api_key='YOUR_API_KEY', whois='reverse', keyword='google', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**whois:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**includes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">ip_whois_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get WHOIS information for an IP
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.ip_whois_lookup(api_key='YOUR_API_KEY', ip='8.8.8.8', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">asn_whois_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get WHOIS information for an ASN
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.asn_whois_lookup(api_key='YOUR_API_KEY', asn='1', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**asn:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">bulk_domain_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Live WHOIS information for more than one domain names
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.bulk_domain_lookup(api_key='YOUR_API_KEY', format='json', domain_names=['whoisfreaks.com', 'jfreaks.com'], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

