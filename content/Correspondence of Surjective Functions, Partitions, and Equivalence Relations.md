---
title: "Correspondence of Surjective Functions, Partitions, and Equivalence Relations"
---

# Statement
Let $X$ be a [[Set]]. Then the following [[Class]]es can be naturally transformed from one to the other:
1. [[Partition]]s of $X$.
2. [[Equivalence Relation]]s on $X$
3. Let $\mathcal{G}$ be the [[Class]] of all [[Surjection]]s from $X$ to some [[Set]] $Y$. Idenitfy [[Surjection]]s if there exists a [[Bijection]] between their [[Function Image]]s of $X$ and call this class $\mathcal{G}'$. Then $\mathcal{G}'$ is in one-to-one correspondence with the (1) and (2).

Furthermore, composing any of these transformations recovers the direct one. That is, these transformations [[Commuting Transforms|Commute]].
# Proof
[[TODO]] ~~redo this to apply the transformation from 1 class to the other and back (or in a loop). Show the transformation is well-defined (easy) and that two different input classes do not map to same output class.~~  I think I will wait on this until I learn more [[Category Theory]]. Basically (and it's not hard to see), there is a natural way to get from any of these to the other. We can create the following [[Category|categories]]:
1. [[Partition]]: [[Object]]s are elements of $X$ and [[Morphism]]s are [[Isomorphism]]s between elements in the same [[Partition]].
2. [[Equivalence Relation]]: [[Object]]s are elements of $X$ and [[Morphism]]s are [[Isomorphism]]s between elements that are equivalent.
3. [[Surjection]] from $X$: [[Object]]s are elements of $X$ and [[Morphism]]s are [[Isomorphism]]s between elements that map to same element in the [[Codomain]].

It's not hard to see that these three [[Category]]s have the same underlying structure. For example, if we change a given [[Category]] from one of a [[Partition]] to one of an [[Equivalence Relation]] then the [[Object]]s and [[Morphism]]s do not change. $\square$

((1) $\Rightarrow$ (3)) Let $\mathcal{S}$ be a [[Partition]] of $X$. Let $g: X \to \mathcal{S}$ be defined so that $g(x) = A$ s.t. $x \in A$. This [[Function]] is [[Well-Defined]] since $\exists ! A \in \mathcal{S}$ s.t. $x \in A$ by definition of a [[Partition]]. This function is a [[Surjection]] because for every $A \in \mathcal{S}$ $\exists x \in A$ so $g(x) = A$. 

((3) $\Rightarrow$ (1)) Let $g: X \to Y$ be a [[Surjection]]. Let $\mathcal{S} = \{g^{-1}(\{y\}) : y \in Y\}$. We claim $\mathcal{S}$ is a [[Partition]] of $X$. We check the 3 criteria:
1. Since $g$ is a [[Surjection]], we know that every $g^{-1}(\{y\}) \neq \emptyset$.
2. By properties of [[Function Preimage]]s, we know if $A \subset Y$ and $B \subset Y$ are [[Disjoint Sets]] then $g^{-1}(A) \cap g^{-1}(B) = \emptyset$. So for $y, z \in Y$, either
	1. $y \neq z$: then $\{y\} \cap \{z\} = \emptyset$ and $g^{-1}(\{y\}) \cap g^{-1}(\{z\}) = \emptyset$.
	2. $y = z$: then $g^{-1}(\{y\}) = g^{-1}(\{z\})$
3. $X = g^{-1}(Y) = g^{-1}(\bigcup\limits_{y \in Y} \{y\}) = \bigcup\limits_{y \in Y} g^{-1}(\{y\})$

We show that each object from one [[Class]] corresponds to a unique object in the other class.

((1) $\Rightarrow$ (2)) Let $\mathcal{S}$ be a [[Partition]] of $X$. Define $\sim$ so that for $x, y \in X$, $x \sim y$ [[If and Only If]] $\exists A \in \mathcal{S}$ s.t. $x,y \in A$. We claim $\sim$ is an [[Equivalence Relation]]. We check the 3 criteria:
1. **Reflexitivity**: Let $x \in X$. Since $\mathcal{S}$ is a [[Partition]], we know there exists $A \in \mathcal{S}$ so that $x \in A$. Then, since $x,x \in A$ we have that $x \sim x$ and $\sim$ is reflexive.
2. **Symmetry**: Let $x, y \in X$ and suppose $x \sim y$. Then we know there exists $A \in \mathcal{S}$ so that $x, y \in A$. Then $y, x \in A$ and $y \sim x$.
3. **Transitivity**: Let $x,y,z \in X$ and suppose $x \sim y$ and $y \sim z$. Then we know there exists $A \in \mathcal{S}$ so that $x,y \in A$ and we know there exists $B \in \mathcal{S}$ so that $y, z \in B$. But since $\mathcal{S}$ is a [[Partition]], if $A \neq B$, we must have that $A \cap B = \emptyset$. Since $A \cap B \supset \{y\}$ we must have that $A = B$. Thus, $x, z \in A$ and $x \sim z$.

Suppose another such [[Equivalence Relation]] relation existed and call it $\sim'$. Then we have that $x \sim y$ [[If and Only If]] there exists $A \in \mathcal{S}$ so that $x, y \in A$ [[If and Only If]] $x \sim' y$. Therefore $\sim = \sim'$.

((2) $\Rightarrow$ (1)) Let $\sim$ be an [[Equivalence Relation]] on $X$. Define $\forall x \in X$, denote $A_{x} = \{y \in X : x \sim y\}$. Then let $\mathcal{S} = \{A_{x} \subset \mathcal{P}(X) : x \in X\}$. We claim that $\mathcal{S}$ is a [[Partition]] of $X$. We check the 3 criteria:
1. Let $A \in \mathcal{S}$. By construction of $\mathcal{S}$, we know there exists $x \in X$ so that $A = A_{x}$. Since $\sim$ is an [[Equivalence Relation]], we know $x \sim x$. Thus $x \in A_{x} = A$ and $A \neq \emptyset$. Thus, $\emptyset \not\in \mathcal{S}$.
2. Suppose $A, B \in \mathcal{S}$. Suppose $A \cap B \neq \emptyset$ . Then there exists $y \in A, B$. We know by construction of $\mathcal{S}$ that there exists $x, z \in X$ so that $A = A_{x}$ and $B = A_{z}$. Now let $a \in A$. We get the following chain of equivalences (after adjusting appropriately using symmetry of $\sim$):
	$$a \sim x \sim y \sim z$$
	Transitivity and symmetry gives us that $z \sim a$ so $a \in B$. A similar argument shows that if $b \in B$ then $b \in A$ as well. Thus $B = A$.
3. Consider $\bigcup\limits_{A_{x} \in \mathcal{S}} A_{x}$. Since $\forall x \in X$ there exists $A_{x} \in \mathcal{S}$ so that $x \in A_{x}$, we have that 
	$$\bigcup\limits_{A_{x} \in \mathcal{S}} A_{x} \supset X$$
	On the other hand, since $\mathcal{S} \subset \mathcal{P}(X)$, we have the opposite subset relation showing us
	$$\bigcup\limits_{A_{x} \in \mathcal{S}} A_{x} = X$$
Now suppose $\mathcal{S}'$ 

((1) $\Rightarrow$ (3)) Let $\mathcal{S}$ be a [[Partition]] of $X$. Construct a part