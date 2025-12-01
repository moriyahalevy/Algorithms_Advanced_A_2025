import heapq

def merge_sorted_lists(lists, key=lambda x: x):
    min_heap = []
    
    # האיבר בערימה יהיה טאפל: (מפתח, ערך מקורי, אינדקס רשימה, אינדקס פריט בתוך הרשימה)
    for list_index, current_list in enumerate(lists):
        if current_list:
            item = current_list[0]
            heapq.heappush(min_heap, (key(item), item, list_index, 0))

    merged_list = []
    
    while min_heap:
        key_val, item, list_index, item_index = heapq.heappop(min_heap)    
        merged_list.append(item)

        next_item_index = item_index + 1
        current_list = lists[list_index]
        # אם יש עוד איברים ברשימה המקורית, מוסיפים את הבא לערימה
        if next_item_index < len(current_list):
            next_item = current_list[next_item_index]
            heapq.heappush(min_heap, (key(next_item), next_item, list_index, next_item_index))
            
    return merged_list

