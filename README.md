flaming-octo-mailman 
====================
Send data to a POST URL and get the output. Easy for use with scripts, and supports many options.

```
usage: main.py [-h] -u URL -f FILE [-s] [-n] [-v]

Sends formatted POST data from a file to a URL

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to POST data
  -f FILE, --file FILE  POST file directory (JSON)
  -s, --save            Save POST output
  -n, --noretry         Do not retry on failure
  -v, --verbose         Verbose logging
```

Example: ``` python3 ./main.py -u 'http://httpbin.org/post' -f example.json -s ```

License 
=======
See LICENSE.md

FAQ 
===
What's up with the weird name?
```
To annoy Churchill
```
