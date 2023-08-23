import os
import openchai
import subprocess
import argparse
from pathlib import Path


def cli():
    parser = argparse.ArgumentParser(description="OpenChai -  CLI")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Chai commands")

    train_parser = subparsers.add_parser("train", help="Training ArgumentParser")
    train_parser.add_argument("--config_path", type=str, required=True, help="Path to the input directory")

    args = parser.parse_args()

    if args.command == "train":
        launch_training(Path(args.config_path))

def launch_training(config_path: Path):
    print(f"Setup training with config file: {config_path}")
    root_dir = Path(os.path.dirname(openchai.__file__))
    execution_path = root_dir / "scripts" / "finetune.py"
    command = f"accelerate launch {execution_path} {config_path}"
    subprocess.check_output(command, shell=True)
