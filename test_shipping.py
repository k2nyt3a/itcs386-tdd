from shipping import shipping_fee
import pytest


# Rule 1 is broken: zero weight must raise ValueError.
@pytest.mark.parametrize("weight_kg", [-1, -0.01, 0])
def test_non_positive_weight_is_refused(weight_kg):
    with pytest.raises(ValueError):
        shipping_fee(weight_kg)


@pytest.mark.parametrize("weight_kg, expected_fee", [
    (0.01, 40),
    (0.5, 40),
    (0.99, 40),
    # Rule 2 is broken: exactly 1 kg must cost 40 baht.
    (1, 40),
    (1.01, 60),
    (3, 60),
    (4.99, 60),
    (5, 60),
    # Rule 4 is broken: a started kilogram above 5 kg must be charged.
    (5.01, 70),
    # Rule 4 is broken: 5.2 kg must cost 70 baht.
    (5.2, 70),
    (6, 70),
    # Rule 4 is broken: starting the second extra kilogram costs 80 baht.
    (6.01, 80),
    # Rule 4 is broken: a partial second extra kilogram must be charged.
    (6.5, 80),
    (7, 80),
    # Rule 4 is broken: starting the third extra kilogram costs 90 baht.
    (7.01, 90),
])

def test_shipping_fee(weight_kg, expected_fee):
    assert shipping_fee(weight_kg) == expected_fee

