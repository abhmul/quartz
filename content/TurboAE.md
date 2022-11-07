---

title: "TurboAE"
tags:
- gitignore

---
[[TurboAE]] is a [[Deep Learning]] [[Machine Learning Model]] implemented and published by [[Yihan Jiang]]. The model attempts to solve the [[Channel Coding]] problem by searching for a [[Neural Network]] [[Coding Encoder]] and [[Coding Decoder]] that mimic the architecture of a [[Turbo Code]].

- [Code](https://github.com/yihanjiang/turboae)
- Paper:
	- [Drive](https://drive.google.com/file/d/1QdbEEwbvubcGWyx4x3Fm9husfZLnWYtd/view?usp=sharing)
	- [Arxiv](https://arxiv.org/abs/1911.03038)

# Architecture Details
## Encoder
The TurboAE encoder is made up of 3 encoders with the following architecture

**Input**: *Batch* x *Block Length* x 1; *Block Length* is usually 100.
1. Window 5, 100 Filter [[Convolutional Layer|Conv]] w/ [[Exponential Linear Unit|ELU]] w/ [[Zero Padding]]-> Batch x Block Length x 100
2. Window 5, 100 Filter [[Convolutional Layer|Conv]] w/ [[Exponential Linear Unit|ELU]] w/ [[Zero Padding]] -> Batch x Block Length x 100
3. TimeDistributed 1 Unit [[Fully Connected Layer|FC]] -> Batch x Block Length x 1
4. Power Constraint
	1. We subtract normalize uniformly all outputs with
		1. [[Mean]]: -0.0215
		2. [[Standard Deviation]]: 0.5114
	2. For [[TurboAE-Binary]], we quantize to  $\pm 1$ using the [[Sign Function]].

**Parameters per encoder**: 50,801
**Total Parameters**: 152,403
> Counts were measured in [cell 7 of this notebook](https://github.com/tripods-xai/turbo-codes/blob/42cb50d49f86952f322ac265d705327702967e53/notebooks/torch_to_tf_conversion.ipynb). These counts match manual calculations:
> $(5*1*100 + 100) + (5*100*100 + 100) + (100 + 1) = 50,801$

## Decoder
[[TODO]]

**Total Parameters**: 2,453,656
> Counts were measured in [cell 6 of this notebook](https://github.com/tripods-xai/turbo-codes/blob/42cb50d49f86952f322ac265d705327702967e53/notebooks/torch_to_tf_conversion.ipynb).

