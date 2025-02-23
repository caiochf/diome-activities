{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "nDIpn3vESeXY",
    "outputId": "c9ff7e6b-0c74-493d-a2b1-fe7da0413d19"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done!\n"
     ]
    }
   ],
   "source": [
    "# Uncomment if needed\n",
    "!pip install gTTS langdetect playsound SpeechRecognition pyjokes --quiet\n",
    "\n",
    "print('Done!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0nAaXaQbdcfz"
   },
   "source": [
    "# Set Up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "yrz0E1euTyTp"
   },
   "outputs": [],
   "source": [
    "from gtts import gTTS\n",
    "from langdetect import detect\n",
    "from IPython.display import Audio"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3qndSVrNdx5R"
   },
   "source": [
    "---\n",
    "\n",
    "# Text 2 speech\n",
    "\n",
    "Here the user can type any text in any language. The code will automatically detect the language and, after, you can hear it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "pJj1WsYrUF4u",
    "outputId": "20e0cdd1-ffab-482c-f3ad-c2ea943a0c12"
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type what you want to be said:  Jo me llamo Caio\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Detected language: es\n"
     ]
    }
   ],
   "source": [
    "speech = input('Type what you want to be said: ')\n",
    "\n",
    "language = detect(speech)\n",
    "\n",
    "print(f'Detected language: {language}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 61
    },
    "id": "saUH6grOTv-a",
    "outputId": "4b92440a-ba6c-420b-cf58-905804633b66"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "                <audio  controls=\"controls\" >\n",
       "                    <source src=\"data:audio/x-wav;base64,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\" type=\"audio/x-wav\" />\n",
       "                    Your browser does not support the audio element.\n",
       "                </audio>\n",
       "              "
      ],
      "text/plain": [
       "<IPython.lib.display.Audio object>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gtts_object = gTTS(text = speech,\n",
    "                  lang = language,\n",
    "                  slow = True)\n",
    "\n",
    "gtts_object.save(\"gtts.wav\")\n",
    "Audio(\"gtts.wav\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Fx40V1eFVRMf"
   },
   "source": [
    "---\n",
    "\n",
    "# Speech 2 text\n",
    "\n",
    "Here the user can say some preestablished commands aloud and they will be done if recognized.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "1eBBiGyKfHbv",
    "outputId": "a76ede54-f2d8-4459-9eb8-defce8701700"
   },
   "outputs": [],
   "source": [
    "!pip install pygame --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "sU2rDZEqVkbP",
    "outputId": "4c7db213-175c-4239-b107-3c2992fdb668"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 2.6.1 (SDL 2.28.4, Python 3.10.12)\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "import os\n",
    "from datetime import datetime\n",
    "import playsound\n",
    "import pyjokes\n",
    "import webbrowser\n",
    "from pygame import mixer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 426
    },
    "id": "080R1VDHVQbP",
    "outputId": "45498fe8-9987-4d3b-cb3e-c80d383a3f5c"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear\n",
      "ALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe\n",
      "ALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_oss.c:397:(_snd_pcm_oss_open) Cannot open device /dev/dsp\n",
      "ALSA lib pcm_oss.c:397:(_snd_pcm_oss_open) Cannot open device /dev/dsp\n",
      "ALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\n",
      "ALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\n",
      "ALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\n",
      "ALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\n",
      "ALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear\n",
      "ALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe\n",
      "ALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\n",
      "ALSA lib pcm_oss.c:397:(_snd_pcm_oss_open) Cannot open device /dev/dsp\n",
      "ALSA lib pcm_oss.c:397:(_snd_pcm_oss_open) Cannot open device /dev/dsp\n",
      "ALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\n",
      "ALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\n",
      "ALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\n",
      "ALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "I am listening...\n",
      "Text from get audio \n",
      "I am listening...\n",
      "Text from get audio \n",
      "I am listening...\n",
      "YouTube\n",
      "Text from get audio youtube\n",
      "nothing\n",
      "I am listening...\n",
      "joke\n",
      "Text from get audio joke\n",
      "I am listening...\n",
      "Text from get audio \n",
      "I am listening...\n",
      "exit\n",
      "Text from get audio exit\n",
      "I am listening...\n",
      "Text from get audio \n",
      "I am listening...\n",
      "exit\n",
      "Text from get audio exit\n",
      "I am listening...\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 86\u001b[0m\n\u001b[1;32m     84\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[1;32m     85\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI am listening...\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m---> 86\u001b[0m     text \u001b[38;5;241m=\u001b[39m \u001b[43mget_audio\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     87\u001b[0m     respond(text)\n",
      "Cell \u001b[0;32mIn[4], line 12\u001b[0m, in \u001b[0;36mget_audio\u001b[0;34m()\u001b[0m\n\u001b[1;32m     10\u001b[0m said \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     11\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m---> 12\u001b[0m     said \u001b[38;5;241m=\u001b[39m \u001b[43mr\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrecognize_google\u001b[49m\u001b[43m(\u001b[49m\u001b[43maudio\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     13\u001b[0m     \u001b[38;5;28mprint\u001b[39m(said)\n\u001b[1;32m     14\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m sr\u001b[38;5;241m.\u001b[39mUnknownValueError:\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/speech_recognition/recognizers/google.py:255\u001b[0m, in \u001b[0;36mrecognize_legacy\u001b[0;34m(recognizer, audio_data, key, language, pfilter, show_all, with_confidence, endpoint)\u001b[0m\n\u001b[1;32m    250\u001b[0m request_builder \u001b[38;5;241m=\u001b[39m create_request_builder(\n\u001b[1;32m    251\u001b[0m     endpoint\u001b[38;5;241m=\u001b[39mendpoint, key\u001b[38;5;241m=\u001b[39mkey, language\u001b[38;5;241m=\u001b[39mlanguage, filter_level\u001b[38;5;241m=\u001b[39mpfilter\n\u001b[1;32m    252\u001b[0m )\n\u001b[1;32m    253\u001b[0m request \u001b[38;5;241m=\u001b[39m request_builder\u001b[38;5;241m.\u001b[39mbuild(audio_data)\n\u001b[0;32m--> 255\u001b[0m response_text \u001b[38;5;241m=\u001b[39m \u001b[43mobtain_transcription\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    256\u001b[0m \u001b[43m    \u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrecognizer\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moperation_timeout\u001b[49m\n\u001b[1;32m    257\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    259\u001b[0m output_parser \u001b[38;5;241m=\u001b[39m OutputParser(\n\u001b[1;32m    260\u001b[0m     show_all\u001b[38;5;241m=\u001b[39mshow_all, with_confidence\u001b[38;5;241m=\u001b[39mwith_confidence\n\u001b[1;32m    261\u001b[0m )\n\u001b[1;32m    262\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m output_parser\u001b[38;5;241m.\u001b[39mparse(response_text)\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/speech_recognition/recognizers/google.py:215\u001b[0m, in \u001b[0;36mobtain_transcription\u001b[0;34m(request, timeout)\u001b[0m\n\u001b[1;32m    213\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mobtain_transcription\u001b[39m(request: Request, timeout: \u001b[38;5;28mint\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28mstr\u001b[39m:\n\u001b[1;32m    214\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 215\u001b[0m         response \u001b[38;5;241m=\u001b[39m \u001b[43murlopen\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    216\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m HTTPError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    217\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m RequestError(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrecognition request failed: \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;241m.\u001b[39mformat(e\u001b[38;5;241m.\u001b[39mreason))\n",
      "File \u001b[0;32m/usr/lib/python3.10/urllib/request.py:216\u001b[0m, in \u001b[0;36murlopen\u001b[0;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[1;32m    214\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m    215\u001b[0m     opener \u001b[38;5;241m=\u001b[39m _opener\n\u001b[0;32m--> 216\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mopener\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mopen\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdata\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/usr/lib/python3.10/urllib/request.py:519\u001b[0m, in \u001b[0;36mOpenerDirector.open\u001b[0;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[1;32m    516\u001b[0m     req \u001b[38;5;241m=\u001b[39m meth(req)\n\u001b[1;32m    518\u001b[0m sys\u001b[38;5;241m.\u001b[39maudit(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124murllib.Request\u001b[39m\u001b[38;5;124m'\u001b[39m, req\u001b[38;5;241m.\u001b[39mfull_url, req\u001b[38;5;241m.\u001b[39mdata, req\u001b[38;5;241m.\u001b[39mheaders, req\u001b[38;5;241m.\u001b[39mget_method())\n\u001b[0;32m--> 519\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mreq\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdata\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    521\u001b[0m \u001b[38;5;66;03m# post-process response\u001b[39;00m\n\u001b[1;32m    522\u001b[0m meth_name \u001b[38;5;241m=\u001b[39m protocol\u001b[38;5;241m+\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m_response\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "File \u001b[0;32m/usr/lib/python3.10/urllib/request.py:536\u001b[0m, in \u001b[0;36mOpenerDirector._open\u001b[0;34m(self, req, data)\u001b[0m\n\u001b[1;32m    533\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m result\n\u001b[1;32m    535\u001b[0m protocol \u001b[38;5;241m=\u001b[39m req\u001b[38;5;241m.\u001b[39mtype\n\u001b[0;32m--> 536\u001b[0m result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_call_chain\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhandle_open\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mprotocol\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mprotocol\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\n\u001b[1;32m    537\u001b[0m \u001b[43m                          \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m_open\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreq\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    538\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m result:\n\u001b[1;32m    539\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[0;32m/usr/lib/python3.10/urllib/request.py:496\u001b[0m, in \u001b[0;36mOpenerDirector._call_chain\u001b[0;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[1;32m    494\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m handler \u001b[38;5;129;01min\u001b[39;00m handlers:\n\u001b[1;32m    495\u001b[0m     func \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mgetattr\u001b[39m(handler, meth_name)\n\u001b[0;32m--> 496\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    497\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m result \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    498\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[0;32m/usr/lib/python3.10/urllib/request.py:1377\u001b[0m, in \u001b[0;36mHTTPHandler.http_open\u001b[0;34m(self, req)\u001b[0m\n\u001b[1;32m   1376\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mhttp_open\u001b[39m(\u001b[38;5;28mself\u001b[39m, req):\n\u001b[0;32m-> 1377\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdo_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhttp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mclient\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mHTTPConnection\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreq\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/usr/lib/python3.10/urllib/request.py:1352\u001b[0m, in \u001b[0;36mAbstractHTTPHandler.do_open\u001b[0;34m(self, http_class, req, **http_conn_args)\u001b[0m\n\u001b[1;32m   1350\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err: \u001b[38;5;66;03m# timeout error\u001b[39;00m\n\u001b[1;32m   1351\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m URLError(err)\n\u001b[0;32m-> 1352\u001b[0m     r \u001b[38;5;241m=\u001b[39m \u001b[43mh\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgetresponse\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   1353\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m:\n\u001b[1;32m   1354\u001b[0m     h\u001b[38;5;241m.\u001b[39mclose()\n",
      "File \u001b[0;32m/usr/lib/python3.10/http/client.py:1375\u001b[0m, in \u001b[0;36mHTTPConnection.getresponse\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1373\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m   1374\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m-> 1375\u001b[0m         \u001b[43mresponse\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbegin\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   1376\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mConnectionError\u001b[39;00m:\n\u001b[1;32m   1377\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclose()\n",
      "File \u001b[0;32m/usr/lib/python3.10/http/client.py:318\u001b[0m, in \u001b[0;36mHTTPResponse.begin\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    316\u001b[0m \u001b[38;5;66;03m# read until we get a non-100 response\u001b[39;00m\n\u001b[1;32m    317\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m--> 318\u001b[0m     version, status, reason \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_read_status\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    319\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m status \u001b[38;5;241m!=\u001b[39m CONTINUE:\n\u001b[1;32m    320\u001b[0m         \u001b[38;5;28;01mbreak\u001b[39;00m\n",
      "File \u001b[0;32m/usr/lib/python3.10/http/client.py:279\u001b[0m, in \u001b[0;36mHTTPResponse._read_status\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    278\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_read_status\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m--> 279\u001b[0m     line \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreadline\u001b[49m\u001b[43m(\u001b[49m\u001b[43m_MAXLINE\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m)\u001b[49m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124miso-8859-1\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    280\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(line) \u001b[38;5;241m>\u001b[39m _MAXLINE:\n\u001b[1;32m    281\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m LineTooLong(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstatus line\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[0;32m/usr/lib/python3.10/socket.py:705\u001b[0m, in \u001b[0;36mSocketIO.readinto\u001b[0;34m(self, b)\u001b[0m\n\u001b[1;32m    703\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[1;32m    704\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 705\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_sock\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrecv_into\u001b[49m\u001b[43m(\u001b[49m\u001b[43mb\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    706\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m timeout:\n\u001b[1;32m    707\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_timeout_occurred \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "#get mic audio\n",
    "def get_audio():\n",
    "    r = sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        r.pause_threshold = 1\n",
    "        # wait for a second to let the recognizer adjust the\n",
    "        # energy threshold based on the surrounding noise level\n",
    "        r.adjust_for_ambient_noise(source, duration=1)\n",
    "        audio = r.listen(source)\n",
    "        said = \"\"\n",
    "        try:\n",
    "            said = r.recognize_google(audio)\n",
    "            print(said)\n",
    "        except sr.UnknownValueError:\n",
    "            speak(\"Sorry, I did not get that.\")\n",
    "        except sr.RequestError:\n",
    "            speak(\"Sorry, the service is not available\")\n",
    "    return said.lower()\n",
    "\n",
    "#speak converted audio to text\n",
    "def speak(text):\n",
    "    tts = gTTS(text=text, lang='en')\n",
    "    filename = \"voice.mp3\"\n",
    "    try:\n",
    "        os.remove(filename)\n",
    "    except OSError:\n",
    "        pass\n",
    "    tts.save(filename)\n",
    "    playsound.playsound(filename)\n",
    "\n",
    "#function to respond to commands\n",
    "def respond(text):\n",
    "    print(\"Text from get audio \" + text)\n",
    "    if 'youtube' in text:\n",
    "        speak(\"What do you want to search for?\")\n",
    "        keyword = get_audio()\n",
    "        if keyword!= '':\n",
    "            url = f\"https://www.youtube.com/results?search_query={keyword}\"\n",
    "            webbrowser.get().open(url)\n",
    "            speak(f\"Here is what I have found for {keyword} on youtube\")\n",
    "    elif 'search' in text:\n",
    "        speak(\"What do you want to search for?\")\n",
    "        query = get_audio()\n",
    "        if query !='':\n",
    "            result = wikipedia.summary(query, sentences=3)\n",
    "            speak(\"According to wikipedia\")\n",
    "            print(result)\n",
    "            speak(result)\n",
    "    elif 'joke' in text:\n",
    "        speak(pyjokes.get_joke())\n",
    "    elif 'empty recycle bin' in text:\n",
    "        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)\n",
    "        speak(\"Recycle bin emptied\")\n",
    "    elif 'what time' in text:\n",
    "        strTime = datetime.today().strftime(\"%H:%M %p\")\n",
    "        print(strTime)\n",
    "        speak(strTime)\n",
    "    # elif 'play music' in text or 'play song' in text:\n",
    "    #     speak(\"Now playing...\")\n",
    "    #     music_dir = \"C:\\\\Users\\\\UserName\\\\Downloads\\\\Music\\\\\" #add your music directory here..\n",
    "    #     songs = os.listdir(music_dir)\n",
    "    #     #counter = 0\n",
    "    #     print(songs)\n",
    "    #     playmusic(music_dir + \"\\\\\" + songs[0])\n",
    "    # elif 'stop music' in text:\n",
    "    #     speak(\"Stopping playback.\")\n",
    "    #     stopmusic()\n",
    "    elif 'exit' in text:\n",
    "        speak(\"Goodbye, till next time\")\n",
    "        exit()\n",
    "#play music\n",
    "# def playmusic(song):\n",
    "#     mixer.init()\n",
    "#     mixer.music.load(song)\n",
    "#     mixer.music.play()\n",
    "# #stop music\n",
    "# def stopmusic():\n",
    "#     mixer.music.stop()\n",
    "\n",
    "#let's try it\n",
    "text = get_audio()\n",
    "speak(text)\n",
    "\n",
    "while True:\n",
    "    print(\"I am listening...\")\n",
    "    text = get_audio()\n",
    "    respond(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "vwBSGP_Ae94v"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
