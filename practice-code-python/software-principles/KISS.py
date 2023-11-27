# KISS: Keep It Simple, Stupid
# Principle: Keep the design and implementation as simple as possible.
# In eXtreme Programming (XP), this principle is indicated by a practice named "Do the simplest thing that could possibly work" (DTSTTCPW).

# Bad Example
def complicated_loop(data):
    result = 0
    for i in range(len(data)):
        # Complex loop logic with unnecessary details
        result += data[i] * (i + 1)
    return result

# Good Example


def simple_loop(data):
    result = 0
    for value in data:
        # Simple loop logic with clear iteration
        result += value
    return result
