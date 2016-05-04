# python_gauth
str URI = python_gauth.generate_otp(label, user, key)
mixed[str|bytes] secureKey = python_gauth.keygen(length)
bytes hmac = python_gauth.hmac_sha1(key, message)
object gauth = python_gauth.GAuth(secret):
    string code = TOTP(myTime = int(time.time()))
    string code = HOTP(increment = 0)
