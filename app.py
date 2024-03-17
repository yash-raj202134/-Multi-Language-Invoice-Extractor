from dotenv import load_dotenv

load_dotenv()  ## load all the environment variables from .env


import streamlit as st
import os
from PIL import Image

import google.generativeai as genai


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


