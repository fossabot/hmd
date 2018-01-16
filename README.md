<p align="center">
  <a href="https://travis-ci.org/initbar/hmd">
    <img src="https://travis-ci.org/initbar/hmd.svg?branch=master">
  </a>
  <br>
  <img src="./docs/images/logo.png">
</p>

**hmd** is the next-generation Hierarchial Multiple Dictionary (HMD) compiler, pattern matching, and text traversal engine. It's designed to be a monolith construct in order to provide a simpler interface during [import](https://docs.python.org/3/reference/import.html) as a module.

## Features

- Modular to support additional syntax and definitions.
- Backward-compatible with the older version **hmd_split.py**.
- Optimized to sort and de-duplicate listed keywords in results (".matrix").
- Optimized to sort and de-duplicate listed rules in results (".matrix").
- Check dictionary syntax during parsing stage.
- Support variables to store repeated strings.
- Syntax highlighting for definitions.
- Pack to single executable binary.
- Complete test suite.

## Usage

```bash
~$ make && cd ./build
~$ ./hmd -h
```

## Module

When importing, use absolte imports directly from the base repository:

```python
import hmd.src.abstract.automata.automata
import hmd.src.abstract.generator.generator
# ..
```

If you're importing from the binary builds, use [zipimport](https://docs.python.org/2/library/zipimport.html) module.

## Documentations

See [syntax](./docs/SYNTAX.md), some [examples](./docs/EXAMPLE.md), or [design](./docs/DESIGN.md).

## License

**hmd** is under [MIT License](./LICENSE.md).
