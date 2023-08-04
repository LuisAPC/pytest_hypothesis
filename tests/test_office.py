from typing import Callable
import pytest
from hypothesis import given
from hypothesis.strategies import integers, composite, SearchStrategy
from ..office import Employee, fire_random_employee, generate_random_team


@composite
def teams(
    draw: Callable[[SearchStrategy[int]], int], min_value=1, max_value=20
):
    # draw function allows us to draw values from another strategy
    rand_val = draw(integers(min_value=1, max_value=20))
    return generate_random_team(rand_val)


@given(integers(max_value=0))
def test_negative_team_size(team_size):
    with pytest.raises(ValueError):
        generate_random_team(team_size)


@given(integers(min_value=1, max_value=20))
def test_team_size(team_size: int):
    assert len(generate_random_team(team_size)) == team_size


# instead of using @given(integers(conditions)) we use our teams strategy
@given(teams())
def test_team_has_CEO(team: list[Employee]):
    assert Employee.CEO in team


@given(integers(min_value=1, max_value=20))
def test_fire_employee(team_size: int):
    team = generate_random_team(team_size)
    team_copy = team.copy()
    fire_random_employee(team_copy)
    assert len(team_copy) == len(team) - 1
