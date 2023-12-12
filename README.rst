### Example usage

ssl_checker = SSLChecker(url_to_check)

if __name__ == "__main__":

    url_to_check = "https://www.google.com"

    ssl_checker = SSLChecker(url_to_check)

    ssl_info = ssl_checker.check_ssl_security()

    print(ssl_info)
