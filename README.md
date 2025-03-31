# Browser Use Agent AWS

This repository contains sample code to complement the blog post available at <replace_url>. It demonstrates how to set up and use the Browser Use Agent AWS package effectively.

## Prerequisites

- `uv` package manager 

## Setup Instructions

### 1. Install `uv`
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create a Virtual Environment

Set up a virtual environment using uv:
```shell
uv venv .venv
```

Activate the virtual environment
on Linux/macOS:

```shell
source .venv/bin/activate
```

on Windows:
```powershell
.venv\Scripts\activate
```

### 3. Sync Dependencies
Install the required dependencies listed in pyproject.toml:

This will ensure all dependencies are installed and up to date.

### 4. Login to AWS
#### Create an AWS CLI Profile

1. Install the AWS CLI if not already installed. Follow the [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

2. Configure your AWS CLI profile:
    ```shell
    aws configure --profile my-profile
    ```
    Replace `my-profile` with your desired profile name. You will be prompted to enter:
    - AWS Access Key ID
    - AWS Secret Access Key
    - Default region name
    - Default output format (e.g., `json`)

3. Follow the guide to use the created AWS profile.


### 5. Run the Application
Run the application using:

```shell
uv run main.py
```