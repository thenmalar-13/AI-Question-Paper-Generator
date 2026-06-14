import pandas as pd

df = pd.read_csv(r"datasets\questions.csv")

ai_topics = [
    "Introduction to AI",
    "Search Algorithms",
    "Knowledge Representation",
    "Expert Systems",
    "Neural Networks"
]

ml_topics = [
    "Supervised Learning",
    "Unsupervised Learning",
    "Classification",
    "Regression",
    "Deep Learning"
]

os_topics = [
    "Process Management",
    "CPU Scheduling",
    "Memory Management",
    "Deadlocks",
    "File Systems"
]

cn_topics = [
    "OSI Model",
    "TCP/IP",
    "Routing",
    "Network Security",
    "Protocols"
]

se_topics = [
    "SDLC",
    "Software Testing",
    "Agile",
    "Requirement Engineering",
    "Software Quality"
]

for i,row in df.iterrows():

    if pd.isna(row["Topic"]):

        if row["Subject"] == "AI":
            df.at[i,"Topic"] = ai_topics[i % len(ai_topics)]

        elif row["Subject"] == "ML":
            df.at[i,"Topic"] = ml_topics[i % len(ml_topics)]

        elif row["Subject"] == "OS":
            df.at[i,"Topic"] = os_topics[i % len(os_topics)]

        elif row["Subject"] == "CN":
            df.at[i,"Topic"] = cn_topics[i % len(cn_topics)]

        elif row["Subject"] == "SE":
            df.at[i,"Topic"] = se_topics[i % len(se_topics)]

df.to_csv(r"datasets\questions.csv", index=False)

print("Topic Assignment Completed!")