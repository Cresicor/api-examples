# Vividly API Examples

Vividly's GraphQL API exports data from the Vividly platform in a format customizable to your needs.

## Requirements

You will need your Vividly _company ID_ as well as an _API token_. These can both be obtained from the `Settings` section of Vividly.

## Use of the Vividly API

Currently the Vividly API is in a _beta_ phase. It is available at this URL: `https://pr-2004.vividly.dev/public/graphql/`

You will need to pass two headers to each API call
- an API bearer token as the `Authorization` header
- your company ID as the `Company` header

## Examples

Please see the `examples/` folder for some examples of the API and its use.
