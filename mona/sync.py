# mona/sync.py
import tomllib
import json
import requests
from mona.config import CONFIG_API, SERVER_URL, validate


def _infer_type(value) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) or isinstance(value, float):
        return "number"
    if isinstance(value, dict):
        return "json"
    return "string"


def _serialize_value(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, dict):
        return json.dumps(value)
    return str(value)


def _prepare_payload(data: dict) -> dict:
    return {
        key: {
            "value": _serialize_value(val),
            "value_type": _infer_type(val),
        }
        for key, val in data.items()
    }


def run_sync():
    validate()

    try:
        with open("lisa.toml", "rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        raise SystemExit("lisa.toml not found — run `mona init` first")

    url = f"{SERVER_URL}/sync/{CONFIG_API}"
    response = requests.post(url, json=_prepare_payload(data))

    if response.status_code != 200:
        raise SystemExit(f"Server error {response.status_code}: {response.text}")

    _print_diff(response.json())


def _print_diff(result: dict):
    added = result.get("added", [])
    updated = result.get("updated", [])
    removed = result.get("removed", [])

    if not any([added, updated, removed]):
        print("✓ already in sync, no changes made")
        return

    if added:
        print(f"\n  added ({len(added)})")
        for key in added:
            print(f"    + {key}")

    if updated:
        print(f"\n  updated ({len(updated)})")
        for key in updated:
            print(f"    ~ {key}")

    if removed:
        print(f"\n  removed ({len(removed)})")
        for key in removed:
            print(f"    - {key}")

    print()
