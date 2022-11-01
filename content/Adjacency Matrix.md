---
title: "Adjacency Matrix"
---

# Definition 1
Suppose $G = (V,E)$ is a [[Directed Graph]]. Then the [[Adjacency Matrix]] of $G$, denoted $\text{Adj}(G) \in \{0, 1\}^{|V| \times |V|}$ is the [[Matrix]] with entries

$$\text{Adj}(G)_{vw} = \begin{cases}1 & \text{if }(v, w) \in E\\ 0 & \text{otherwise}\end{cases}$$
# Definition 2
Suppose $G = (V, E)$ is an [[Undirected Graph]]. Let $G'$ be the [[Represent an Undirected Graph as a Directed Graph|Directed Graph representation]] of $G$. Then the [[Adjacency Matrix]] of $G$, denoted $\text{Adj}(G) \in \{0, 1\}^{|V| \times |V|}$ is $\text{Adj}(G')$.

## Properties
1. [[Adjacency Matrix of an Undirected Graph is Symmetric]]
2. [[Adjacency Matrix of an Undirected Graph has an all 0 main diagonal]]

# Other Outlinks
