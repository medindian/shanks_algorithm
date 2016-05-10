#author : medina d n
#date : 10 Mei 2016
#description : mencari nilai y dari y^2 = n (mod p) dengan menggunakan algoritma shanks

#metode untuk melakukan perhitungan modular p
def pow_mod(x, n, p):
	if n == 0:
		return 1
	#melakukan perulangan hingga n = 0
	if n & 1:
		return (pow_mod(x, n-1, p) * x) % p
	x = pow_mod(x, n/2, p)
	return (x*x) % p

def shanks(n, p):
	s = 0
	q = p - 1
	#untuk mencari nilai s dan q
	while (q & 1) == 0:
		q /= 2
		s += 1

	#jika s = 1, maka r langsung dihitung R = +- n^(p+1)/4 (mod p)
	if s == 1:
		r = pow_mod(n, (p+1)/4, p)
		if ((r * r) % p == n):
			return r
		return 0
	
	#jika s != 1, maka dicari nilai z yg memenuhi (z/p) = -1 (mod p)
	z = 0
	while pow_mod(z, (p-1)/2, p) != p-1:
		z+=1

	#set nilai c, r, t, dan m
	c = pow_mod(z, q, p) #c = z^q (mod p)
	r = pow_mod(n, (q+1)/2, p) #r = n^((q+1)/2) (mod p)
	t = pow_mod(n, q, p) #t = n^q (mod p)
	m = s

	#jika t = 1, maka nilai r yang sudah didapat merupakan outputnya
	#jika tidak, dicari nilai i yang memenuhi t^(2^i) = 1 (mod p)
	while t != 1:
		tt = t
		i = 0
		#perulangan untuk mencari i
		while (tt != 1):
			tt = (tt * tt) % p
			i += 1
			if i == m:
				return 0
		#jika nilai i sudah ketemu dan i != m, dicari nilai b
		b = pow_mod(c, pow_mod(2, m-i-1, p-1), p) #b = c^(2M-2i-2) (mod p)
		b2 = (b * b) % p #b^2 (mod p)
		r = (r * b) % p #r = r * b (mod p)
		t = (t * b2) % p #t = t * b^2 (mod p)
		c = b2 #c = b^2 (mod p)
		m = i
#	print (r * r) % p
#	print n
	if (r * r) % p == n:
		return r
	return 0

k = 10
p = 13
#print 'pow_mod(5, 10, 3) = ', pow_mod(5,10,3)
#print 'pow(5, 10, 3) = ', pow(5,10,3)
print shanks(k, p)
print 'k = 10, p = 13. [R, p-R] = [', shanks(k, p), ', ', p-shanks(k, p),']'
