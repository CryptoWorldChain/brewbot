import codecs
from ctypes import *
import os
import platform
#ska functions

__DLL_NAME = None
if platform.system() == 'Windows':
    __DLL_NAME = 'ska.dll'
elif platform.system() == 'Darwin':
    __DLL_NAME = 'libska.dylib'
else:
    __DLL_NAME = 'libska.so'
DLL_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], __DLL_NAME)

SKA_DLL = CDLL(DLL_PATH)

class KeyPair(Structure):
    _fields_ = [('ecp_size', c_uint16),
                ('key_mask', c_uint16),
                ('pri', c_ubyte*32),
                ('pub', c_ubyte*68)]


class SkaError(Exception):
    """ska lib exceptions"""
    pass

# void skac_start_log(int level, const char* path)
skac_start_log = CFUNCTYPE(None, c_int, c_char_p)(("skac_start_log", SKA_DLL))
# skac_context_t* skac_context_init(skac_ec_type_t ec_type, int* error)
skac_ctx_init = CFUNCTYPE(c_void_p, c_int, c_void_p)(("skac_context_init", SKA_DLL))
# void skac_context_free(skac_context_t* ctx)
skac_ctx_free = CFUNCTYPE(None, c_void_p)(("skac_context_free", SKA_DLL))
# int skac_rand(skac_txn_t* txn, uint8_t* buf, size_t buf_size)
skac_rand = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t)(("skac_rand", SKA_DLL))
# skac_txn_t* skac_txn_init(skac_context_t* ctx, skac_param_t* param, int* err)
skac_txn_init = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p)(("skac_txn_init", SKA_DLL))
# void skac_txn_free(skac_txn_t* txn)
skac_txn_free = CFUNCTYPE(None, c_void_p)(("skac_txn_free", SKA_DLL))
# void skac_txn_clear(skac_txn_t* txn)
skac_txn_clear = CFUNCTYPE(None, c_void_p)(("skac_txn_clear", SKA_DLL))
# int skac_hash(skac_txn_t* txn, int hash_type, const uint8_t* data, size_t data_size, uint8_t* out, size_t* out_size);
skac_hash = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p, c_size_t, c_void_p,
                      POINTER(c_uint64))(("skac_hash", SKA_DLL))
# int skac_hmac(skac_txn_t* txn, int hash_type, const uint8_t* key, size_t key_size,
#               const uint8_t* data, size_t data_size, uint8_t* out, size_t* out_size);
skac_hmac = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p, c_size_t, c_void_p,
                      c_size_t, c_void_p, c_void_p)(("skac_hmac", SKA_DLL))
# int skac_cipher_reset(skac_txn_t* txn, int cipher, int padding,
#         const uint8_t* key, size_t key_size, const uint8_t* iv, size_t iv_size, const uint8_t* ext, size_t ext_size)
skac_cipher_reset = CFUNCTYPE(c_int, c_void_p, c_int, c_int, c_void_p, c_size_t, c_void_p, c_size_t, c_void_p, c_size_t)(("skac_cipher_reset", SKA_DLL))
# int skac_encrypt(skac_txn_t* txn, uint8_t* data, size_t data_size, uint8_t* out, size_t* out_size);
skac_encrypt = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t, c_void_p, c_void_p)(("skac_encrypt", SKA_DLL))
# int skac_decrypt(skac_txn_t* txn, uint8_t* data, size_t data_size, uint8_t* out, size_t* out_size);
skac_decrypt = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t, c_void_p, c_void_p)(("skac_decrypt", SKA_DLL))
# int skac_cipher_set_key(skac_txn_t* txn, uint8_t* key, size_t key_size)
skac_cipher_set_key = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t)(("skac_cipher_set_key", SKA_DLL))
# int skac_cipher_set_iv(skac_txn_t* txn, uint8_t* iv, size_t iv_size)
skac_cipher_set_iv = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t)(("skac_cipher_set_iv", SKA_DLL))
# int skac_pbkdf2_hmac(skac_txn_t* txn, const uint8_t* password, size_t password_size,
#                     const uint8_t* salt, size_t salt_size, uint32_t count, uint32_t key_len, uint8_t* key)
skac_pbkdf2_hmac = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t, c_void_p,
                             c_size_t, c_uint32, c_uint32, c_void_p)(("skac_pbkdf2_hmac", SKA_DLL))
skac_ec_genkey = CFUNCTYPE(c_int, c_void_p, POINTER(KeyPair))(("skac_ec_genkey", SKA_DLL))
# int skac_keypair_load(skac_txn_t* txn, const uint8_t* prikey, size_t prikey_size,
#                      const uint8_t* pubkey, size_t pubkey_size, skac_keypair_t* keypair);
skac_keypair_load = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t, c_void_p,
                              c_size_t, c_void_p)(("skac_keypair_load", SKA_DLL))
# int skac_ec_sign(skac_txn_t* txn, skac_keypair_t* keypair, int hash_type, int sign_type,
#                 const uint8_t* data, size_t data_size, uint8_t* sign, size_t* sign_size)
skac_ec_sign = CFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_int, c_void_p, c_size_t,
                         c_void_p, c_void_p)(("skac_ec_sign", SKA_DLL))
#int skac_ec_check_ex(skac_txn_t* txn, int hash_type, int sign_type, const uint8_t* data, size_t data_size,
#                     const uint8_t* sign, size_t sign_size, const uint8_t* pubkey, size_t pubkey_size, int* result);
skac_ec_check_ex = CFUNCTYPE(c_int, c_void_p, c_int, c_int, c_void_p, c_size_t,
                             c_void_p, c_size_t, c_void_p, c_size_t,
                             c_void_p)(("skac_ec_check_ex", SKA_DLL))
# int skac_pri_to_pub(skac_txn_t* txn, const uint8_t* prikey, size_t prikey_size, int pub_type, uint8_t* pubkey, size_t* pubkey_size);
skac_pri_to_pub = CFUNCTYPE(c_int, c_void_p, c_void_p, c_size_t, c_int, c_void_p,
                            c_void_p)(("skac_pri_to_pub", SKA_DLL))

skac_pub_check = CFUNCTYPE(c_int, c_void_p, POINTER(KeyPair), POINTER(c_int))(("skac_pub_check", SKA_DLL))
# int skac_pripub_check(skac_txn_t* txn, const skac_keypair_t* keypair, int* result);
skac_pripub_check = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)(("skac_pripub_check", SKA_DLL))
skac_pub_extend = CFUNCTYPE(c_int, c_void_p, POINTER(c_uint8), c_uint64, POINTER(c_uint8),
                            POINTER(c_uint64))(("skac_pub_extend", SKA_DLL))
# int skac_pub_to_addr(skac_txn_t* txn, int addr_type, const uint8_t* pubkey, size_t pubkey_size, uint8_t* addr, size_t *addr_size);
skac_pub_to_addr = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p, c_size_t, c_void_p,
                             c_void_p)(("skac_pub_to_addr", SKA_DLL))
skac_sign_to_pub = CFUNCTYPE(c_int, c_void_p, c_int, c_int, POINTER(c_uint8), c_uint64, POINTER(c_uint8),
                             c_uint64, POINTER(c_uint8), POINTER(c_uint64))(("skac_sign_to_pub", SKA_DLL))
skac_sign_to_addr = CFUNCTYPE(c_int, c_void_p, c_int, c_int, c_int, POINTER(c_uint8), c_uint64, POINTER(c_uint8),
                              c_uint64, POINTER(c_uint8), POINTER(c_uint64))(("skac_sign_to_addr", SKA_DLL))

CIPHER_AES_128_ECB = 2
CIPHER_AES_192_ECB = 3
CIPHER_AES_256_ECB = 4
CIPHER_AES_128_CBC = 5
CIPHER_AES_192_CBC = 6
CIPHER_AES_256_CBC = 7
CIPHER_AES_128_CFB128 = 8
CIPHER_AES_192_CFB128 = 9
CIPHER_AES_256_CFB128 = 10
CIPHER_AES_128_CTR = 11
CIPHER_AES_192_CTR = 12
CIPHER_AES_256_CTR = 13
CIPHER_AES_128_GCM = 14
CIPHER_AES_192_GCM = 15
CIPHER_AES_256_GCM = 16
CIPHER_CAMELLIA_128_ECB = 17
CIPHER_CAMELLIA_192_ECB = 18
CIPHER_CAMELLIA_256_ECB = 19
CIPHER_CAMELLIA_128_CBC = 20
CIPHER_CAMELLIA_192_CBC = 21
CIPHER_CAMELLIA_256_CBC = 22
CIPHER_CAMELLIA_128_CFB128 = 23
CIPHER_CAMELLIA_192_CFB128 = 24
CIPHER_CAMELLIA_256_CFB128 = 25
CIPHER_CAMELLIA_128_CTR = 26
CIPHER_CAMELLIA_192_CTR = 27
CIPHER_CAMELLIA_256_CTR = 28
CIPHER_CAMELLIA_128_GCM = 29
CIPHER_CAMELLIA_192_GCM = 30
CIPHER_CAMELLIA_256_GCM = 31
CIPHER_DES_ECB = 32
CIPHER_DES_CBC = 33
CIPHER_DES_EDE_ECB = 34
CIPHER_DES_EDE_CBC = 35
CIPHER_DES_EDE3_ECB = 36
CIPHER_DES_EDE3_CBC = 37
CIPHER_BLOWFISH_ECB = 38
CIPHER_BLOWFISH_CBC = 39
CIPHER_BLOWFISH_CFB64 = 40
CIPHER_BLOWFISH_CTR = 41
CIPHER_ARC4_128 = 42
CIPHER_AES_128_CCM = 43
CIPHER_AES_192_CCM = 44
CIPHER_AES_256_CCM = 45
CIPHER_CAMELLIA_128_CCM = 46
CIPHER_CAMELLIA_192_CCM = 47
CIPHER_CAMELLIA_256_CCM = 48
CIPHER_SM4_ECB = 49
CIPHER_SM4_CBC = 50
CIPHER_SM4_CFB128 = 51
CIPHER_SM4_CTR = 52
CIPHER_SM4_GCM = 53
CIPHER_SM4_CCM = 54

CIPHER_PADDING_PKCS7 = 0
CIPHER_PADDING_ONE_AND_ZEROS = 1
CIPHER_PADDING_ZEROS_AND_LEN = 2
CIPHER_PADDING_ZEROS = 3
CIPHER_PADDING_NONE = 4

CIPHER_ENCRYPT = 0
CIPHER_DECRYPT = 1

HASH_MD5 = 3
HASH_SHA1 = 4
HASH_SHA224 = 5
HASH_SHA256 = 6
HASH_SHA384 = 7
HASH_SHA512 = 8
HASH_RIPEMD160 = 9
HASH_SHA3 = 10
HASH_SHA3_224 = 11
HASH_SHA3_256 = 12
HASH_SHA3_384 = 13
HASH_SHA3_512 = 14
HASH_SNAKE128 = 15
HASH_SNAKE256 = 16
HASH_SM3 = 17

EC_256K1 = 0
EC_256R1 = 1

SIGN_RAW = 0
SIGN_ASN1 = 1
SIGN_WITH_RECOVER = 2
SIGN_CSC = 3
SIGN_ETHEREUM = 4
SIGN_CWV = 5

PUBKEY_UNCOMPRESS = 0
PUBKEY_COMPRESS = 1
PUBKEY_BITCOIN = 2
PUBKEY_RAW = 3

ADDR_RIPEMD = 1
ADDR_BITCOIN = 2
ADDR_ETHEREUM = 3
ADDR_EOS = 4
ADDR_CSC = 5
ADDR_CWV = 6

HASH_MAX_SIZE = 64
SIGN_MAX_SIZE = 192
PUBKEY_MAX_SIZE = 65
ADDR_MAX_SIZE = 128
EC_SIZE = 32

if __name__ == '__main__':
    err = c_int(0)
    d = ''
    buf = create_string_buffer(64)
    size = c_size_t(0)
    ctx = skac_ctx_init(0, byref(err))
    skac_ctx_free(ctx)
    print("type:{}, sha3:{}".format(type(buf), codecs.encode(buf[:size.value], 'hex')))
    # ctx = (FUNCTIONS[FUNC_CTX_INIT]((FUNC_CTX_INIT, dll)))(0, byref(err))
    # txn = (FUNCTIONS[FUNC_TXN_INIT]((FUNC_TXN_INIT, dll)))(ctx, None, byref(err))
    # ret = (FUNCTIONS[FUNC_HASH]((FUNC_HASH, dll)))(txn, 10, d, len(d), buf, byref(size))
    # print("type:{}, sha3:{}".format(type(buf), codecs.encode(buf[:size.value], 'hex')))
    # (FUNCTIONS[FUNC_TXN_FREE]((FUNC_TXN_FREE, dll)))(txn)
    # (FUNCTIONS[FUNC_CTX_FREE]((FUNC_CTX_FREE, dll)))(ctx)
    print(DLL_PATH, err.value)
