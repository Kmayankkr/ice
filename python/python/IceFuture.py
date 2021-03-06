# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

#
# This file should only be used in Python >= 3.5.
#

import asyncio

#
# This class defines an __await__ method so that coroutines can call 'await <future>'.
#
# Python 2.x rejects this code with a syntax error because a return statement is not allowed in a generator.
#
class FutureBase(object):
    def __await__(self):
        if not self.done():
            yield self
        return self.result()

def wrap_future(future, *, loop=None):
    '''Wrap Ice.Future object into an asyncio.Future.'''
    if isinstance(future, asyncio.Future):
        return future

    assert isinstance(future, FutureBase), 'Ice.Future is expected, got {!r}'.format(future)

    if loop is None:
        loop = asyncio.get_event_loop()

    af = loop.create_future()

    def callback():
        if future.cancelled():
            af.cancel()
        elif future.exception():
            af.set_exception(future.exception())
        else:
            af.set_result(future.result())

    future.add_done_callback(lambda f: loop.call_soon_threadsafe(callback))
    return af
