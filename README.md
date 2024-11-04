# AI Sales Assistant Chatbot

## Project Goal

This project aims to create a realistic, low-latency chatbot that functions as an AI sales assistant for Nooks, an AI-powered sales development platform.
The chatbot responds when the user falls silent for some time, simulating a natural conversation flow.

The current implementation is relatively slow to respond the the user - the goal is to make it faster.

Demo of the current implementation: [Loom](https://www.loom.com/share/c276d63215b9435b89c72a7e02cdb173)

Demo of a reference solution that responds faster: [Loom](https://www.loom.com/share/7ef5215244e941aba41c543433e67578)

## Current Implementation

The system consists of three main components:

1. Speech-to-text (STT) using AssemblyAI's hosted API for real-time transcription
2. A sales chatbot powered by OpenAI's GPT-4 model (note - not gpt4o which is faster but not as accurate in some cases)
3. Text-to-speech (TTS) using ElevenLabs for voice output

The chatbot listens to user input, transcribes it in real-time, and generates a response when the user stops speaking. The AI's response is then converted to speech and played back to the user.

## Task

Assume that you are not allowed to modify the services used (you must use Assembly's hosted model for STT, OpenAI's GPT-4 for the chatbot, and ElevenLabs with this voice setting for TTS).

In addition, you are not allowed to tinker with certain configuration settings that affect the bot's realism. For example, the Assembly chatbot waits 500ms for the user to be silent before a response. This adds to the perceived latency (because the chatbot only responds after 500ms), but is necessary to maintain the realism of the bot and not have it interrupt you mid phrase. Your solution must maintain the property of waiting for 500ms of silence from the user before any bot responds, and should NOT configure this to be lower (for higher latency) or higher (for more realism).

How would you modify the code to make the chatbot lower latency & respond faster?

### Evaluation Criteria

Your solution will be evaluated based on:

1. Reduction in overall latency (comparable to the "reference solution" above). Please share a demo video so we can easily evaluate.
2. Maintenance of conversation quality and realism (i.e the chatbot doesn't interrupt the human speaker while they're in the middle of speaking. The chatbot must say the same things that the reference solution would have said.)
3. Code quality and clarity of explanation in README.md


## Getting Started

1. Review the existing code in `main.py`, `lib/sales_chatbot.py`, and `lib/elevenlabs_tts.py`
2. Install the requirements by running `pip install -r requirements.txt` (or use a virtual environment if you prefer)
3. Set your OpenAI, AssemblyAI, and ElevenLabs API keys in `.env` - you should have received them via email.
4. Run the current implementation to understand its behavior by running `python3 main.py`
5. Begin your optimization process. Document your changes and reasoning in this README.md file when done.

## Poetry Setup

If you're getting stuck with installation issues, we offer an alternative Poetry-based installation method.

1. Install [Poetry](https://python-poetry.org/docs/#installing-with-pipx)
2. Install all requirements by running `poetry install`. You will need to `brew install ffmpeg`, `brew install portaudio`, `pip3 install "assemblyai[extras]"` (MacOS) if you haven't already.
3. Run the current implementation by running `poetry run python3 main.py`

Good luck!

## Bonus

Right now a lot of the latency comes from external services (TTS, LLM inference, STT). An easy way to reduce latency would be to use local models.
For example you could use:

- Nemo ASR for STT
- Llama for the chatbot
- bark or tortoise for TTS
  Try building a version of this chatbot that is local-only and see what speedup you achieve!


## Your Approach

Please describe your approach here.
First, I reduced the token limit for responses to 50, which restricts the chatbot’s response length and allows it to produce short, focused answers much faster. Since the assistant’s responses are designed to be concise, this smaller token limit helps streamline response generation without sacrificing clarity or relevance, giving the interaction a more immediate feel.

Building on this, I enabled streaming for OpenAI's GPT-4 model. This means the bot now processes each chunk of text as it arrives, rather than waiting for the entire response to be generated. The moment the bot receives the first few words, it can start preparing to speak, cutting down the wait time before initiating text-to-speech (TTS). Streaming helps maintain a smooth conversational flow and gives the impression of a more responsive assistant.

For TTS, I optimized the setup by switching to ElevenLabs' streaming API, which allows audio to be generated in real-time and start playing almost immediately. Additionally, I switched to the “eleven_turbo_v2_5” model, optimized for lower latency. This setup minimizes the lag between the bot generating a response and the user hearing it, creating a more natural pace that feels more like a live interaction.

To push latency reduction even further, I experimented with asynchronous processing using Python’s asyncio. The goal here was to let the bot continue transcribing while speaking, but I ran into some challenges with managing transcription sessions and handling potential overlaps. I could see potential for further latency reduction here, but with midterms and other assignments, I ran out of time to fully explore this route, as this project was intended for a three-hour timeframe.

Overall, these optimizations—reducing token size, enabling streaming, optimizing TTS playback, and exploring async processing—combine to make the bot feel faster and more interactive while keeping a natural flow. This project was fascinating to work on, and I'm really excited to hear back from Nooks as I’d love the chance to contribute to the mission at Nooks!


Please also include a recorded video showing how fast your chatbot implementation is to respond.
Link to video (uses google drive sharing): https://drive.google.com/file/d/1CjFyTjYBg-NGZb5qKsBF_pCGjPOSEfkx/view?usp=sharing.

