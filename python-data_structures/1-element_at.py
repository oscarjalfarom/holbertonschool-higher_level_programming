#!/usr/bin/python3
# 1-element_at.py
# Oscar J Alfaro M <5826@holbertonschool.com>
#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0:
        return None
    elif idx > (len(my_list)):
        return None
    else:
        return my_list[idx]
