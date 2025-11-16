# System Testing Instructions

## Setup
Activate your virtual environment and install dependencies:
```bash
pip install -r requirements.txt

```

## Run System Tests

```
python -m unittest courseProjectDocs/system-testing/quadratic_probing.py

```

## Notes

- Tests validate the application as a whole via public interfaces (insert_data, bulk_insert, keys).
- No internal code structure is referenced.