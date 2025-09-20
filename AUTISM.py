import streamlit as st

# Title
st.title("M-CHAT Autism Screening Questionnaire")

# Initialize counters
yes_count = 0
no_count = 0

# List of 20 questions
questions = [
    "1. If you point at something across the room, does your child look at it?",
    "2. Have you ever wondered if your child might be deaf?",   # REVERSE
    "3. Does your child play pretend or make-believe?",
    "4. Does your child like climbing on things?",
    "5. Does your child make unusual finger movements near his or her eyes?",  # REVERSE
    "6. Does your child point with one finger to ask for something or to get help?",
    "7. Does your child point with one finger to show you something interesting?",
    "8. Is your child interested in other children?",
    "9. Does your child show you things by bringing them to you or holding them up for you to see?",
    "10. Does your child respond when you call his or her name?",
    "11. When you smile at your child, does he or she smile back at you?",
    "12. Does your child get upset by everyday noises?",  # REVERSE
    "13. Does your child walk?",
    "14. Does your child look you in the eye when you are talking to him or her, playing with him or her, or dressing him or her?",
    "15. Does your child try to copy what you do?",
    "16. If you turn your head to look at something, does your child look around to see what you are looking at?",
    "17. Does your child try to get you to watch him or her?",
    "18. Does your child understand when you tell him or her to do something?",
    "19. If something new happens, does your child look at your face to see how you feel about it?",
    "20. Does your child like movement activities?"
]

# Questions with reversed scoring
reverse_scoring = {2, 5, 12}

# Create select boxes for each question
answers = {}
for i, q in enumerate(questions, start=1):
    answers[i] = st.selectbox(q, ["Select", "Yes", "No"], key=f"q{i}")

# Button to calculate result
if st.button("Submit"):
    for i, ans in answers.items():
        if ans == "Select":
            continue
        if i in reverse_scoring:
            if ans == "Yes":
                no_count += 1
            else:
                yes_count += 1
        else:
            if ans == "Yes":
                yes_count += 1
            else:
                no_count += 1

    # Display results
    st.subheader("Result")
    st.write(f"✅ Yes Count: {yes_count}")
    st.write(f"❌ No Count: {no_count}")

    if no_count < 3:
        st.success("No need to follow up.")
    elif 3 <= no_count <= 7:
        st.warning("Need to follow up.")
    elif no_count >= 8:
        st.error("Need to consult the doctor immediately.")
