"""
AppID Social-Auth Backend
"""
from social_core.backends.open_id_connect import OpenIdConnectAuth
import base64
import json
import src.store.settings as s


class AppID(OpenIdConnectAuth):

    name = 'appid'
    OIDC_ENDPOINT = s.SOCIAL_AUTH_APPID_OAUTH_SERVER_URL
    ACCESS_TOKEN_METHOD = 'POST'
    USERNAME_KEY = 'email'

    #JWT DECODE and validation options
    JWT_DECODE_OPTIONS = {
        'verify_signature': True,
        'verify_aud': True,
        'verify_iat': False,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iss': True,
        'verify_sub': False,
        'verify_jti': False,
        'verify_at_hash': False,
        'leeway': 0,
    }


    def construct_basic_auth_header(self):
        auth = "%s:%s" % (s.SOCIAL_AUTH_APPID_KEY, s.SOCIAL_AUTH_APPID_SECRET)
        return 'basic ' + base64.b64encode(auth.encode("ascii")).decode("ascii")

    def auth_headers(self):
        return {'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json',
                'Authorization': self.construct_basic_auth_header()}

    # Need to override this because, Django needs 'alg' in jwks and we don't have it there.
    # Also no way to set alg globally for a backend.
    def get_remote_jwks_keys(self):
        response = self.request(self.jwks_uri())
        keys = json.loads(response.text)['keys']
        for key in keys:
            key['alg'] = 'RS256'
        return keys