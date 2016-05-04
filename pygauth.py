import math
import base64
import time
import hashlib
import hmac
import struct
import os

def generate_otp(label, user, key):
    """Generates a otpauth:// URI"""
    return "otpauth://totp/%s:%s?secret=%s&issuer=%s" % (label,user,key,label)

class keygen:
    """Generates a secure key that __str__ to b32 and __bytes__ to bytes"""
    myKey = b""
    def __init__(self, l=20):
        myKey = os.urandom(l)
    
    def __str__(self):
        return base64.b32decode(self.myKey)
    
    def __bytes__(self):
        return self.myKey

def hmac_sha1(key, message):
    hms1 = hmac.new(key, message, hashlib.sha1)
    return hms1.digest()

#Implimented based on the code at
#https://en.wikipedia.org/wiki/Google_Authenticator#Technical_description
class GAuth:
    secret = ""
    def __init__(self, secret):
        self.secret = base64.b32decode(secret)
        
    def TOTP(self, myTime=None):
        if myTime == None:
            myTime = int(time.time())
        
        message = math.floor(myTime / 30)
        hash = hmac_sha1(self.secret, struct.pack(">I", message))
        offset = hash[19] & 0x0F #0x0F = 00001111
        
        #4 bytes starting at the offset
        truncatedHash = struct.unpack(">I", hash[offset:offset+4])[0]
        
        #remove the most significant bit
        #0x7FFFFFFF = 01111111111111111111111111111111
        truncatedHash = truncatedHash & 0x7FFFFFFF
        code = truncatedHash % 1000000
        return ("000000"+str(code))[-6:]
    
    def HOTP(self, ioff=0):
        message = struct.unpack(">Q", ioff)[0]
        hash = hmac_sha1(self.secret, message)
        offset = hash[19] & 0x0F #0x0F = 00001111
        
        #4 bytes starting at the offset
        truncatedHash = struct.unpack(">I", hash[offset:offset+4])[0]
        
        #remove the most significant bit
        #0x7FFFFFFF = 01111111111111111111111111111111
        truncatedHash = truncatedHash & 0x7FFFFFFF
        return ("000000"+str(code))[-6:]

if name == '__main__': #Test bed
    gauth = GAuth()
    print(gauth.TOTP("ACDEFGHI"))