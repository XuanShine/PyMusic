
import pytest

from proba_music import *

@pytest.fixture
def list_test():
    return ([1, 2, 3, 4],
            [1, 2, 2, 3, 3, 3],
            [1, 2, 3, 4, 1, 2, 3, 4],
            [2, 4, 2, 5, 2, 5, 7, 7, 1, 1])

def test_occurrence(list_test):
    assert occurrence(list_test[0]) == {1: 1, 2: 1, 3: 1, 4: 1}
    assert occurrence(list_test[1]) == {1: 1, 2: 2, 3: 3}
    assert occurrence(list_test[2]) == {1: 2, 2: 2, 3: 2, 4: 2}
    assert occurrence(list_test[3]) == {1: 2, 2: 3, 4: 1, 5: 2, 7: 2}

def test_n_occurrence(list_test):
    assert n_occurrence(list_test[0], 1) == {(1,): {2: 1}, (2,): {3: 1},
       (3,): {4: 1}}
    assert n_occurrence(list_test[1], 1) == {(1,): {2: 1}, (2,): {2: 1, 3: 1},
       (3,): {3: 2}}
    assert n_occurrence(list_test[2], 1) == {(1,): {2: 2}, (2,): {3: 2},
       (3,): {4: 2}, (4,): {1: 1}}
    assert n_occurrence(list_test[3], 1) == {(1,): {1: 1}, (2,): {4: 1, 5: 2},
       (4,): {2: 1}, (5,): {2: 1, 7: 1}, (7,): {1: 1, 7: 1}}
    assert n_occurrence(list_test[0], 2) == {(1,2): {3: 1}, (2,3): {4: 1}}
    assert n_occurrence(list_test[1], 2) == {(1,2): {2: 1}, (2,2): {3: 1},
       (2,3): {3: 1}, (3,3): {3: 1}}
    assert n_occurrence(list_test[2], 2) == {(1,2): {3: 2}, (2,3): {4: 2},
       (3,4): {1: 1}, (4, 1): {2: 1}}
    assert n_occurrence(list_test[3], 2) == {(2, 4): {2: 1},
       (2, 5): {2: 1, 7: 1}, (4, 2): {5: 1}, (5, 2): {5: 1}, (5, 7): {7: 1},
       (7, 1): {1: 1}, (7, 7): {1: 1}}
    assert n_occurrence(list_test[0], 3) == {(1,2,3): {4: 1}}
    assert n_occurrence(list_test[1], 3) == {(1, 2, 2): {3: 1},
       (2, 2, 3): {3: 1}, (2, 3, 3): {3: 1}}
    assert n_occurrence(list_test[2], 3) == {(1,2,3):{4:2}, (2,3,4):{1:1},
       (3,4,1):{2:1}, (4,1,2):{3:1}}
    assert n_occurrence(list_test[3], 3) == {(2, 4, 2): {5: 1},
       (2, 5, 2): {5: 1}, (2, 5, 7): {7: 1}, (4, 2, 5): {2: 1},
       (5, 2, 5): {7: 1}, (5, 7, 7): {1: 1}, (7, 7, 1): {1: 1}}


@pytest.fixture
def dict_test():
    return ({1: 2, 2: 3, 4: 1, 5: 2, 7: 2},
            {(1,): {1: 1}, (2,): {4: 1, 5: 2}, (4,): {2: 1}, (5,): {2:1, 7:1},
               (7,): {1: 1, 7: 1}},
            {(2, 4, 2): {5: 1}, (2, 5, 2): {5: 1}, (2, 5, 7): {7: 1},
               (4, 2, 5): {2: 1}, (5, 2, 5): {7: 1}, (5, 7, 7): {1: 1},
               (7, 7, 1): {1: 1}})

def test_proba_dict(dict_test):
    assert proba_dict(dict_test[1]) == {(1,): (1, {1: 1}),
                                        (2,): (3, {4: 1, 5: 2}),
                                        (4,): (1, {2: 1}),
                                        (5,): (2, {2: 1, 7: 1}),
                                        (7,): (2, {1: 1, 7: 1})}

def test_calcul_occurrence_with_proba(list_test):
    assert calcul_occurrence(list_test[3]) == \
        [(10, {1: 2, 2: 3, 4: 1, 5: 2, 7: 2}),
         {(1,): (1, {1: 1}), (2,): (3, {4: 1, 5: 2}), (4,): (1, {2: 1}),
          (5,): (2, {2: 1, 7: 1}), (7,): (2, {1: 1, 7: 1})},
         {(2, 4): (1, {2: 1}), (2, 5): (2, {2: 1, 7: 1}), (5, 2): (1, {5: 1}),
          (5, 7): (1, {7: 1}), (7, 1): (1, {1: 1}), (7, 7): (1, {1: 1}),
          (4, 2): (1, {5: 1})},
         {(2, 4, 2): (1, {5: 1}), (2, 5, 2): (1, {5: 1}),
          (2, 5, 7): (1, {7: 1}), (4, 2, 5): (1, {2: 1}),
          (5, 2, 5): (1, {7: 1}), (5, 7, 7): (1, {1: 1}),
          (7, 7, 1): (1, {1: 1})},
         {(2, 4, 2, 5): (1, {2: 1}), (2, 5, 2, 5): (1, {7: 1}),
          (2, 5, 7, 7): (1, {1: 1}), (4, 2, 5, 2): (1, {5: 1}),
          (5, 2, 5, 7): (1, {7: 1}), (5, 7, 7, 1): (1, {1: 1})},
         {(2, 4, 2, 5, 2): (1, {5: 1}), (2, 5, 2, 5, 7): (1, {7: 1}),
          (2, 5, 7, 7, 1): (1, {1: 1}), (4, 2, 5, 2, 5): (1, {7: 1}),
          (5, 2, 5, 7, 7): (1, {1: 1})},
         {(2, 4, 2, 5, 2, 5): (1, {7: 1}), (2, 5, 2, 5, 7, 7): (1, {1: 1}),
          (4, 2, 5, 2, 5, 7): (1, {7: 1}), (5, 2, 5, 7, 7, 1): (1, {1: 1})},
         {(2, 4, 2, 5, 2, 5, 7): (1, {7: 1}),
          (2, 5, 2, 5, 7, 7, 1): (1, {1: 1}),
          (4, 2, 5, 2, 5, 7, 7): (1, {1: 1})},
         {(2, 4, 2, 5, 2, 5, 7, 7): (1, {1: 1}),
          (4, 2, 5, 2, 5, 7, 7, 1): (1, {1: 1})},
         {(2, 4, 2, 5, 2, 5, 7, 7, 1): (1, {1: 1})}]

# 2014/04/03 4 tests passed
