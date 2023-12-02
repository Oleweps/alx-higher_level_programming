#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status.
"""

import urllib.request

if __name__ == "__main__":
        # Define the URL to fetch
        url = "https://intranet.hbtn.io/status"

        # Add a user-agent header to the request (optional)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        request = urllib.request.Request(url, headers=headers)

        try:
            # Make the request and read the response
            with urllib.request.urlopen(request) as response:
                body = response.read()

                # Print the response details
                print("Body response:")
                print("\t- type: {}".format(type(body)))
                print("\t- content: {}".format(body))
                print("\t- utf8 content: {}".format(body.decode("utf-8")))

        except urllib.error.HTTPError as e:
            # Handle HTTP errors
            print(f"HTTP Error {e.code}: {e.reason}")

