# Text Summarizer

A small Python tool that summarizes any text file into 3 lines using AI.

## What it does
Reads a text file, sends it to the Gemini API, and saves a short summary in a new file.

## How it works
1. Reads the text from `article.txt`
2. Sends it to the Gemini API as a request
3. Gets the answer back as JSON and pulls out the summary
4. Saves it to `summary.txt`

## How to run it
1. Install Python and the requests library: `pip install requests`
2. Get a free API key from Google AI Studio
3. Create a file called `key.txt` and paste your key in it (one line, nothing else)
4. Put the text you want summarized in `article.txt`
5. Run `summarizer.py`

Your API key stays in `key.txt` and is never written in the code.

## Tools used
Python, JSON, Gemini API, file handling

## Example
Input: a few paragraphs about learning to code
Output: a 3-line summary saved in `summary.txt`# text-summarizer
Summarizes a text file using AI (Python + Gemini API)
