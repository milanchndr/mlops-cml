import os
def test_model_weights_file_exists():
    assert os.path.exists("model.weights.h5"), "Model weight not found"

