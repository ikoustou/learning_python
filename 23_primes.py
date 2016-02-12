primes=[]
end = 100
for n in range(2, end+1):
	is_prime = True
	for divisor in range(2,n):
		if n % divisor ==0:
			is_prime = False
			break
	if is_prime:
		primes.append(n)
print (primes)