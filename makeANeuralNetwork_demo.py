from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed the random numbers generator, so it generate same numbers
        # every time the program runs.
        random.seed(1)

        # We model a single neuron, with 3 input connection, and 1 output
        # We assign random weight to a 3 x 1 matrix, with value
        # in range -1 to 1 and mean 0.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

        # the Sigmoid function, which describes an s shaped curved
        # we pass the weighted sum of the input through this function
        # normalise them between 0 and 1.
        def _sigmoid(self, x):
            return 1 / (1 + exp(-x))

        #the derivative of the Sigmoid function
        # this is the gradient of Sigmoid curve
        # It indicates how confident we are about exist weight
        def _sigmoid_derivative(self, x):
            return x * (1 - x)

        # we train the neural network through a process trail and error
        # Adjusting the synaptic weights each time.
        def train(self, training_set_inputs, tranining_set_outputs, number_of_training_iterations):
            for iteration in xrange(number_of_training_iterations):
                out.think(training_set_inputs)

                # Calculate the error
                # and predicted output
                error = training_set_outputs - output

                # Multiply the error by the input and again by gradient Sigmoid
                # this mean less confident weight are adjusted.
                # This mean input, which are zero
                adjustment = dot(training_set_inputs.T, error * self._sigmoid_derivative(output))

                #Adjust the weight
                self.synaptic_weights += adjustments

        # the neural network think
        def think(self, inputs):
            # pass the input to neural network(our signal neuro)
            return self._sigmoid(dot(input, self.synaptic_weights))

if __name__ == "__main__":
    #Intialise a single neuron NeuralNetwork.
    neural_network = NeuralNetwork()
    print "Random starting synaptic weight:"
    print neural_network.synaptic_weights

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print "New synaptic weights after training: "
    print neural_network.synaptic_weights

    # Test the neural network with a new situation.
    print "Considering new situation [1, 0, 0] -> ?: "
    print neural_network.think(array([1, 0, 0]))
