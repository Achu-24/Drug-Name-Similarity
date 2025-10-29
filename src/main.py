from drug_similarity import get_similar_drugs

if __name__=="__main__":
    user_input=input("Enter a drug name: ")
    matches=get_similar_drugs(user_input)
    if matches:
        print("Did you mean: ")
        for m in matches:
            print("=>",m)
    else:
        print("No Similar Drugs Found.")