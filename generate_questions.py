# -*- coding: utf-8 -*-
"""
Master Question Bank Generator for MedBank Studio.
Combines all curated, brand-new clinical questions (Part 1, Part 2, Part 3)
and Professional Dilemmas questions into questions.json.
All previous questions have been replaced with this fresh, high-yield bank.
"""

import json
import random
from part1_questions import PART1_QUESTIONS
from part2_questions import PART2_QUESTIONS
from part3_questions import PART3_QUESTIONS
from pd_questions import PD_QUESTIONS
from part4_questions import PART4_QUESTIONS

# Fixed seed for deterministic generation
random.seed(42)

def generate_questions():
    all_raw_questions = PART1_QUESTIONS + PART2_QUESTIONS + PART3_QUESTIONS + PART4_QUESTIONS + PD_QUESTIONS
    
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
            # For ranking, options can be shuffled, but correct_answer is the ordered list (rank 1 to 5)
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
            # For selection, options can be shuffled, correct_answer contains the 3 chosen options
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
        
    print(f"Successfully generated {len(questions)} brand-new questions across all categories.")

if __name__ == "__main__":
    generate_questions()
