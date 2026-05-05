"""Gera os 10 áudios da aula 4 (5 prática + 5 APS) via gTTS.
Roda uma vez. Os .mp3 ficam ao lado deste script."""

from gtts import gTTS
from pathlib import Path

DIR = Path(__file__).parent

AUDIOS = {
    # --- 5 áudios da prática em aula ---
    "pratica_01_pizza.mp3": (
        "Boa noite, queria pedir uma pizza grande de calabresa "
        "pra rua das Flores 234, apartamento 502."
    ),
    "pratica_02_acai.mp3": (
        "Oi, quero um açaí 500 mililitros com banana, leite condensado e granola. "
        "Pode ser pro meu trabalho na avenida central 1100."
    ),
    "pratica_03_cancela.mp3": (
        "Cancela meu pedido por favor, esqueci que tenho jantar fora hoje."
    ),
    "pratica_04_reclamacao.mp3": (
        "Onde está o entregador? Já passou uma hora e nada."
    ),
    "pratica_05_gaucho.mp3": (
        "Bah, manda uma quentinha do executivo lá da Tia Nilda. "
        "Tu pode botar bastante arroz?"
    ),

    # --- 5 áudios da APS 2 ---
    "aps_01_simples.mp3": (
        "Quero uma pizza média de mussarela e uma coca 2 litros "
        "pra rua dos Andradas 567, perto do mercado."
    ),
    "aps_02_multi.mp3": (
        "Manda dois X-burguer com batata grande, sem cebola num deles, "
        "e um suco de laranja natural. "
        "É pra avenida Bento Gonçalves 1456, apartamento 1203."
    ),
    "aps_03_restaurante.mp3": (
        "Oi tudo bem? Quero um sushi combinado pra duas pessoas do Niwa, sem peixe cru. "
        "Endereço é rua General Câmara 89."
    ),
    "aps_04_endereco_impreciso.mp3": (
        "Quero pedir uma marmita do Verdurama, opção fitness, e uma água de coco. "
        "Pra entregar agora na praça da matriz, lado da igreja."
    ),
    "aps_05_ambiguo.mp3": (
        "Bota uma pizza grande, metade calabresa metade portuguesa, "
        "borda recheada de cheddar. "
        "Endereço é o de sempre, rua Lobo da Costa 200."
    ),
}


def main() -> None:
    for nome, texto in AUDIOS.items():
        destino = DIR / nome
        if destino.exists():
            print(f"✓ {nome} já existe — pulando")
            continue
        print(f"⏳ Gerando {nome}...")
        tts = gTTS(text=texto, lang="pt-br", slow=False)
        tts.save(str(destino))
        print(f"✅ {nome}")
    print(f"\n🎉 {len(AUDIOS)} áudios em {DIR}")


if __name__ == "__main__":
    main()
