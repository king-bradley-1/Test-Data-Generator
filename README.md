# Test Data Generator

This project is a flexible test data generator written in Python. It reads a YAML configuration file to generate fake data using the [Faker](https://faker.readthedocs.io/) library and outputs the data as a CSV file.

## Features

- Configurable fields and record count via YAML
- Supports custom arguments for Faker providers (e.g., date ranges, min/max values)
- Handles argument remapping for compatibility with Faker methods
- Outputs data as a CSV file

## Requirements

- Python 3.7+
- pandas
- pyyaml
- Faker

Install dependencies:
```bash
pip install pandas pyyaml Faker
```

## Usage

1. **Configure your YAML file** (`data_config.yml`):

    ```yaml
    fields:
      name:
        args: {}
      date_between:
        args:
          start_date: '-30d'
          end_date: 'today'
      pyfloat:
        args:
          min_value: 10
          max_value: 1000
    records: 100
    output_file: output.csv
    ```

2. **Run the generator:**
    ```bash
    python main.py
    ```

3. **Output:**  
   The generated CSV file will be saved as specified in the YAML (`output.csv`).

## Notes

- Ensure argument names in the YAML match the Faker provider's method signature (e.g., `start_date`, `end_date`, `min_value`, `max_value`).
- If you use different argument names, update the code to remap them accordingly.

## License

MIT License
