## Python Lib for  BrewChain Encrypto

# Author Brew
#

from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.% import DSS

from Crypto.Protocol.KDF import HKDF

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



cipher = AES.new(key, AES.MODE_CBC,iv=bytearray.fromhex("ff69d48fe2bf0f98ccfc42676bac6f33"))



940fd1a3a74c91d93212eb6b53bd637c9148094101d65c9f7049081abba2c160cd50d8a88f77fc7bdc890442f2df0d13cf12ac783d0e75ba58a6d110bbbbbe275ef2f802d0a2224d513e08e1e4d1e57316f90b712b25e31792b7d6cf4f8c3df8e65d90ddc64279fcd36460e538bc4f1f09a8e29db8a3458d4f505059b0db9a0a53b138ab76ffd378b9cd8db35f57962a97ded5b3d47803fa83ab41354ee4adee3e45053d263a49f21c6c7ee3987f260de8c24f1bbe255e76588f6faa583372d41f86952ee9e4853de504f0c4fa8b3b459ff440fc68092eb4121801d112335451cd04d287a9dacad49e6201fb2805c3eb34a28ae1e72d64a2d41eccdc349eef2c554577c245f52fee61bb759c50a45fe5



def encode(text):
        l = len(text)
        output = StringIO.StringIO()
        val = 16 - (l % 16)
        for _ in xrange(val):
            output.write('%02x' % val)
        return text + binascii.unhexlify(output.getvalue())


def pkcs7padding(data):
        bs = 16
        padding = bs - len(data) % bs
        padding_text = chr(padding) * padding
        return data + padding_text



