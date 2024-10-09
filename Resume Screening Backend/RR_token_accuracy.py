import pandas as pd
from app.utils.File_constant import f_const

file_path1 = r"C:/Users/kauth/PycharmProjects/ResumeRanking/Dataset/jd csv/" + f_const + ".csv"
file_path2 = r"C:/Users/kauth/PycharmProjects/ResumeRanking/Dataset/tokenized_jd/tokenized_words_frequency" + f_const + ".csv"

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

words_set1 = set(df1['Word'])
words_set2 = set(df2['Word'])

intersection = words_set1.intersection(words_set2)
union = words_set1.union(words_set2)
jaccard_similarity = len(intersection) / len(union)
print(f"Similarity: {jaccard_similarity:.2f}")

missing_tokens = words_set1 - words_set2
total_important_tokens = len(words_set1)
present_tokens = total_important_tokens - len(missing_tokens)
accuracy = (present_tokens / total_important_tokens) * 100

print(f"Total important tokens: {total_important_tokens}")
print(f"Tokens present in tokenized file: {present_tokens}")
print(f"Tokens missing in tokenized file: {len(missing_tokens)}")
print(f"Accuracy: {accuracy:.2f}%")