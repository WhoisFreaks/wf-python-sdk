# Reference
<details><summary><code>client.<a href="src/whoisfreaks/client.py">whois_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch live and historical WHOIS data for any domain, and perform reverse lookups to find domains associated with a specific registrant, company, email, or keyword. Instantly retrieve current registration details, explore past WHOIS records, or discover all domains linked to a specific registrant, company, email, or keyword.
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
client = WhoisfreaksApi()
client.whois_lookup(whois='whois', api_key='apiKey', )

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

**whois:** `str` — The type of WHOIS lookup (live, historical, reverse)
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` — The domain name for Live and Historical WHOIS lookup
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword to search for in registrant information (optional)
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email to search for (optional)
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` — Owner to search for (optional)
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — Company to search for (optional)
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` — Mode of search (optional)
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[str]` — Exact match flag (optional)
    
</dd>
</dl>

<dl>
<dd>

**includes:** `typing.Optional[str]` — Include specific details (optional)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — The page number of the reverse records (optional)
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Two formats are available JSON, XML. If you don't specify the 'format' parameter, the default format will be JSON.
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">bulk_domain_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch Live WHOIS information for a list of domains in bulk
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
client = WhoisfreaksApi()
client.bulk_domain_lookup(api_key='apiKey', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Two formats are available JSON, XML. If you don't specify the 'format' parameter, the default format will be JSON.
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Optional[typing.Sequence[str]]` — List of domain names to lookup
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">ip_whois_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve real-time information for an IPv4 or IPv6 address
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
client = WhoisfreaksApi()
client.ip_whois_lookup(api_key='apiKey', ip='ip', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — The IPv4 or IPv6 for lookup
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Two formats are available JSON, XML. If you don't specify the 'format' parameter, the default format will be JSON.
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">asn_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve real-time information for an Autonomous System Number
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
client = WhoisfreaksApi()
client.asn_lookup(api_key='apiKey', asn='asn', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**asn:** `str` — The ASN number for which information is being requested (e.g., "1" or "AS1").
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Two formats are available JSON, XML. If you don't specify the 'format' parameter, the default format will be JSON.
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">ssl_live_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve live SSL information for a specific domain.
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
client = WhoisfreaksApi()
client.ssl_live_lookup(api_key='apiKey', domain_name='domainName', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` — The domain name for which live SSL information is requested (e.g., "example.com").
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[bool]` — A boolean flag indicating whether to include SSL certificate chain information.
    
</dd>
</dl>

<dl>
<dd>

**ssl_raw:** `typing.Optional[bool]` — A boolean flag indicating whether to include raw SSL certificate information.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Two formats are available JSON, XML. If you don't specify the 'format' parameter, the default format will be JSON.
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">domain_availability_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check availability of a Domain Name.
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
client = WhoisfreaksApi()
client.domain_availability_lookup(api_key='apiKey', domain='whoisfreaks.com', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — The domain name for which availability is being checked.
    
</dd>
</dl>

<dl>
<dd>

**sug:** `typing.Optional[bool]` — A boolean flag indicating whether suggested domains are included.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of suggested domains to return.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Format of the response (optional). Default is JSON.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — Source information for the domain availability check (optional).
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">live_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve live DNS information for a specific domain or IP address.
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
client = WhoisfreaksApi()
client.live_dns_lookup(api_key='apiKey', type='type', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The DNS record type (e.g., A, MX, NS).
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` — The domain name for which live DNS information is requested (e.g., "example.com").
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — The IP address for which live DNS information is requested (e.g., "8.8.8.8").
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — The output format (JSON or XML).
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">historical_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve historical DNS information for a specific domain.
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
client = WhoisfreaksApi()
client.historical_dns_lookup(api_key='apiKey', domain_name='domainName', type='type', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` — The domain name for which historical DNS information is requested (e.g., "example.com").
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The DNS record type (e.g., A, MX, NS).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number for paginated results.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — The output format (JSON or XML).
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">reverse_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve reverse DNS information for a given DNS record.
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
client = WhoisfreaksApi()
client.reverse_dns_lookup(api_key='apiKey', value='value', type='type', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — The IP address for which reverse DNS information is requested (e.g., "8.8.8.8").
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of DNS record to search for (e.g., "A", "MX").
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination (optional).
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — The output format (JSON or XML).
    
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

<details><summary><code>client.<a href="src/whoisfreaks/client.py">bulk_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve DNS information for multiple domains or IP addresses in bulk.
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
client = WhoisfreaksApi()
client.bulk_dns_lookup(api_key='apiKey', type='type', )

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

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The DNS record type to filter by (e.g., "A", "MX", "all").
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — The output format (JSON or XML).
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Optional[typing.Sequence[str]]` — List of domain names for which DNS information is requested.
    
</dd>
</dl>

<dl>
<dd>

**ip_addresses:** `typing.Optional[typing.Sequence[str]]` — List of IP addresses for which reverse DNS information is requested.
    
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

