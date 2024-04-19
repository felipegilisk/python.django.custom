var totalValorMensal = 0;
var tabela_medicao = document.querySelector('#table_1>tbody');

function parseStringToDate(s) {
    return new Date(s.replace(' ', 'T'))
    // return new Date(b[2], b[1] - 1, b[0], b[3], b[4]);
}

function formatarData(d) {
    const dia = String(d.getDate()).padStart(2, '0');
    const mes = String(d.getMonth() + 1).padStart(2, '0');
    const ano = d.getFullYear();
    const hora = String(d.getHours()).padStart(2, '0');
    const minuto = String(d.getMinutes()).padStart(2, '0');
    
    return `${dia}/${mes}/${ano} ${hora}:${minuto}`;
}



// indisp_ser.forEach(function(item) {
//     totalValorMensal += parseFloat(item.valor);

//     var new_row = tabela_medicao.insertRow();

//     var cell_tipo = new_row.insertCell();
//     var cell_placa = new_row.insertCell();
//     var cell_modelo = new_row.insertCell();
//     var cell_grupo = new_row.insertCell();
//     var cell_inicio = new_row.insertCell();
//     var cell_fim = new_row.insertCell();
//     var cell_horas = new_row.insertCell();
//     var cell_editar = new_row.insertCell();
//     var cell_excluir = new_row.insertCell();
//     var cell_valor = new_row.insertCell();

//     cell_tipo.textContent = item.tipo;
//     cell_placa.textContent = item.placa;
//     cell_modelo.textContent = item.marca_modelo;
//     cell_grupo.textContent = item.grupo;
//     // datas
//     inicio = parseStringToDate(item.inicio);
//     cell_inicio.textContent = formatarData(inicio);
//     termino = parseStringToDate(item.termino);
//     cell_fim.textContent = formatarData(termino);
//     // botões
//     if (item.tipo != "Base") {
//         var link_editar = document.createElement("a");
//         link_editar.setAttribute("class", "btn btn-primary btn-sm");
//         var icone_editar = document.createElement("i");
//         icone_editar.setAttribute("class", "bi bi-pencil");

//         var link_excluir = document.createElement("a");
//         link_excluir.setAttribute("class", "btn btn-danger btn-sm")
//         var icone_excluir = document.createElement("i");
//         icone_excluir.setAttribute("class", "bi bi-trash")
//         if (item.tipo == "Indisponibilidade") {
//             link_editar.setAttribute('href', "/core/editar_indisponibilidade/" + item.id_edit);
//             link_excluir.setAttribute('href', "/core/excluir_indisponibilidade/" + item.id_edit);
//         } else if (item.tipo == "Reserva") {
//             link_editar.setAttribute('href', '/core/editar_apontamento_reserva/' + item.id_edit);
//             link_excluir.setAttribute('href', '/core/excluir_apontamento_reserva/' + item.id_edit);
//         }
//         cell_editar.appendChild(link_editar);
//         link_editar.appendChild(icone_editar);
//         cell_excluir.appendChild(link_excluir);
//         link_excluir.appendChild(icone_excluir);
//     }
    
//     cell_horas.textContent = item.total_horas;
//     cell_valor.textContent = "R$ "+ parseFloat(item.valor).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
// });

// var tfoot = document.querySelector('tfoot>tr');
// var cell_total = tfoot.insertCell();
// cell_total.textContent = "R$ "+ totalValorMensal.toLocaleString('pt-BR', { minimumFractionDigits: 2 });
