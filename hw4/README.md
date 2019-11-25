# Question 1: Clearly state what are the parameters associated with the HMM. Under the maximum likelihood estimation (MLE), what would be the values for the optimal model parameters? Clearly show how each parameter is estimated exactly. (10 points)

## 1.1 Parameters associated with MLE

The HMM is defined by a tuple $<T, O, \theta>$

- The parameter that we are interested in is $\theta$ which comprises of 2 very important parameters 
  - Transition probability $a_{u, v}$
  - Emission probability $b_{u}(o)$

## 1.2 Values for the optimal model parameters

<u>**Transitions probability calculations $a_{u, v}$**</u>

Table of counts for the transitions $count(u, v)$

| u\v   | X    | Y    | Z    | STOP |
| ----- | ---- | ---- | ---- | ---- |
| START | 2    | 0    | 3    | 0    |
| X     | 0    | 3    | 2    | 1    |
| Y     | 1    | 0    | 1    | 4    |
| Z     | 3    | 3    | 0    | 0    |

Counting the total number of transitions 

- Inner transitions = 3 + 2 + 4 + 2 + 2 = 13
- Outer Transitions (Start and Stop) = 5(2) = 10
- Total transitions = 13 + 10 = 23

Count specific occurrences $count(u)$

| State | Count |
| ----- | ----- |
| Start | 5     |
| X     | 6     |
| Y     | 6     |
| Z     | 6     |

Estimates for transition probabilities $a_{u, v}$

- $a_{u, v} = \frac{count(u, v)}{count(u)}$ 

| u\v   | X           | Y         | Z           | STOP        |
| ----- | ----------- | --------- | ----------- | ----------- |
| START | 2/5 = 0.4   | 0/5 = 0   | 3/5 = 0.6   | 0/5 = 0     |
| X     | 0/6 = 0     | 3/6 = 0.5 | 2/6 = 0.333 | 1/6 = 0.166 |
| Y     | 1/6 = 0.166 | 0/6 = 0   | 1/6 = 0.166 | 4/6 = 0.667 |
| Z     | 3/6 = 0.5   | 3/6 = 0.5 | 0/6 = 0     | 0/6 = 0     |

<u>**Emission probability calculations $b_{u}(o)$**</u>

Table of counts for the transitions between state and output count(u→o)

| u\o  | a             | b             | c             |
| ---- | ------------- | ------------- | ------------- |
| X    | 0+1+0+0+0 = 1 | 2+0+0+1+0 = 3 | 0+0+1+0+1 = 2 |
| Y    | 0+1+0+1+0 = 2 | 0+0+0+0+0 = 0 | 1+0+2+0+1 = 4 |
| Z    | 1+0+0+0+0 = 1 | 0+0+2+0+0 = 2 | 0+1+0+1+1 = 3 |



Estimates for Emission probabilities $b_{u} (o)$

- $b_{u} (o)= \frac{count(u ->o)}{count(u)}$ 

| u\o  | a            | b            | c            |
| ---- | ------------ | ------------ | ------------ |
| X    | 1/6 = 0.166  | 3/6 = 0.5    | 2/6 = 0. 333 |
| Y    | 2/6 = 0. 333 | 0/6 = 0      | 4/6 = 0.667  |
| Z    | 1/6 = 0.166  | 2/6 = 0. 333 | 3/6 = 0.5    |



# Question 2. Now, consider during the evaluation phase, you are given the following new observation sequence. Using the parameters you just estimated from the data, find the most probable state sequence using the Viterbi algorithm discussed in class. Clearly present the steps that lead to your final answer. (10 points)

Observation sequence (b, b)

Diagram 

<img src="assets/01_qn2.PNG" style="zoom:50%;" />

<u>**Viterbi algorithm**</u> 

<u>Step 1: Initialization</u>

<img src="assets/03.PNG" style="zoom:50%;" />

Result of step 1

<img src="assets/04.PNG" style="zoom:50%;" />

<u>Step 2</u>

<img src="assets/05.PNG" style="zoom:50%;" />

**Step 2.1** 

Consider the first layer of nodes after the START, j=0, compute for each node v, 

$\pi(1, u)$ = $max_{v}\{\pi(j,v) \cdot b_{u}(x_{j+1}) \cdot a_{v,u}\}$ = $\pi(0,START) \cdot b_{u}(b) \cdot a_{v,START}$ since there is no need to maximize sine there is only the START node in the previous layer

| v    | $\pi(j,v) \cdot b_{u}(x_{j+1}) \cdot a_{v,u}$ |
| ---- | --------------------------------------------- |
| x    | 1 x 0.5 x 0.4 = 0.2                           |
| y    | 1 x 0 x 0 = 0                                 |
| z    | 1 x 1/3 x 0.6 = 0.2                           |

Updated weight diagram

<img src="assets/06.PNG" style="zoom:50%;" />

Step 2.2

Consider the first layer of nodes after the the layer j=1, compute for each node v, 

$\pi(2, u)$ = $max_{v}\{\pi(j,v) \cdot b_{u}(x_{j+1}) \cdot a_{v,u}\}$ = $max_{v}\{\pi(1,v) \cdot b_{u}(x_{b}) \cdot a_{v,u}\}$

| u    | v    | $\pi(1,v) \cdot b_{u}(x_{b}) \cdot a_{v,u}$ |
| ---- | ---- | ------------------------------------------- |
| X    | X    | 0.2 x  0.5 x 0 = 0                          |
| X    | Y    | 0 x 0.5 x 1/6 = 0                           |
| X    | Z    | 0.2 x  0.5 x 0.5 = 0.05                     |
| Y    | X    | 0.2 x 0 x 0.5 = 0                           |
| Y    | Y    | 0 x 0 x 0 = 0                               |
| Y    | Z    | 0.2 x 0 x 0.5 = 0                           |
| Z    | X    | 0.2 x 1/3 x 1/3 = 1/45                      |
| Z    | Y    | 0 x 1/6 x 1/3 = 0                           |
| Z    | Z    | 0.2 x 0 x 1/3 = 0                           |

From this table we can find the max

| u    | $max_{v}\{\pi(1,v) \cdot b_{u}(x_{b}) \cdot a_{v,u}\}$ |
| ---- | ------------------------------------------------------ |
| X    | 0.05                                                   |
| Y    | 0                                                      |
| Z    | 1/45                                                   |

Update the weights

<img src="assets/07.PNG" style="zoom:50%;" />

<u>Step 3</u>

![](assets/08.PNG)

Consider the layer of the STOP node which is j=3, compute for each node v, 

$\pi(3, STOP)$ = $max_{v}\{\pi(n,v) \cdot a_{v,u}\}$ = $max_{v}\{\pi(2,v) \cdot a_{v,STOP}\}$

| u    | v    | $\pi(2,v) \cdot a_{v,STOP}$ |
| ---- | ---- | --------------------------- |
| STOP | X    | 0.05 x 1/6 = 1/120          |
| STOP | Y    | 0 x 2/3 = 0                 |
| STOP | Z    | 1/45 x 0 = 0                |

Hence, taking the max we get 1/120 

Update the weights

<img src="assets/09.PNG" style="zoom:50%;" />

<u>**Step 4: Find sequences from the weights**</u>

<img src="assets/10.PNG" style="zoom:50%;" />

**Start from layer n=2**

$y_{n}^{*} = argmax_{v}\{\pi(n,v)\cdot a_{v,STOP}\}$ = $argmax_{v}\{\pi(2,v)\cdot a_{v,STOP}\}$

| v    | $\pi(2,v)\cdot a_{v,STOP}$ |
| ---- | -------------------------- |
| X    | 1/20 x 1/6 = 1/120         |
| Y    | 0 x 2/3 = 0                |
| Z    | 1/45 x 0 = 0               |

Since the maximum value which is $\frac{1}{120}$ comes from v=X, the label at layer 2 is `X`

**Proceed to layer n =1. Note that the node they transit to is X**

$y_{n}^{*} = argmax_{v}\{\pi(n,v)\cdot a_{v,y^{*}_{j+1}}\}$ = $argmax_{v}\{\pi(1,v)\cdot a_{v,2}\}$

| v    | $\pi(1,v)\cdot a_{v,2}$ |
| ---- | ----------------------- |
| X    | 0.2 x 0 = 0             |
| Y    | 0 x 1/6 = 0             |
| Z    | 0.2 x 0.5 = 0.1         |

Since the maximum value which is 0.1 comes from v=Z, the label at layer 1 is `Z`

**<u>Conclusion</u>**

The state sequence is `{Z, X}`

# Question 3. Clearly describe how to modify the Viterbi algorithm to perform such a new decoding task. (10 points)

We are incorporating knowledge that the SPECIFIC observation $x_{i}$ has certain states that does not reach it. The example given is that $y_{i} \neq V$ 

<u>**Step 0: Setting some known facts**</u>

If word = "The" at position i, the emission probability from state V (verb) to "The" is 0

if $x_{i}=The$: 

​	$b_{u=V}(x_{i})=0$

<u>**Step 1: Initialization (This step still remains the same)**</u>

- Initialize all the scores of the path to each node to be 0
- Initialize the score of the start node to be 1

<u>**Step 2: This step is modified a bit**</u>

> For j = 0 … n − 1, for each u ∈ T
>
> ​	At a layer j+1,
>
> ​		if x<sub>j+1</sub> == "The" and j+1 == i:
>
> ​			$\pi(j+1, u) = 0$ (We do this because we know that the emission probability is 0 and this saves computation time. This is run only if the 2 conditions are met)
>
> ​		else:
>
> ​			$\pi(v, u) = max_{v}\{\pi(j,v) \cdot b_{u}(x_{j+1}) \cdot a_{v,u}\}$

<u>**Step 3: This is the same**</u>

$\pi(n+1, STOP) = max_{v}\{\pi(n,v) \cdot a_{v,u}\}$

<u>**Step 4: Once the weights are chosen, we need to choose the highest scoring path**</u> 

We consider the final layer first

>  if x<sub>n</sub> == "The" and n==i:
>
> ​	$y_{n}^{*} = argmax_{v\neq V}\{\pi(n,v)\cdot a_{v,STOP}\}$ (Since we know that the state cannot be a verb if the word is "The" at position i)
>
> else:
>
> ​	$y_{n}^{*} = argmax_{v}\{\pi(n,v)\cdot a_{v,STOP}\}$

Then we consider the rest of the layers

>  if x<sub>n</sub> == "The" and n==i:
>
> ​	$y_{n}^{*} = argmax_{v\neq V}\{\pi(n,v)\cdot a_{v,y^{*}_{j+1}}\}$ (Since we know that the state cannot be a verb if the word is "The" at position i)
>
> else:
>
> ​	$y_{n}^{*} = argmax_{v}\{\pi(n,v)\cdot a_{v,y^{*}_{j+1}}\}$



# Question 4. Clearly define the forward and backward scores in a way analogous to HMM. Give algorithms for computing the forward and backward scores. Analyze the time complexity associated with your algorithms (10points)

This is an unsupervised problem as we are only given the observation states. Thus, we require a forward backward algorithm to first find the counts (E step) before we can proceed to the M step.

<u>**Formulating the problem**</u>

$p(x_{1}, x_{2}, ..., x_{j-1}, y_{1}, y_{2}, ..., y_{j-1}, z_{j}=u, x_{j}, x_{j+1},...,x_{n}, y_{j}, y_{j+1},...,y_{n}; \theta)$

= $p(x_{1}, x_{2}, ..., x_{j-1}, y_{1}, y_{2}, ..., y_{j-1}, z_{j}=u; \theta)$ x $p(x_{j}, x_{j+1},...,x_{n}, y_{j}, y_{j+1},...,y_{n} | z_{j}=u; \theta)$

= $\alpha_{u}(j) \cdot \beta_{u}(j)$

Where $\alpha_{u}(j)$ is the forward probability and $\beta_{u}(j)$ is the backward probability.

<u>**Solving for alpha and beta**</u>

**Solving for alpha - Forward**

$\alpha_{u}(j+1) = \sum_{v} \alpha_{v}(j)\alpha_{v,u}\beta_{v}(x_{j})$

With base case $\alpha_{u}(1) = \alpha_{START,u}$

**Solving for beta - Backward**

$\beta_{u}(j) = \sum_{v} a_{u,v}b_{u}(x_{j})b_{u}(y_{j})\beta_{v}(x_{j+1})$

This time we add an extra term because we must also emit `y` and this means that we need to include the emission probability for $y_{j}$

With base case  

$\beta_{u}(n) = a_{u,STOP}b_{u}(x_{n})b_{u}(y_{n})$

Again, for the base case we need to add an additional emission probability 

<u>**Complexity analysis**</u> 

Overall: O(nT<sup>2</sup>) for an observation pair

- Where T is the set of possible states 
- n is the length of the observation pair sequence

**Forward algorithm**

For each layer, and for each state, we have to compute with T other such states which gives T<sup>2</sup> possibilities. This is multiplied by n which is the length of the observation pair sequence. Hence O(nT<sup>2</sup>)

For the backward the same logic applies and we get O(nT<sup>2</sup>)

Overall it is O(2nT<sup>2</sup>) which can be simplified to O(nT<sup>2</sup>) since we are using big O notation