var totalValorMensal = 0;
var tabela_medicao = document.querySelector('#table_1>tbody');

veic_ser.forEach(function(veiculo) {
    totalValorMensal += parseFloat(veiculo.grupo_veiculo.valor_mensal);
    var new_row = tabela_medicao.insertRow();
    var cell_tipo = new_row.insertCell();
    cell_tipo.textContent = "Base";
    var cell_placa = new_row.insertCell();
    cell_placa.textContent = veiculo.placa;
    var cell_modelo = new_row.insertCell();
    cell_modelo.textContent = veiculo.marca_modelo;
    var cell_grupo = new_row.insertCell();
    cell_grupo.textContent = veiculo.grupo_veiculo.id_grupo_veiculo + " - " + veiculo.grupo_veiculo.descricao_grupo;
    var cell_valor = new_row.insertCell();
    cell_valor.textContent = "R$ "+ parseFloat(veiculo.grupo_veiculo.valor_mensal).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
});

indisp_ser.forEach(function(indisp) {
    totalValorMensal -= parseFloat(indisp.valor_indisponibilidade);
    var new_row = tabela_medicao.insertRow();
    var cell_tipo = new_row.insertCell();
    cell_tipo.textContent = "Indisponibilidade";
    var cell_placa = new_row.insertCell();
    cell_placa.textContent = indisp.veiculo.placa;
    var cell_modelo = new_row.insertCell();
    cell_modelo.textContent = indisp.veiculo.marca_modelo;
    var cell_grupo = new_row.insertCell();
    cell_grupo.textContent = indisp.veiculo.grupo_veiculo.id_grupo_veiculo + " - " + indisp.veiculo.grupo_veiculo.descricao_grupo;
    var cell_valor = new_row.insertCell();
    cell_valor.textContent = "- R$ "+ parseFloat(indisp.valor_indisponibilidade).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
});

var tfoot = document.querySelector('tfoot>tr');
var cell_total = tfoot.insertCell();
cell_total.textContent = "R$ "+ totalValorMensal.toLocaleString('pt-BR', { minimumFractionDigits: 2 });
