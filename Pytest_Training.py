# ========================================
def square(x):
    # print(f"The square of {x} is:")
    return x**2


# ========================================
# PYTEST tests
def test_square_4():
    assert square(4) == 16


def test_square_8():
    assert square(8) == 64


def test_square_9():
    assert square(9) == 81


def test_square_10():
    assert square(10) == 100