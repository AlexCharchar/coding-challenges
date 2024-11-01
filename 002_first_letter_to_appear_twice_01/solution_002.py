def repeatedCharacter(s):
	store = {}
   
	for char in s:
        # Increment the count for each character, starting from 0 if it's new
            store[char] = store.get(char, 0) + 1
        
        # Return the character as soon as it appears twice
            if store[char] == 2:
                return char
