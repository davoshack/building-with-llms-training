# Setup

If you are using Codespaces, go and create one here:

[https://github.com/pamelafox/python-3.13-playground](https://github.com/pamelafox/python-3.13-playground)

It can take a few minutes to start the first time, so click the button now!

If you're not using Codespaces you'll need a Python 3.9+ environment that you can install packages into. You'll likely want a virtual environment to avoid conflicts with other projects.

## Installing the packages

```bash
git clone git@github.com:davoshack/building-with-llms-training.git

# Optional if you want a virtual environment (no need to do this on Codespaces):
python -m venv venv
source venv/bin/activate

# Install the project requirements
pip install -r requirements.txt
```

Run this command to see if the packages installed correctly:

```bash
llm --version
```
You should see this:
```
llm, version 0.26a0
```

## Configuring the OpenAI API key

You'll need an OpenAI API key for this workshop. You can either get your own here:

[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)


Key obtained, you can configure it for LLM like this:

```bash
llm keys set openai
# Paste your key here
```

## Testing that it worked

Test that the keys works like this:
```bash
llm 'five fun facts about cats'
```
The key will be saved to a JSON file. You can see the location of that file by running:
```bash
llm keys path
```

A useful trick is that `llm keys get openai` will print the key out again. You can use this pattern to use that key with other tools that require an environment variable:

```bash
export OPENAI_API_KEY="$(llm keys get openai)"
```
