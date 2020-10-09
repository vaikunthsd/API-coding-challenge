import urllib.request
import json

"""
Class ApiHandler

This class acts as a middleware between the client and
the provided API JSONplaceholder.
A client can get, post, and delete posts, albums, and comments from/to the API.
"""


class ApiHandler:

    def __init__(self):
        self.__url = 'https://jsonplaceholder.typicode.com/'

    def get(self, route, id):
        try:
            # Forming the complete url for request
            url = self.__url+route+'/'+str(id)
            with urllib.request.urlopen(url) as response:
                html = response.read()
                data = str(html, "utf-8")  # Converting data to string
                return json.loads(data)
        except urllib.request.URLError as url_Error:
            return {"title": "N/A"}
        except urllib.request.HTTPError as http_Error:
            return {"title": "N/A"}

    def post(self, route, values):
        try:
            # Converting dictionary data to string
            data = urllib.parse.urlencode(values)
            # Converting string data to bytes
            data = data.encode('utf-8')
            req = urllib.request.Request(self.__url+route, data)
            with urllib.request.urlopen(req) as response:
                html = response.read()
                json1 = json.loads(str(html, "utf-8"))
                info = response.info()
                # Searching for the "X-Powered-By" headers in response headers
                for header in info._headers:
                    if(header[0] == "X-Powered-By"):
                        return (json1["id"], response.getcode(), header[1],)
        except urllib.request.URLError as url_Error:
            return ("Error", url_Error.reason,)
        except urllib.request.HTTPError as http_Error:
            return ("Error", http_Error.code,)

    def delete(self, route, id):
        try:
            req = urllib.request.Request(self.__url+route+'/'+str(id))
            req.get_method = lambda: "DELETE"
            with urllib.request.urlopen(req) as response:
                for header in response.info()._headers:
                    # Searching for the "X-Content-Type-Options" header
                    if(header[0] == 'X-Content-Type-Options'):
                        return (response.getcode(), header[1],)
        except urllib.request.URLError as url_Error:
            return ("Error", url_Error.reason,)
        except urllib.request.HTTPError as http_Error:
            return ("Error", http_Error.code,)
