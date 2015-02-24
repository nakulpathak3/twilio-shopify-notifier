def is_shopify_hmac(data,secret,headerval):
    ''' Validates the HMAC signature from shopify. If not there, deny request.'''
    hm = hmac.new(secret,data,hashlib.sha256)
    hm_digest_verify = base64.b64encode(hm.digest())
    if hm_digest_verify != headerval:
        return False
    else:
        return True