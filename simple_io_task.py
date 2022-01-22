import requests as r

# define the function responsible for downloading the files
def download_pics(urls):
	for url in urls:
		r.get(url)


# excute as main
if __name__ == "__main__":
	urls = [
		"https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png"

	]
	download_pics(urls)