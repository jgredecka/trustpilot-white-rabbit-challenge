# Follow The White Rabbit - Trustpilot Challenge

You've made an important decision. Now, let's get to the matter.

We have a message for you. But we hid it.
Unless you know the secret phrase, it will remain hidden.

Can you write the algorithm to find it?

Here is a couple of important hints to help you out:
- An anagram of the phrase is: `"poultry outwits ants"`
- There are three levels of difficulty to try your skills with
- The MD5 hash of the easiest secret phrase is `"e4820b45d2277f3844eac66c903e84be"`
- The MD5 hash of the more difficult secret phrase is `"23170acc097c24edb98fc5488ab033fe"`
- The MD5 hash of the hard secret phrase is `"665e5bcb0c20062fe8abaaf4628bb154"`

## Method
- Narrow down the search scope by filtering out words that cannot be part of the anagram. These include words containing characters not present in the anagram or exceeding the character frequency of the anagram. This reduces the total number of words to work with from `99175` to `1659`.  
- Compute word combinations starting with 3-word combinations (my original assumption was the phrase contains 3 words given the number of spaces). This is increased to 4-letter word combinations as the search continues.
- Compute permutations for each combination. 
- The secret phrase is identified when the MD5 hash of the permuted phrase matches one of the provided hashes.
- Found easy and medium phrases: `ty outlaws printouts` and `printout stout yawls`. Difficult phrase has not been found (or at least not within a reasonable time frame).

## Running locally

Pre-requisites:
- Python 3.9

To run in the terminal:

```python phrase_finder.py```

### Alternative - using Docker

You can use the following command to run the script using Docker instead:

```docker build -t md5_challenge . && docker run -it md5_challenge```
