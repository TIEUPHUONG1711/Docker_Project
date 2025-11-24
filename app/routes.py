from flask import Blueprint, jsonify
import random
from flask import render_template 

main = Blueprint('main', __name__)

# Danh sách quotes
quotes = [
    "Do one thing every day that scares you. – Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Keep going. Be all in. – Bryan Hutchinson",
    "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "Dream big and dare to fail. – Norman Vaughan",
    "The best way to predict the future is to create it. – Peter Drucker",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Courage is grace under pressure. – Ernest Hemingway",
    "The journey of a thousand miles begins with one step. – Lao Tzu",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Believe in yourself and all that you are. – Christian D. Larson",
    "Act as if what you do makes a difference. It does. – William James",
    "Great things never come from comfort zones.",
    "Don’t wait for opportunity. Create it.",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau"
]


@main.route('/')
def quote_of_the_day():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})


@main.route('/web')
def quote_web():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote) 