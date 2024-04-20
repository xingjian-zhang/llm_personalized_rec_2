.PHONY: scripts

scripts:
	mkdir -p scripts
	python generate_scripts.py

clean:
	rm -rf scripts
	rm -rf log
	rm -rf log_tensorboard
	rm -rf slurm_logs

sbatch: scripts
	for script in scripts/*.sh; do \
		sbatch $$script; \
	done
