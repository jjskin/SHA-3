import hashlib

zeros = hashlib.sha3_512()
trng_p = hashlib.sha3_512()

input = open("0.bit", "rb")
read0 = input.read()
input2 = open("TRNG_P.bit", "rb")
readtrng = input2.read()

tmp1 = b''
tmp2 = b''

for i in range(0,130000000,511) :
    zeros.update(read0[i:i+511])
    trng_p.update(readtrng[i:i+511])
    print(i)
    tmp1 +=zeros.digest()
    tmp2 += trng_p.digest()

out0 = open('0_sha3.bit', 'wb')
out0.write(tmp1)
out0.close()

outrng = open('trng_p_sha3.bit', 'wb')
outrng.write(tmp2)
outrng.close()

input.close()
input2.close()