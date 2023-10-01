![commandgpt](header.png)

A command-line utility tool which allows you to use OpenAI to help you generate bash commands.

You need an OPENAI_API_KEY env variable set with your OpenAI API key.

## Options
`-q` Will allow you to receive commands that match your natural language query

`-r` Will run commands that match your natural language query

## Examples

`commandgpt -q "List all files"` will return the answer:
`ls`

`commandgpt -r "List all files"` will run ls, displaying all files on the current directory on your filesystem