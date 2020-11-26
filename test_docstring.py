def is_redirect_safe(target: Optional[str]) -> bool:
    """Check if redirect is safe, that is using HTTP protocol and is pointing
    to the same site.
    
    :param target: redirect target url
    :type target: str
    :return: flag signalling whether redirect is safe
    :rtype: bool
    """

    if not target:
        return False
