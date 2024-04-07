var totalValorMensal = 0;

veic_ser.forEach(function(veiculo) {
    totalValorMensal += parseFloat(veiculo.grupo_veiculo.valor_mensal);
});

var tfoot = document.querySelector('tfoot>tr');
var newCell = tfoot.insertCell();
newCell.textContent = totalValorMensal.toLocaleString('pt-BR', { minimumFractionDigits: 2 });
