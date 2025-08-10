import pandas as pd
import yaml
from faker import Faker


def create_data():
    try:
        with open("data_config.yml") as f:
            data = yaml.safe_load(f)
        op_data = []
        fake = Faker()
        fields = data.get("fields")
        records = data.get("records")
        for _ in range(records):
            each_record = {}
            for name, value in fields.items():
                if "args" in value:
                    each_record[name] = getattr(fake, name)(**value["args"])
                else:
                    each_record[name] = getattr(fake, name)()
            op_data.append(each_record)
        df = pd.DataFrame(op_data)
        df.to_csv(data.get("output_file"))
    except FileNotFoundError as e:
        print(f"Input yaml file not found. {e}")
    except (AttributeError, TypeError) as e:
        print(f"Invalid value in the config file. {e}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_data()
