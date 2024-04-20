import argparse

from recbole.quick_start import run_recbole

parser = argparse.ArgumentParser()
parser.add_argument("model", type=str)
parser.add_argument("dataset", type=str)
parser.add_argument("model_config", type=str)
parser.add_argument("dataset_config", type=str)
args = parser.parse_args()

results = run_recbole(
    model=args.model,
    dataset=args.dataset,
    config_file_list=[args.model_config, args.dataset_config],
)
