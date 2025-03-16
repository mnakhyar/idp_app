# pages/dashboard.py
import streamlit as st
from PIL import Image
import os
import pandas as pd


def show():
    # SET PAGE TITLE
    st.title("Dashboard")
    st.write("**Selamat datang di halaman Dashboard**")

    # Contoh: data profil
    profile_data = {
        "photo_path": "assets/profile_photo.jpg",  # Ganti dengan path foto profil (jika ada)
        "name": "Admin",
        "gender": "Laki-Laki",
        "birth_place": "Bandung",
        "birth_date": "14 Maret 2025",
        "nik": "19997284991237",
        "email": "admin@injourneyairports.id"
    }

    # Contoh: data job description
    job_data = {
        "position": "Learning Management Specialist",
        "directorate": "Human Capital",
        "group": "Learning & Development",
        "division": "Learning Management",
        "job_family": "People Management",
        "competencies": [
            "Learning & Development Management",
            "Instructional Design",
            "E-Learning Development",
            "Training Needs Analysis",
            "Competency-Based Learning"
        ]
    }

    # PERSONAL VALUE
    if "legacy" not in st.session_state:
        st.session_state["legacy"] = (
             "Legacy (Warisan Profesional yang Ditinggalkan)\n\n"
        "Menciptakan Budaya Belajar yang Berkelanjutan\n"
        "→ Membangun sistem pembelajaran yang terus berkembang dan beradaptasi dengan perubahan industri.\n\n"
        "Meningkatkan Kapabilitas Karyawan melalui Teknologi\n"
        "→ Mengimplementasikan LMS dan teknologi pembelajaran inovatif yang membuat pembelajaran lebih efektif.\n\n"
        "Mendesain Program Pembelajaran yang Berdampak\n"
        "→ Membantu individu dan organisasi dalam mencapai pertumbuhan berkelanjutan melalui pembelajaran."
        )
    if "life_motto" not in st.session_state:
        st.session_state["life_motto"] = (
            "Life Motto (Motto Hidup):\n\n"
        "\"Belajar bukan sekadar proses, tetapi investasi terbaik untuk masa depan.\"\n\n"
        "Saya percaya bahwa setiap orang memiliki potensi untuk berkembang jika diberikan akses dan kesempatan belajar yang tepat. "
        "Oleh karena itu, saya selalu berusaha untuk menciptakan pengalaman pembelajaran yang tidak hanya bermanfaat secara teknis, "
        "tetapi juga mampu menginspirasi individu untuk terus tumbuh. "
        "Baginya, sukses bukan hanya tentang pencapaian pribadi, tetapi juga tentang bagaimana ilmu yang ia sebarkan dapat membawa perubahan bagi banyak orang."

        )

    # Buat layout dengan kolom (untuk Profile + Job Description)
    col1, col2 = st.columns([1, 2], gap="large")

    # -------------------------------------
    # BAGIAN PROFILE (col1)
    # -------------------------------------
    with col1:
        st.subheader("Profile")

        # Tampilkan foto profil (jika file ada)
        if os.path.exists(profile_data["photo_path"]):
            img = Image.open(profile_data["photo_path"])
            st.image(img, use_container_width=True)
        else:
            st.image(
                "https://img.freepik.com/premium-photo/smiling-teen-indian-man-with-blond-straight-hair-flat-illustration-portrait-business-character-white-background-business-person-casual-clothes-ai-generated-square-cartoon-illustration_107173-55249.jpg",
                width=200, 
                use_container_width=True
            )

        st.write(f"**Nama:** {profile_data['name']}")
        st.write(f"**Jenis Kelamin:** {profile_data['gender']}")
        st.write(f"**Tempat, Tanggal Lahir:** {profile_data['birth_place']}, {profile_data['birth_date']}")
        st.write(f"**Nomor Induk Karyawan:** {profile_data['nik']}")
        st.write(f"**Email:** {profile_data['email']}")

    # -------------------------------------
    # BAGIAN JOB DESCRIPTION (col2)
    # -------------------------------------
    with col2:
        st.subheader("Job Description")
        st.write(f"**Posisi:** {job_data['position']}")
        st.write(f"**Directorate:** {job_data['directorate']}")
        st.write(f"**Group:** {job_data['group']}")
        st.write(f"**Division:** {job_data['division']}")
        st.write(f"**Job Family:** {job_data['job_family']}")

        # Competencies dalam box hijau
        st.markdown("**Kompetensi:**")
        for comp in job_data["competencies"]:
            st.markdown(
            f"""
            <div style="
                display: inline-block;
                border-radius: 10px; 
                background-color: #d1e7dd; 
                padding: 8px; 
                margin: 5px 5px 5px 0;
                word-wrap: break-word;
            ">
            {comp}
            </div>
            """,
            unsafe_allow_html=True
            )

    st.markdown("---")
    # -------------------------------------
    # CURRENT PERFORMANCES (carousel dummy)
    # -------------------------------------
    st.subheader("Certification & Other Documents")
    st.caption("_Contoh tampilan dokumen dalam bentuk carousel sederhana_")

    # Contoh list dokumen
    docs = [
        {"title": "SAP Human Capital Management", "image": "assets/doc1.jpeg"},
        {"title": "People Analytics", "image": "assets/doc2.jpeg"},
        {"title": "Generative AI in HR", "image": "assets/doc3.jpeg"},
    ]

    if "current_doc_idx" not in st.session_state:
        st.session_state["current_doc_idx"] = 0

    # Menampilkan 3 dokumen dalam satu waktu
    current_idx = st.session_state["current_doc_idx"]

    # Mengambil 3 dokumen secara berurutan
    docs_to_display = [
        docs[(current_idx + i) % len(docs)] for i in range(3)
    ]

    # Membuat 3 kolom untuk menampilkan gambar
    cols = st.columns(3)

    # Menampilkan gambar dan judul di dalam masing-masing kolom
    for col, doc in zip(cols, docs_to_display):
        with col:
            st.write(f"**{doc['title']}**")
            if os.path.exists(doc["image"]):
                st.image(doc["image"], width=250)
            else:
                st.image("https://via.placeholder.com/250x150?text=No+Document")

    # Tombol Prev / Next untuk navigasi
    cols_doc = st.columns([1, 1, 1])
    if cols_doc[0].button("← Prev", key="prev_doc"):
        st.session_state["current_doc_idx"] = (current_idx - 1) % len(docs)
    if cols_doc[2].button("Next →", key="next_doc"):
        st.session_state["current_doc_idx"] = (current_idx + 1) % len(docs)

    st.markdown("---")
    # -------------------------------------
    # COMPETENCY ASSESSMENT RESULT
    # -------------------------------------


    # Buat layout dengan dua kolom (untuk Personal Values + Data Competency Assessment)
    col1, col2 = st.columns(2)

    # -------------------------------------
    # PERSONAL VALUE (col1)
    # -------------------------------------
    with col1:
        st.subheader("Personal Value")

        st.write("**Legacy for Company** (Bisa diubah & disave):")
        new_legacy = st.text_area("Legacy for Company:", value=st.session_state["legacy"], height=300)
        if st.button("Simpan Legacy"):
            st.session_state["legacy"] = new_legacy
            st.success("Legacy berhasil disimpan.")

        st.write("**Life Moto Strengths** (Bisa diubah & disave):")
        new_life_motto = st.text_area("Life Motto:", value=st.session_state["life_motto"], height=200)
        if st.button("Simpan Moto"):
            st.session_state["life_motto"] = new_life_motto
            st.success("Motto berhasil disimpan.")

    # -------------------------------------
    # COMPETENCY ASSESSMENT RESULT (col2)
    # -------------------------------------
    with col2:
        st.subheader("Competency Assessment Result")

        # Data competency assessment
        data_kompetensi = {
            "KOMPETENSI INTI": [
            {"No": 1, "Nama Kompetensi": "Customer Focus (Service Orientation)", "Baseline": 3, "Assessment": 3},
            {"No": 2, "Nama Kompetensi": "Building Strategic Partnership", "Baseline": 3, "Assessment": 2},
            {"No": 3, "Nama Kompetensi": "Driving Innovation (Creativity)", "Baseline": 3, "Assessment": 3},
            ],
            "KOMPETENSI MANAJERIAL": [
            {"No": 4, "Nama Kompetensi": "Digital Leadership", "Baseline": 2, "Assessment": 2},
            {"No": 5, "Nama Kompetensi": "Global Business Savvy", "Baseline": 2, "Assessment": 1},
            {"No": 6, "Nama Kompetensi": "Strategic Orientation", "Baseline": 2, "Assessment": 2},
            {"No": 7, "Nama Kompetensi": "Driving Execution", "Baseline": 2, "Assessment": 3},
            {"No": 8, "Nama Kompetensi": "Developing Organizational Capabilities", "Baseline": 2, "Assessment": 2},
            {"No": 9, "Nama Kompetensi": "Leading Change", "Baseline": 2, "Assessment": 1},
            {"No": 10, "Nama Kompetensi": "Managing Diversity", "Baseline": 2, "Assessment": 2},
            ],
            "KOMPETENSI PROFESIONAL": [
            {"No": 11, "Nama Kompetensi": "Airport Management", "Baseline": 3, "Assessment": 3},
            {"No": 12, "Nama Kompetensi": "Customer Experience Management", "Baseline": 3, "Assessment": 2},
            ],
            "KOMPETENSI FUNGSIONAL TEKNIS": [
            {"No": 13, "Nama Kompetensi": "Organization Development", "Baseline": 3, "Assessment": 3},
            {"No": 14, "Nama Kompetensi": "Workforce Planning", "Baseline": 3, "Assessment": 2},
            {"No": 15, "Nama Kompetensi": "Business Process Optimization", "Baseline": 3, "Assessment": 3},
            ],
            "KOMPETENSI FUNGSIONAL PERILAKU": [
            {"No": 16, "Nama Kompetensi": "Conceptual Thinking", "Baseline": 3, "Assessment": 3},
            {"No": 17, "Nama Kompetensi": "Optimize Work Process", "Baseline": 2, "Assessment": 2},
            {"No": 18, "Nama Kompetensi": "Concern for Order & Accuracy", "Baseline": 2, "Assessment": 1},
            {"No": 19, "Nama Kompetensi": "Impact Through Influence", "Baseline": 2, "Assessment": 2},
            ]
        }

        for kategori, items in data_kompetensi.items():
            st.markdown(f"**{kategori}**")
            st.table(pd.DataFrame(items).set_index('No'))

       
