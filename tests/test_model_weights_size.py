import os

def test_model_weights_not_empty():
    path = "model.weights.h5"
    assert os.path.exists(path), f"{path} does not exist"
    size = os.path.getsize(path)
    assert size > 1000, f"{path} file is too small ({size} bytes)"
