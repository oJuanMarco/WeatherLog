from app.functions.data_treatment import treat
import pandas as  pd

def test_db_treat():
    dados_ficticios = pd.DataFrame({
        "data": ["2026-09-01", "2026-09-02"],
        "temperatura_media": [22.5, 24.1],
        "sensacao_termica_media": [21.0, 23.5],
        "maxima": [24.7, 20.5],
        "minima": [15.0, 16.5],
        "chances_de_chuva": [33.0, 13.5],
        "volume_de_chuva(mm)": [0.6, 0.0],
    })

    resultado = treat(dados_ficticios)
    assert resultado is not None