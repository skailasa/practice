# alchemist

Welcome to Alchemist! The number one Python Library for alchemical
simulations.

## Installation

Install.

```bash
python setup.py install
```

Install for usage in editable mode.

```bash
pip install -e .
```

Install development and testing requirements.

```bash
pip install -e .[dev]
```

## Usage

One can use alchemist either as a Python library, or from the command
line.

### As a Python Library

```python
>>> from alchemist.laboratory import load_substance_data
>>> from alchemist.laboratory import Laboratory
>>>
>>> data = load_substance_data('test_data.yml') 
>>> print(data)
{'lower': ['a'], 'upper': ['antia']}
>>>
>>> lab = Laboratory(data)
>>>
>>> # run a full experiment until all possible reactions complete
>>> lab.run_experiment()
{'lower': [], 'upper': []}
>>>
>>> # count the number of reactions
>>> lab.reaction_count
2
```

### From the Command Line

One can also use the package as a command line tool.

```bash
abracadabra data.yml --reactions
```

This returns the final composition of your shelves only to stdout.
The optional `--reactions` returns the number of reactions only to
stdout. 

NOTE: `data.yml` **MUST** contain a dict of lists, where the keys are
the shelf names, and the values in a respective list are the substances
in that shelf.

e.g. The shelves,

```python
{'lower': ['a', 'antib'], 'upper': ['b', 'antia']}

```

should be stored in YAML as a dict of lists, either:

```yaml
lower
- a
- antib
upper
- b
- antia
```

or

```yaml
{
  lower: [
    a, 
    antib
  ], 
  upper: [
    b, 
    antia
  ]
}
```

At present only two shelf standard laboratories are supported.


### Testing

Make sure to have install the `dev` requirements.

```python
# run tests
pytest alchemist/tests/

# run coverage
pytest --cov=alchemist/tests/
```