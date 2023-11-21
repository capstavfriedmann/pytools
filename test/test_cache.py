from pytools.cacher.caching_utils import cache_json, _is_in_cache

def test_insert_cache_json():
    # for caching purposes, ignore the positional_argument
    @cache_json(["name"])
    def test_func(positional_argument, name=None):
        return positional_argument
    

    test_func("some random argument", name="keyword argument")

    assert not _is_in_cache("some value")
    assert _is_in_cache("keyword argument")

    result = test_func("different_arg", name="keyword argument")
    assert result == "some random argument"

    # in this case use all arguments
    @cache_json()
    def test_func2(many, positional, arguments):
        return f"{many}, {positional}, {arguments}"

    result = test_func2("these", 2, "args")
    assert _is_in_cache("these" + str(2) + "args")
    assert not _is_in_cache("any3args")


