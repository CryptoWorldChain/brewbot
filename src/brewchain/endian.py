## Python Lib for  BrewChain Encrypto

# Author Brew
#

from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.% import DSS

class EndianHelper:
	@staticmethod
	def revert(hexbb):
		print("helloBB3.")
		return 11

	@staticmethod
	def test():
		key = ECC.generate(curve='secp256r1')
		print key.public_key()
		x = key.public_key().pointQ.x
		y = key.public_key().pointQ.y

		hx=hex(int(str(x)))
		bytearray.fromhex(hx[2:64])[::-1]
		reversed_arr=result[::-1]

		x=key.public_key().pointQ.x
		hx=hex(int(str(x)))
		rx = bytearray.fromhex(hx[2:66])[::-1]


		y=key.public_key().pointQ.y
		hy=hex(int(str(y)))
		ry = bytearray.fromhex(hy[2:66])[::-1]	

		''.join('{:02x}'.format(x) for x in rx+ry)

		addr=SHA256.new(rx+ry).hexdigest()[:40]


		"".join("{:02x}".format(ord(c)) for c in pps)


		p = ECC.construct(curve='secp256r1',d=70054409939411066367955879351487264564474994114056648764946442729447023254584)
		signer = DSS.new(p, 'fips-186-3')
		pps=signer.sign(h)

5cad7b932f2eb3216ab34ce0109ec06a33e762cd99b453f66c16e927d93e273e
41ee855cc25ce1d160f5b4087fa4fb8935e9765c8d7d0fdb8a7f9b85bcd06be3
a377899edf497f251ee9d3261f451527e45d58e29a2589a2d501ad7d294f2e5d
2ab5a20f1d11867b3bb824cdda4c16f37627000373674f2b6b5249adab233b52
e8970a87737b45ea89c168326351f1fdf439d7e686555a367f35d5474d6bfd52


from Crypto.Cipher import AES





