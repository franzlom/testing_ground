import json
import jwt

if __name__ == '__main__':
    message = {
        'something': 123,
        'another_thing': [1, 2, 3]
    }

    alg = 'HS256'
    secret = 'WrnXKLqI1SAade2blUZb07H7Rn6xAVB7B2dq5jIO1d7DwaUtz0Vn4cbY3pXqrjPtvvhtuRPfPWzQx7zIkrGPuQ=='

    encode = jwt.encode(message, secret, algorithm=alg)
    print(encode)

    decoded = jwt.decode(encode, secret, algorithms=alg)
    print(decoded)

