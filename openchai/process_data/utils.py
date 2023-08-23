from datasets import load_dataset

def get_raw_dataset(dataset_name, val_set_size=0.01, max_samples=-1):
    raw_datasets = load_dataset(dataset_name)
    max_samples = (
        min(max_samples, len(raw_datasets["train"]))
        if max_samples > 0
        else len(raw_datasets["train"])
    )
    if val_set_size > 0:
        if "validation" not in raw_datasets.keys():
            max_val = int(max_samples * val_set_size)
            raw_datasets["validation"] = load_dataset(
                dataset_name,
                split=f"train[:{max_val}]",
            )
            raw_datasets["train"] = load_dataset(
                dataset_name,
                split=f"train[{max_val}:{max_samples}]",
            )
        else:
            raw_datasets["train"] = raw_datasets["train"].select(range(max_samples))
    else:
        raw_datasets["train"] = load_dataset(
            dataset_name,
            split=f"train[:{max_samples}]",
        )
    return raw_datasets
