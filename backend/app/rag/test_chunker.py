from chunker import chunk_text

paragraph = """
Gradient descent is an optimization algorithm used to minimize a loss function.
During training, a neural network makes predictions and calculates the error.
Backpropagation then calculates gradients of the loss with respect to the model's
parameters. These gradients indicate how each parameter contributed to the error.
The optimizer uses those gradients to update the weights and biases. This process
repeats over many training examples until the model improves.
"""

text = paragraph * 20

chunks = chunk_text(text)

print(len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk.get_content())



