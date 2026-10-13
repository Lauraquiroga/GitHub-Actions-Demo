def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b