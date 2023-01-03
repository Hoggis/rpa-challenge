from RPA.Robocorp.Vault import Vault

_secret = Vault().get_secret("credentials")

USER_NAME = _secret["username"]
PASSWORD = _secret["password"]