from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbolError(Exception):
    pass


class NameContainSymbolsError(Exception):
    pass


NAME_LENGTH = 4
VALID_DOMAIN = (".com", ".bg", ".net", ".org")

pattern = r'\.?\w+'
email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not email.split("@")[0] == findall(pattern, email)[0]:
        raise NameContainSymbolsError("Name can contain only letters and underscore")

    if findall(pattern, email)[-1] not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
