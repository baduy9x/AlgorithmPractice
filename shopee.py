# Input: [("a", "b"), ("m", "n"), ("n", "s"), ("a", "f"), ("f", "z")]
# Output:[["a", "b", "f", "z"], ["m", "n", "s"]]



from collections import defaultdict

def agg_element(s):
    mapping = defaultdict(list)
    for i, item in enumerate(s):
        mapping[item[0]].append(i)
        mapping[item[1]].append(i)
        
    seen_idx = set()
    seen_character = set()
    final_result = []
    
    for i, item in enumerate(s):
        result_element = []
        
        if i in seen_idx:
            continue
        
        seen_idx.add(i)
        
        stack = [item[0]]
        while stack:
            current_element = stack.pop()
            
            #print(current_element, seen_character)
            
            if current_element in seen_character:
                continue
            
            
            seen_character.add(current_element)
            result_element.append(current_element)
            
            for idx in mapping[current_element]:
                if idx not in seen_idx:
                    if s[idx][0] not in seen_character:
                        stack.append(s[idx][0])
                        seen_idx.add(idx)
                    
                    if s[idx][1] not in seen_character:
                        stack.append(s[idx][1])
                        seen_idx.add(idx)
                        
        stack = [item[1]]
        while stack:
            current_element = stack.pop()
            
            if current_element in seen_character:
                continue
            
            seen_character.add(current_element)
            
            result_element.append(current_element)
            
            for idx in mapping[current_element]:
                if idx not in seen_idx:
                    if s[idx][0] not in seen_character:
                        stack.append(s[idx][0])
                        seen_idx.add(idx)
                    
                    if s[idx][1] not in seen_character:
                        stack.append(s[idx][1])
                        seen_idx.add(idx)
        
        final_result.append(result_element)
        #print(result_element)
    return final_result
            
    
    

if __name__ == '__main__':
    print(agg_element([("a", "b"), ("m", "n"), ("n", "s"), ("a", "f"), ("f", "z")]))
     
