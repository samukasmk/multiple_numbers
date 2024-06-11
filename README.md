multiplicable_numbers
---

Welcome [Fáilte] to `multiple_numbers` project. It's just a simple example of how to detect multiple numbers of your choice and convert int numbers into literal words.

- By: Samuel Maciel Sampaio
- Email: [samuel.maciel.sampaio@gmail.com](mailto:samuel.maciel.sampaio@gmail.com)
- Github: @samukasmk

# Installing

## External tools

This project requires some external tools like: `git`, `docker`, and `docker-compose`.

If you don't have some of those external tools mentioned. You should read these articles:
- [How to install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [How to install Docker Engine](https://docs.docker.com/engine/install/)
- [How to install Docker-Compose](https://docs.docker.com/compose/install/)


## Cloning this project

```
git clone https://github.com/samukasmk/multiple_numbers.git
```

## Building docker image

```sh
docker-compose build multiple-numbers
```

# Running

## Running by docker-compose
After `git` project was cloned and the `docker` image was built successfully, to run the python script by docker-compose is just the simple command below:

```sh
docker-compose run multiple-numbers
Creating multiple_numbers_multiple-numbers_run ... done
```

The script by default will start detecting multiples of 3 and 5, within a number from 1 to 100:
```sh
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

## Displaying other options
But you can display other argument options with `--help` to run with other parameters:


```sh
$ docker-compose run multiple-numbers --help
Creating multiple_numbers_multiple-numbers_run ... done
```

```sh
usage: multiple-numbers [-h] [-m [MULTIPLICABLES ...]] [-i INITIAL_NUMBER] [-f FINAL_NUMBER]

A command line tools that tells if is multiple numbers.

options:
  -h, --help            show this help message and exit
  -m [MULTIPLICABLES ...], --multiplicables [MULTIPLICABLES ...]
                        The multiplicable numbers to do the detections.
  -i FIRST_NUMBER, --first-number FIRST_NUMBER
                        The initial number to start the iteration
  -f LAST_NUMBER, --last-number LAST_NUMBER
                        The final number to start the iteration
```

## Running with different arguments

```sh
$ docker-compose run multiple-numbers --first-number 1 --last-number 10 --multiplicables 2 4 6
Creating multiple_numbers_multiple-numbers_run ... done
```

```sh
1
Two
3
TwoFour
5
TwoSix
7
TwoFour
9
Two
```


# Testing

To run unit tests by docker-compose previous defined, just execute the simple command:

```sh
docker-compose run tests
```

```sh
Creating multiple_numbers_tests_run ... done
test_multiplicables_by_three_and_five (test_detects_multiplicable_numbers.TestDetectsMultiplicableNumbers.test_multiplicables_by_three_and_five) ... ok
test_multiplicables_just_by_five (test_detects_multiplicable_numbers.TestDetectsMultiplicableNumbers.test_multiplicables_just_by_five) ... ok
test_multiplicables_just_by_three (test_detects_multiplicable_numbers.TestDetectsMultiplicableNumbers.test_multiplicables_just_by_three) ... ok
test_non_multiplicables_by_five (test_detects_multiplicable_numbers.TestDetectsMultiplicableNumbers.test_non_multiplicables_by_five) ... ok
test_non_multiplicables_by_three (test_detects_multiplicable_numbers.TestDetectsMultiplicableNumbers.test_non_multiplicables_by_three) ... ok
test_non_multiplicables_by_three_five (test_detects_multiplicable_numbers.TestDetectsMultiplicableNumbers.test_non_multiplicables_by_three_five) ... ok
test_one_to_a_hundred_with_six_and_nine_multiplicables (test_displays_detected_numbers.TestDisplaysDetectedNumbers.test_one_to_a_hundred_with_six_and_nine_multiplicables) ... ok
test_one_to_a_hundred_with_three_and_five_multiplicables (test_displays_detected_numbers.TestDisplaysDetectedNumbers.test_one_to_a_hundred_with_three_and_five_multiplicables) ... ok
test_one_to_a_hundred_with_tow_and_four_multiplicables (test_displays_detected_numbers.TestDisplaysDetectedNumbers.test_one_to_a_hundred_with_tow_and_four_multiplicables) ... ok
test_multiplicables_by_five (test_multiplicable_validations.TestMultiplicableValidations.test_multiplicables_by_five) ... ok
test_multiplicables_by_three (test_multiplicable_validations.TestMultiplicableValidations.test_multiplicables_by_three) ... ok
test_non_multiplicables_by_five (test_multiplicable_validations.TestMultiplicableValidations.test_non_multiplicables_by_five) ... ok
test_non_multiplicables_by_three (test_multiplicable_validations.TestMultiplicableValidations.test_non_multiplicables_by_three) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.003s

OK
```