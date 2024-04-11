$(document).ready(function () {
  $('#valor_mensal').on('blur', function () {
      var valor = $(this).val();
      var valorFormatado = parseFloat(valor).toFixed(2);
      $(this).val(valorFormatado);
  });
url: "{% url 'veiculo_get_valor_mensal' veiculoId %}",
  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

  $('#id_mes_medicao_day').hide();
  $('#id_mes_medicao_day').prop('disabled', true);
  $('#id_mes_medicao_day option:not(:nth-child(2))').remove();

});

const placaInput = document.querySelector('input[name="placa"]');


// apontamento de reservas 
$(document).ready(function() {
  if ($('#id_tem_reserva').length) {
      $('#id_tem_reserva').change(function() {
          if ($(this).prop('checked')) {
              $('#reserva_form').show();
          } else {
              $('#reserva_form').hide();
          }
      });
  }
  $('#id_veiculo').change(function() {
    var veiculoId = $(this).val();
    // Faz uma requisição AJAX para obter os detalhes do veículo
    $.ajax({
      url: "/locacao/veiculo_get_valor_mensal/" + veiculoId,
        type: 'GET',
        success: function(data) {
            // Define o valor do campo "valor_base_veiculo" com o valor mensal retornado
            $('#id_valor_base_veiculo').val(data.valor_mensal);
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Erro ao obter valor mensal do veículo:', errorThrown);
        }
    });
});
});
