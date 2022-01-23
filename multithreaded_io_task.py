# imports
# if not installed use pip install requests or conda install requests
import requests as r

# needed for multithreading
from queue import Queue
from threading import Thread

# define number of threads
NUM_THREADS = 5
q = Queue()

# define the function responsible for downloading the files
def download_pics():
	global q

	while True:

		# get current url
		url = q.get()

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
			# if not successful we break
			# print('For file %s the download was not successfull' %filename)
			break

		q.task_done()


# excute if main
if __name__ == "__main__":
	urls = [
		"https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png"
	]
	# put the 100 urls one by one into a queue object
	for url in urls*100:
		q.put(url)

	for t in range(NUM_THREADS):
		worker = Thread(target=download_pics)
		worker.daemon = True
		worker.start()

	q.join()