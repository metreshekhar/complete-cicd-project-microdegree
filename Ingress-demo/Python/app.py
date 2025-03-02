from flask import Flask, render_template

app = Flask(__name__)

# Data representing some information about Naruto
naruto_info = {
    "title": "Naruto Uzumaki",
    "description": "Naruto Uzumaki is a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the village leader. He is the main protagonist of the anime series 'Naruto' and 'Naruto Shippuden'.",
    "background": "Born as the son of the Fourth Hokage, Naruto's life was marked by hardship as he was shunned by the villagers due to the Nine-Tails fox demon sealed within him.",
    "goals": "Naruto's goal is to become the Hokage, protect his village, and gain the respect of the people who once feared and hated him.",
    "quotes": [
        "I never go back on my word! That's my nindo: my ninja way!",
        "The reason I keep going is because I know there's always something better ahead.",
        "A lesson without pain is meaningless. That’s because no one can gain without sacrificing something. But by enduring that pain and overcoming it, he shall obtain a powerful, unmatched heart."
    ]
}

# Characters data
characters = [
    {
        "name": "Naruto Uzumaki",
        "role": "Main protagonist, the jinchuriki of the Nine-Tails",
        "image": "https://example.com/naruto.jpg"  # You can replace this with a real URL for images.
    },
    {
        "name": "Sasuke Uchiha",
        "role": "Naruto’s best friend and rival",
        "image": "https://example.com/sasuke.jpg"
    },
    {
        "name": "Sakura Haruno",
        "role": "One of Naruto’s teammates, skilled in medical ninjutsu",
        "image": "https://example.com/sakura.jpg"
    },
    {
        "name": "Kakashi Hatake",
        "role": "Naruto’s sensei and one of the strongest ninjas in the series",
        "image": "https://example.com/kakashi.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html', naruto_info=naruto_info, characters=characters)

@app.route('/about')
def about():
    return render_template('about.html', naruto_info=naruto_info)

@app.route('/characters')
def characters_page():
    return render_template('characters.html', characters=characters)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
