import pandas as pd
from openai import OpenAI
import whisperx
import torch
import whisper
import yt_dlp
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel, Field
from typing import Literal, List
from llama_index.core.response_synthesizers import TreeSummarize
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

print("## Loading pandas")
df = pd.DataFrame({
    'title': [
        'Trees in space',
        'Taxes on people who are in outer space',
        'Medical expenses for aliens',
        'Pinecones orbiting the planet'
    ]
})


print("## Loading whisper tiny.en")
model = whisper.load_model("tiny.en")

print("## Loading whisperx tiny.en")
model = whisperx.load_model("tiny.en", "cpu", compute_type="int8")


print("## Running yt-dlp (video)")

url = "https://www.youtube.com/watch?v=uvQK7WTkKpI"

ydl_opts = {
    'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',  # Max 720p
    'outtmpl': '%(title)s.%(ext)s',  # Save file as video title
    'merge_output_format': 'mp4',  # Ensure MP4 format
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("## Running yt-dlp (audio)")

url = "https://www.youtube.com/watch?v=uvQK7WTkKpI"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'},  # Converts to MP3
        {'key': 'FFmpegMetadata'},  # Embeds metadata
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


print("## Running Pydantic")
class TranscriptSummary(BaseModel):
    """Data model for a transcript."""
    topic: str = Field(description="One-sentence blurb about transcript content")
    summary: str = Field(description="Summary of content covered, covering all major points")
    highlights: str = Field(description="Most interesting fact(s) from transcript")

print("## Classifying")
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")


print("## Translating")
en_fr_translator = pipeline("translation_en_to_fr")
en_fr_translator("How old are you?")

print("## More translating")
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
translator("How old are you?")

translator = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh")
translator("How old are you?")

translator = pipeline("translation_zh_to_en", model="Helsinki-NLP/opus-mt-zh-en")
translator("你几岁了?")

print("## More translating x2")
translator = pipeline(
    "translation_ja_to_en",
    model="facebook/nllb-200-distilled-600M")
translator("私は鉛筆です")

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang='jpn_Jpan',
    tgt_lang='eng_Latn')
translator("私は鉛筆です")

print("## Embedding")

sentences = ["cat"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

print("## Cosine similarity")

similarities = cosine_similarity(embeddings)

# Turn into a dataframe
pd.DataFrame(similarities,
            index=sentences,
            columns=sentences) \
            .style \
            .background_gradient(axis=None)

print("## More embeddings")

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')
embeddings = model.encode(sentences)


def greet(name):
    return "Hello " + name + "!!"

print("## Gradio")

iface = gr.Interface(fn=greet, inputs="text", outputs="text")


embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
embeddings = embed_model.get_text_embedding("Hello World!")

print("## Encode some things")

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")
Settings.embed_model = embed_model