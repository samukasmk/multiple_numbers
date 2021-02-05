multiplicable_numbers
---

This is a sample project that tries to detects multiplicable numbers and for true cases converts int numbers in literal words.

## Instaling and executing
```
$ pip install -e git://github.com/samukasmk/multiplicable_numbers.git@v0.1.1#egg=multiplicable_numbers.egg-info
```

## Executing on command line
After the pip install the setup will create a command on your terminal called `detects-multiplicable-numbers`
Just executes the commands below on your command line terminal with the default parameters
that the program will start detecting multiples of 3 and 5, within a number from 1 to 100
```
$ detects-multiplicable-numbers
1
2
Three
4
Five
Three
7
8
Three
Five
11
Three
13
14
ThreeFive
16
17
Three
19
Five
Three
22
23
Three
Five
26
Three
28
29
ThreeFive
31
32
Three
34
Five
Three
37
38
Three
Five
41
Three
43
44
ThreeFive
46
47
Three
49
Five
Three
52
53
Three
Five
56
Three
58
59
ThreeFive
61
62
Three
64
Five
Three
67
68
Three
Five
71
Three
73
74
ThreeFive
76
77
Three
79
Five
Three
82
83
Three
Five
86
Three
88
89
ThreeFive
91
92
Three
94
Five
Three
97
98
Three
Five
```

The command is modular you can change the multiplicablea and the range numbers of comparison

```
$ detects-multiplicable-numbers --help
usage: detects-multiplicable-numbers [-h] [-m [MULTIPLICABLES ...]] [-i INITIAL_NUMBER] [-f FINAL_NUMBER]

A command line tools that tells if is multiple numbers.

optional arguments:
  -h, --help            show this help message and exit
  -m [MULTIPLICABLES ...], --multiplicables [MULTIPLICABLES ...]
                        The multiplicable numbers to do the detections.
  -i INITIAL_NUMBER, --initial-number INITIAL_NUMBER
                        The initial number to start the iteration
  -f FINAL_NUMBER, --final-number FINAL_NUMBER
                        The final number to start the iteration
```

This is another example of runs but detecting multiples of three, six and nine on range of 50 numbers
```
$ detects-multiplicable-numbers -i 1 -f 50 -m 3 6 9 
1
2
Three
4
5
ThreeSix
7
8
ThreeNine
10
11
ThreeSix
13
14
Three
16
17
ThreeSixNine
19
20
Three
22
23
ThreeSix
25
26
ThreeNine
28
29
ThreeSix
31
32
Three
34
35
ThreeSixNine
37
38
Three
40
41
ThreeSix
43
44
ThreeNine
46
47
ThreeSix
49
50
```