import aifeynman

# Download example data
aifeynman.get_demos("example_data")

# Run AI Feynman on the first example
# Parameters:
# - Directory containing the data
# - Filename of the data
# - Time limit for brute force (60 seconds)
# - Operations file to use
# - Degree of polynomial fit
# - Number of neural network epochs
result = aifeynman.run_aifeynman(
    "./example_data/",
    "example1.txt",
    60,
    "14ops.txt",
    polyfit_deg=3,
    NN_epochs=500
)

print("Results:", result) 