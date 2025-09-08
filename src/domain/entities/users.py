from dataclasses import dataclass

Name = str
Email = str

@dataclass(kw_only=True)
class User:
    id: int
    name: Name
    email: Email