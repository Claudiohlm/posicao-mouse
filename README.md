# 🖱️ Monitor de Posição do Mouse

Script desenvolvido em **Python** utilizando a biblioteca **PyAutoGUI** para monitorar e exibir em tempo real as coordenadas **X e Y** da posição do cursor na tela.

## 🛠️ Tecnologias

* Python
* PyAutoGUI
* Time

## 📦 Instalação

Instale a dependência necessária:

```bash
pip install pyautogui
```

## ▶️ Como usar

Execute o script:

```bash
python monitor_mouse.py
```

Após iniciar, mova o mouse pela tela. O programa exibirá continuamente as coordenadas atuais do cursor:

```text
X: 850  Y: 420
```

Para encerrar o programa, pressione:

```text
CTRL + C
```

## 🎯 Objetivo

O projeto foi desenvolvido como uma ferramenta simples para identificar as coordenadas do cursor na tela, podendo ser utilizado como apoio no desenvolvimento de automações com **PyAutoGUI**.

## 📌 Funcionamento

O programa verifica a posição do mouse a cada **0,5 segundo** e atualiza as coordenadas exibidas no terminal.

As coordenadas seguem o padrão:

* **X:** posição horizontal
* **Y:** posição vertical
* **(0, 0):** canto superior esquerdo da tela

