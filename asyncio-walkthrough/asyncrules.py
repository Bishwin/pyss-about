async def f(x):
    y = await z(x) # ok - `await` and `return` allowed in coroutine
    return y

async def g(x):
    yield x # ok - this is an async generator

async def m(x):
    yield from gen(x) # No - SyntaxError

def m(x):
    y = await z(x) # No - SyntaxError (no `async def` here)
    return y


