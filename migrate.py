import glob
import os
import pathlib
import time

import requests
import yaml
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = pathlib.Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path)

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

WAIT = 0.1

host = os.getenv("AIBLECODE_API_HOST")

curr = (pathlib.Path(__file__).parent / "problem").absolute()

res = requests.post(
    f"{host}/token",
    data={
        "grant_type": "password",
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
        "scope": "",
    },
)
print(res)
token = res.cookies
time.sleep(WAIT)

for category in glob.glob(f"{curr}/*"):
    if not os.path.isdir(category):
        continue

    with open(f"{category}/metadata.yml") as f:
        category_meta = yaml.load(f, Loader=yaml.SafeLoader)

    category_path = category.replace(f"{curr}/", "")
    title = category_meta["category"]["title"]
    description = category_meta["category"]["description"]

    res = requests.post(
        f"{host}/create_category",
        json={
            "path_id": category_path,
            "title": title,
            "description": description,
        },
        cookies=token,
    )
    time.sleep(WAIT)

    if res.status_code != 200:
        print(f"Failed to create category: {category_path}")
        print(res.text)
        exit(1)

    print("Success to create category:", category_path)

    for problem in glob.glob(f"{category}/*"):
        if not os.path.isdir(problem):
            continue

        with open(f"{problem}/metadata.yml") as f:
            problem_meta = yaml.load(f, Loader=yaml.SafeLoader)

        problem_path = problem.replace(f"{category}/", "")
        ignore = problem_meta["problem"].get("ignore", False)

        title = problem_meta["problem"]["title"]
        statement = open(f"{problem}/statement.md").read()
        level = problem_meta["problem"]["level"]
        time_limit = problem_meta["problem"]["time_limit"]
        memory_limit = problem_meta["problem"]["memory_limit"]

        res = requests.post(
            f"{host}/create_problem",
            json={
                "path_id": problem_path,
                "title": title,
                "statement": statement,
                "category_path_id": category_path,
                "level": level,
                "time_limit": time_limit,
                "memory_limit": memory_limit,
            },
            cookies=token,
        )
        time.sleep(WAIT)

        if res.status_code != 200:
            print(f"Failed to create problem: {problem_path}")
            print(res.text)
            exit(1)

        print("Success to create problem:", problem_path)

        judge = problem_meta["problem"].get("judge", None)

        if judge:
            res = requests.post(
                f"{host}/set_judge",
                json={
                    "category_path_id": category_path,
                    "problem_path_id": problem_path,
                    "judge_type": judge,
                    "code": open(f"{problem}/codes/judge.py").read(),
                },
                cookies=token,
            )
            time.sleep(WAIT)

            if res.status_code != 200:
                print(f"Failed to create judge: {problem_path}")
                print(res.text)
                exit(1)

            print("Success to create judge:", problem_path)

        input_files = sorted(glob.glob(f"{problem}/testcases/in/*"))
        output_files = sorted(glob.glob(f"{problem}/testcases/out/*"))

        input_set = set(
            [f.replace(f"{problem}/testcases/in/", "") for f in input_files]
        )
        output_set = set(
            [f.replace(f"{problem}/testcases/out/", "") for f in output_files]
        )

        if input_set != output_set:
            print(f"Input and output files do not match for {problem_path}")
            print("Extra input files:", *(input_set - output_set))
            print("Extra output files:", *(output_set - input_set))
            exit(1)

        for path in sorted(input_set & output_set):
            input_file = f"{problem}/testcases/in/{path}"
            output_file = f"{problem}/testcases/out/{path}"

            res = requests.post(
                f"{host}/create_testcase",
                json={
                    "category_path_id": category_path,
                    "problem_path_id": problem_path,
                    "name": path,
                    "input": open(input_file).read(),
                    "output": open(output_file).read(),
                },
                cookies=token,
            )
            time.sleep(WAIT)

            print(res)

            if res.status_code != 200:
                print(f"Failed to create testcase: {path}")
                print(res.text)
                exit(1)

            print("Success to create testcase:", path)

requests.post(f"{host}/logout", cookies=token)
print("Migration completed")
