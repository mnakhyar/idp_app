# pages/elevate.py
import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Elevate Your Journey")

    # -----------------------------------------------------
    # 1) ACTION PLAN (GANTT CHART)
    # -----------------------------------------------------
    st.subheader("Action Plan")

    # Contoh data action plan untuk tabel (silakan sesuaikan)
    action_plan_data = [
        {
            "Week": "Week 1",
            "Task": "Strategic Thinking & Business Acumen",
            "Start": "2025-01-01",
            "Finish": "2025-01-07",
            "Resource": "Online Course / Workshop"
        },
        {
            "Week": "Week 2",
            "Task": "Data Analytics & Decision Making",
            "Start": "2025-01-08",
            "Finish": "2025-01-14",
            "Resource": "Hands-on Project"
        },
        {
            "Week": "Week 3",
            "Task": "Leadership & Change Management",
            "Start": "2025-01-15",
            "Finish": "2025-01-21",
            "Resource": "Cross-functional Project"
        },
    ]

    # Tampilkan dalam bentuk tabel
    df_action_plan = pd.DataFrame(action_plan_data)
    st.table(df_action_plan)

    # Form untuk menambahkan data baru
    with st.form("add_task_form"):
        st.write("Tambah Task Baru")
        week = st.text_input("Week")
        task = st.text_input("Task")
        start = st.date_input("Start")
        finish = st.date_input("Finish")
        resource = st.text_input("Resource")
        submitted = st.form_submit_button("Add Task")

        if submitted:
            new_task = {
                "Week": week,
                "Task": task,
                "Start": start,
                "Finish": finish,
                "Resource": resource
            }
            action_plan_data.append(new_task)
            df_action_plan = pd.DataFrame(action_plan_data)
            st.table(df_action_plan)

    df_gantt = pd.DataFrame(action_plan_data)
    fig = px.timeline(
        df_gantt, 
        x_start="Start", 
        x_end="Finish", 
        y="Task", 
        color="Resource",
        title="Gantt Chart - Action Plan",
    )
    fig.update_yaxes(autorange="reversed")  # Agar task paling atas
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -----------------------------------------------------
    # 2) LIST MODUL PEMBELAJARAN
    # -----------------------------------------------------
    st.subheader("List Modul Pembelajaran")

    # Data modul pembelajaran (3 modul utama)
    modules_data = {
        "Strategic Thinking & Business Acumen": [
            {
                "Sub-modul": "Fundamentals of Business Strategy",
                "Materi": "Pengantar strategi bisnis, analisis SWOT, PESTEL",
                "Durasi": "4 jam",
                "Metode": "Online Course (Harvard Business Review, Coursera)"
            },
            {
                "Sub-modul": "Financial Acumen for Decision Making",
                "Materi": "Laporan keuangan dasar, ROI dalam pembelajaran, pengambilan keputusan berbasis data keuangan",
                "Durasi": "5 jam",
                "Metode": "Workshop (Business Acumen Training)"
            },
            {
                "Sub-modul": "Aligning Learning Strategy with Business Goals",
                "Materi": "Cara menyelaraskan strategi pembelajaran dengan target perusahaan",
                "Durasi": "3 jam",
                "Metode": "Case Study & On-the-Job Project"
            }
        ],
        "Data Analytics & Decision Making": [
            {
                "Sub-modul": "Introduction to Data Analytics",
                "Materi": "Pengantar data analytics, konsep dasar statistik, tipe data",
                "Durasi": "4 jam",
                "Metode": "Online Course (Coursera - Data Analytics for Business)"
            },
            {
                "Sub-modul": "Tools for Data Analytics (SQL & Power BI)",
                "Materi": "Dasar-dasar SQL, penggunaan Power BI untuk dashboard",
                "Durasi": "6 jam",
                "Metode": "Hands-on Workshop"
            },
            {
                "Sub-modul": "Data-Driven Decision Making",
                "Materi": "Cara membaca insight dari data, storytelling dengan data",
                "Durasi": "3 jam",
                "Metode": "Real Case Analysis"
            }
        ],
        "Leadership & Change Management": [
            {
                "Sub-modul": "Leadership Essentials",
                "Materi": "Gaya kepemimpinan, emotional intelligence, membangun tim",
                "Durasi": "5 jam",
                "Metode": "Leadership Coaching"
            },
            {
                "Sub-modul": "Managing Organizational Change",
                "Materi": "Manajemen perubahan, cara mengatasi resistensi perubahan",
                "Durasi": "4 jam",
                "Metode": "Cross-functional Project & Simulation"
            },
            {
                "Sub-modul": "Stakeholder Engagement & Communication",
                "Materi": "Teknik komunikasi efektif dengan stakeholder internal & eksternal",
                "Durasi": "3 jam",
                "Metode": "Role Play & Case Study"
            }
        ]
    }

    for module_title, submodules in modules_data.items():
        st.markdown(f"### {module_title}")
        for idx, sub in enumerate(submodules, start=1):
            st.markdown(f"**Sub-modul {idx}: {sub['Sub-modul']}**")
            st.write(f"📌 **Materi**: {sub['Materi']}")
            st.write(f"⏳ **Durasi**: {sub['Durasi']}")
            st.write(f"🎯 **Metode**: {sub['Metode']}")
            st.markdown("---")

    st.markdown("---")

    # -----------------------------------------------------
    # 3) SCHEDULE - JADWAL MENTORING
    # -----------------------------------------------------
    st.subheader("Schedule (Jadwal Mentoring)")

    mentoring_schedule = [
        {
            "Tanggal": "18 Maret 2025 | 10:00 - 11:30",
            "Topik": "Business Acumen & Strategic Thinking",
            "Mentor/PIC": "Head of Strategy",
            "Lokasi": "Meeting Room A"
        },
        {
            "Tanggal": "25 Maret 2025 | 14:00 - 15:30",
            "Topik": "Financial Acumen for Decision Making",
            "Mentor/PIC": "CFO atau Finance Lead",
            "Lokasi": "Zoom Meeting"
        },
        {
            "Tanggal": "1 April 2025 | 09:00 - 10:30",
            "Topik": "Data Analytics for Decision Making",
            "Mentor/PIC": "Head of Data",
            "Lokasi": "Training Room 2"
        },
        {
            "Tanggal": "8 April 2025 | 13:30 - 15:00",
            "Topik": "Power BI & SQL Training",
            "Mentor/PIC": "BI Analyst",
            "Lokasi": "Online Workshop"
        },
        {
            "Tanggal": "15 April 2025 | 10:00 - 11:30",
            "Topik": "Leadership & Stakeholder Engagement",
            "Mentor/PIC": "Senior Leadership Coach",
            "Lokasi": "Executive Lounge"
        },
        {
            "Tanggal": "22 April 2025 | 14:00 - 15:30",
            "Topik": "Change Management in Organization",
            "Mentor/PIC": "HC Director",
            "Lokasi": "Meeting Room B"
        },
    ]

    # Tampilkan dalam bentuk tabel
    df_schedule = pd.DataFrame(mentoring_schedule)
    st.table(df_schedule)
