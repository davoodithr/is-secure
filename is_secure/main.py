import urllib.request
import ssl

class SSLChecker:
    def __init__(self, url):
        self.url = url


    def check_ssl_security(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            req = urllib.request.Request(self.url, headers=headers)

            with urllib.request.urlopen(req) as response:
                # Check if the connection was successful
                if response.status == 200:
                    print(f"Connection to {self.url} successful.")
                    # Check SSL details
                    ssl_info = response.info()

                    # Additional SSL information
                    ssl_version = response.version
                    return {
                        "SSL Version": str(ssl_version),
                        "Response Headers": dict(response.headers),
                    }
                else:
                    print(f"Failed to connect to {self.url}. HTTP Status Code: {response.status}")
        except Exception as e:
            print(f"Error connecting to {self.url}: {e}")

