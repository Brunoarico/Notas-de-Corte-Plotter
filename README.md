# Notas-de-Corte-Plotter
Programas e bases de dados utilizados para análise de dados das notas de corte da Fuvest desde 2012 até 2020.

## OCR
a Fuvest Libera os dados de notas de corte, vagas, etc por meio de formato PDF, o programa "extract_table.py" é o responsavel pela extração desses dados em formato aberto, facil de trabalhar e padronizado, em CSV. 

## Dados
Os dados utilizados para a geração dos gráficos estão no folder PDF, esses são os PDF's origiais fornecidos pela Fuvest. No folder CSV temos os dados já extraidos e fortados a partir dos PDF's originais. No folder Plot temos alguns exemplos de plots gerados para os dados de notas de corte

## Plots
O programa responsavel pelo plot e refinamento dos dados para isso é o "load\_n\_plot.py"


