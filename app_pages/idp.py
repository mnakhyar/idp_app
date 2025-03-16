# pages/idp.py
import streamlit as st
import pandas as pd

def show():
    st.title("Individual Development Plan")

    # -------------------------------------
    # CAREER ASPIRATION
    # -------------------------------------
    st.subheader("Career Aspiration")
    next_position = st.text_input("Jabatan selanjutnya:", "Learning Management Division Head")
    other_division = st.text_input("Divisi lain yang diinginkan (jika ada):", "Customer Insight & Quality Management Division Head")

    if st.button("Save"):
        st.write(f"**Jabatan selanjutnya:** {next_position}")
        st.write(f"**Divisi lain yang diinginkan (jika ada):** {other_division}")

    st.markdown("---")

    # -------------------------------------
    # DEVELOPMENT AREA
    # -------------------------------------
    st.subheader("Development Area")

    # Skills and competencies to learn (green box)
    skill_need_learn = [
        "Strategic Learning & Development",
        "Leadership & Change Management",
        "Business & Financial Acumen",
        "Learning Technology & Analytics",
        "Stakeholder Management"
    ]
    st.write("**Skill dan kompetensi yang perlu dipelajari:**")
    for skill in skill_need_learn:
        st.markdown(
            f"""
            <div style="
                background-color: #d1e7dd; 
                border-radius: 8px; 
                padding: 8px; 
                margin-bottom: 5px;
                display: inline-block;
                width: auto;
                max-width: 100%;
                word-wrap: break-word;
            ">
            {skill}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Skills and competencies to master (orange box)
    skill_want_master = [
        "Customer Experience & Journey Mapping",
        "Data Analytics & Insight Generation",
        "Service Quality Management",
        "Process Improvement & Innovation",
        "Leadership & Stakeholder Engagement"
    ]
    st.write("**Skill dan kompetensi yang ingin dikuasai:**")
    for skill in skill_want_master:
        st.markdown(
            f"""
            <div style="
                background-color: #fde7d2; 
                border-radius: 8px; 
                padding: 8px; 
                margin-bottom: 5px;
                display: inline-block;
                width: auto;
                max-width: 100%;
                word-wrap: break-word;
            ">
            {skill}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Top 3 Competencies
    top_3_competencies = [
        "Strategic Thinking & Business Acumen",
        "Data Analytics & Decision Making",
        "Leadership & Change Management"
    ]
    st.write("**Top 3 Competencies:**")
    for competency in top_3_competencies:
        st.markdown(
            f"""
            <div style="
                background-color: #d0e2ff; 
                border-radius: 8px; 
                padding: 8px; 
                margin-bottom: 5px;
                display: inline-block;
                width: auto;
                max-width: 100%;
                word-wrap: break-word;
            ">
            {competency}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------------------------------------
    # LEARNING PATH
    # -------------------------------------
    st.subheader("Learning Path")

    # Data learning path dalam bentuk list of dict
    learning_path_data = [
        {
            "No": 1,
            "Topic": "Strategic Thinking & Business Acumen",
            "Method": "Online Course, Workshop",
            "Formal Learning": [
                {
                    "Kursus": "[Strategic Thinking](https://www.coursera.org/learn/strategicthinking)",
                    "Deskripsi": "Kursus ini membantu Anda memahami konsep berpikir strategis melalui studi kasus dan perencanaan skenario.",
                    "Durasi": "1 jam",
                    "Sumber": "Coursera"
                },
                {
                    "Kursus": "[Strategic Thinking for Everyone Specialization](https://www.coursera.org/specializations/strategicthinkingforeveryone)",
                    "Deskripsi": "Spesialisasi ini mengajarkan cara membayangkan dan merencanakan skenario masa depan, mengidentifikasi data relevan, dan memilih pendekatan optimal dalam interaksi Anda.",
                    "Durasi": "4 kursus",
                    "Sumber": "Coursera"
                }
            ],
            "Social Learning": [
                {
                    "Aktivitas": "Bergabung dengan komunitas eksekutif di platform profesional seperti LinkedIn Learning Groups untuk berbagi pengalaman dan praktik terbaik.",
                    "Sumber": "[Harvard Business Review Discussion Group](https://www.linkedin.com/groups/3044917/)"
                }
            ],
            "Experimental Learning": [
                {
                    "Aktivitas": "Berpartisipasi dalam penyusunan strategi untuk proyek lintas divisi di organisasi Anda untuk menerapkan konsep yang dipelajari dalam situasi nyata."
                }
            ]
        },
        {
            "No": 2,
            "Topic": "Data Analytics & Decision Making",
            "Method": "Certification, Hands-on Project",
            "Formal Learning": [
                {
                    "Kursus": "[Google Data Analytics Professional Certificate](https://www.coursera.org/professional-certificates/google-data-analytics)",
                    "Deskripsi": "Program sertifikat ini mencakup keterampilan yang dibutuhkan dalam data analytics, termasuk penggunaan alat seperti SQL, R, dan Tableau.",
                    "Durasi": "8 kursus",
                    "Sumber": "Coursera"
                },
                {
                    "Kursus": "[Data-driven Decision Making](https://www.coursera.org/learn/data-driven-decision-making)",
                    "Deskripsi": "Kursus ini memberikan pengenalan tentang Data Analytics dan perannya dalam pengambilan keputusan bisnis.",
                    "Durasi": "4 modul",
                    "Sumber": "Coursera"
                }
            ],
            "Social Learning": [
                {
                    "Aktivitas": "Mentorship dengan Head of Data atau Business Intelligence di perusahaan Anda untuk mendapatkan wawasan praktis dan bimbingan langsung."
                }
            ],
            "Experimental Learning": [
                {
                    "Aktivitas": "Menganalisis data proyek nyata dan mempresentasikan rekomendasi berdasarkan temuan Anda kepada tim manajemen."
                }
            ]
        },
        {
            "No": 3,
            "Topic": "Leadership & Change Management",
            "Method": "Leadership Coaching, Cross-functional Project",
            "Formal Learning": [
                {
                    "Kursus": "[Business Acumen & Strategic Thinking Learning Lab (2025)](https://eatyourcareer.com/strategic-thinking/)",
                    "Deskripsi": "Workshop intensif yang berfokus pada pengembangan pemahaman bisnis dan pemikiran strategis.",
                    "Durasi": "6 jam",
                    "Sumber": "Eat Your Career"
                }
            ],
            "Social Learning": [
                {
                    "Aktivitas": "Coaching dengan senior leaders untuk mendapatkan umpan balik dan saran dalam mengelola perubahan organisasi."
                }
            ],
            "Experimental Learning": [
                {
                    "Aktivitas": "Memimpin inisiatif perubahan dalam tim atau organisasi untuk mengembangkan keterampilan kepemimpinan dan manajemen perubahan secara praktis."
                }
            ]
        }
    ]

    for item in learning_path_data:
        st.markdown(f"**{item['No']}. {item['Topic']}**")
        st.write(f"**Method:** {item['Method']}")
        
        st.write("**Formal Learning:**")
        for formal in item["Formal Learning"]:
            st.markdown(f"- **{formal['Kursus']}**: {formal['Deskripsi']} ({formal['Durasi']}, {formal['Sumber']})")
        
        st.write("**Social Learning:**")
        for social in item["Social Learning"]:
            st.markdown(f"- {social['Aktivitas']} ({social.get('Sumber', 'N/A')})")
        
        st.write("**Experimental Learning:**")
        for experimental in item["Experimental Learning"]:
            st.markdown(f"- {experimental['Aktivitas']}")
        
        st.markdown("---")

    df = pd.DataFrame(learning_path_data)
    df.set_index('No', inplace=True)




    # -------------------------------------
    # SUPERVISOR NOTES
    # -------------------------------------
    st.subheader("Supervisor Notes")

    feedbacks = [
        {
            "Judul": "Perkuat pemahaman bisnis sebelum naik ke level strategis",
            "Isi": "Pastikan untuk memahami bagaimana pembelajaran atau customer insights berdampak langsung pada profit dan efisiensi perusahaan."
        },
        {
            "Judul": "Asah kemampuan decision-making berbasis data",
            "Isi": "Belajar menggunakan data analytics tools dan mengambil keputusan berbasis insight, bukan hanya asumsi."
        },
        {
            "Judul": "Tingkatkan kemampuan memimpin perubahan",
            "Isi": "Berlatih dalam situasi nyata untuk mengelola resistensi terhadap perubahan dan memastikan keberhasilan implementasi strategi."
        }
    ]

    for fb in feedbacks:
        st.markdown(f"**• {fb['Judul']}**")
        st.write(f"{fb['Isi']}")

