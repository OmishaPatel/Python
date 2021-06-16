def autocomplete(str, list1):
    back = []
    for elem in list1:
        if elem.startswith(str):
            back.append(elem)
    return back
print(autocomplete("de", ["dog","deer","deal","not","this","one","dasd"]))

  
        