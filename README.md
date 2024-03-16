## What is this

It's an attempt at building a UI framework powered by an LLM, that is
The LLM decides what to display, based on the following:

* Current State
* User Input
* Other Context

## How does it work

### Right now

* We pass the UI Schema (ie: Available widgets) as context to the LLM
* We pass the current state as JSON
* The LLM is instructed to create a new state based on the input (Including the user instruction)


#### Problems with the approach

* Scalability, the more "widgets" we have the more context we need 

### Next approach

TBD

## How can I run it

* `make be # This will run the backend (Websocket server)` 
* `make fe # This will run the frontend (Static site, that connects to websocket)`
