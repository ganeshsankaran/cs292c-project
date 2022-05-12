# Experiment 1

python3 graph.py -p ../results/csv/experiment1_results_consolidated.csv \
    -x "human time" -y "time (naive)" \
    -xl "Human Time (s)" -yl "Z3 Time (s)" \
    -t "Z3 Time vs Human Time with Naive Symbolic Compilation"

python3 graph.py -p ../results/csv/experiment1_results_consolidated.csv \
    -x "human time" -y "time" \
    -xl "Human Time (s)" -yl "Z3 Time (s)" \
    -t "Z3 Time vs Human Time with Compact Symbolic Compilation"

python3 graph.py -p ../results/csv/experiment1_results_consolidated.csv \
    -x "human time" -y "rlimit count (naive)" \
    -xl "Human Time (s)" -yl "Resource Usage" \
    -t "Resource Usage vs Human Time with Naive Symbolic Compilation"

python3 graph.py -p ../results/csv/experiment1_results_consolidated.csv \
    -x "human time" -y "rlimit count" \
    -xl "Human Challenge Time (s)" -yl "Resource Usage" \
    -t "Resource Usage vs Human Time with Compact Symbolic Compilation"

python3 graph.py -p ../results/csv/experiment1_results_consolidated.csv \
    -x "human time" -y "model count" \
    -xl "Human Challenge Time (s)" -yl "Model Count"

# Experiment 2

python3 graph.py -p ../results/csv/experiment2_results.csv \
    -x "num_holes" -y "rlimit count" \
    -xl "# Holes" -yl "Resource Usage"

python3 graph.py -p ../results/csv/experiment2_results.csv \
    -x "num_holes" -y "time" \
    -xl "# Holes" -yl "Time (s)"

python3 graph.py -p ../results/csv/experiment2_results.csv \
    -x "num_holes" -y "memory" \
    -xl "# Holes" -yl "Memory Usage (MB)"

# Experiment 3

python3 graph.py -p ../results/csv/experiment3_results.csv \
    -x "size (nxn)" -y "rlimit count" \
    -xl "Size" -yl "Resource Usage"

python3 graph.py -p ../results/csv/experiment3_results.csv \
    -x "size (nxn)" -y "time" \
    -xl "Size" -yl "Time (s)"

python3 graph.py -p ../results/csv/experiment3_results.csv \
    -x "size (nxn)" -y "memory" \
    -xl "Size" -yl "Memory Usage (MB)"