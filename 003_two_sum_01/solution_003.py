def twoSum(nums, target):
    hash_map = {}  # Dictionary to store value:index pairs for quick lookups
    
    for i in range(len(nums)):
        # Calculate the number needed to reach the target
        match_pair = target - nums[i]  
     
        # Check if the required number is already in the dictionary
        if match_pair in hash_map:
            # If found, return the indices of the matching pair
            return (hash_map[match_pair], i)
    
        # Store the current number and its index in the dictionary
        hash_map[nums[i]] = i