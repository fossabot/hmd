[![Build Status](https://travis-ci.org/initbar/hmdc.svg?branch=master)](https://travis-ci.org/initbar/hmdc)
[![](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/download/releases/2.7/)

# hmdc

**hmdc** is the next-generation Hierarchial Multiple Dictionary (HMD) compiler.

## Features

- Modular to support additional syntax and definitions.
- Backward-compatible with the older version **hmd_split.py**.
- Optimized to sort and de-duplicate listed keywords in results (".matrix").
- Optimized to sort and de-duplicate listed rules in results (".matrix").
- Convert dictionary terms into lemma using NLP engine.
- Check dictionary syntax during parsing stage.
- Support variables to store repeated strings.
- Syntax highlighting for definitions.
- Pack to single executable binary.
- Complete test suite.

## Dependencies

```bash
~$ sudo pip install nltk
```

## Build

```bash
~$ ./build.sh
```

## Test

```bash
~$ # cd ./build
~$ python ./hmdc -t
```

## Usage

```bash
~$ # cd ./build
~$ python ./hmdc -h
```

## Syntax

See [syntax](./SYNTAX.md).

## Example

See [example](./EXAMPLE.md).

## Design

**hmdc** is a modified compiler, which has similarities to conventional compilers. All user input goes into `FACTORY`, a singleton-wrapper instance that spawns and dies with the program's lifetime, and outputs as compiled matrix:

![](https://hmdc.surge.sh/design.png)

By default, `LEXER` will only tokenize a string into primitive characters, numbers, and symbols. If a user provides custom rules (as [regular expression](https://wikipedia.org/wiki/Regular_expression)), it will use that instead.

Since the syntax of Hierarchial Multiple Dictionary (HMD) does not resemble that of a conventional programming language, custom language grammar was defined as inheritable abstractions of [deterministic finite automata](https://wikipedia.org/wiki/Deterministic_finite_automaton):

![](https://hmdc.surge.sh/automata.png)

`PARSER` also uses similar technique as the [Shunting Yard algorithm](https://wikipedia.org/wiki/Shunting-yard_algorithm) to split the operator and scalar values. However, it has heavily modified the algorithm to accomodate variables and comments:

![](https://hmdc.surge.sh/shuntingyard.svg)

`GENERATOR` is an overridable class that can be defined with custom compiling implementations.

## License

> The MIT License
>
> Copyright (c) 2017 Herbert Shin
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
