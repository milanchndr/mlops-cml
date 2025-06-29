import pandas as pd

def test_metrics_csv():
    df = pd.read_csv("metrics.csv")

    # Check required columns exist
    required_columns = {"accuracy", "val_accuracy", "loss", "val_loss"}
    assert required_columns.issubset(df.columns), "Missing expected columns in metrics.csv"

    # Check that accuracy is increasing
    assert df["accuracy"].iloc[-1] >= df["accuracy"].iloc[0], "Accuracy did not improve over epochs"

    # Check that validation accuracy is acceptable
    assert df["val_accuracy"].max() >= 0.80, "Validation accuracy did not reach 80% threshold"
