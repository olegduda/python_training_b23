import requests


class AuthApi:

    @staticmethod
    def auth_user(prefix: str, username: str, password: str) -> str:
        prefix_auth = "index.php"
        response = requests.post(f'{prefix}{prefix_auth}', data=f'user={username}&pass={password}')
        cookie = response.headers.get("Set-Cookie")
        return cookie

