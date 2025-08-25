"""
This code will load the imaging data from a CSV file, infer its schema using Pandera,
and save the schema to a YAML file.
It's a starting point for us to define our data validation and processing pipeline.
"""

import pandas as pd
import pandera.pandas as pa

if __name__ == "__main__":
    file_path = "data/POSTDOC_FEDERATED_LEARNING/X_RAYS_PLEFF-EDEMA/dataset.csv"
    imaging_df = pd.read_csv(file_path)
    # Create schema from the DataFrame and save to YAML
    output_path = "src/typed_ml/domain"
    filename = "imaging_data_schema_auto"
    schema = pa.infer_schema(imaging_df)
    schema_yaml = schema.to_yaml()
    if schema_yaml is not None:
        with open(f"{output_path}/{filename}.yaml", "w") as file:
            file.write(schema_yaml)
