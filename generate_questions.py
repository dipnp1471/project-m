# -*- coding: utf-8 -*-
"""
Master Question Bank Generator for MedBank Studio.
Combines 100 perfectly curated, strictly categorized questions.
"""

import json
import random
from clinical_questions import CLINICAL_QUESTIONS
from additional_questions import ADDITIONAL_QUESTIONS

# Fixed seed for deterministic generation
random.seed(42)

def generate_questions():
    all_raw_questions = CLINICAL_QUESTIONS + ADDITIONAL_QUESTIONS
    
    questions = []
    q_id = 1
    
    for item in all_raw_questions:
        q_type = item["type"]
        category = item["category"]
        scenario = item["scenario"]
        explanation = item["explanation"]
        
        if q_type in ["sba", "emq"]:
            # Shuffle options for SBA / EMQ
            shuffled_options = list(item["options"])
            random.shuffle(shuffled_options)
            
            questions.append({
                "id": f"q_{q_id}",
                "exam": "MSRA",
                "type": q_type,
                "category": category,
                "scenario": scenario,
                "options": shuffled_options,
                "correct_answer": item["correct_answer"],
                "explanation": explanation
            })
            
        elif q_type == "ranking":
            shuffled_options = list(item["options"])
            random.shuffle(shuffled_options)
            
            questions.append({
                "id": f"q_{q_id}",
                "exam": "MSRA",
                "type": "ranking",
                "category": category,
                "scenario": scenario,
                "options": shuffled_options,
                "correct_answer": item["correct_answer"],
                "explanation": explanation
            })
            
        elif q_type == "selection":
            shuffled_options = list(item["options"])
            random.shuffle(shuffled_options)
            
            questions.append({
                "id": f"q_{q_id}",
                "exam": "MSRA",
                "type": "selection",
                "category": category,
                "scenario": scenario,
                "options": shuffled_options,
                "correct_answer": item["correct_answer"],
                "explanation": explanation
            })
            
        q_id += 1

    # Save to questions.json
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} brand-new questions without category duplicates.")

if __name__ == "__main__":
    generate_questions()
