# Movie Magic: Your Personalized Film Guide

Welcome to the **Movie Recommendation Enchanter** – your ticket to discovering a world of cinematic wonders tailored just for you! 🍿🎬
![Picture](https://github.com/Hrishita-Shah/Movie-Recommendation-Enchanter/assets/97698248/4d66dd50-e907-4fb2-a449-0f916c83f0b7)

[![Watch the Video](https://github.com/Hrishita-Shah/Movie-Recommendation-Enchanter/assets/97698248/4d66dd50-e907-4fb2-a449-0f916c83f0b7)](https://www.kapwing.com/videos/64e904e752f0f2001e280d94)

## Lights, Camera, Algorithm!

Lights dimmed, algorithm powered up! 🌟 Brace yourself for a movie journey like no other. The Movie Recommendation Enchanter, meticulously crafted and tested on the enchanting lands of Windows 11 with Python 3.9, is ready to sweep you off your feet.

## What's the Buzz?

What's the Buzz?
Have you ever wondered how Netflix seems to know your cinematic cravings even before you do? Ever wished for a movie sidekick that could read your mind? Look no further! This web app is a silver screen oracle, conjuring movie recommendations based on your searches.


## A Tapestry of Recommendations

In the realm of recommendation, three archetypes reign supreme:

1. **Content-Based Enchantment**: The algorithm peers into a movie's heart – its title, overview, genre, director, actors – and crafts suggestions based on these enchanting threads.
2. **Collaborative Conjuring**: Through the collective cinematic consciousness, the system unveils recommendations, aligning with the viewer's past choices.
3. **Hybrid Harmony**: By fusing the powers of content-based magic and collaborative sorcery, a harmonious blend of recommendations is born.


## The Enchanted Mechanics

Curious about the mechanics? Let's peer behind the curtains! 🧐 At its core, this system weaves its magic thus:

1. The original dataset is forged anew through preprocessing, birthing the ultimate dataset.
2. This dataset serves as the canvas for our recommendations. It is transformed into a tapestry of vectors, wherein the threads of similarity are woven.
3. Behold the algorithm's artistry! The top 9 recommendations emerge, each shimmering with cinematic allure.
4. Delve deeper! With the help of the IMDb module, the movie's essence is distilled – ratings, story, cast, genres, and more.
5. But that's not all – the trailer, a glimpse into the movie's soul, is summoned using the Youtube API.
6. Behold the posters, plucked from the ethereal realm of TMDB, all thanks to our web scraping incantations.
7. The grand stage, the web app, is conjured through the powers of Streamlit.


## Unveiling the Cinematic Spell

Let's unravel the cinematic spell, shall we? 🧙‍♂️ To embark on this journey, here's your enchanted map:

1. Clone this magical repository to your realm.
2. Retrieve the mystic TMDB movie dataset from Kaggle (tap here: [TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)).
3. Gently place the dataset within the folder.
4. Brew a virtual environment using Python 3.9, and invoke the packages listed in the requirements.txt spellbook.
5. Cast the spell of Movie-Recommender-System.ipynb within the folder realm, yielding the cherished artifact - tmdb_5000_credits.csv and tmdb_5000_movies.csv.
6. Summon the Movie Recommender System.ipynb, conjuring two enchanted artifacts: similarity.pkl and movies_dict.pkl. These artifacts hold the key to our recommendations.
7. Safely transport these artifacts to the main folder, ready to empower the enchantment.
8. Bestow your TMDB API key within the app.py spellbook, under the watchful eye of the fetch_poster function.
9. With bated breath, chant the incantation "streamlit run app.py" within your terminal, while stationed within the main directory. A web app shall awaken before you, an apparition mirroring the image in the scroll below.

## Secrets of the API Key

Ah, the fabled API key! To unlock the cinematic vaults, follow this ritual:

1. Ascend to the realm of [The Movie Database](https://www.themoviedb.org/).
2. In your account sanctum, traverse to the API section, nestled in the sidebar.
3. There, scribe your details, beseeching for the coveted API key. Fear not, even if your realm lacks a digital home, simply scribe "NA."
4. As the cosmic winds carry your request, the API key shall materialize in the sacred API sidebar.


## The Alchemist's Toolkit

Every enchanter wields tools of power. Our arsenal includes:

- The scrolls of SKlearn, Numpy, Pandas, Scipy, Streamlit and Python.
- The messenger, Requests, for communing with distant servers.
- The linguistic gem, NLTK, for language mastery and the ultimate enchantment:
  - **CountVectorizer**: A spellbinding NLP technique that transforms movie tags – from overview to genres, keywords, and even the cast & crew – into numerical vectors.
  - **Cosine Similarity**: Our chosen metric of magic, which quantifies the angles between these vectors, summoning forth the power of similarity.


## License and Open-Source Contributions

📜 **License**: The Movie Recommendation Enchanter is proudly enchanted under the [MIT License](LICENSE). This means you're free to use, modify, and distribute this enchantment as you please, but do remember to credit the original enchanter and include the license notice.

🤝 **Open-Source Contributions**: Magic flourishes when minds converge! If you're as passionate about cinema and algorithms as we are, we welcome your contributions to this magical endeavor. Whether it's fixing a bug, enhancing recommendations, or weaving new features, every spell you cast is appreciated. Just follow the incantations in our [Contributing Guidelines](CONTRIBUTING.md) to get started on your journey.

## Your Cinematic Destiny Awaits

Unveil the curtain, embrace the magic, and immerse yourself in the captivating world of the **Movie Recommendation Enchanter**. Your cinematic destiny awaits! 🌌🎥🔮
