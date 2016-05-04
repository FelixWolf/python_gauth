# python_gauth
```python
str URI = pygauth.generate_otp(label, user, key)
mixed[str|bytes] secureKey = pygauth.keygen(length)
bytes hmac = pygauth.hmac_sha1(key, message)
object gauth = pygauth.GAuth(secret):
    string code = TOTP(myTime = int(time.time()))
    string code = HOTP(increment = 0)
```
