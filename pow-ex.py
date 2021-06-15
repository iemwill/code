from hashlib import sha256
from time import perf_counter

txs = b"Assume this are transactions we want to mine for our block, which we already have checked to be all valid. Now we need some leading zeroes of the SHA256."

print("One leading zero:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[0] == "0"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")

print("Two leading zeroes:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[:2] == "00"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")

print("Three leading zeroes:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[:3] == "000"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")

print("Four leading zeroes:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[:4] == "0000"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")

print("Five leading zeroes:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[:5] == "00000"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")

print("Six leading zeroes:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[:6] == "000000"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")

print("Seven leading zeroes:")
start_time = perf_counter()
newTry = True
nonce = 0
while(newTry):
	if(sha256(txs + str(nonce).encode()).hexdigest()[:7] == "0000000"):
		newTry = False
	else:
		nonce += 1
end_time = perf_counter()
print(sha256(txs + str(nonce).encode()).hexdigest())
print("nonce: " + str(nonce))
print ("Execution-time in seconds: " + str(end_time - start_time))
print("--------------------------------------------------------------")