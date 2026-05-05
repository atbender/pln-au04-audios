# Áudios — Aula 4 (UC PLN e IoT, MBA Senac)

10 áudios curtos em PT-BR usados na aula 4 (IoT + Speech) e na APS 2 da UC *Processamento de Linguagem Natural e IoT* — MBA Senac, cohort MBB25.1III, 2026.1.

## Conteúdo

**5 áudios para a prática em aula** (`pratica_*.mp3`):

| Arquivo | Característica |
|---|---|
| `pratica_01_pizza.mp3` | Pedido simples |
| `pratica_02_acai.mp3` | Multi-itens |
| `pratica_03_cancela.mp3` | Cancelamento |
| `pratica_04_reclamacao.mp3` | Reclamação de atraso |
| `pratica_05_gaucho.mp3` | Regionalismo gaúcho |

**5 áudios para a APS 2** (`aps_*.mp3`):

| Arquivo | Característica |
|---|---|
| `aps_01_simples.mp3` | Pedido simples, 2 itens |
| `aps_02_multi.mp3` | Multi-itens com observação |
| `aps_03_restaurante.mp3` | Restaurante mencionado |
| `aps_04_endereco_impreciso.mp3` | Endereço com referência |
| `aps_05_ambiguo.mp3` | Ambiguidade ("endereço de sempre") |

## Geração

Áudios gerados via Google TTS (`gTTS`) — voz `pt-br`, gratuita, qualidade pedagógica suficiente. Script de geração: `_gerar_audios.py`.

Pra regenerar:

```bash
pip install gtts
python3 _gerar_audios.py
```

## Uso nos notebooks

Os notebooks da aula (`whisper.ipynb`, `aps2_template.ipynb`) baixam os áudios da raw URL deste repo:

```python
BASE_URL = "https://raw.githubusercontent.com/atbender/pln-au04-audios/main"
```

## Licença

Conteúdo pedagógico — uso livre para fins educacionais.
