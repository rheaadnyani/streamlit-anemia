import numpy as np
import joblib
import streamlit as st

# Membaca model
anemia_model = joblib.load('Coba_lagi_RF_model.sav')

# Judul web
st.title('Prediksi Anemia Pada Anak Usia 6-59 Bulan')

# Input pengguna
Age_Years_input = st.text_input('Input usia anak dalam tahun')
Sex_input = st.selectbox(
    "Pilih jenis kelamin:",
    ('Laki-Laki', 'Perempuan')
)
gender_mapping = {'Laki-Laki': 1, 'Perempuan': 0}
Sex_y = gender_mapping[Sex_input]

# Menampilkan hasil prediksi
st.write('Anda memilih jenis kelamin:', Sex_input)
RBC_count_in_Millions_input = st.text_input('Input nilai Red Blood Cell (RBC) (10^6/μL)')
HGB_Alltitude_Adjusted_input = st.text_input('Input nilai Hemogoblin (g/dL) ')
HCT_input = st.text_input('Input nilai Hematokrit (%) ')
MCV_input = st.text_input('Input nilai Mean Corpuscular Volume (MCV) (fL)')
MCH_input = st.text_input('Input nilai Mean Corpuscular Hemoglobin (MCH) (pg)')
MCHC_input = st.text_input('Input nilai Mean Corpuscular Hemoglobin Concentration (MCHC) (g/dL)')
RDW_input = st.text_input('Input nilai Red Cell Distribution Width (RDW) (%)')

# Validasi input
if Age_Years_input.strip() and Sex_input.strip() and RBC_count_in_Millions_input.strip() and HGB_Alltitude_Adjusted_input.strip() and HCT_input.strip() and MCV_input.strip() and MCH_input.strip() and MCHC_input.strip() and RDW_input.strip():
    Age_Years = float(Age_Years_input)
    Sex = float(Sex_y)
    RBC_count_in_Millions = float(RBC_count_in_Millions_input)
    HGB_Alltitude_Adjusted = float(HGB_Alltitude_Adjusted_input)
    HCT = float(HCT_input)
    MCV = float(MCV_input)
    MCH = float(MCH_input)
    MCHC = float(MCHC_input)
    RDW = float(RDW_input)

    # Code untuk prediksi
    # Membuat tombol untuk prediksi
    if st.button('Test Prediksi Anemia'):
        input_data = np.array([Age_Years, Sex, RBC_count_in_Millions, HGB_Alltitude_Adjusted, HCT, MCV, MCH, MCHC, RDW]).reshape(1, -1)
        anem_prediction = anemia_model.predict(input_data)

        # Menampilkan hasil prediksi
        if anem_prediction[0] == 1:
            anem_diagnosis = 'Anak tidak terkena Anemia'
        else:
            anem_diagnosis = 'Anak terkena Anemia'

        st.success(anem_diagnosis)
else:
    st.warning('Mohon lengkapi semua kolom input.')
