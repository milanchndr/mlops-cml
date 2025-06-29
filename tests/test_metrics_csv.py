import pandas as pd

def test_metrics_format():
        df = pd.read_csv("metrics.csv")
            assert "accuracy" in df.columns or "val_accuracy" in df.columns
                assert df.shape[0] > 0

