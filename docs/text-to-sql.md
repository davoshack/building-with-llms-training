# Building a text to SQL tool

We're going to build something *genuinely useful*. Weirdly enough, this is a "hello world" exercise for prompt engineering.

Ask a question of your database in English, get a response from a custom SQL query written by the LLM.

## Prototyping against the logs database

We're going to use the LLM logs database itself, and prototype against it using the `sqlite-utils` CLI tool:

```bash
sqlite-utils schema "$(llm logs path)"
```
Let's write that to a file:

```bash
sqlite-utils schema "$(llm logs path)" > schema.sql
```

Now we can feed it to LLM and write our first query:

```bash
llm -f schema.sql \
  -s "reply with sqlite SQL" \
  "how many conversations are there?"
```

I got back this:

````
```sql
SELECT COUNT(*) AS conversation_count FROM conversations;
```
````
As you can see, the LLM decided to wrap it in a fenced code block.

We could ask it not to, but we can also use the `--extract` flag to extract the SQL from the response:

```bash
llm -f schema.sql \
  -s "reply with sqlite SQL" \
  --extract \
  "how many conversations are there?"
```
