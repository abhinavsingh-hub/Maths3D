"""
Mathematical Verification Tests for M3 Animation Video
Verifies all algebraic and numerical claims for f(x) = x^3 - 3x using SymPy.
Course: Linear Algebra & Calculus (M3)
"""

import sys
from pathlib import Path
import pytest
import sympy as sp

# Add M3_Code directory to path
M3_CODE_DIR = Path(__file__).resolve().parent.parent
if str(M3_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(M3_CODE_DIR))

from helpers import f_func, f_sympy, x_sym


def test_integer_evaluations():
    """Verify f(2) = 2, f(-2) = -2, f(-1) = 2, f(1) = -2, f(0) = 0."""
    assert f_func(2) == 2
    assert f_func(-2) == -2
    assert f_func(-1) == 2
    assert f_func(1) == -2
    assert f_func(0) == 0

    # Also verify via sympy exact symbolic substitution
    assert f_sympy.subs(x_sym, 2) == 2
    assert f_sympy.subs(x_sym, -2) == -2
    assert f_sympy.subs(x_sym, -1) == 2
    assert f_sympy.subs(x_sym, 1) == -2
    assert f_sympy.subs(x_sym, 0) == 0


def test_roots():
    """Verify roots of f(x) are exactly {0, sqrt(3), -sqrt(3)}."""
    roots = sp.solve(f_sympy, x_sym)
    expected_roots = {0, sp.sqrt(3), -sp.sqrt(3)}
    assert set(roots) == expected_roots
    # Also verify substitution gives exact zero
    for r in expected_roots:
        assert sp.simplify(f_sympy.subs(x_sym, r)) == 0


def test_odd_symmetry():
    """Verify f(-x) + f(x) simplifies to 0 (f is an odd function)."""
    f_neg_x = f_sympy.subs(x_sym, -x_sym)
    sum_expr = sp.simplify(f_neg_x + f_sympy)
    assert sum_expr == 0
    # Also verify f(-x) == -f(x)
    assert sp.simplify(f_neg_x - (-f_sympy)) == 0


def test_large_value_evaluations():
    """Verify end behaviour numbers: f(10) = 970, f(-10) = -970."""
    assert f_func(10) == 970
    assert f_func(-10) == -970
    assert f_sympy.subs(x_sym, 10) == 970
    assert f_sympy.subs(x_sym, -10) == -970


def test_horizontal_line_three_intersections():
    """Verify f(x) = 1 has exactly 3 real solutions (not one-to-one)."""
    eq = sp.Eq(f_sympy, 1)
    sols = sp.real_roots(f_sympy - 1)
    assert len(sols) == 3


def test_infinite_limits():
    """Verify limits as x -> +oo and x -> -oo are +oo and -oo."""
    lim_pos = sp.limit(f_sympy, x_sym, sp.oo)
    lim_neg = sp.limit(f_sympy, x_sym, -sp.oo)
    assert lim_pos == sp.oo
    assert lim_neg == -sp.oo


def test_turning_points_values():
    """Verify the local extremum values at x = -1 (max = 2) and x = 1 (min = -2)."""
    # First derivative zeroes without showing calculus on screen
    df = sp.diff(f_sympy, x_sym)
    crit_pts = sp.solve(df, x_sym)
    assert set(crit_pts) == {-1, 1}
    assert f_sympy.subs(x_sym, -1) == 2
    assert f_sympy.subs(x_sym, 1) == -2
