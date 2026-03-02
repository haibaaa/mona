# Mona cli
Mona is the cli-interface for configuring your lisa projects

---

## Features

- Initialize configuration templates for new projects
- Sync remote config variables with lisa
- Works with `.env` files via python-dotenv
- Simple CLI interface built with Click

---

## Installation

Once published to PyPI:

```bash
pip install mona-cli
````

Using uv:

```bash
uv pip install mona-cli
```

---

## Usage

After installation, the `mona` command is available on the system PATH.

```bash
mona --help
```

Expected output:

```bash
Usage: mona [OPTIONS] COMMAND [ARGS]...

  Mona – sync your local config to Lisa

Options:
  --help  Show this message and exit.

Commands:
  init  Initialize a template
  sync  Sync config variables across project
```

---

## Usage
### mona init

Initializes a configuration template in the current project.

```bash
mona init
```

### mona sync

Synchronizes local configuration values with the Lisa remote configuration server.

```bash
mona sync
```
---

## Configuration

Mona requires your project config_api\
To generate a project run
```bash 
curl -X POST https://lisa-aopa.onrender.com/create/<project_name>
```
and copy the returned client and config apis to a safe place as they\
will not be displayed again

```env
LISA_CONFIG_URL=https://config.example.com
```
Environment variables are loaded automatically using python-dotenv.

