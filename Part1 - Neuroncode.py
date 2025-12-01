#Here we will see a very simple implementation of a neuron (from matrix) to initially understand and take it forward
#Please refer to the each part's Notes.md for understanding the code and the neuron implementations

inputs = [1.2, 5.1, 2.1] 
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias # these are the final added output from that neuron 
print(output)

