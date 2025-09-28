import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io

# Title
st.title("M-CHAT Autism Screening Questionnaire")

# Language selection
language = st.radio("Choose Language / भाषा चुनें / ਭਾਸ਼ਾ ਚੁਣੋ:", ["English", "Hindi", "Punjabi"])

# Questions dictionary
questions_dict = {
    "English": [
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
    ],
    "Hindi": [
        "1. यदि आप कमरे में किसी चीज़ की ओर इशारा करते हैं, तो क्या आपका बच्चा उसकी ओर देखता है?",
        "2. क्या आपने कभी सोचा है कि आपका बच्चा बहरा हो सकता है?",   # REVERSE
        "3. क्या आपका बच्चा खेल-खेल में कुछ बनने या दिखावा करने का खेल खेलता है?",
        "4. क्या आपके बच्चे को चीज़ों पर चढ़ना पसंद है?",
        "5. क्या आपका बच्चा अपनी आँखों के पास अजीब उँगली की हरकतें करता है?",  # REVERSE
        "6. क्या आपका बच्चा किसी चीज़ की माँग करने या मदद लेने के लिए एक उंगली से इशारा करता है?",
        "7. क्या आपका बच्चा आपको कुछ दिलचस्प दिखाने के लिए एक उंगली से इशारा करता है?",
        "8. क्या आपके बच्चे को अन्य बच्चों में रुचि है?",
        "9. क्या आपका बच्चा चीज़ें आपको दिखाने के लिए लाता है या आपके सामने उठाता है?",
        "10. जब आप अपने बच्चे का नाम पुकारते हैं, तो क्या वह जवाब देता है?",
        "11. जब आप अपने बच्चे को मुस्कुराते हैं, तो क्या वह भी आपको मुस्कुराकर जवाब देता है?",
        "12. क्या आपका बच्चा रोज़मर्रा की आवाज़ों से परेशान हो जाता है?",  # REVERSE
        "13. क्या आपका बच्चा चलता है?",
        "14. क्या आपका बच्चा आपसे बात करते समय, खेलते समय या कपड़े पहनाते समय आपकी आँखों में देखता है?",
        "15. क्या आपका बच्चा आपकी नकल करने की कोशिश करता है?",
        "16. यदि आप अपना सिर घुमाते हैं और किसी चीज़ की ओर देखते हैं, तो क्या आपका बच्चा भी देखता है?",
        "17. क्या आपका बच्चा चाहता है कि आप उसे देखें?",
        "18. क्या आपका बच्चा समझता है जब आप उसे कुछ करने को कहते हैं?",
        "19. यदि कुछ नया होता है, तो क्या आपका बच्चा आपके चेहरे की ओर देखता है कि आपकी क्या प्रतिक्रिया है?",
        "20. क्या आपके बच्चे को हिलने-डुलने वाली गतिविधियाँ पसंद हैं?"
    ],
    "Punjabi": [
        "1. ਜੇ ਤੁਸੀਂ ਕਮਰੇ ਵਿੱਚ ਕਿਸੇ ਚੀਜ਼ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰੋ, ਤਾਂ ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਉਸ ਵੱਲ ਵੇਖਦਾ ਹੈ?",
        "2. ਕੀ ਤੁਹਾਨੂੰ ਕਦੇ ਲੱਗਿਆ ਕਿ ਤੁਹਾਡਾ ਬੱਚਾ ਬਹਿਰਾ ਹੋ ਸਕਦਾ ਹੈ?",   # REVERSE
        "3. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਖੇਡ ਵਿੱਚ ਨਕਲ ਜਾਂ ਬਣਾਵਟੀ ਖੇਡਾਂ ਖੇਡਦਾ ਹੈ?",
        "4. ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਚੀਜ਼ਾਂ ਤੇ ਚੜ੍ਹਨਾ ਪਸੰਦ ਹੈ?",
        "5. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਆਪਣੀਆਂ ਅੱਖਾਂ ਕੋਲ ਅਜੀਬ ਉਂਗਲਾਂ ਦੀਆਂ ਹਰਕਤਾਂ ਕਰਦਾ ਹੈ?",  # REVERSE
        "6. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਕਿਸੇ ਚੀਜ਼ ਲਈ ਮੰਗ ਕਰਨ ਜਾਂ ਮਦਦ ਲਈ ਇੱਕ ਉਂਗਲੀ ਨਾਲ ਇਸ਼ਾਰਾ ਕਰਦਾ ਹੈ?",
        "7. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਤੁਹਾਨੂੰ ਕੁਝ ਦਿਲਚਸਪ ਦਿਖਾਉਣ ਲਈ ਇੱਕ ਉਂਗਲੀ ਨਾਲ ਇਸ਼ਾਰਾ ਕਰਦਾ ਹੈ?",
        "8. ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਹੋਰ ਬੱਚਿਆਂ ਵਿੱਚ ਦਿਲਚਸਪੀ ਹੈ?",
        "9. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਚੀਜ਼ਾਂ ਤੁਹਾਨੂੰ ਦਿਖਾਉਣ ਲਈ ਲਿਆਉਂਦਾ ਹੈ ਜਾਂ ਉੱਪਰ ਕਰਦਾ ਹੈ?",
        "10. ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ ਬੱਚੇ ਦਾ ਨਾਮ ਲੈਂਦੇ ਹੋ, ਤਾਂ ਕੀ ਉਹ ਜਵਾਬ ਦਿੰਦਾ ਹੈ?",
        "11. ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ ਬੱਚੇ ਨੂੰ ਮੁਸਕਰਾਉਂਦੇ ਹੋ, ਤਾਂ ਕੀ ਉਹ ਵੀ ਮੁਸਕਰਾਉਂਦਾ ਹੈ?",
        "12. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਰੋਜ਼ਾਨਾ ਦੀਆਂ ਆਵਾਜ਼ਾਂ ਨਾਲ ਪ੍ਰੇਸ਼ਾਨ ਹੁੰਦਾ ਹੈ?",  # REVERSE
        "13. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਤੁਰਦਾ ਹੈ?",
        "14. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਤੁਹਾਡੇ ਨਾਲ ਗੱਲ ਕਰਦਿਆਂ, ਖੇਡਦਿਆਂ ਜਾਂ ਕੱਪੜੇ ਪਾਉਂਦਿਆਂ ਤੁਹਾਡੀਆਂ ਅੱਖਾਂ ਵਿੱਚ ਵੇਖਦਾ ਹੈ?",
        "15. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਤੁਹਾਡੀ ਨਕਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ?",
        "16. ਜੇ ਤੁਸੀਂ ਸਿਰ ਮੋੜ ਕੇ ਕਿਸੇ ਚੀਜ਼ ਵੱਲ ਵੇਖਦੇ ਹੋ, ਤਾਂ ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਵੀ ਵੇਖਦਾ ਹੈ?",
        "17. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਚਾਹੁੰਦਾ ਹੈ ਕਿ ਤੁਸੀਂ ਉਸਨੂੰ ਵੇਖੋ?",
        "18. ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਸਮਝਦਾ ਹੈ ਜਦੋਂ ਤੁਸੀਂ ਉਸਨੂੰ ਕੁਝ ਕਰਨ ਲਈ ਕਹਿੰਦੇ ਹੋ?",
        "19. ਜੇ ਕੁਝ ਨਵਾਂ ਹੁੰਦਾ ਹੈ, ਤਾਂ ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਤੁਹਾਡੇ ਚਿਹਰੇ ਵੱਲ ਵੇਖਦਾ ਹੈ ਕਿ ਤੁਸੀਂ ਕੀ ਸੋਚ ਰਹੇ ਹੋ?",
        "20. ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਹਿਲਣ-ਡੁੱਲਣ ਵਾਲੀਆਂ ਗਤੀਵਿਧੀਆਂ ਪਸੰਦ ਹਨ?"
    ]
}

# Reverse scoring questions
reverse_scoring = {2, 5, 12}

# Load questions
questions = questions_dict[language]

# Create radio buttons (MCQ)
answers = {}
for i, q in enumerate(questions, start=1):
    answers[i] = st.radio(q, ["Yes", "No"], key=f"q{i}")

# Calculate results
if st.button("Submit"):
    yes_count, no_count = 0, 0
    for i, ans in answers.items():
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

    # Result
    st.subheader("Result / परिणाम / ਨਤੀਜਾ")

    if no_count < 3:
        result_text = "✅ No need to follow up."
    elif 3 <= no_count <= 7:
        result_text = "⚠️ Need to follow up."
    else:
        result_text = "❌ Need to consult the doctor immediately."

    st.write(result_text)

    # Generate PDF report
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("M-CHAT Autism Screening Report", styles['Title']))
    elements.append(Spacer(1, 12))

    for i, q in enumerate(questions, start=1):
        elements.append(Paragraph(f"{q} - {answers[i]}", styles['Normal']))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Final Result: {result_text}", styles['Heading2']))

    doc.build(elements)
    buffer.seek(0)

    st.download_button(
        label="📥 Download Report",
        data=buffer,
        file_name="MCHAT_Report.pdf",
        mime="application/pdf"
    )
