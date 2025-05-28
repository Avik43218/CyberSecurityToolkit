from main import sha256
import time

start = time.perf_counter()

message = b"Avik Roy Choudhury"
print(sha256(message=message))

end = time.perf_counter()

print(end - start)
