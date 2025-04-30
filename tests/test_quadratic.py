import pytest
import numpy as np
from polysolve.polysolve import quadratic

def test_quadratic():
    """Tests that quadratic finds the root for a known problem."""
    params = [3., 0., -1.]
    roots = quadratic(*params)
    assert all(np.isclose(np.polyval(params, root), 0.) for root in roots)

@pytest.mark.parametrize('params, expected', [(['feet', 'eyeball', 'shoes'], TypeError)])
def test_string_input_quadratic(params, expected):
    """Check that input of strings fails"""
    # params = ['feet', 'eyeball', 'shoes']
    with pytest.raises(expected) as e:
        quadratic(*params)
