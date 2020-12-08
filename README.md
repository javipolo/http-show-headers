# Service that prints the received HTTP headers in JSON

## Use the container
It's a simple docker container that listens on 8080

You can build it yourself or use the latest image hosted at dockerhub:
```
docker run -p 8080:8080 javipolo/http-show-headers:latest
```

and test
```
$ curl http://localhost:8080
{
  "Accept": "*/*", 
  "Content-Length": "", 
  "Content-Type": "text/plain", 
  "Host": "localhost:8080", 
  "User-Agent": "curl/7.58.0"
}
```

## Deploy or upgrade in kubernetes with helm
Copy or modify values.yaml and deploy as usual:

```
helm upgrade -i http-show-headers -f values.yaml helm/
```
and test
```
$ curl https://your-hostname.org/http-show-headers
{
  "Accept": "*/*", 
  "Accept-Encoding": "gzip", 
  "Cf-Connecting-Ip": "1.2.3.4", 
  "Cf-Ipcountry": "ES", 
  "Cf-Ray": "7ab76225dc702929-MAD", 
  "Cf-Visitor": "{\"scheme\":\"https\"}", 
  "Connection": "close", 
  "Content-Length": "", 
  "Content-Type": "text/plain", 
  "Host": "your-hostname.org", 
  "True-Client-Ip": "1.2.3.4", 
  "User-Agent": "curl/7.58.0", 
  "X-Forwarded-For": "4.5.6.7", 
  "X-Forwarded-Host": "your-hostname.org", 
  "X-Forwarded-Port": "443", 
  "X-Forwarded-Proto": "https", 
  "X-Original-Forwarded-For": "1.2.3.4", 
  "X-Original-Uri": "/http-show-headers", 
  "X-Real-Ip": "4.5.6.7", 
  "X-Request-Id": "9d217a0481b2f44df488e9dc84711a53", 
  "X-Scheme": "https"
}
```
