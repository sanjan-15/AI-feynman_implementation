from aifeynman import run_aifeynman

run_aifeynman("../example_data/", "coulomb_force.txt", 20,
              "14ops.txt", polyfit_deg=3, NN_epochs=100)