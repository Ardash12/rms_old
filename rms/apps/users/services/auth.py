from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken


def get_token_http_reponse(user, refresh_token: str = None) -> HttpResponse:
    """
    Generates and returns an HTTP response that includes the access and refresh tokens for the given user.

    Arguments:
    - user: A UserModel object representing the user to generate tokens for.
    - refresh_token: user's 'refresh' token. If provided, generates a new 'access' token for user.

    Return:
    - An HttpResponse object with cookies set for access and refresh tokens.
    
    The function creates an empty HttpResponse object with a 200 status code and then either generates a refresh token using 
    the `RefreshToken.for_user` method or new access token based on provided refresh token using 'RefreshToken'. 
    The user's access token is added to the access token cookie using the `http_response.set_cookie` method with the httponly and secure options set to True. 
    Similarly, the refresh token is added to the refresh token cookie. Finally, the http_response object is returned.
    """
    
    http_response = HttpResponse(status=200)
    if refresh_token:
        token = RefreshToken(token=refresh_token)
    else:
        token = RefreshToken.for_user(user)
        http_response.set_cookie('refresh', str(token), httponly=True)
    http_response.set_cookie('access', str(token.access_token), httponly=True)
    return http_response


def get_logout_http_response(token: str) -> HttpResponse:
    """
    Perform logout fuctionality by blacklisting user's refresh token.

    Arguments:
    - token: user's 'refresh' token.

    Return:
    - An HttpResponse object wich deletes cookies for access and refresh tokens.
    
    The function creates a RefreshToken object based on provided refresh token and blacklists it. Then creates an empty HttpResponse 
    object with a 204 status code and deletes stored in cookies 'access' and 'refresh' tokens Finally, the http_response object is returned.
    """

    token = RefreshToken(token)
    token.blacklist()
    http_response = HttpResponse(status=204)
    http_response.delete_cookie('access')
    http_response.delete_cookie('refresh')
    return http_response
