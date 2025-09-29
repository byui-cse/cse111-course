from practice_solution import compute_monthly_payment, compute_total_payment

from pytest import approx
import pytest

def test_compute_monthly_payment():
   """Test the compute monthly payment function."""

   # Test zeros
   assert compute_monthly_payment(0, 0, 0) == approx(0, abs=0.01)
   assert compute_monthly_payment(0, .05, 10) == approx(0, abs=0.01)
   assert compute_monthly_payment(120, 0, 1) == approx(10, abs=0.01)
   assert compute_monthly_payment(120, .1, 0) == approx(120, abs=0.01)
   assert compute_monthly_payment(120, 0, 0) == approx(120, abs=0.01)

   # Normal cases
   # Micro loan
   assert compute_monthly_payment(100, .1, 1) == approx(8.79, abs=0.01)

   # Small loan
   assert compute_monthly_payment(1000, .05, 10) == approx(10.61, abs=0.01)

   # Medium loan
   assert compute_monthly_payment(20000, .04, 7) == approx(273.38, abs=0.01)

   # Large loan, like a home mortgage
   assert compute_monthly_payment(500000, .075, 30) == approx(3496.07, abs=0.01)


def test_compute_total_payment():
   """Test compute_total_payment function."""

   # What if the user types a 0?
   assert compute_total_payment(compute_monthly_payment(0,0,0), 0) == approx(0, abs=0.01)

   # Some normal use cases
   monthly_payment = compute_monthly_payment(100, .1, 1)
   assert compute_total_payment(monthly_payment, 1) == approx(105.50, abs=0.01)

   monthly_payment = compute_monthly_payment(1000, .05, 10)
   assert compute_total_payment(monthly_payment, 10) == approx(1272.79, abs=0.01)

   monthly_payment = compute_monthly_payment(20000, .04, 7)
   assert compute_total_payment(monthly_payment, 7) == approx(22_963.59, abs=0.01)

   monthly_payment = compute_monthly_payment(500000, .075, 30)
   assert compute_total_payment(monthly_payment, 30) == approx(1_258_586.12, abs=0.01)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
# pytest.main(["-v", "--tb=line", "-rN", __file__])
pytest.main(["-v", "-rN", __file__])
