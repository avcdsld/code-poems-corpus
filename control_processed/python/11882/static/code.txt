async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)