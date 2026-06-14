
import streamlit as st
import pandas as pd
import random
from docx import Document

st.set_page_config(
    page_title="AI Question Paper Generator",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1{
    text-align:center;
    color:#1E3A8A;
}

.stButton button{
    background-color:#2563EB;
    color:white;
    border-radius:12px;
    height:50px;
    width:100%;
    font-size:18px;
    font-weight:bold;
}

.stDownloadButton button{
    background-color:#16A34A;
    color:white;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = pd.read_csv("datasets/questions.csv")

# ---------- TITLE ----------
st.markdown("""
<h1>🎓 AI QUESTION PAPER GENERATOR</h1>
<h4 style='text-align:center;'>
Generate Smart University Question Papers Automatically
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    college = st.text_input(
        "College Name",
        "CIT College"
    )

with col2:
    department = st.text_input(
        "Department",
        "Computer Science"
    )

with col3:
    semester = st.selectbox(
        "Semester",
        [1,2,3,4,5,6,7,8]
    )

exam_name = st.text_input(
    "Exam Name",
    "Model Examination"
)

st.markdown("---")

mode = st.radio(
    "Choose Generation Mode",
    ["Automatic Blueprint", "Custom Blueprint"]
)

# ---------- AUTOMATIC ----------
# ---------- AUTOMATIC ----------
if mode == "Automatic Blueprint":

    st.subheader("📘 Automatic Blueprint")

    col1, col2 = st.columns(2)

    with col1:
        partA_count = st.number_input(
            "Number of 2-Mark Questions",
            min_value=1,
            max_value=20,
            value=5
        )

    with col2:
        partB_count = st.number_input(
            "Number of 10-Mark Questions",
            min_value=1,
            max_value=20,
            value=5
        )

    include_ai = st.checkbox(
        "Include AI Generated Questions (Experimental)"
    )

    st.info(
        f"""
        Part A : {partA_count} Questions

        Part B : {partB_count} Questions

        Estimated Total Marks :
        {(partA_count*2)+(partB_count*10)}
        """
    )

    if st.button("🚀 Generate Paper"):

        partA = df[df["Marks"].astype(str) == "2"]
        partB = df[df["Marks"].astype(str) == "10"]

        selectedA = partA.sample(
            min(partA_count, len(partA))
        )

        selectedB = partB.sample(
            min(partB_count, len(partB))
        )

        total_marks = (
            len(selectedA)*2 +
            len(selectedB)*10
        )

        st.markdown(f"""
# 🏫 {college}

### Department of {department}

### {exam_name}

### Semester {semester}

<div style='text-align:right;font-size:22px'>
<b>TOTAL MARKS : {total_marks}</b>
</div>

---
""", unsafe_allow_html=True)

        st.markdown("## PART - A (2 Marks Each)")

        qno = 1

        for _, row in selectedA.iterrows():

            st.write(
                f"{qno}. {row['Question']} ({row['Subject']})"
            )

            qno += 1

        st.success(
            f"{len(selectedA)} × 2 = {len(selectedA)*2} Marks"
        )

        st.markdown("---")

        st.markdown("## PART - B (10 Marks Each)")

        for _, row in selectedB.iterrows():

            st.write(
                f"{qno}. {row['Question']} ({row['Subject']})"
            )

            qno += 1

        st.success(
            f"{len(selectedB)} × 10 = {len(selectedB)*10} Marks"
        )

        st.markdown("---")

        st.subheader(
            f"TOTAL MARKS : {total_marks}"
        )

        st.markdown("### 📊 Subject Distribution")

        all_questions = pd.concat(
            [selectedA, selectedB]
        )

        subject_count = (
            all_questions["Subject"]
            .value_counts()
        )

        st.dataframe(subject_count)

        # DOCX EXPORT

        doc = Document()

        doc.add_heading(
            college,
            level=1
        )

        doc.add_paragraph(
            f"Department : {department}"
        )

        doc.add_paragraph(
            f"Exam : {exam_name}"
        )

        doc.add_paragraph(
            f"Semester : {semester}"
        )

        doc.add_paragraph(
            f"TOTAL MARKS : {total_marks}"
        )

        doc.add_paragraph("")

        doc.add_heading(
            "PART A (2 Marks Each)",
            level=2
        )

        qno = 1

        for _, row in selectedA.iterrows():

            doc.add_paragraph(
                f"{qno}. {row['Question']} ({row['Subject']})"
            )

            qno += 1

        doc.add_paragraph(
            f"{len(selectedA)} x 2 = {len(selectedA)*2} Marks"
        )

        doc.add_heading(
            "PART B (10 Marks Each)",
            level=2
        )

        for _, row in selectedB.iterrows():

            doc.add_paragraph(
                f"{qno}. {row['Question']} ({row['Subject']})"
            )

            qno += 1

        doc.add_paragraph(
            f"{len(selectedB)} x 10 = {len(selectedB)*10} Marks"
        )

        doc.add_paragraph(
            f"TOTAL MARKS : {total_marks}"
        )

        doc.save("question_paper.docx")

        with open(
            "question_paper.docx",
            "rb"
        ) as file:

            st.download_button(
                "📥 Download Question Paper DOCX",
                file,
                file_name="question_paper.docx"
            )
# ---------- CUSTOM ----------
else:

    st.subheader("Custom Blueprint")

    subjects = ["AI", "ML", "OS", "CN", "SE"]

    blueprint = {}

    for subject in subjects:

        st.markdown(f"### {subject}")

        c1, c2 = st.columns(2)

        with c1:
            two = st.number_input(
                f"{subject} - 2 Marks",
                min_value=0,
                max_value=10,
                value=1,
                key=f"{subject}_2"
            )

        with c2:
            ten = st.number_input(
                f"{subject} - 10 Marks",
                min_value=0,
                max_value=10,
                value=1,
                key=f"{subject}_10"
            )

        blueprint[subject] = {
            "2": two,
            "10": ten
        }

    if st.button("🚀 Generate Custom Paper"):

        paper = []

        for subject in subjects:

            rows2 = df[
                (df["Subject"] == subject) &
                (df["Marks"].astype(str) == "2")
            ]

            rows10 = df[
                (df["Subject"] == subject) &
                (df["Marks"].astype(str) == "10")
            ]

            if len(rows2) > 0:

                sample2 = rows2.sample(
                    min(
                        blueprint[subject]["2"],
                        len(rows2)
                    )
                )

                paper.extend(
                    sample2.to_dict("records")
                )

            if len(rows10) > 0:
                sample10 = rows10.sample(
                    min(
                        blueprint[subject]["10"],
                        len(rows10)
                    )
                )

                paper.extend(
                    sample10.to_dict("records")
                )

        total_marks = sum(
            int(q["Marks"])
            for q in paper
        )

        st.markdown(f"""
## {college}

### Department of {department}

### {exam_name}

### Semester {semester}

# TOTAL MARKS : {total_marks}
""")

        paper.sort(
            key=lambda x: int(x["Marks"])
        )

        qno = 1

        st.markdown("## QUESTION PAPER")

        for q in paper:

            st.write(
                f"{qno}. {q['Question']} ({q['Subject']})"
            )

            qno += 1

        st.markdown("---")

        st.subheader(
            f"TOTAL MARKS : {total_marks}"
        )
                # ---------- DOCX EXPORT ----------

        doc = Document()

        doc.add_heading(
            college,
            level=1
        )

        doc.add_paragraph(
            f"Department : {department}"
        )

        doc.add_paragraph(
            f"Exam : {exam_name}"
        )

        doc.add_paragraph(
            f"Semester : {semester}"
        )

        doc.add_paragraph(
            f"TOTAL MARKS : {total_marks}"
        )

        doc.add_paragraph("")

        doc.add_heading(
            "QUESTION PAPER",
            level=2
        )

        qno = 1

        for q in paper:

            doc.add_paragraph(
                f"{qno}. {q['Question']} ({q['Subject']})"
            )

            qno += 1

        doc.add_paragraph("")
        doc.add_paragraph(
            f"TOTAL MARKS : {total_marks}"
        )

        doc.save(
            "custom_question_paper.docx"
        )

        with open(
            "custom_question_paper.docx",
            "rb"
        ) as file:

            st.download_button(
                "📥 Download Custom Paper DOCX",
                file,
                file_name="custom_question_paper.docx"
            )
    
    st.markdown("---")

st.caption(
    "🎓 AI Question Paper Generator | Built using Python, Machine Learning, Streamlit and TensorFlow"
)
