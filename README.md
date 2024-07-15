# python-email-send

This sample will show you to easily send an email with the Nylas Python SDK.

You can follow along step-by-step in our blog post ["How to Send Emails with the Nylas Python SDK"](https://www.nylas.com/blog/how-to-send-emails-with-the-nylas-python-sdk/).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
NYLAS_API_KEY = ""
NYLAS_API_URI=""
NYLAS_GRANT_ID = ""
RECIPIENT_EMAIL = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install nylas
```

## Usage

Run the script using the `python3` command:

```bash
$ python3 SendEmail.py
```

When your message is successfully sent, you'll get the following output in your terminal:

```text
Message "With Love, from Nylas" was sent with ID 111111111111111111
```

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/python-sdk/) to learn more.
