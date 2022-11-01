Dates: [[2022-07-21]]

# Conversation with Ben
I was talking to [[Ben Girardeau]] about my ideas for abstract memory. Below is the conversation log:

**You sent**: If I've organized my understanding of the world in some high dimensional euclidean space
**You sent**: I don't need to store that understanding in mempry
**You sent**: I just need to be able to access it
**You sent**: As in if I have a function that can take as input a query and output an answer
**You sent**: Then the function only needs to be able to retrieve the answer from the "understanding space"
**You sent**: It does not need to "store" that understanding space
**You sent**: I'm thinking of how an algorithm can solve complicated problems without actually "storing" a huge memory of examples
### Mon 11:15 PM
**Ben**: huh interesting, like I can compute the value of f for any x without having to have actually stored every possible value?
### Mon 11:47 PM
**You sent**: Yea, like if you could learn algorithms that capture the inherent organization, say in images, you don't need to store every pattern that can occur in an image
### Tue 2:19 AM
**Ben**: that sounds really cool
### Tue 7:45 PM
**You sent**: Maybe a good analogy is manipulating the cursor on a computer
**You sent**: You don't need to have a full storage of the computer to manipulate the cursor and accomplish things
**You sent**: Likewise, you could have an abstract space with a point that is your "cursor".
**You sent**: Using the "cursor" I could go find information that I have not actually stored
**You sent**: Maybe you can view memory in this way too
**You sent**: Suppose I've got some abstract space: 1. A query Q 2. An efficient fetching function f that takes as input the query and returns a point in the space that corresponds to the memory
**You sent**: When "storing" a memory, I instead modify my fetching function so when I query for the memory I want to store, the fetching function returns the memory.
**You sent**: Forgetting would amount to passing in an old query that was designed for an older version of the fetching function, and getting back something that doesn't make sense
**You sent**: Computer memory is a special instance of this. The query is an address and the fetching function is the retrieval of the bit at that address.
**You sent**: The fetching function is static in computers so long as the data at that address doesn't change
### Wed 11:16 PM
**Ben**: that makes sense I think
Ben
the hard part (obviously) seems like coming up with and modifying this function
**You sent**: It's very abstract
**Ben**: I guess you also have some notion of function "version" to understand if your query will still work
**You sent**: You could say gradient descent on neural networks is a way of modifying this function, and the fetcher function is the network
**You sent**: This is what it means to say the network "remembers" it's training samples
**Ben**: is this similar to what neural networks are doing then?
**You sent**: I think this is just a framework for analyzing it
**You sent**: Not sure if you could say this is what it is "doing"
**You replied to yourself**:
> *Original message*: Not sure if you could say this is what it is "doing"

That's more about interpretation
**You sent**: *up to interpretation
**Ben**: so more interpreting the output than interpreting the process of getting there?
**You sent**: I meant that describing what the network is "doing" is a bit subjective
**You sent**: And you could explain how the network got its output in terms of memory or in terms of the particular transforms applied by the network
**Ben**: ah ok makes sense
**You sent**: What if you had a function that took as input: 1. A query 2. An attention "cursor" and output an "update" (e.g. a vector) to the cursor. Then you could "think" by updating your cursor n times
**You sent**: The next cursor is the previous cursor + update

# [[Information Theory of Deep Learning]]

I have been thinking about how to make the [[Information Theory of Deep Learning]] recently. I last thought about this in [[Thinking about the information theory of NNs]]. We want to capture the idea that at initialization, the network does not encode anything useful, but by the end of training, it encodes structure relating to the [[Classification Problem]]. What if we looked for this in the abstract memory space learned by the [[Neural Network]] as a result of training on its training data? In this model we have:
1. A query, $x \in \mathbb{R}^{n}$, that is the input sample
2. The fetcher [[Function]], $f: \mathbb{R}^{n} \to \mathbb{R}^{m}$ that is the neural network.

At initialization, $f$ is randomly initialized. $f$ [[Implicit Function|implicitly]] defines a [[Topological Manifold]] in $\mathbb{R}^{n \times m}$: $y - f(x) = 0$ for $y \in \mathbb{R}^{m}$.... this is not really going anywhere. I do need to read more regularly. I do want to get to answers about how memory can work. 

It may be worthwhile to investigate [[Hopfield Network]]s and try to understand it through my model of memory. There is work on [[Modern Hopfield Network]]s