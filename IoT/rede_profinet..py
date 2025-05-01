import snap7
from snap7.util import *
from snap7.snap7types import *

def ler_dado_profinet(ip, rack=0, slot=1):
    client = snap7.client.Client()
    client.connect(ip, rack, slot)

    # Lê 4 bytes a partir do DB1 (Database 1), byte 0
    data = client.db_read(1, 0, 4)

    valor_lido = get_real(data, 0)  # Converte os 4 bytes em float (REAL no TIA Portal)
    print(f"Valor lido do CLP via Profinet: {valor_lido}")

    client.disconnect()
    return valor_lido

def ler_dados_industriais():
    try:
        valor = ler_dado_profinet("192.168.0.1")  # IP do CLP Siemens
        return {
            "sensor_temperatura": valor,
            "timestamp_leitura": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Erro ao ler Profinet: {e}")
        return None
