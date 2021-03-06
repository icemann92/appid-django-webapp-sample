## Running the Sample

1. Run `pip3 install -r requirements.txt`
2. Configure App ID to work with the sample. Add the oauthServerUrl, client_id, and secret obtained from App ID to the `src/store/settings.py` file 
    - oauthServerUrl to `SOCIAL_AUTH_APPID_OAUTH_SERVER_URL` 
    - client_id to `SOCIAL_AUTH_APPID_KEY` 
    - secret to `SOCIAL_AUTH_APPID_SECRET`

3. Run `python manage.py migrate`
5. Add the redirect url to your App Id instance. `http://localhost:8000/*`
4. Finally run `python3 manage.py runserver`
5. Sample app runs on http://localhost:8000
6. Once you login. You can see view the access token on the homepage


## Implementation 
Sample uses the [python-social-auth](https://python-social-auth.readthedocs.io/en/latest/) library.
Check out the `webapp/authentication/appid.py` module for AppID integration with the library. It basically extends the 
OpenIDConnect module and implements a few things required for AppID


