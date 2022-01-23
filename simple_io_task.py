# imports
# if not installed use pip install requests or conda install requests
import requests as r

# define the function responsible for downloading the files
def download_pics(urls):
	for url in urls:
		# make the reqeuest
		# By default, when you make a request, the body of the response is downloaded immediately. 
		# You can override this behaviour and defer downloading the response body until you access the Response.content attribute
		# For this we set stream=True so that requests doesn't download the whole image into memory first.
		res = r.get(url, stream = True)

		# extract the filename of the url
		filename = f"{url.split('/')[-1]}"

		# check if we made a successful http request
		if res.status_code == 200:
			# write the pic with name filename to the current directory
			with open(filename,"wb") as f:
				# download the image bytewise and write each block (bytesize = 128 by default) to current directory
				# if different bytesize is desireable, use res.iter_content(bytesize) instead of res
				for block in res: 
					f.write(block)
		else:
			# if not successful we move on to the next url
			# print('For file %s the download was not successfull' %filename)
			continue


# excute if main
if __name__ == "__main__":
	url = [
		"https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png"
	]
	# download the url 10 times
	download_pics(url*10)