import time

from ska_defines import *


class SkaTxn(c_void_p):
    def __init__(self, ctx):
        self.__ctx = ctx

    def __enter__(self):
        err = c_int(0)
        self.value = skac_txn_init(self.__ctx, None, byref(err))
        if err.value != 0:
            raise SkaError("init txn error: {}".format(err.value))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        skac_txn_free(self.value)

startlog = skac_start_log

class Ska(object):
    def __init__(self, ectype):
        err = c_int(0)
        self.__ctx = skac_ctx_init(ectype, byref(err))
        if err.value != 0:
            raise  SkaError("init ctx error: {}".format(err.value))

    def __del__(self):
        if skac_ctx_free is not None:
            skac_ctx_free(self.__ctx)

    def startlog(self, level, path):
        skac_start_log(level, path)

    def txn(self):
        return SkaTxn(self.__ctx)

    def rand(self, txn, len):
        buf = create_string_buffer(len)
        ret = skac_rand(txn, buf, len)
        if ret != 0:
            raise SkaError("rand error:{}".format(ret))
        return buf

    def hash(self, txn, hashtype, data):
        size = c_size_t(0)
        buf = create_string_buffer(HASH_MAX_SIZE)
        ret = skac_hash(txn, hashtype, data, len(data), buf, byref(size))
        if ret != 0:
            raise SkaError("hash error:{}".format(ret))
        return buf[:size.value]

    def hmac(self, txn, hashtype, key, data):
        size = c_size_t(0)
        buf = create_string_buffer(HASH_MAX_SIZE)
        ret = skac_hmac(txn, hashtype, key, len(key), data, len(data), buf, byref(size))
        if ret != 0:
            raise SkaError("hmac error:{}".format(ret))
        return buf[:size.value]

    def pbkdf2(self, txn, pwd, salt,count, keylen):
        buf = create_string_buffer(keylen)
        ret = skac_pbkdf2_hmac(txn, pwd, len(pwd), salt, len(salt), count, keylen, buf)
        if ret != 0:
            raise SkaError("pbkdf2 error:{}".format(ret))
        return buf

    def ecsign(self, txn, hashtype, signtype, prikey, data):
        buf = create_string_buffer(SIGN_MAX_SIZE)
        size = c_size_t(0)
        kp = KeyPair()
        ret = skac_keypair_load(txn, prikey, len(prikey), None, 0, byref(kp))
        if ret != 0:
            raise SkaError("sign load prikey error:{}".format(ret))
        ret = skac_ec_sign(txn, byref(kp), hashtype, signtype, data, len(data), buf, byref(size))
        if ret != 0:
            raise SkaError("sign error:{}".format(ret))
        return buf[:size.value]

    def ecverify(self, txn, hashtype, signtype, pubkey, data, sign):
        result = c_int(0)
        ret = skac_ec_check_ex(txn, hashtype, signtype, data, len(data), sign, len(sign), pubkey, len(pubkey), byref(result))
        if ret != 0:
            raise SkaError("verify error:{}".format(ret))
        return result.value == 1

    def pripubverify(self, txn, prikey, pubkey):
        result = c_int(0)
        kp = KeyPair()
        ret = skac_keypair_load(txn, prikey, len(prikey), pubkey, len(pubkey), byref(kp))
        if ret != 0:
            raise SkaError("pripub check load keypair error:{}".format(ret))
        ret = skac_pripub_check(txn, byref(kp), byref(result))
        if ret != 0:
            raise SkaError("pripub check error:{}".format(ret))
        return result.value != 0

    def pri2pub(self, txn, pubtype, prikey):
        buf = create_string_buffer(PUBKEY_MAX_SIZE)
        size = c_size_t(0)
        ret = skac_pri_to_pub(txn, prikey, len(prikey), pubtype, buf, byref(size))
        if ret != 0:
            raise SkaError("pri2pub error:{}".format(ret))
        return buf[:size.value]

    def pub2addr(self, txn, addrtype, pubkey):
        buf = create_string_buffer(ADDR_MAX_SIZE)
        size = c_size_t(0)
        ret = skac_pub_to_addr(txn, addrtype, pubkey, len(pubkey), buf, byref(size))
        if ret != 0:
            raise SkaError("pub2addr error:{}".format(ret))
        return buf[:size.value]

    def cipherreset(self, txn, cipher, padding, key, iv):
        ret = skac_cipher_reset(txn, cipher, padding, key, len(key), iv, len(iv), None, 0)
        if ret != 0:
            raise SkaError("cipher reset error:{}".format(ret))

    def ciphersetkey(self, txn, key):
        ret = skac_cipher_set_key(txn, key, len(key))
        if ret != 0:
            raise SkaError("cipher set key error:{}".format(ret))

    def ciphersetiv(self, txn, iv):
        ret = skac_cipher_set_key(txn, iv, len(iv))
        if ret != 0:
            raise SkaError("cipher set key error:{}".format(ret))

    def encrypt(self, ciphertxn, data):
        buf = create_string_buffer(len(data)+16)
        size = c_size_t(0)
        ret = skac_encrypt(ciphertxn, data, len(data), buf, byref(size))
        if ret != 0:
            raise SkaError("cipher encrypt error:{}".format(ret))
        return buf[:size.value]

    def decrypt(self, ciphertxn, data):
        buf = create_string_buffer(len(data))
        size = c_size_t(0)
        ret = skac_decrypt(ciphertxn, data, len(data), buf, byref(size))
        if ret != 0:
            raise SkaError("cipher decrypt error:{}".format(ret))
        return buf[:size.value]

    def txnclear(self, txn):
        skac_txn_clear(txn)

    def sign2pub(self, txn, pubtype, signtype, data, sign):
        buf = create_string_buffer(PUBKEY_MAX_SIZE)
        size = c_size_t(0)
        ret = skac_sign_to_pub(txn, pubtype, signtype, data, len(data), sign, len(sign), buf, byref(size))
        if ret != 0:
            raise SkaError("sign to pub error:{:02X}".format(ret))
        return buf[:size.value]

    def sign2addr(self, txn, signtype, addrtype, data, sign):
        buf = create_string_buffer(ADDR_MAX_SIZE)
        size = c_size_t(0)
        ret = skac_sign_to_addr(txn, signtype, addrtype, data, len(data), sign, len(sign), buf, byref(size))
        if ret != 0:
            raise SkaError("sign to addr error:{}".format(ret))
        return buf[:size.value]

    def md5(self, txn, data):
        return self.hash(txn, HASH_MD5, data)

    def sha2(self, txn, data):
        """sha2-256"""
        return self.hash(txn, HASH_SHA256, data)

    def sha512(self, txn, data):
        """sha2-512"""
        return self.hash(txn, HASH_SHA512, data)

    def sha3(self, txn, data):
        return self.hash(txn, HASH_SHA3, data)

    def hmac256(self, txn, key, data):
        return self.hmac(txn, HASH_SHA256, key, data)

    def hmac512(self, txn, key, data):
        return self.hmac(txn, HASH_SHA512, key, data)


if __name__ == '__main__':
    err = c_int(0)
    k = ''
    d = '239293sjfiwefwf'
    ctx = Ska(EC_256R1)
    ctx.startlog(4, 'logs/ska.log')

    with ctx.txn() as txn:
        pri = codecs.decode("1a7264ae5078f2a0c5b5e567457bbcedf1bdc3263ad32576c9a3c512c386ed6f", 'hex')
        pri = pri[::-1]
        key = ctx.rand(txn, 32)
        iv = ctx.rand(txn, 16)
        ctx.txnclear(txn)
        print("pri", codecs.encode(pri, 'hex'))
        pub = ctx.pri2pub(txn, PUBKEY_UNCOMPRESS, pri)
        ctx.txnclear(txn)
        print("pub", codecs.encode(pub, 'hex'))
        print("rand", codecs.encode(ctx.rand(txn, 32), 'hex'))
        ctx.txnclear(txn)
        print("md5", codecs.encode(ctx.md5(txn, d), 'hex'))
        ctx.txnclear(txn)
        print("sha3", codecs.encode(ctx.sha2(txn, d), 'hex'))
        ctx.txnclear(txn)
        print("sha2", codecs.encode(ctx.sha3(txn, d), 'hex'))
        ctx.txnclear(txn)
        print("sha512", codecs.encode(ctx.sha512(txn, d), 'hex'))
        ctx.txnclear(txn)
        print("hmac256", codecs.encode(ctx.hmac256(txn, k, d), 'hex'))
        ctx.txnclear(txn)
        print("hmac512", codecs.encode(ctx.hmac512(txn, k, d), 'hex'))
        ctx.txnclear(txn)
        print("pbkdf2", codecs.encode(ctx.pbkdf2(txn, k, d, 2000, 64), 'hex'))
        ctx.txnclear(txn)
        sign = ctx.ecsign(txn, HASH_SHA3, SIGN_CWV, pri, d)
        ctx.txnclear(txn)
        print("sign", codecs.encode(sign, 'hex'))
        result = ctx.ecverify(txn, HASH_SHA3, SIGN_CWV, pub, d, sign)
        ctx.txnclear(txn)
        print("verify result", result)
        # ctx.cipherreset(txn, CIPHER_AES_256_CBC, CIPHER_PADDING_PKCS7, key, iv)
        for i in range(10):
            ctx.cipherreset(txn, CIPHER_AES_256_CBC, CIPHER_PADDING_PKCS7, key, iv)
            endata = ctx.encrypt(txn, d)
            print("encrypt", codecs.encode(endata, 'hex'))
            dedata = ctx.decrypt(txn, endata)
            print("decrypt", dedata)

        ctx.ciphersetkey(txn, ctx.rand(txn, 32))
        endata = ctx.encrypt(txn, d)
        print("encrypt with set key", codecs.encode(endata, 'hex'))
        dedata = ctx.decrypt(txn, endata)
        print("decrypt with set key", dedata)
        checkret = ctx.pripubverify(txn, pri, pub)
        print("check pri pub result", checkret)
        pubfromsign = ctx.sign2pub(txn, PUBKEY_RAW, SIGN_CWV, d, sign)
        addrfromsign = ctx.sign2addr(txn, SIGN_CWV, ADDR_CWV, d, sign)
        print("sign to pub", len(pubfromsign), codecs.encode(pubfromsign, 'hex'))
        print("sign to addr", len(addrfromsign), codecs.encode(addrfromsign, 'utf-8'))


    del ctx
