from libsonata import NodeStorage, EdgeStorage
from pathlib import Path

DATA_DIR = Path(__file__).parent.absolute() / "files"


def test_nodes_file():
    storage = NodeStorage(str(DATA_DIR/"nodes.h5"))
    assert list(storage.population_names)[0] == "default"
    pop = storage.open_population("default")
    assert pop.size == 7687


def test_edges_file():
    storage = EdgeStorage(str(DATA_DIR/"edges.h5"))
    assert list(storage.population_names)[0] == "default"
    pop = storage.open_population("default")
    assert pop.size == 507693
