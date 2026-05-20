from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F


model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def get_final_news_score(news_list):
    total_positive = 0
    total_negative = 0
    count = len(news_list)

    print(f"--- Individual Headline Analysis ---")
    
    for headline in news_list:
        # 1. Tokenize and Predict
        inputs = tokenizer(headline, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        
        probs = F.softmax(outputs.logits, dim=-1)
        pos, neg, neu = float(probs[0][0]), float(probs[0][1]), float(probs[0][2])
        
        # Accumulate scores
        total_positive += pos
        total_negative += neg
        
        print(f"Headline: {headline[:50]}...")
        print(f"  -> Positive: {pos:.2%}, Negative: {neg:.2%}, Neutral: {neu:.2%}\n")

    # 2. Calculate Averages
    avg_pos = total_positive / count
    avg_neg = total_negative / count
    
    # 3. The Final Sentiment Score Formula: (Avg Positive - Avg Negative)
    # This gives a range from -1 to +1
    final_score = avg_pos - avg_neg
    
    return final_score

news_data = [
    "Aeroflex Industries sees breakout above descending trendline with higher highs, lows. Stock shows bullish signals with rounded bottom, increasing volume, and engulfing candles.",
    "QE Securities LLP bought 725,159 shares of Aeroflex Industries at an avg price of 385.8.",
    "Junomoneta Finsol Pvt Ltd bought 802,493 shares of Aeroflex Industries at ₹388.3 avg."
]

final_sentiment = get_final_news_score(news_data)
final_sentiment = final_sentiment  * 100 
final_sentiment = round(final_sentiment, 2)
print(f"--- FINAL SUMMARY ---")
print(f"Final Aggregate Score: {final_sentiment}%")


# Interpretation logic
if final_sentiment > 15.0:
    print("Verdict: BULLISH")
elif final_sentiment  < -15.0:
    print("Verdict: BEARISH")
else:
    print("Verdict: NEUTRAL / MIXED")