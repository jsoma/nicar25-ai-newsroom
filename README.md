# AI in the Newsroom

## NICAR 2025, Minneapolis

Jonathan Soma

jonathan.soma@gmail.com / [@dangerscarf](https://twitter.com/dangerscarf) / [jonathansoma.com](https://jonathansoma.com/)

## Using this on the cloud

[Visit Google Colab here](http://colab.research.google.com/github/jsoma/nicar25-ai-newsroom/)

## NICAR computer setup instructions you can probably ignore

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