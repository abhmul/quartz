---
tags:
- GraphExclude
title: House Rules and Conventions
---

 

I've been working on this for a while and feel like I have to come up with the same conventions everytime I write because I'm not sure what the prior convention was. So, I'm starting a page where I can keep track of conventions and rules as I write.

# *Definition* note structure
[[TODO]] - fill this in as I go
- [ ] What role does a definition fill?

# *Statement* note structure
Anything that needs to be proved is a *Statement*. It is similar to a "Proposition".

1. A *Statement* should specify the mathematical **result** in a mathematically precise statement. 
	1. Exceptions to the above rule are when the statement is a simple connection or extension of other *Statement*s and *Definition*s.
2. The *Statement* takes H1 (top heading) and *Proof*, *Remark*, or *Properties* takes H2 (first subheading).

# *Counterexample* note structure
A *Counterexample* is a note that provides some example to show a statement is false.

# *Definition*, *Statement*, or *Counterexample*
1. Use a *Statement* instead of a *Definition* if we are defining a concept with something that needs to be proven. 
	- See [[Discrete Topology]] for an example.

# *Proof* section structure
1. A *Proof* should express the result as a sequence of logical steps. It should be self-contained, and reference other necessary results and concepts through links.
	1. An exception is if the proof is a simple connection of other concepts.
2. If a proof complete and mathematically precise, it should end with a $\blacksquare$. If a proof is sketched, but not necessarily precise, it should end with a $\square$. If the proof is incomplete, it should be tagged with a [[TODO]].
3. All $\blacksquare$ or $\square$ ending a proof should occur *after* the period ending the last sentence.
4. Upon completion of a checkpoint (e.g. proving the [[Non-Degeneracy]] property of an [[Inner Product]]), the sentence should end with a $\checkmark$. The $\checkmark$ should occur *before* the period ending the sentence.
	1. some exceptions are occasionally necessary.
5. Upon reaching a [[Proof by Contradiction|contradiction]], a $\unicode{x21af}$ symbol should be used. Like the $\checkmark$, it should occur *before* the period ending the sentence. If not referenced in the proof, [[Proof by Contradiction]] should be referenced in *Other Outlinks*.

# *Properties* section structure
1. The *Properties* section of a note is meant to capture the **most important** properties, not necessarily all of them. The more exhaustive list can be found in the "backlinks" on the rightside panel.
2. If a property needs to be referenced more than a few times, it should get its own note.

# Incomplete or Unstarted notes
When I want to use a result I don't have yet, I can reference a note that doesn't exist. Obsidian will suggest this note in autocomplete. It is best practice to always complete a result whenever I create it, but that is not always feasible given limited time.

1. If the note has been started but is incomplete, I should add a [[TODO]], along with some checkboxes about what needs to get done.

# Referencing Style
1. If I reference a more specific object, I don't need to also reference the more general object (e.g. "[[Open]] set" instead of "[[Open]] [[Set]]", or [[Continuous Function]] instead of [[Continuous Function|continuous]] [[Function]]).
2. It's okay to not reference a concept if I've already referenced it somewhere else. However, there is not much harm in referencing it multiple times when it is used.

# *Other Outlinks* section
1. When done writing an article, go through and link any concepts used that are not already linked in the note.
2. It's okay if something is in the outlinks and is linked in the note. The goal of the *Other Outlinks* section is to create backlinks into those concepts used, as well as allow users to navigate to those concepts if they don't understand something.
3. *Other Outlinks* always takes H1 (top heading).
4. Some primitive concepts like [[Set]] don't need to be referenced on every page. The same goes for basic set operations ([[Set Union]], [[Set Intersection]], [[Complement]], [[Subset Relation]]).


# Use of MathJax

## Stylistic Conventions
1. Whenever a I denote another object $A$ with some symbol $a$, I should write $a := A$ or $A =: a$. The "$:$" always goes on the side of the new symbol being defined.

## Displaymath
1. If outside a bullet or enumerated list, all display math should go on its own line. Within a bullet or enumerated list, displaymath should be writting inline due so I can get the desired nesting.
2. If a sentence ends with displaymath, then the period should go inside the displaymath. This ensures the period is not on a different line.

# TODO tracking
1. The [[TODO]] page should not have any content. All TODOs should be written on the relevant page along with any of the following
	1. some directions about what needs to be done.
	2. A reference to an incomplete or unstarted note
	3. Some notes describing any thinking or progress I've made to resolving the TODO.
2. Each TODO should have associated checkboxes.
	- [ ] This is a checkbox.