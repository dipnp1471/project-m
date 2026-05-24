import json
import sys

def verify():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            questions = json.load(f)
    except Exception as e:
        print(f"Error loading questions.json: {e}")
        sys.exit(1)
        
    print(f"Loaded {len(questions)} questions.")
    errors = 0
    
    for idx, q in enumerate(questions):
        q_id = q.get("id", f"unknown_{idx}")
        q_type = q.get("type")
        
        # Verify required keys
        required_keys = ["id", "exam", "type", "category", "scenario", "options", "correct_answer", "explanation"]
        for key in required_keys:
            if key not in q:
                print(f"Error in {q_id}: Missing key '{key}'")
                errors += 1
                
        # Check type
        if q_type not in ["sba", "emq", "ranking", "selection"]:
            print(f"Error in {q_id}: Unknown type '{q_type}'")
            errors += 1
            
        options = q.get("options", [])
        correct = q.get("correct_answer")
        
        # Verification per type
        if q_type == "sba":
            if not isinstance(correct, str):
                print(f"Error in {q_id}: correct_answer should be a string, got {type(correct)}")
                errors += 1
            elif correct not in options:
                print(f"Error in {q_id}: correct_answer '{correct}' not in options {options}")
                errors += 1
                
        elif q_type == "emq":
            if not isinstance(correct, str):
                print(f"Error in {q_id}: correct_answer should be a string, got {type(correct)}")
                errors += 1
            elif correct not in options:
                print(f"Error in {q_id}: correct_answer '{correct}' not in options {options}")
                errors += 1
                
        elif q_type == "ranking":
            if not isinstance(correct, list):
                print(f"Error in {q_id}: correct_answer should be a list for ranking, got {type(correct)}")
                errors += 1
            else:
                for c in correct:
                    if c not in options:
                        print(f"Error in {q_id}: Ranked answer option '{c}' not found in options {options}")
                        errors += 1
                        
        elif q_type == "selection":
            if not isinstance(correct, list):
                print(f"Error in {q_id}: correct_answer should be a list for selection, got {type(correct)}")
                errors += 1
            elif len(correct) != 3:
                print(f"Error in {q_id}: correct_answer must contain exactly 3 options, got {len(correct)}")
                errors += 1
            else:
                for c in correct:
                    if c not in options:
                        print(f"Error in {q_id}: Selected answer option '{c}' not found in options {options}")
                        errors += 1
                        
    if errors == 0:
        print("Verification SUCCESS! All questions are valid.")
        sys.exit(0)
    else:
        print(f"Verification FAILED with {errors} errors.")
        sys.exit(1)

if __name__ == "__main__":
    verify()
