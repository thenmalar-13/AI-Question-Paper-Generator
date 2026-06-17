import pandas as pd
import random

subjects = {
    "AI": [
        "Artificial Intelligence",
        "Intelligent Agents",
        "Knowledge Representation",
        "Search Algorithms",
        "Expert Systems",
        "Computer Vision",
        "Natural Language Processing",
        "Robotics",
        "Neural Networks",
        "Deep Learning",
        "Reasoning Systems",
        "Game Playing",
        "Planning Systems",
        "Machine Perception",
        "Fuzzy Logic",
        "Genetic Algorithms",
        "Constraint Satisfaction",
        "Inference Systems",
        "AI Ethics",
        "Applications of AI"
    ],

    "ML": [
        "Machine Learning",
        "Supervised Learning",
        "Unsupervised Learning",
        "Classification",
        "Regression",
        "Clustering",
        "Feature Selection",
        "Overfitting",
        "Underfitting",
        "Decision Trees",
        "Random Forest",
        "SVM",
        "KNN",
        "Naive Bayes",
        "Neural Networks",
        "Deep Learning",
        "Model Evaluation",
        "Cross Validation",
        "Ensemble Learning",
        "Reinforcement Learning"
    ],

    "CN": [
        "OSI Model",
        "TCP/IP",
        "Routing",
        "Switching",
        "IP Addressing",
        "Subnetting",
        "DNS",
        "HTTP",
        "FTP",
        "SMTP",
        "Network Security",
        "Firewalls",
        "Congestion Control",
        "Error Detection",
        "Data Link Layer",
        "Transport Layer",
        "Application Layer",
        "Network Layer",
        "Wireless Networks",
        "Cryptography"
    ],

    "OS": [
        "Operating System",
        "Process Management",
        "Thread Management",
        "CPU Scheduling",
        "Deadlock",
        "Memory Management",
        "Paging",
        "Segmentation",
        "Virtual Memory",
        "File Systems",
        "Disk Scheduling",
        "Synchronization",
        "Semaphores",
        "Mutex",
        "Inter Process Communication",
        "Resource Allocation",
        "Kernel",
        "System Calls",
        "Multitasking",
        "Protection Mechanisms"
    ],

    "SE": [
        "Software Engineering",
        "SDLC",
        "Agile Model",
        "Waterfall Model",
        "Requirement Engineering",
        "Software Testing",
        "Unit Testing",
        "Integration Testing",
        "System Testing",
        "Project Management",
        "Risk Management",
        "Software Metrics",
        "UML",
        "Design Patterns",
        "Maintenance",
        "Version Control",
        "DevOps",
        "Quality Assurance",
        "Verification",
        "Validation"
    ]
}

easy = [
    "Define {}",
    "What is {}",
    "List the applications of {}",
    "State the features of {}",
    "Name the advantages of {}"
]

hard = [
    "Explain {} in detail",
    "Discuss the architecture of {}",
    "Analyze the importance of {}",
    "Evaluate the performance of {}",
    "Compare different approaches in {}",
    "Describe the working of {}",
    "Discuss advantages and limitations of {}",
    "Justify the need for {}",
    "Analyze real-world applications of {}",
    "Explain challenges in {}"
]

rows = []

for subject, topics in subjects.items():

    for _ in range(500):

        topic = random.choice(topics)

        q2 = random.choice(easy).format(topic)

        rows.append([
            q2,
            2,
            "Easy",
            subject,
            topic
        ])

        q10 = random.choice(hard).format(topic)

        rows.append([
            q10,
            10,
            "Hard",
            subject,
            topic
        ])

df = pd.DataFrame(
    rows,
    columns=[
        "Question",
        "Marks",
        "Difficulty",
        "Subject",
        "Topic"
    ]
)

df.to_csv(
    "big_questions.csv",
    index=False
)

print("Dataset Created")
print("Total Questions:", len(df))