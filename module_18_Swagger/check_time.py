import timeit
from clients import BookClient

def send_requests(n):
   client = BookClient()
   for _ in range(n):
       client.get_all_books()

# Measure the time taken to send 10 requests
start_time = timeit.default_timer()
send_requests(10)
elapsed = timeit.default_timer() - start_time
print(f"Time taken to send 10 requests: {elapsed}")

# Measure the time taken to send 100 requests
start_time = timeit.default_timer()
send_requests(100)
elapsed = timeit.default_timer() - start_time
print(f"Time taken to send 100 requests: {elapsed}")

# Measure the time taken to send 1000 requests
start_time = timeit.default_timer()
send_requests(1000)
elapsed = timeit.default_timer() - start_time
print(f"Time taken to send 1000 requests: {elapsed}")

#
# import requests
# import time
#
# def send_requests(n):
#    url = 'http://127.0.0.1:5000/api/books/' # Replace with your server's URL
#    for _ in range(n):
#        response = requests.get(url)
#        assert response.status_code == 200
#
# start_time = time.time()
# send_requests(10)
# elapsed = time.time() - start_time
# print(f"Time taken to send 10 requests: {elapsed}")
#
#
# start_time = time.time()
# send_requests(100)
# elapsed = time.time() - start_time
# print(f"Time taken to send 100 requests: {elapsed}")
#
#
# start_time = time.time()
# send_requests(1000)
# elapsed = time.time() - start_time
# print(f"Time taken to send 1000 requests: {elapsed}")
