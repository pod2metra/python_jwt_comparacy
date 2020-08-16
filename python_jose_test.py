import os
import timeit


_jwt = os.environ["JWT_IMPORT"]
COUNTER = 1000

RS_PRIV = b'''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''


RS_PUB = '''ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDCnzlf+XwBQoxh7xFejEHHuxCTrzCrpJ/KtTBc8dcO+pR2nk1mkXFAhF/MueOA6JJggc26Pn0i8SjAAUL8sJH9qUNuz0Eyq+QVu8bKEKrgcf6r/4vCbwb7qfPXaggLIbFlLwOK+RjazYsdQYm6MLx6jyJsyWpS2uA63wQkXM7uOJwRXSzlXSXYSjn6/70F9e7WUx6i8ZsBXxItOKEAW9Ef1mtuMwCDDyZBCJSWHtTvB/di1nFnQK5HK2NX3fEPzH4TmU0eefc6fLFLhgevDWzrNnF6JCqolQLTHgpJczojQ1s84nHg2zSP3Vf2vulRzHmD3n+aHXOCUr8kwYx9qcoZu/PI+iDLreTUjM27agGfTUlvb32T5+QntGBCbX2OXzoLbSXAbYA9tY83x2Wup+ldA76ArkLCeHATQIf7qYRtvplSQ1gSS4sPInTd27mzDl0q/qht3BoXolGCNKAotEIYc8fVZ8QDJKFGITy9hfjKm7yAFlwu+dBlXOeMAbAXC/E01Z+7IHguvjgUsZPFjGWHN6Kn6zzr2d2aoPth8HXgIitc6hNO8ZUO49vfXxKCm+ryRU5Wvo45oc70vjAXNAlnMMwpQtaUbscXx9Stg1ibDz2kT9SbAKC0p2NfFzapIlCVWiotwP323o5x3Aeeg7gq8/jkAS+7wUdiE/A018iqvw== user@example.com'''


def encode(alg):
    return jwt.encode(
        {
          "sub": "1234567890",
          "name": "John Doe",
          "iat": 1516239022
        },
        'secret' if alg.startswith('HS') else RS_PRIV,
        algorithm=alg,
    )


def authlib_encode(alg):
    return jwt.encode(
        {'alg': alg},
        {
          "sub": "1234567890",
          "name": "John Doe",
          "iat": 1516239022
        },
        'secret' if alg.startswith('HS') else RS_PRIV,
    )


def decode(token, alg):
    jwt.decode(token, 'secret' if alg.startswith('HS') else RS_PUB)


if _jwt == 'jose.jwt':
    from jose import jwt
elif _jwt == 'authlib.jose.jwt':
    from authlib.jose import jwt
    encode = authlib_encode
elif _jwt == 'jwt':
    import jwt
else:
    raise ValueError(f"Unknown jwt module {_jwt}")


print("====")
print("encode HS256:")
print(timeit.timeit(lambda: encode("HS256"), number=COUNTER))
print("encode HS512:")
print(timeit.timeit(lambda: encode("HS512"), number=COUNTER))
print("encode HS384:")
print(timeit.timeit(lambda: encode("HS384"), number=COUNTER))
print("encode RS256:")
try:
    print(timeit.timeit(lambda: encode("RS256"), number=COUNTER))
except Exception:
    print("-")
print("encode RS512:")
try:
    print(timeit.timeit(lambda: encode("RS512"), number=COUNTER))
except Exception:
    print("-")
print("encode RS384:")
try:
    print(timeit.timeit(lambda: encode("RS384"), number=COUNTER))
except Exception:
    print("-")
print("====")
print("decode HS256:")
token = encode("HS256")
print(timeit.timeit(lambda: decode(token, "HS256"), number=COUNTER))
print("====")
print("decode HS512:")
token = encode("HS512")
print(timeit.timeit(lambda: decode(token, "HS512"), number=COUNTER))
print("====")
print("decode HS384:")
token = encode("HS384")
print(timeit.timeit(lambda: decode(token, "HS384"), number=COUNTER))
print("====")
print("decode RS256:")
try:
    token = encode("RS256")
    print(timeit.timeit(lambda: decode(token, "RS256"), number=COUNTER))
except Exception:
    print("-")
print("====")
print("decode RS512:")
try:
    token = encode("RS512")
    print(timeit.timeit(lambda: decode(token, "RS512"), number=COUNTER))
except Exception:
    print("-")
print("====")
print("decode RS384:")
try:
    token = encode("RS384")
    print(timeit.timeit(lambda: decode(token, "RS384"), number=COUNTER))
except Exception:
    print("-")
print("====")
