from kitchen import Quantity, grams, ounces

def test_multiplication():
    flour = grams(200)
    assert  flour.times(3).amount == 600

def test_multiplication_by_two():
    flour = grams(200)
    assert flour.times(2).amount == 400

def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400

def test_multiplication():
    flour = grams(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400

def test_multiplication():
    flour = grams(200)
    assert flour.times(3).amount == 600

def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)

def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)