from pathlib import Path
import argparse
import os
import json


def generate(path2folder: Path, path: Path):
    """
    Concatenate the 10k datasets (jsonl format) into a 100k dataset (jsonl format)
    :param path2folder: folder where the 10k datasets are stored
    :param path: path where the 100k dataset will be stored
    :return: None
    """
    # Check if the folder exists
    if not path2folder.exists():
        raise FileNotFoundError(f"{path2folder} does not exist")
    # Check if the folder is empty
    if not os.listdir(path2folder):
        raise FileNotFoundError(f"{path2folder} is empty")
    
    # read all the files in the folder
    original = []
    for i in range(10):
        with open(path2folder / f"LLMGooAQ-100k-{i}.jsonl", "r") as f:
            data = f.readlines()
            # load json
            data = [json.loads(d) for d in data]
            original.extend(data)
            
    # write the concatenated dataset
    with open(path, "w") as f:
        for d in original:
            f.write(json.dumps(d) + "\n")
            
    print(f"100k dataset is stored at {path}")
            
        
if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--path2folder", type=str, help="folder where the 10k datasets are stored", default="data-100k")
    argparse.add_argument("--path", type=str, help="path where the 100k dataset will be stored", default="data-100k/LLMGooAQ-100k.jsonl")
    args = argparse.parse_args()
    generate(Path(args.path2folder), Path(args.path))