linhas = {
    "castelo": {
        "2146": {
            "ida": ["2146D Maricá X Castelo", "2146M Garagem Rio do Ouro X Castelo"],
            "volta": ["2146D Castelo X Maricá", "2146M Castelo X Maricá"]
        },

        "4146": {
            "ida": ["4146D Recanto x Castelo", "4146T Terminal Itaipuaçu X Castelo", "4146B Recanto X Castelo - via Vivendas", "4146G Terminal Itaipuaçu X Castelo"],
            "volta": ["4146D Castelo X Recanto", "4146T Castelo X Terminal de Itaipuaçu", "4146B Castelo X Recanto - via Vivendas", "4146G Castelo X Terminal Itaipuaçu - via Vivendas"]
        },

        "6146": {
            "ida": ["Rua 128 X Castelo", "6146E Rua 128 X Castelo - Via Barroco"],

            "volta": ["6146D Castelo X Rua 128", "6146E Castelo X Rua 128 - Via Barroco"] 
            
        },

        "2590": {
            "ida": ["2590R Ponta Negra x Castelo"],
            "volta": ["2590R Castelo X Ponta Negra"],
        },
    },

    "niteroi": {
        "4144": {
            "ida": ["4144R Recanto x Niterói", "4144T Terminal Itaipuaçu X Niterói", "4144C Recanto X Niterói - via Vivendas", "4144S  Terminal Itaipuaçu X Niterói - via Vivendas"],
            "volta": ["4144D Niterói X Recanto", "4144T Niterói X Terminal de Itaipuaçu", "4144B Niterói X Recanto - via Vivendas", "4144G Niterói X Recanto - via Vivendas"]
        },

        "6144": {
            "ida": ["6144R Rua 128 X Niterói - via Barroco"],
            "volta": ["6144U Rua 128 X Niterói - via Cajueiros"]
        },

        "534": {
            "ida": ["534A Jaconé X Niterói"],
            "volta": ["534A Niterói X Jaconé"]
        }
    }
}

print(linhas["castelo"]["2146"]["ida"][1])
#for i, valor in enumerate(linhas["castelo"]["2146"]["ida"], start=1):
    #print(i, valor)