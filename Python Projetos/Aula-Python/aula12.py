nome = """
Lorem ipsum dolor sit amet. Sit consectetur quos aut delectus 
labore aut aspernatur voluptatem est repudiandae porro sed nostrum magnam.
Ut quis asperiores At beatae neque est eveniet repudiandae est modi illum est 
aliquid aspernatur ea sapiente accusantium quo saepe Quis. Vel beatae officia et
cupiditate autem et incidunt rerum ut commodi dolores. A sapiente sunt non assumenda
consequatur ad veniam voluptatem ea maxime dolore in dolorum saepe aut debitis ipsum 
aut velit dolores. </p><p>At quae eius et molestiae iste non dolorem reiciendis ab 
odit possimus quo voluptas tenetur ea odio perspiciatis. Aut possimus Quis ut
consectetur praesentium et harum neque sed laboriosam galisum et voluptas ipsum 
non voluptatem amet. </p><p>In iusto cumque est dolorem velit id maxime exercitationem
aut beatae quibusdam sed voluptas dolorum! Et sint suscipit aut obcaecati corrupti
et molestiae corrupti aut distinctio recusandae
"""
i = 0

while i < len(nome):
    letra_autal = nome[i]

    qtd_letra_apariceu = nome.count(letra_autal)

    print(letra_autal,qtd_letra_apariceu ,)
    i += 1