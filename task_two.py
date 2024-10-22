from collections import deque

def is_palindrome(s: str) -> bool:
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    deq = deque(cleaned_str)

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    
    return True

print(is_palindrome("Pan ap"))  
