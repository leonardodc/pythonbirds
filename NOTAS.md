# ANOTAÇÕES DO PROJETO PYTHONBIRDS

* PROBLEMA COM TESTES
* PROBLEMA COM UNITTEST
* PROBLEMA COM PATH NOS ARQUIVOS DE TESTES

# CONFIGURANDO TESTES NO VSCODE

## CORRIGIR O ARQUIVO settings.json
### Precisa corrigir o endereço da pasta
    
    
    {
        "python.testing.pytestArgs": [
            "OLD"
        ],
        "python.testing.unittestEnabled": true,
        "python.testing.pytestEnabled": false,
        "python.testing.unittestArgs": [
            "-v",
            "-s",
            "./DEVPRO/pythonbirds/testes",
            "-p",
            "test_*.py"
        ]
    }
    

# CONFIGURAÇÃO DE PATH
    ### colocar em cada arquivo que precise importar de outros arquivos

    
    import os
    import sys

    project_dir = os.path.join(os.path.dirname(__file__), '..')
    project_dir = os.path.normpath(project_dir)
    sys.path.append(project_dir) 

    