from ingestion import ingest_note

note_text = """Neural networks are machine learning models made of layers of connected units. Each connection has a numerical weight, and those weights determine how strongly information moves through the network. When data enters the model, it passes through the input layer and then through one or more hidden layers. Each layer performs mathematical operations on the incoming values, usually multiplying them by weights, adding biases, and applying an activation function.

During training, the neural network tries to make predictions from the input data. Those predictions are compared with the correct answers using a loss function. The loss function measures how wrong the model's prediction is. A large loss means the prediction is far from the desired result, while a smaller loss means the model is performing better.

After the loss is calculated, the model needs to determine which weights were responsible for the error. Backpropagation is the process used to calculate this information. It works backward through the neural network and computes gradients for the weights and biases. A gradient describes how much the loss would change if a particular parameter changed slightly.

The gradients are then passed to an optimizer. The optimizer uses those gradients to decide how the model's weights should be updated. Gradient descent is one common optimization method. It adjusts parameters in the direction that reduces the loss. The learning rate controls how large each update is. If the learning rate is too large, training may become unstable. If it is too small, training may take a very long time.

This sequence of forward prediction, loss calculation, backpropagation, and parameter updating is repeated many times during training. A single pass through the full training dataset is often called an epoch. Neural networks usually require many epochs before their parameters become useful.

Matrix operations are heavily used inside neural networks because they allow many values to be processed at the same time. Instead of calculating every neuron separately, the model can represent activations, weights, and inputs as vectors and matrices. Matrix multiplication allows entire groups of calculations to be performed efficiently.

Activation functions are another important part of neural networks. Without activation functions, multiple layers would behave like a single linear transformation. Functions such as ReLU introduce nonlinearity, allowing the network to learn more complicated relationships in the data. ReLU commonly returns zero for negative inputs and returns the original value for positive inputs.

Once training is complete, the model can be used for inference. During inference, the model receives new input and performs only the forward computations necessary to produce an output. Backpropagation and gradient descent are not normally used during inference because the model's parameters are no longer being updated.

Embedding models are a different type of neural network application. An embedding model converts text or other data into numerical vectors. These vectors represent patterns in meaning so that related pieces of text tend to have vectors that are closer together. Vector databases can store these embeddings and perform similarity searches to find related information.

In a retrieval augmented generation system, documents are often divided into smaller chunks before embeddings are generated. Chunking is important because a long document may discuss many unrelated ideas. Creating one embedding for the entire document would mix those ideas together. By splitting the document into smaller sections, each embedding can represent a more focused piece of information.

Chunk overlap can also be used during this process. If one chunk ends in the middle of an explanation and the next chunk begins afterward, some context could be lost. Overlap allows a small amount of text from the end of one chunk to appear again at the beginning of the next chunk. This helps preserve continuity between neighboring chunks.

After chunks are created, each chunk can be sent to an embedding model. The resulting vector can then be stored in a vector database along with the original chunk text and metadata. Metadata can include information such as the source document, note identifier, chunk index, and the date the information was added.

When a user asks a question, the question can also be converted into an embedding. The vector database compares the query embedding with the stored chunk embeddings and returns the closest matches. Those retrieved chunks can then be supplied to a language model as context so that the language model can answer using the user's stored knowledge."""

ingest_note("data_220_week1", note_text)
