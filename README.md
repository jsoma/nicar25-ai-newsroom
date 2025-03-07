# AI in the Newsroom

## NICAR 2025, Minneapolis

Jonathan Soma

jonathan.soma@gmail.com / [@dangerscarf](https://twitter.com/dangerscarf) / [jonathansoma.com](https://jonathansoma.com/)

## Setup and Installation

Avoid setup and just [use these notebooks on Google Colab](http://colab.research.google.com/github/jsoma/nicar25-ai-newsroom/).

### Your own machine

Various Pythons may or may not work for this – I use 3.10 or 3.11, not exactly sure about more recent ones. I think all of the `pip install` commands are in the Jupyter notebooks themselves, so you shouldn't need anything on that front. Maybe `brew install ffmpeg`, depending on what you're up to.

### NICAR computer setup instructions you can probably ignore

I mean you can also run this on your computer I guess but no guarantees!

```
brew install ffmpeg
brew install pyenv
mkdir -p ~/Desktop/hands_on_classes/20250307-friday-using-ai-tools-in-the-newsroom-pre-registered-attendees-only
cd ~/Desktop/hands_on_classes/20250307-friday-using-ai-tools-in-the-newsroom-pre-registered-attendees-only
pyenv install "3.11"
pyenv local "3.11"
PYENV_VERSION=3.11 pyenv exec python -m venv env
source env/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name="ai-newsroom" --display-name="AI Newsroom"
python test/test-cache.py
```

Also, download [Msty](https://msty.app/) and then open it up and click 'setup local AI' (or 'continue' down at the bottom if there are any ollama models around).