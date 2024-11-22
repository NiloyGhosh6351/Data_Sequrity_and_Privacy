from pyope.ope import OPE

ope = OPE(b'abcdefghijklmnop')


def encrypt_weight(weight):
    return ope.encrypt(weight)


def decrypt_weight(encrypted_weight):
    return ope.decrypt(encrypted_weight)
