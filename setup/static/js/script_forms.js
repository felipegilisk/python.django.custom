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
  if (veiculoId != "") {
    $.ajax({
      url: "/core/veiculo_get_valor_mensal/" + veiculoId,
        type: 'GET',
        success: function(data) {
            var valorBase = data.valor_mensal
            $('#id_valor_base_veiculo').val(valorBase);
            var valorReserva = $('#id_valor_mensal_considerado').val();
            if (valorReserva > valorBase) {
              $('#id_valor_mensal_considerado').val(data.valor_mensal);
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Erro ao obter valor mensal do veículo:', errorThrown);
        }
    });
  } else {
    $('#id_valor_base_veiculo').val("0.00");
  }
});

$('#id_veiculo_reserva').change(function() {
  var veiculoId = $(this).val();
  if (veiculoId != "") {
    $.ajax({
      url: "/core/veiculo_get_valor_mensal/" + veiculoId,
        type: 'GET',
        success: function(data) {
            var valorReserva = data.valor_mensal
            var valorBase = $('#id_valor_base_veiculo').val();
            if (valorReserva > valorBase) {
              valorReserva = valorBase
            }
            $('#id_valor_mensal_considerado').val(valorReserva);
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Erro ao obter valor mensal do veículo:', errorThrown);
        }
    });
  } else {
    $('#id_valor_mensal_considerado').val("0.00");
  }
});
});
