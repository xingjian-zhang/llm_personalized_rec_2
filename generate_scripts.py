import os

BASE_SCRIPT = r"""#!/bin/bash
#SBATCH --job-name=llm4rec
#SBATCH --mail-user=jimmyzxj@umich.edu
#SBATCH --mail-type=END,FAIL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4gb
#SBATCH --gres=gpu:1
#SBATCH --time=300:00
#SBATCH --account=qmei3
#SBATCH --partition=gpu
#SBATCH --output=/home/jimmyzxj/Course/eecs598_llm/llm_personalized_rec_2/slurm_logs/%x-%j.log

cd /home/jimmyzxj/Course/eecs598_llm/llm_personalized_rec_2/
"""

PYTHON_ARGS = r"""/home/jimmyzxj/miniconda3/envs/python38_gpu/bin/python3.8 baseline.py \
    {model_name} \
    {dataset_name} \
    {model_config} \
    {dataset_config}"""

models = os.listdir("configs/models/")
datasets = os.listdir("configs/datasets/")

for model in models:
    for dataset in datasets:
        model_name = model.split(".")[0]
        dataset_name = dataset.split(".")[0]
        model_config = os.path.join("configs/models", model)
        dataset_config = os.path.join("configs/datasets", dataset)
        script = BASE_SCRIPT + "\n" + PYTHON_ARGS.format(
            model_name=model_name,
            dataset_name=dataset_name,
            model_config=model_config,
            dataset_config=dataset_config)
        with open(f"scripts/{model_name}_{dataset_name}.sh", "w") as f:
            f.write(script)
