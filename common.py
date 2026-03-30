def iscat(name: str) -> bool:
    for s in ["Russian_Blue", "Birman"]:
        if s in name:
            return True
    return False


def isdog(name: str) -> bool:
    for s in ["samoyed", "pug"]:
        if s in name:
            return True
    return False
