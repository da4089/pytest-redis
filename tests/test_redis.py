"""Module containing all tests for pytest-redis."""

from pytest_redis import factories


def test_redis(redisdb):
    """Check that it's actually working on redis database."""
    redisdb.set('test1', 'test')
    redisdb.set('test2', 'test')

    test1 = redisdb.get('test1')
    assert test1 == b'test'

    test2 = redisdb.get('test2')
    assert test2 == b'test'


redis_proc2 = factories.redis_proc(port=6381)
redisdb2 = factories.redisdb('redis_proc2')


def test_second_redis(redisdb, redisdb2):
    """Check that two redis prorcesses are separate ones."""
    redisdb.set('test1', 'test')
    redisdb.set('test2', 'test')
    redisdb2.set('test1', 'test_other')
    redisdb2.set('test2', 'test_other')

    test1 = redisdb.get('test1')
    assert test1 == b'test'

    test2 = redisdb.get('test2')
    assert test2 == b'test'

    assert redisdb2.get('test1') == b'test_other'
    assert redisdb2.get('test2') == b'test_other'
