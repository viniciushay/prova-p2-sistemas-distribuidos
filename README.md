# prova-p2-sistemas-distribuidos
aluno: vinicius hay mussi becalito
1. qual é a função do semáforo no processamendo dos pedidos
R=O semáforo controla a quantidade de pedidos

2. por que é necessario sincronizar os dados entre servidor principal e a replica?
R=Porque a réplica precisa ter os mesmos dados atualizados do servidor principal

3. o que significa tolerãncia a falhas e como ela aparece neste programa?
R=Tolerância a falhas é a capacidade de um sistema continuar funcionando mesmo quando uma parte dele apresenta problemas.

4. para que serve o lock no programa e como o controle de acesso aos recursos ajuda a previnir problemas da concorrencia
R=O Lock impede que várias threads alterem o estoque ao mesmo tempo.

5. considerando a sequência de eventos, a sincronização do estoque deve acontecer antes ou depois do processamento?
R=A sincronização deve acontecer depois do processamento dos pedidos,assim a réplica recebe o valor atualizado do estoque após todos os pedidos serem concluídos.