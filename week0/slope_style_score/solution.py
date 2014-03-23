def slope_style_score(scores):
    scores = sorted(scores)[1:len(scores)-1]
    return int((sum(scores))/len(scores)*100)/100
