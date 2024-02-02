## How to use
To read the dataset, you can use the pandas library.
```
import pandas as pd

dataset = pd.read_json(
    path_or_buf="data/LLMGooAQ.jsonl",
    lines=True
)

print(dataset.head())
```