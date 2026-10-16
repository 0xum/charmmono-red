# Charmmono Red

Dois temas para VS Code em uma única extensão: **Charmmono Red Light** e
**Charmmono Red Dark**, baseados no Charmmono 0.3.1 de Sumangal Karan (MIT).

O Light preserva integralmente a [variação Red Light existente](https://github.com/0xum/charmmono-red-light).
O Dark parte do **Charmmono Dark original**, mantendo seus fundos escuros,
texto, regras de sintaxe e tokens semânticos. Seus destaques roxos passam a
vermelho coral, com seleções em carmim e palavras-chave em vermelho rosado.
Diagnósticos, indicadores Git e cores ANSI do terminal preservam as cores originais.

| Uso | Light | Dark |
| --- | --- | --- |
| Fundo do editor | `#FFFFFF` | `#171F2B` |
| Texto do editor | `#1F2939` | `#D9DFE7` |
| Destaques e funções | `#B4232D` | `#F28B82` |
| Palavras-chave | `#AA2532` | `#F6A0A6` |
| Borda de foco | `#C9434C` | `#E05A64` |
| Seleção | `#F7B9B399` | `#A63C4880` |

## Instalar

Baixe ou clone este repositório. O pacote pronto contém as duas variações:

```sh
code --install-extension dist/charmmono-red-1.0.0.vsix --force
```

Também é possível usar **Extensions → … → Install from VSIX…** e escolher
esse arquivo. Depois, abra **Preferences: Color Theme** na paleta de comandos
e escolha **Charmmono Red Light** ou **Charmmono Red Dark**.

Para acompanhar o modo claro/escuro do sistema, configure no VS Code:

```json
{
  "window.autoDetectColorScheme": true,
  "workbench.preferredLightColorTheme": "Charmmono Red Light",
  "workbench.preferredDarkColorTheme": "Charmmono Red Dark"
}
```

A extensão tem identidade própria (`delta-local.charmmono-red`) e não precisa
da extensão original. Ela contém apenas temas, sem código de ativação ou
dependências. Os ícones continuam sendo controlados pelo tema de ícones escolhido.
Se a antiga extensão `delta-local.charmmono-red-light` estiver instalada,
ela pode ser desinstalada para evitar duas opções com o mesmo nome.

## Ajustar e empacotar

O Light é editado diretamente em `themes/charmmono-red-light-color-theme.json`.
Para o Dark, ajuste os destaques em `generate_dark.py` e regenere o JSON:

```sh
python3 generate_dark.py
python3 build.py
code --install-extension dist/charmmono-red-1.0.0.vsix --force
```

Os scripts usam apenas a biblioteca padrão do Python 3. No Windows, pode-se
usar `py -3` em vez de `python3`. O pacote também funciona em macOS e Linux.
Se editar o JSON do Dark diretamente, não execute o gerador depois, pois ele
recria esse arquivo a partir da fonte original e dos destaques definidos no script.

`build.py` empacota os dois arquivos em `dist/`, com a versão de `package.json`.
Se alterar a versão, ajuste o caminho do VSIX no comando de instalação.
Versione os temas e o VSIX atualizado para manter a instalação pronta.
Se necessário, use **Developer: Reload Window** após reinstalar.

A fonte original do Dark está em `upstream/`; o histórico da origem está em
`upstream/README.md`. A licença MIT e a atribuição original estão em `LICENSE.txt`.
