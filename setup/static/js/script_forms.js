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
              calcular();
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
              var valorBase = parseFloat(data.valor_mensal)
              var valorMax = parseFloat($('#id_valor_mensal_considerado').attr('max'));
              if (valorBase > valorMax) {
                $('#id_valor_mensal_considerado').val(valorMax.toFixed(2));
              } else {
                $('#id_valor_mensal_considerado').val(valorBase.toFixed(2));
              }
              calcular();
          },
          error: function(xhr, textStatus, errorThrown) {
              console.log('Erro ao obter valor mensal do veículo:', errorThrown);
          }
      });
    } else {
      $('#id_valor_base_veiculo').val("0.00");
    }
  });

  $('#id_data_hora_inicio').change(function() {
    calcular();
  });

  $('#id_data_hora_termino').change(function() {
    calcular();
  });

  function calcular() {
    valorBase = parseFloat($('#id_valor_base_veiculo').val());
    if (isNaN(valorBase)){
      valorBase = $('#id_valor_mensal_considerado').val();
    }
    dataInicial = new Date($("#id_data_hora_inicio").val());
    dataTermino = new Date($("#id_data_hora_termino").val());
    if (dataInicial != "Invalid Date" && dataTermino != "Invalid Date" && dataInicial < dataTermino && valorBase > 0) {
      horas = parseInt((dataTermino - dataInicial)/(60*60*1000));
      $("#id_valor_indisponibilidade").val((valorBase*horas/720).toFixed(2));
      $("#id_valor_total_uso").val((valorBase*horas/720).toFixed(2));
    } else {
      $("#id_valor_indisponibilidade").val("0.00");
      $("#id_valor_total_uso").val("0.00");
    }
    return null;
  }
});
