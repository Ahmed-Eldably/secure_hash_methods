import hashlib
import sha3_256
import scrypt
import secrets
import bcrypt
import uuid


# string that has to be hashed
password = "foo"

# encode the string
encoded_word = password.encode()

# create a sha-3_256 object
sha3_256_obj = hashlib.sha3_256(encoded_word)

# print the results in hexadecimal
print("\nSHA3-256 Hash: ", sha3_256_obj.hexdigest())

# generate a strong salt
salt = uuid.uuid4().hex

#  encrypt using scrypt
scrypt_key = scrypt.hash(password, salt, N=16384, r=8, p=1)

# print the salt and the scrypt_key
print('\nSalt: ', salt)
print('\nScrypt Key: ', scrypt_key)