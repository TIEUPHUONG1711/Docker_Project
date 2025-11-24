from flask import Blueprint, jsonify
import random

main = Blueprint('main', __name__)

# Danh sách quotes
quotes = [
    "Do one thing every day that scares you. – Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Keep going. Be all in. – Bryan Hutchinson"
]

@main.route('/')
def quote_of_the_day():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})
