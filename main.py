import json

from pororo import Pororo
from input_list import file_list

def generate_sentences(file_path):
    sentences = []

    with open(file_path, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        json_comments_data = json_data["comments"]

        for comments in json_comments_data:
            sentence = ""

            if comments["headline"] != None: sentence += comments["headline"] + " "
            if comments["review"] != None: sentence += comments["review"]

            sentences.append(sentence)

    return sentences

def sentiment_analysis(sentences):
    sa = Pororo(task="sentiment", model="brainbert.base.ko.shopping", lang="ko")

    positive_count = 0
    negative_count = 0

    for sentence in sentences:
        if sa(sentence) == "Positive":
            positive_count += 1
        else:
            negative_count += 1
    
    return float(positive_count) / float(positive_count + negative_count)

if __name__ == "__main__":
    result = open("result/result.txt", 'w')

    for file_name in file_list:
        sentences = generate_sentences("input/" + file_name + ".json")
        positive_percent = sentiment_analysis(sentences)

        ## add result
        result_text = file_name + ": %f\n" % positive_percent
        result.write(result_text)
        print(result_text)

    result.close()