from brainrender import Scene
from brainrender.actors import Points
import numpy as np

import pytest


def test_points_working():
    s = Scene(title="BR")

    act = Points(np.load("tests/files/random_cells.npy"))
    act2 = Points("tests/files/random_cells.npy", colors="k")
    act3 = Points("tests/files/random_cells.npy", name="test")
    assert act3.name == "test"

    s.add(act)
    s.add(act2)


def test_points_error():
    with pytest.raises(FileExistsError):
        Points("tests/files/testsfsdfs.npy", colors="k")
    with pytest.raises(NotImplementedError):
        Points("tests/files/random_cells.h5", colors="k")
